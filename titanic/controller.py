import sys
sys.path.insert(0, '/Users/USER/SbaProjects')

from titanic.entity import Entity
from titanic.service import Service
# 
class Controller:
    def __init__(self) :
        self.entity = Entity()
        self.service = Service()

    def preprocessing(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train) # payload
        this.test = service.new_model(test)
        return this
    
    def modelling(self, train, test) :
        service = self.service
        this = self.preprocessing(train, test)
        print(f'훈련 컬럼 : {this.train.columns}')
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this
        
    def learning(self) :
        pass

    def submit(self) :
        pass

if __name__ == '__main__':
    ctrl = Controller()
    ctrl.modelling('train.csv', 'test.csv')

