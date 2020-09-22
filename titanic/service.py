import sys
sys.path.insert(0, '/Users/USER/SbaProjects')

from titanic.entity import Entity
import pandas as pd
import numpy as np

"""
PassengerId  고객ID,
Survived 생존여부, -> 머신 러닝 모델이 맞춰야 할 답
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
"""

class Service : 
    def __init__(self) :
        self.entity = Entity() # @autowired Entity entity(spring) #entity 파일 불러오기

    def new_model(self, payload) -> object:
        this = self.entity
        
        this.fname = payload
        return pd.read_csv(this.context + this.fname) #p.139(read_csv) df=tensor

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1) #train은 답이 제거된 데이터셋이다.
    
    @staticmethod
    def create_label(this) -> object: # label = 지도학습
        return this.train['Survived'] #label은 곧 답이 된다.

    @staticmethod
    def drop_feature(this, feature) -> object: # 데이터가 정제되어 있지 않으면 차원 축소를 해야함
        this.train = this.train.drop([feature], axis = 1) #feature를 뽑아서 지워라
        this.test = this.test.drop([feature], axis = 1) #149p
        return this



