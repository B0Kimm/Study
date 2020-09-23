import sys
sys.path.insert(0, '/Users/USER/SbaProjects')

from miner.entity import Entity

import re
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
from konlpy.tag import Komoran
import pandas as pd
from nltk import FreqDist
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image 
from wordcloud import ImageColorGenerator
from bs4 import BeautifulSoup
from gensim.models import word2vec

class Service:
    def __init__(self):
        self.texts = []
        self.tokens = []
        self.okt = Okt()
        self.stopwords = []
        self.freqtxt = []
    
    
    def extract_token(self, payload):
        print('>>> text 문서에서 token 추출')
        filename = payload.context + payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.texts = f.read()
        # print(f'{self.texts[:300]}')
    
    
    def extract_hanguel(self):
        print('>>> 한글만 추출')
        texts = self.texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ ㄱ-힣]')
        self.texts = tokenizer.sub('', texts)
        # print(f'{self.texts[:300]}')
    
    
    def conversion_token(self):
        print('>>> 토큰으로 변환')
        self.tokens = word_tokenize(self.texts)
        # print(f'{self.tokens[:300]}')
    
    
    def compound_noun(self):
        print('>>> 복합명사는 묶어서 fitering 으로 출력')
        print('>>> ex) 삼성전자의 스마트폰은 --> 삼성전자 스마트폰')
        noun_token = []
        for token in self.tokens:
            token_pos = self.okt.pos(token)
            temp = [txt_tag[0] for txt_tag in token_pos
                    if txt_tag[1] == 'Noun']
            if len("".join(temp)) > 1:
                noun_token.append("".join(temp))
        self.texts = " ".join(noun_token)
        # print(f'{self.texts[:300]}')
    
    
    def extract_stopword(self, payload):
        print('>>> text 문서에서 token 추출')
        filename = payload.context + payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.stopwords = f.read()
        self.stopwords = self.stopwords.split(' ')
        # print(f'{self.stopwords[:10]}')
    
    
    def filtering_text_with_stopword(self):
        print('>>> stopword 로 필터링 ')
        self.texts = word_tokenize(self.texts)
        self.texts = [text for text in self.texts
                      if text not in self.stopwords]
    
    
    def frequent_text(self):
        print('>>> 빈도수로 정렬 ')
        self.freqtxt = pd.Series(dict(FreqDist(self.texts)))\
            .sort_values(ascending=False)
        # print(f'{self.freqtxt[:10]}')
    
    
    def draw_wordcloud(self, payload):
        print('>>> 워드크라우드 작성 ')
        filename = payload.context + payload.fname
        wcloud = WordCloud(filename,
                           relative_scaling=0.2,
                           background_color='white').generate(" ".join(self.texts))
        plt.figure(figsize=(12,12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    @staticmethod
    def tag_pos(text) :
        komo = Komoran()
        result = komo.pos(text)
        for myitem in result:
            somedata = '단어 : %s, 품사 : %s' % (myitem[0], myitem[1])
            print(somedata)
        return result

    @staticmethod
    def only_nouns(text) :
        komo = Komoran()
        print('명사만 추출해보기')
        nouns = komo.nouns(text)
        print(nouns)
        return nouns

    @staticmethod
    def word_bigram(text) :
        only_nouns = []
        komo = Komoran()
        result = komo.pos(text)
        for myitem in result:
            if (myitem[1] in ['NNG', 'NNP']) :
                if(len(myitem[0]) >= 3):
                    somedata = '단어 : %s, 품사 : %s' % (myitem[0], myitem[1])
                    only_nouns.append(myitem[0])
                else :
                    print(myitem[0] + '은 제외합니다.')

    @staticmethod
    def make_stem_list(fname):
        
        myfile = open(fname, 'rt', encoding='utf-8')
        soup = BeautifulSoup(myfile, 'html.parser')
        mydata = soup.text

        results = [] # 결과 저장소
        okt = Okt()

        datalines = mydata.split('\n')
        print(len(datalines))

        for oneline in datalines :
            mypos = okt.pos(oneline, norm = True, stem = True)

        imsi = []# 임시 리스트
        for word in mypos :
            if not word[1] in ['Josa', 'Eomi', 'Punctuation', 'Verb']:
                if len(word[0]) >= 2 :
                imsi.append(word[0])

        temp = (' '.join(imsi)).strip()
        results.append(temp)
        return results

    @staticmethod
    def word2vec(results) :
        prepro_file = 'word2vec.prepro'
        with open(prepro_file, 'wt', encoding='utf-8') as myfile :
            myfile.write('\n'.join(results))

        print(prepro_file + ' 파일 생성됨')

        data = word2vec.LineSentence(prepro_file)
        print(type(data))

        model = word2vec.Word2Vec(data, size=200, window=10, min_count=2, sg=1)
        print(type(model))

        model_filename = 'word2vec.model'

        model.save(model_filename)
        print(model_filename + ' 파일 생성됨')

        print('finished')


    @staticmethod
    def showGraph(bargraph):
        plt.rc('font', family='Malgun Gothic')

        length = len(bargraph)
        myticks = list(mydata[0] for mydata in bargraph)
        chartdata = list(mydata[1] for mydata in bargraph)
        mycolor = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#56FFCC', '#00CCFF', '#CCDDEE']

        plt.figure()
        plt.barh(myticks, chartdata, color=mycolor, align='center')
        plt.yticks(range(length), myticks, rotation='10')
        plt.xlim(min(chartdata) - 0.02, max(chartdata) + 0.02)
        filename = (f'{bargraph}.png')
        plt.savefig(filename)
        

    @staticmethod
    def makePie(piegraph):
        myticks = list(mydata[0] for mydata in piegraph)
        chartdata = list(mydata[1] for mydata in piegraph)
        mycolor = ['b', 'g', 'r', 'c', 'm']

        plt.figure()
        plt.pie(chartdata, colors=mycolor, labels=myticks, startangle=90, shadow=False,
                explode=(0, 0.05, 0, 0, 0), autopct='%1.2f%%', normalize=True)
        filename = (f'{piegraph}.png')
        plt.savefig(filename)

    @staticmethod
    def create_wordlist(fname, stopwordfile) :
        filename = fname
        ko_con_text = open(filename, 'rt', encoding='utf-8').read()

        okt = Okt()
        token_ko = okt.nouns(ko_con_text)

        stop_word_file = stopwordfile
        stop_file = open(stop_word_file, 'rt', encoding='utf-8')
        stop_words = [ word.strip() for word in stop_file.readlines()]
        
        token_ko = [each_word for each_word in token_ko if each_word not in stop_words]

        ko = nltk.Text(tokens=token_ko)

        wordlist = list()

        data = ko.vocab().most_common(500)
        for word, count in data :
            if (count >= 50 and len(word) >= 2):
                wordlist.append((word, count))
        return wordlist

    def makeWorCloud(self, wordlist,fname_to_save,color_file): 
        plt.rc('font', family='Malgun Gothic')

        alice_color_file = (f'{color_file}.png')
        alice_coloring = np.array(Image.open(alice_color_file))
        fontpath = 'malgun.ttf'
        wordcloud = WordCloud(font_path=fontpath, mask=alice_coloring,
                              relative_scaling = 0.2,background_color='lightyellow')
        wordcloud = wordcloud.generate_from_frequencies(self.wordDict)

        image_colors = ImageColorGenerator(alice_coloring)

        newwc = wordcloud.recolor(color_func=image_colors, random_state=42)

        plt.imshow(newwc)
        plt.axis('off')

        filename = (f'{fname_to_save}.png')
        plt.savefig(filename)
        plt.figure(figsize=(16,8))

    def makeBarChart(self, wordlist,fname_to_save): # 막대 그래프
        plt.rc('font', family='Malgun Gothic')

        # result를 이용하여 막대 그래프를 그려 보세요.
        result = self.wordlist[0:10] # 10개 데이터

        barcount = 10  # 막대 갯수 : 10개만 그리겠다.
        xlow, xhigh = - 0.5, barcount - 0.5

        result = self.wordlist[:barcount]
        chartdata = []  # 차트 수치
        xdata = []  # 글씨
        mycolor = ['r', 'g', 'b', 'y', 'm', 'c', '#FFF0F0', '#CCFFBB', '#05CCFF', '#11CCFF']

        for idx in range(len(result)):
            chartdata.append(result[idx][1])
            xdata.append(result[idx][0])

            value = str(chartdata[idx]) + '건'  # 예시 : 60건
            # 그래프의 위에 "건수" 표시
            plt.text(x=idx, y=chartdata[idx] - 20, s=value, fontsize=8, horizontalalignment='center')

        plt.xticks(range(barcount), xdata, rotation=45)
        plt.bar(range(barcount), chartdata, align='center', color=mycolor)

        plt.title('상위 ' + str(barcount) + '빈도수')
        plt.xlim([xlow, xhigh])
        plt.xlabel('주요 키워드')
        plt.ylabel('빈도수')

        filename = (f'{fname_to_save}.png')
        plt.savefig(filename, dpi=400, bbox_inches='tight')
        print(filename + ' 파일이 저장되었습니다.')


