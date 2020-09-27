<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 24429448bf9c9728c794e7114a5128e1fe34e689
import sys
sys.path.insert(0, '/Users/USER/SbaProjects')

from crawler.entity import Entity
from crawler.service import Service

class Controller :
    def __init__(self) :
        self.entity = Entity()
        self.service = Service()


    def naver_cartoon(self):
        pass

if __name__ == "__main__":
    api = Controller()
    service = Service()
<<<<<<< HEAD
=======
=======
import sys
sys.path.insert(0, '/Users/USER/SbaProjects')

from crawler.entity import Entity
from crawler.service import Service

class Controller :
    def __init__(self) :
        self.entity = Entity()
        self.service = Service()

    def preprocessing(self) :
        pass

    def modeeling(self) :
        pass

    def learning(self) :
        pass

    def submit(self) :
        pass

if __name__ == "__main__":
    api = Controller()
    service = Service()
>>>>>>> 88e3d89821e46f18a11e0022f1728d72e5a886b5
>>>>>>> 24429448bf9c9728c794e7114a5128e1fe34e689
    service.naver_cartoon('https://comic.naver.com/webtoon/weekday.nhn')