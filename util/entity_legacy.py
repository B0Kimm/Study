class Entity:
    
    # 밑의 것이 위의 것으로 간소화 됨     
    def __init__(self, context, fname, train, test, id, label):
         self._context = context # _ 1개는 default 접근 의미, _ 2개는 private 접근 의미
         self._fname = fname
         self._train = train
         self._test = test
         self._id = id
         self._label = label

    # get, set을 만듭니다.
    
    @property #decorator
    def context(self) -> str: 
        return self._context

    @context.setter
    def context(self, context) :
        self._context = context

    
    # fname get, set을 만듭니다.

    @property
    def fname(self) -> str: 
        return self._fname

    @fname.setter
    def fname(self, fname) :
        self._fname = fname
    
    # train get, set을 만듭니다.

    @property
    def train(self) -> str: 
        return self._train

    @train.setter
    def train(self, train) :
        self._train = train
    
    # test get, set을 만듭니다.

    @property
    def test(self) -> str: 
        return self._test

    @test.setter
    def test(self, test) :
        self._test = test
   
    # id get, set을 만듭니다.

    @property
    def id(self) -> str: 
        return self._id

    @id.setter
    def id(self, id) :
        self._id = id

    # label get, set을 만듭니다.

    @property
    def label(self) -> str: 
        return self._label

    @label.setter
    def label(self, label) :
        self._label = label
