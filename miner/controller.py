import sys
sys.path.insert(0, '/Users/USER/SbaProjects')

from miner.entity import Entity
from miner.service import Service

import nltk

class Controller:
    def __init__(self):
        pass

    def download_dictionary(self):
        nltk.download('all')

    def data_analysis(self):
        entity = Entity()
        service = Service()
        entity.fname = 'kr-Report_2018.txt'
        entity.context = './data/'
        service.extract_token(entity)
        service.extract_hanguel()
        service.conversion_token()
        service.compound_noun()
        entity.fname = 'stopwords.txt'
        service.extract_stopword(entity)
        service.filtering_text_with_stopword()
        service.frequent_text()
        entity.fname = 'D2Coding.ttf'
        service.draw_wordcloud(entity)
    
    @staticmethod
    def raw_data_analysis() :
        text = '세일즈 우먼인 아름다운 그녀가 아버지 가방에 들어 가시나 ㅎㅎ'
        Service.only_nouns()
        Service.tag_pos

    def data_analysis2(self) :
        entity.fname = 'TojiText,txt'
        entity.context = './data/'
        entity.fname = 'stopwordfile'
        service.create_wordlist(entity)
        service.makeWorCloud()
        service.makeBarChart()

    def data_analysis3(self) :
        eentity.fname = '문재인대통령신년사.txt'
        entity.context = './data/'
        service.make_stem_list(entity)
        service.word2vec()

if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. 사전 다운로드')
        print('2. 삼성 전략보고서 분석')
        print('3. 토지 분석')
        print('4. 문재인대통령신년사 분석')
        print('5. 텍스트 분석')
        return input('Select Menu\n')
        
    app = Controller()
    while 1:
        menu = print_menu()
        if menu == '1':
            app.download_dictionary()
        if menu == '2':
            app.data_analysis()
        if menu == '3':
            app.data_analysis2()
        if menu == '4':
            app.data_analysis3()
        if menu == '5':
            app.raw_data_analysis()
        elif menu == '0':
            break