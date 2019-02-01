from googletrans import Translator
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet as wn
from nltk import ngrams
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
import math
import pandas as pd

class Sentiwordnet():

    def translate(self, list_review):
        translator = Translator()
        for index in range(len(list_review)):
            translation = translator.translate(list_review[index])
            list_review[index] = translation.text
        return list_review

    def penn_to_wn(self, tag):
        """
        Convert between the PennTreebank tags to simple Wordnet tags
        """
        if tag.startswith('J'):
            return wn.ADJ
        elif tag.startswith('N'):
            return wn.NOUN
        elif tag.startswith('R'):
            return wn.ADV
        elif tag.startswith('V'):
            return wn.VERB
        return wn.ADJ

    def calculate_sentiment_score(self, reviews):
        list_hasil_skor = []
        lemmatizer = WordNetLemmatizer()
        not_found_unigram_count = 0
        list_not_found_word = []

        for index in range(len(reviews)):
            senti_count = 0
            pos_score = 0
            neg_score = 0

            tagged_review = pos_tag(word_tokenize(reviews[index]))  # buat nyari part of speechnya
            for word, tag in tagged_review:
                wn_tag = self.penn_to_wn(tag)  # buat ngerubah POS Tagnya sesuai dengan standar wordnet
                if wn_tag not in (wn.NOUN, wn.ADV, wn.ADJ, wn.VERB):
                    continue
                lemma = lemmatizer.lemmatize(word,
                                             pos=wn_tag)  # bukan pakai stemmer lagi, sekarang pakai lemmatizer jadi sesuai part of speechnya
                if not lemma:
                    continue
                if len(tagged_review) == 1:
                    synsets = wn.synsets(lemma, pos=wn.ADJ)
                else:
                    synsets = wn.synsets(lemma, pos=wn_tag)
                if not synsets:
                    not_found_unigram_count += 1
                    list_not_found_word.append(word)
                    continue
                synset = synsets[0]
                senti = swn.senti_synset(synset.name())

                if (senti.pos_score() > 0):
                    pos_score += senti.pos_score()
                    senti_count += 1
                if (senti.neg_score() > 0):
                    neg_score += senti.neg_score()
                    senti_count += 1

            if senti_count == 0:
                skor_akhir = 0
            else:
                """total_skor = pos_score + neg_score
                skor_akhir = total_skor / senti_count"""
                skor_akhir = (pos_score - neg_score) / senti_count

            list_hasil_skor.append(skor_akhir)

            """for word in list_not_found_word:
                print(word)
            """
        # print('\nJumlah kata :', word_count)
        # print('Kata positif :', pos_unigram_count)
        # print('Kata_negatif :', neg_unigram_count)
        print('Kata yang tidak ketemu synsetnya :', not_found_unigram_count, '\n')
        # print('List kata yang tidak ketemu synsetnya : \n')
        # for word in not_found_word:
        # print(word)
        # print('\n')
        # print(not_found_word)
        #print("Skor maksimal : ", skor_max)
        #print("Skor minimal : ", skor_min)
        return list_hasil_skor

    def classify_sentiment(self, reviews):
        list_hasil_skor = self.calculate_sentiment_score(reviews)
        list_hasil_sentiment = []

        """sorted_score = sorted(list_hasil_skor)
        kuartil_bawah = 0.25 * (len(sorted_score) + 1)
        value_kuartil_bawah = (sorted_score[math.floor(kuartil_bawah)] + sorted_score[math.ceil(kuartil_bawah)]) / 2
        print("Nilai kuartil bawah : ", value_kuartil_bawah)
        kuartil_atas = 0.75 * (len(sorted_score) + 1)
        value_kuartil_atas = (sorted_score[math.floor(kuartil_atas)] + sorted_score[math.ceil(kuartil_atas)]) / 2
        print("Nilai kuartil atas : ", value_kuartil_atas)"""

        for index in range(len(list_hasil_skor)):
            if list_hasil_skor[index] >= 0.05:
                list_hasil_sentiment.append(1)
            elif list_hasil_skor[index] <= -0.05:
                list_hasil_sentiment.append(0)
            elif (list_hasil_skor[index] > -0.05) & (list_hasil_skor[index] < 0.05):
                list_hasil_sentiment.append(2)

        return list_hasil_sentiment

    def classify(self, reviews):
        reviews = reviews['COMMENT'].values.tolist()
        translated_reviews = self.translate(reviews)
        predicted_sentiment = self.classify_sentiment(translated_reviews)
        return predicted_sentiment
