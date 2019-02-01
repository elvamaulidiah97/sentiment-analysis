# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:03:05 2018

@author: laptopku
"""
import nltk
nltk.download('wordnet')
nltk.download('sentiwordnet')
from nltk.corpus import sentiwordnet as swn

happy = [':-)', ':)', ':-]', ':]', ':-3', ':3', ':->', ':>', '8-)', '8)', ':-}', ':}', ':o)', ':c)', ':^)', '=]', '=)', 
'(?^o^?)', '(^v^)', '(^u^)', '(^?^)', '( ^)o(^ )', '(^O^)', '(^o^)', '(^?^)', ')^o^(', '(*^?^*)', '(????)']
laugh = [':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=D', '=3', 'B^D'] 
very_happy = [':-))']
sad = [':-(', ':(', ':-c', ':c', ':-<', ':<', ':-[' ':[', ':-||']	
angry  = ['>:[', ':{', ':@', '>:(']
cry = [':\'(', ':"-(', ':"(]', '(T_T)', ' (;_;)', '(;_;(;_:)', '(;O;)', '(:_;)', '(ToT)', '(T?T)', ' ;_;', ';-;', ';n;', ' ;;', ' Q.Q', ' T.T', ' TnT', ' QQ', ' Q_Q']
tears_happiness = [':"-)', ':")']
kiss  = [':-*', ':*', ':×', ':-*', ' :*', ' :×']
shock = [':-O', ':O', ':-o', ':o', ':-0', '8-0', '>:O']
cheeky  = [':-P', ':P', 'X-P', 'XP', 'x-p', 'xp', ':-p', ':p', ':-Þ', ':Þ', ':-þ', ':þ', ':-b', ':b', 'd:', '=p', '>:P']
sceptic = [':-.',   '>:/',  '=/',	':L', 	'=L', ':/', ':-/', ':S']
flat = [':-|', ':|']
embarrassed = [':$', '(-_-;)', '(~_~;)',  ' ^^;', '^_^;', '(#^.^#)']
tongue_tied= [':-X', ':X', ':-#', ':#', ':-&', ':&']
angel = ['O:-)', 'O:)', '0:-3', '0:3', '0:-)', '0:)', '0;^)']
demon = ['>:-)', '>:)', '}:-)', '}:)', '3:-)', '3:)', '>;)' ]
#nervous = = ['(^_^;)',  '(^^;)']
troubled = ['(·.·;)', '(·_·;)', '(··;)', '(>_<)', '(>_<)>']
confused= ['((+_+))', '(+o+)', '(°°)' , '(°-°)', '(°.°)', '(°_°)', '(°_°>)', '(°?°)']
shame = ['(?_?)!!', '(-.-)', '(-_-)', '(??)', '(;?_?)']
tired = ['(=_=)']
shocked = ['(???;)', '°o°°O°', ':O o_', 'Oo_', '0o.O', '(o.o)', 'oO', ' ( ? ??)', '(°?°)']
grinning = ['(???)']
worried = ['(-"-)', '(???)', '(^_^?)', '(-_-?)', '(~_~?)', '(--?)', ' (·?·)', '(`´)', '<`~´>', '<`?´>', '(??;)']
laughing = ['(*^^)v', '(^^)v', '(^_^)v', '(’-’*)', ' (^v^)', '(^?^)', '(·?·)', '(´?`)', '(???)']
amazed =  ['(*_*)', '(*_*;', '(+_+)', ' (@_@)', '(@_@?', '(@_@;)', '\(?o?)/!']
excited  =  ['\(~o~)/', '\(^o^)/', '\(-o-)/', ' ?(^?^)?', '?(^o^)?', '(*^0^*)']
waving =  ['(^^)', '/~~~', '(^_^)/', '~(;_;)', '/~~~', '(^.^)', '/~~~', '(-_-)', '/~~~ ', '($··)', '/~~~', '(@^^)', '/~~~', '(T_T)', '/~~~', '(ToT)', '/~~~']
#happy normal =  ['>^_^<', '<^!^>', '^/^', '(*^_^*)', '§^.^§', '(^<^)', ' (^.^)', '(^?^)', '(^·^)', '(^.^)', '(^_^.)', '(^_^)', '(^^)', ' (^J^)', '(*^.^*)', '^_^', '(#^.^#)', '(^—^)']
confusion = ['(··?(?_?)']
questioning = ['\(°?\)', '(/?°)/']
sleeping = ['(-_-)zzz']
#wink = ['(^_-)' , '(^_-)-?', ';-)'. ';)' , '*-)', '*)', ';-]', ';]', ';^)', ':-,', ';D']	
mellow = ['?(´?`)+', '¯\_(?)_/¯']
sick = [':-###.', '. :###..']
drunk = ['%-)', '%)']
cool =  ['|;-)']
bored = '|-O'
sadness = ['D-\':', ' D:<', '  D:', ' D8', 'D;', ' D=', ' DX']
surprised = ['( ? ??)', '(°?°)']
deflated = ['(´???`)', '(‘A`)']
infatuation = ['(*´?`*)', '(*°?°)=3']
dissatisfied = ['(*?m?)', '(~o~)', '(~_~)', '(^^?']
eyeglasses = ['(^0_0^)']
apologize = ['(__)', '_(._.)_', '_(_^_)_', '<(_ _)>',  '<m(__)m>', 'm(__)m', 'm(_ _)m']
opposite  = [':v', ':V']

emoticon_with_score = {}

emot = {}

emotion =['happy', 'laugh', 'sad', 'angry', 'cry', 'kiss', 'shock', 'cheeky', 'embarrassed', 
          'tongue_tied', 'demon', 'angel', 'troubled',  'confused', 'shame', 'tired',
          'shocked', 'grinning', 'worried', 'laughing', 'amazed', 'excited', 'waving', 
          'confusion', 'questioning', 'sleeping', 'mellow', 'sick', 'drunk', 'cool', 'bored', 
          'sadness', 'surprised', 'deflated', 'infatuation', 'dissatisfied', 'eyeglasses', 'apologize', 'opposite']

emot['happy'] = happy
emot['laughing'] = laughing
emot['sadness'] = sadness
emot['sad'] = sad
emot['angry'] = angry
emot['cry'] = cry
emot['kiss'] = kiss
emot['shock'] = shock
emot['cheeky'] = cheeky
emot['embarrassed'] = embarrassed
emot['tongue_tied'] = tongue_tied
emot['demon'] = demon
emot['angel'] = angel
emot['shame'] = shame
emot['tired'] = tired
emot['laugh'] = laugh
emot['confused'] = confused
emot['shocked'] = shocked
emot['confused'] = confused
emot['grinning'] = grinning
emot['worried'] = confused
emot['amazed'] = amazed
emot['excited'] = excited
emot['waving'] = waving
emot['amazed'] = amazed
emot['confusion'] = confusion
emot['questioning'] = questioning
emot['sleeping'] = sleeping
emot['mellow'] = mellow
emot['sick'] = sick
emot['drunk'] = drunk
emot['cool'] = cool
emot['bored'] = bored
emot['surprised'] = surprised
emot['deflated'] = deflated
emot['infatuation'] = infatuation
emot['dissatisfied'] = dissatisfied
emot['eyeglasses'] = eyeglasses
emot['apologize'] = apologize
emot['opposite'] = opposite


emot_gaada = {
        ':\')': [':)', ':\'('],
        '>:O' : ['>:[', ':O']
    }

#synsets = list(swn.senti_synsets('laugh'))

def ambigu(emoticon):
        unique_char = list(set(emoticon))
        score = 0
        
        much = {}

        for character in unique_char:
            if emoticon.count(character) > 1:
                much[character] = emoticon.count(character)
#                if much[character] = '(':
                score = emoticon.count(character) * 0.1
            fix = ''.join(sorted(set(emoticon),  key=emoticon.index))
        if score > 1:
            score = 1
        return fix, score

value_emoticon = {}

for icon in emotion:
    synsets = list(swn.senti_synsets(icon))
    for synset in synsets:
        if synset.pos_score() > 0 or synset.neg_score() > 0:
            value_emoticon[icon] = [synset.pos_score(), synset.neg_score()]
            break

def predict_score(emoticon):
    positive = 0
    negative = 0
    flag = 0
    for key, value in emot.items():
        if emoticon in value:
            pos = value_emoticon[key][0]
            neg = value_emoticon[key][1]
            sentiment = []
            if pos > neg:
                sentiment.append('positif')
            elif neg > pos:
                sentiment.append('negatif')
            else:
                sentiment.append('netral')
#            print(key + ' = ' + 'positive: ' + str(pos) + ' | negative: ' + str(neg) + ' | ' + str(sentiment))
            flag = 1
            positive = pos
            negative = neg
            break
#        return pos, neg

    if flag == 0:
        word, score = ambigu(emoticon)
#        print(score)
        pos = 0
        neg = 0
        sentiment = []
        for key, value in emot.items():   
            if word in value :
                if ':)' in value :
                    pos = (value_emoticon[key][0] + score)
                    neg = (value_emoticon[key][1])
                    if pos > 1:
                        pos = 1
                        neg = 0
                    
#                    print(key + ' = ' + 'positive: ' + str(pos) + ' | negative: ' + str(neg) + ' | ')
                elif ':(' in value :
                    pos = (value_emoticon[key][0])
                    neg = (value_emoticon[key][1] - score)
                    if neg < 0:
                        neg = 0
                flag = 1
                positive = pos
                negative = neg
                if pos > neg:
                    sentiment.append('positif')
                elif neg > pos:
                    sentiment.append('negatif')
                else:
                    sentiment.append('netral')
                break
            
#        print(key + ' = ' + 'positive: ' + str(pos) + ' | negative: ' + str(neg) + ' | ' )  
                    
#                
#                print(key + ' = ' + 'positive: ' + str(pos) + ' | negative: ' + str(neg) + ' | ')
            
    if flag == 0:
            cat = []
            pos_total = 0
            neg_total = 0
            if emoticon in emot_gaada:
                emots = emot_gaada[emoticon]
                for emoti in emots:
                    for key, value in emot.items():
                        if emoti in value:
    #                        print(str(value_emoticon[key][0]) + '|' + str(value_emoticon[key][1]))
                            
                            pos_total = (pos_total + value_emoticon[key][0])
                            neg_total = (neg_total + value_emoticon[key][1])
                            
                            sentiment =[]
                            if pos_total > pos_total:
                                sentiment.append('positif')
                            elif neg_total > pos_total:
                                sentiment.append('negatif')
                            else:
                                sentiment.append('netral')
                            cat.append(str(key))
                positive = pos_total / 2
                negative = neg_total / 2
            else:
                print(emoticon + " belum ada di dictonary. Perlu dicari buat cara menangani kasus kayak gini")
                positive = 0
                negative = 0
    
    return positive, negative
#            print(cat[0] + ', ' +  cat[1] + '=  positive: ' + str(pos_total) + ' | negative: ' + str(neg_total) + ' | ' + str(sentiment))
  
ex1 = [':\')', ':D', '(~_~;)', ':)))', ':(((', ':\'(', ':)',  ':(', ':((((((((((']
ex2 =  [ '>:O',  ':×',  ':(', ':O', '<(_ _)>']
ex3 = [':)', 'O:)', '(-_-;)', ':((((((']
ex4 = [':)']
    
            
for j in ex1:
    print('Emoticon: ' + j)
    pos, neg = predict_score(j)
    print('Positive: ' + str(pos))
    print('Negative: ' + str(neg))

                
