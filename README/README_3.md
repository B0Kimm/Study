ML : 지도, 비지도, 강화
ML Process 4 :
1. Preprocessing
2. modelling
3. Learning
4. evaluation

ML Algorithm
0. 뉴런(neuron)
1. 회귀
2. 분류
3. SVM
4. dtree(decision tree)
5. kmean = cluster
6. PCA
7. RF (R-forest)
8. NLP
9. DL (Deep learning)
----Chatper3-------

Tensorflow

--------------------------
비지니스 로직 - service
processing하는 파일명
    1. Preprocessing
    2. modelling
    3. Learning/evaluation
    4. 완성되면 Submit(파일로 저장)

# 외부에 있는 파이썬 파일(.py)을 import해야 속성, 기능을 사용할 수 있다.
# 내부에서는 이것을 인스턴스화(instance)해야 한다
# entity = Entity()
# 이때 소문자 entitiy는 인스턴스라고 하고 이를 객체로 정의한다.
# 대문자 Entitiy는 클래스
# 라운드 브레이스가 있는 Entity()는 생성자라고 한다.
# 결론..객체지향(OOP)에서는 속성과 기능을 호출하는 구조로
# 두가지 방식이 있는데
# calc = Calculator() 있다고 하면
# calc는 인스턴스 객체가 되고
# Calculator는 클래스 객체(스태틱)이라고 한다.
# calc.sum()하면 인스턴스 호출방식 = 다이나믹
# Calculator.sum()하면 클래스 호출방식 = 스태틱이라 한다.
from titanic.entity import entity
from titanic.service import Service

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

===================================

payload 페이로드(컴퓨팅) : 전송되는 데이터

this.fname = payload ; setter 할당연산자 (=) 있으면 setter
this.fname만 있으면 ; getter 할당연산자 (=) 없으면 getter

====================================
passengerId, Survived ... => 메타데이터 = 스키마 = features =  variables =  property
1, 0, 3 .... => row, 행, 인스턴스, raw 데이터


====================================================

차원 (dim)

variable (변수) x=3 스칼라, 0차원
array [] = {1, 2, 3} 벡터, 1차원이 되고, array 내부에서 variable은 element가 된다
matrix [[]] = {{1, 2, 3}, {4, 5, 6}} 매트릭스, 2차원 (pandas; Dataframe), array라 하지 않고 vector라고 한다.

===================================
지도 학습에서 반드시 해야할 일은 dataset을 생성하는 것이니다.
그 때 dataset은 반드시 train, test 두가지 형태로 작성합니다. p.149