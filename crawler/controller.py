import sys
sys.path.insert(0, '/Users/USER/SbaProjects')

from crawler.entity import Entity
from crawler.service import Service

class Controller:
    def __init__(self) :
        self.entity = Entity()
        self.service = Service()
        

    def preprocessing(self, train, test):
         pass
    
     def modelling(self, train, test):
         pass
        
     def learning(self) :
         pass

     def submit(self) :
         pass

if __name__ == '__main__' :
    api = Controller()
    servicne = Service()
    service.naver_cartoon('https://comic.naver.com/webtoon/weekday.nhn')


    
