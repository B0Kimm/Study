import sys
sys.path.insert(0, '/Users/USER/SbaProjects')

from util.file_handler import FileReader

import pandas as pd
import numpy as np

# sklearn algorithm : classification, regression, clustering, reduction(dimension)
from sklearn.tree import DecisionTreeClassifier #dtree
from sklearn.ensemble import RandomForestClassifier #rforest
from sklearn.naive_bayes import GaussianNB #nb
from sklearn.neighbors import KNeighborsClassifier #knn
from sklearn.svm import SVC #svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold # k값은 count 의미로 이해
from sklearn.model_selection import cross_val_score
# dtree,rforest,nb,knn,svm

class Service : 
    def __init__(self) :
        self.fileReader = FileReader() # @autowired Entity entity(spring) #entity 파일 불러오기

    def new_model(self, payload) -> object:
        this = self.fileReader
        this.context = '/Users/USER/SbaProjects/kaggle/data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname) #p.139(read_csv) df=tensor

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1) #train은 답이 제거된 데이터셋이다.
    
    @staticmethod
    def create_label(this) -> object: # label = 지도학습 (전처리)
        return this.train['Survived'] #label은 곧 답이 된다.

    @staticmethod
    def drop_feature(this, feature) -> object: # 데이터가 정제되어 있지 않으면 차원 축소를 해야함
        this.train = this.train.drop([feature], axis = 1) #feature를 뽑아서 지워라
        this.test = this.test.drop([feature], axis = 1) #149p
        return this

    @staticmethod
    def pclass_ordinal(this) -> object :
        return this

    @staticmethod
    def title_nominal(this) -> object :
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.',expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Mme','Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer','Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady','Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
        title_mapping = {'Mr':1, 'Miss':2, 'Mrs': 3, 'Master':4, 'Royal':5, 'Rare':6}
        for dataset in combine:
            dataset['Title'] = dataset['Title'].map(title_mapping)
            dataset['Title'] = dataset['Title'].fillna(0) #unknown
        this.train = this.train
        this.test = this.test
        return this

    @staticmethod
    def sex_nominal(this) -> object :
        combine = [this.train, this.test] # train과 test가 묶입니다.
        sex_mapping = {'male':0 , 'female': 1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)

        # this.train['Sex'] = this.train['Sex'].map({'male':0, 'female': 1}) 
        # this.test['Sex'] = this.test['Sex'].map({'male':0, 'female': 1}) 
        this.train = this.train #overriding this.train =combine[0]
        this.test = this.test # this.test =combine[1]
        return this

    @staticmethod
    def age_ordinal(this) -> object :
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        # age를 평균으로 넣기도 애매하고, 다수결로 넣기도 근거가 없다.
        # 특히 age는 생존률 판단에서 가중치(weight)가 상당하므로 디테일한 접근이 필요
        # 나이를 모르는 승객은 모르는 상태로 처리해야 값의 왜곡을 줄일 수 있어서
        # -0.5라는 (어느곳에서 속하지 않는)중간값으로 처리
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf] # []에 있으니 이것은 변수명 
        # np.inf: 범위를 뜻합니다 -1이상, 0미만, 60이상 rlxk
        labels = ['Unknown', 'Baby', 'Child', 'Teenager','Student', 'Young Adult', 'Adult', 'Senior']
        # []은 변수명으로 선언
        train['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
        test['AgeGroup'] = pd.cut(test['Age'], bins, labels=labels)
        age_title_mapping = {
            0: 'Unknown', 
            1:'Baby', 
            2:'Child', 
            3:'Teenager', 
            4:'Student',
            5:'Young Adult', 
            6:'Adult', 
            7:'Senior'
        } # labels를 값으로 처리/ 이렇게 []에서 {}으로 처리하면 labels를 값으로 처리하겠네요
        for x in range(len(train['AgeGroup'])) :
            if train['AgeGroup'][x] == 'Unknown' : 
                train['AgeGroup'][x] = age_title_mapping[train['Title'][x]]
        for x in range(len(test['AgeGroup'])) :
            if test['AgeGroup'][x] == 'Unknown' : 
                test['AgeGroup'][x] = age_title_mapping[test['Title'][x]]

        age_mapping = {
            'Unknown' : 0, 
            'Baby': 1, 
            'Child': 2, 
            'Teenager': 3, 
            'Student': 4,
            'Young Adult' : 5, 
            'Adult': 6, 
            'Senior' : 7
        }
        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)
        this.train = train
        this.test = test
        
        return this

    @staticmethod
    def sibsp_numeric(this) -> object :
        return this

    @staticmethod
    def parch_numeric(this) -> object :
        return this

    @staticmethod
    def fare_ordinal(this) -> object :
        this.train['FareBand'] = pd.qcut(this['Fare'], 4, labels={1, 2, 3, 4})
        # qcut(quarter-cut); 4등분
        this.test['FareBand'] = pd.qcut(this['Fare'], 4, labels={1, 2, 3, 4})
        return this

    @staticmethod
    def fareBand_nominal(this) -> object : # 요금이 다양하니 클러스터링을 하기 위한 준비
        this.train = this.train.fillna({'FareBand' : 1}) #FareBand는 없는 변수인데 추가
        this.test = this.test.fillna({'FareBand' : 1})
        return this

    @staticmethod
    def embarked_nominal(this) -> object :
        this.train = this.train.fillna({'Embarked':'S'}) #null 값을 S로 치환
        this.test =  this.test.fillna({'Embarked':'S'}) # 지도 학습에서 train set과 test set을 같이 코딩
        # 많은 머신러닝 라이브러리는 클래스 레이블이 *정수*로 인코딩 되었다고 기대
        # 교과서 146 문자 blue =0, green = 1, red = 2로 치환(mapping)합니다.
        this.train['Embarked'] = this.train['Embarked'].map({'S':1, 'C': 2, 'Q':3}) # ordinal이 아니므로 순서 상관 없음
        this.test['Embarked'] = this.test['Embarked'].map({'S':1, 'C': 2, 'Q':3})
        return this 

    # Machine Learning Algorithm 중에서 dtree,rforest,nb,knn,svm 이것을 대표로 사요하겠습니다.

    @staticmethod
    def create_k_fold() :
        return KFold(n_splits=10, shuffle=True, random_state=0)

    def accuracy_by_dtree(self, this):
        dtree = DecisionTreeClassifier()
        score = cross_val_score(dtree, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    def accuracy_by_rforest(self, this):
        rforest = RandomForestClassifier()
        score = cross_val_score(rforest, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    def accuracy_by_nb(self, this) :
        nb = GaussianNB()
        score = cross_val_score(nb, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    def accuracy_by_knn(self, this) :
        knn = KNeighborsClassifier()
        score = cross_val_score(knn, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    def accuracy_by_svm(self, this) :
        svm = SVC()
        score = cross_val_score(svm, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    """
    print(f'결정트리 검증결과 : {service.accuracy_by_dtree(this)}')
    print(f'랜덤포레스트 검증결과 : {service.accuracy_by_rforest(this)}')
    print(f'나이브베이즈 검증결과 : {service.accuracy_by_nb(this)}')
    print(f'KNN 검증결과 : {service.accuracy_by_knn(this)}')
    print(f'SVM 검증결과 : {service.accuracy_by_svm(this)}')
    """


class Controller:
    def __init__(self) :
        self.fileReader = FileReader()
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
        this = self.fileReader
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
        print(f'-----------------------------------TRAIN 정제 결과-----------------------------------')
        print(f'{this.train.head()}')
        print(f'-----------------------------------TEST 정제 결과-----------------------------------')
        print(f'{this.test.head()}')
        print(f'-----------------------------------TRAIN na 체크-----------------------------------')
        print(f'{this.train.isnull().sum()}')
        print(f'-----------------------------------Test na 체크-----------------------------------')
        print(f'{this.test.isnull().sum()}')

        return this
    
    def learning(self, train, test) : #모델링
        service = self.service
        this = self.modelling(train, test)
        print('===================================Learning 결과==========================')
        print(f'결정트리 검증결과 : {service.accuracy_by_dtree(this)}')
        print(f'랜덤포레스트 검증결과 : {service.accuracy_by_rforest(this)}')
        print(f'나이브베이즈 검증결과 : {service.accuracy_by_nb(this)}')
        print(f'KNN 검증결과 : {service.accuracy_by_knn(this)}')
        print(f'SVM 검증결과 : {service.accuracy_by_svm(this)}')
        return this


    def submit(self, train, test) :
        this = self.modelling(train, test)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame(
            {'PassengerId':this.id, 'Survived':prediction}
        ).to_csv(this.context +'submission.csv', index=False)
        

        
if __name__ == '__main__':
    ctrl = Controller()
    ctrl.submit('train.csv', 'test.csv')

