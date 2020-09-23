import sys
sys.path.insert(0, '/Users/USER/SbaProjects')

from titanic.entity import Entity
from titanic.service import Service

class Controller:
    def __init__(self) :
        self.entity = Entity()
        self.service = Service()

    def modelling(self, train, test) :
        service = self.service
        this = self.preprocessing(train, test)
        # print(f'훈련 컬럼 : {this.train.columns}')
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this
        
    def preprocessing(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train) # payload
        this.test = service.new_model(test)
        this.id = this.test['PassengerId'] # 머신에게는 이것이 Question이 됩니다.
        print(f'variables/features before drop : {this.train.columns}')
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        print(f'variables/features after drop : {this.train.columns}')

        this = service.embarked_nominal(this)
        print(f'승선한 항구 정제 결과 : {this.train.head()}')
        this = service.title_nominal(this)
        print(f'타이틀 정제 결과 : {this.train.head()}')
        # name 변수에서 title을 추출했으니 name은 필요가 없어졌고, str이니
        # 후에 ML-lib가 이를 인식하는 과정에서 에러를 발생시킬것이다.
        this = service.drop_feature(this, 'Name')
        this = service.drop_feature(this, 'PassengerId')
        this = service.age_ordinal(this)
        print(f'나이 정제 결과 : {this.train.head()}')
        this = service.sex_nominal(this)
        print(f'성별 정제 결과 : {this.train.head()}')
        this = service.fareBand_nominal(this)
        print(f'요금 정제 결과 : {this.train.head()}')
        this = service.drop_feature(this, 'Fare')
        print(f'전체 정제 결과 : {this.train.head()}')
        print(f'train na 정제 결과 : {this.train.isnull().sum()}')
        print(f'test na 정제 결과 : {this.train.isnull().sum()}')

        return this
    
    def learning(self) :
        pass

    def submit(self) : # machine이 된다. 이 단계에서는 캐글에게 내 머신을 보내서 평가 받게 하는 것
        pass

if __name__ == '__main__':
    ctrl = Controller()
    ctrl.modelling('train.csv', 'test.csv')

