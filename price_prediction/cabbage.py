<<<<<<< HEAD
import sys
sys.path.insert(0, '/Users/USER/SbaProjects')
from util.file_handler import FileReader
import pandas as pd
import numpy as np
import tensorflow as tf
from dataclasses import dataclass

@dataclass
class Cabbage:
    
    # year,avgTemp,minTemp,maxTemp,rainFall,avgPrice
    # 20100101,-4.9,-11,0.9,0,2123
    # 멤버변수
    year : int = 0
    avgTemp: float = 0.0
    minTemp: float = 0.0
    maxTemp: float = 0.0
    rainFall: float = 0.0
    avgPrice: int =0

    # 클래스 내부에서 공유하는 객체, 상수값
    def __init__(self):
        self.fileReader = FileReader() # 안바뀜. 기능은 -> 상수로 처리
        self.context = '/Users/USER/SbaProjects/price_prediction/data/'


    def new_model(self, payload) -> object:
        this = self.fileReader
        this.context = self.context
        this.fname = payload
        return pd.read_csv(this.context + this.fname, sep=',')

    def create_tf(self, payload):
        xy = np.array(payload, dtype=np.float32)
        x_data = xy[:,1:-1] # feature
        y_data = xy[:,[-1]] # price
        X = tf.compat.v1.placeholder(tf.float32, shape=[None, 4])
        Y = tf.compat.v1.placeholder(tf.float32, shape=[None, 1])
        W = tf.Variable(tf.random.normal([4, 1]), name='weight')
        b = tf.Variable(tf.random.normal([1]), name='bias')
        hyposthesis = tf.matmul(X, W) + b
        cost = tf.reduce_mean(tf.square(hyposthesis - Y))
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.000005)
        train = optimizer.minimize(cost)
        sess = tf.compat.v1.Session()
        sess.run(tf.compat.v1.global_variables_initializer())
        for step in range(100000):
            cost_, hypo_, _ = sess.run([cost, hyposthesis, train], feed_dict={X: x_data, Y: y_data})
            if step % 500 == 0:
                print(f'# {step} 손실비용: {cost_} ')
                print(f'- 배추가격 : {hypo_[0]}')

        saver = tf.compat.v1.train.Saver()
        saver.save(sess, self.context+'saved_model.ckpt')
        print('저장완료')

    def test(self) :
        self.avgPrice = 100
        return self.avgPrice

    def service(self):
        print('################### service ##################')
        X = tf.compat.v1.placeholder(tf.float32, shape=[None, 4])
        # year,avgTemp,minTemp,maxTemp,rainFall,avgPrice
        # 에서 avgTemp,minTemp,maxTemp,rainFall 입력받겠다
        # year는 모델에서 필요 없는 값 -> 상관 관계 없음
        # avgPrice는 얻고자 하는 답; 종속변수
        # avgTemp,minTemp,maxTemp,rainFall는 종속변수를 결정하는 독립 변수
        # 그리고 avgPrice를 결정하는 요소로 사용되는 파라미터(이것이 중요!!)
        # 이제 우리는 통계와 확률로 들어감. 용어 정의!!
        # y = ax + b 선형관계 linear regression
        # X는 대문자를 사용하고 확률 변수라고 합니다.
        # 비교. 웹프로그래밍(C, Java) 소문자 x 이렇게 하는데 이것은 한 타음에 하나의 value
        # 그리고 그 값은 외부에서 주어지는 하나의 값이므로 그냥 -- 변수
        # 지금은 X의 값이 제한적이지만 집합 상태로 많은 값이 있는 상태
        # 이럴때는 확률 -- 변수
        W = tf.Variable(tf.random.normal([4, 1]), name='weight')
        b = tf.Variable(tf.random.normal([1]), name='bias')
        # 텐서에서 변수는 웹에서 변수와 다릅니다.
        # 이 변수를 결정하는 것은 외부값이 아니라 텐서가 내부에서 사용하는 변수입니다.
        # 기존 웹에서 사용하는 변수는 placeholder 입니다.
        saver = tf.train.Saver()
        with tf.Session() as sess:
            sess.run(tf.compat.v1.global_variables_initializer())
            saver.restore(sess, self.context+'saved_model.ckpt')
            print(f'avgTemp :{self.avgTemp} , minTemp: {self.minTemp}, maxTemp: {self.maxTemp}, rainFall: {self.rainFall}')
            data = [[self.avgTemp, self.minTemp, self.maxTemp, self.rainFall],]
            arr = np.array(data, dtype = np.float32)
            dict = sess.run(tf.matmul(X, W) + b, {X: arr[0:4]})
            # Y = WX + b 를 코드로 표현하면 위 처럼
            # y = wx + b
            print(dict[0])
        return int(dict[0])

if __name__ == '__main__':
    cabbage= Cabbage()
    # 체크포인트 만들기
    # dframe = cabbage.new_model('price_data.csv')
    # print(dframe.head())
    # cabbage.create_tf(dframe)
    print(cabbage.test())
=======
import sys
sys.path.insert(0,'/Users/USER/SbaProjects' )
from util.file_handler import FileReader
import pandas as pd
import numpy as np
import tensorflow as tf

class Model : 
    def __init__(self):
        self.fileReader = FileReader()
    
    def new_model(self, payload) -> object :
        this = self.fileReader
        this.context = '/Users/USER/SbaProjects/price_prediction/data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname, sep = ',')

    def create_tf(self, payload) :
        xy = np.array(payload, dtype=np.float32)
        x_data = xy[:,1:-1] #feature
        y_data =xy[:,[-1]] #price
        X = tf.compat.v1.placeholder(tf.float32, shape =[None,4])
        Y = tf.compat.v1.placeholder(tf.float32, shape =[None,2])
        W = tf.Variable(tf.random.normal([4, 1]), name='weight')
        b = tf.Variable(tf.random.normal([1]), name='bias')
        hypothesis = tf.matmul(X, W) + b
        cost = tf.reduce_mean(tf.square(hypothesis - Y))
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.00005)
        train = optimizer.minimize(cost)
        sess = tf.compat.v1.Session()
        sess.run(tf.compat.v1.global_variables_initializer())
        for step in range(100000) :
            cost_, hypo_, =sess.run([cost, hypothesis, train],
                                    feed_dict={X:x_data, Y:y_data})
            if step % 500 == 0:
                print(f'# {step} 손실비용: {cost_}')
                print(f'- 배추가격 : {hypo_[0]}')

        saver = tf.compat.v1.train.Saver()
        print('저장완료')



# if __name__ == "__main__":
#     m=Model()
#     dframe = m.new_model('price_data.csv')
#     print(dframe.head())
>>>>>>> 24429448bf9c9728c794e7114a5128e1fe34e689
