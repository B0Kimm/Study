<<<<<<< HEAD
class Calculator:
    def __init__(self, num1, num2) : #init: 생성자 함수
        self.num1 = num1
        self.num2 = num2
        # 속성값
    
        #함수
    def sum(self):
        return self.num1 + self.num2
    
    def subs(self) :
        return self.num1 - self.num2

    def mult(self) :
        return self.num1 * self.num2
        
    def div(self) :
        return self.num1 // self.num2

    

if __name__=='__main__':
    calc = Calculator(6, 2) # num1 =6, num2 =2 클래스 이름 정의 Calculator
    sumResult = calc.sum()
    print('덧셈 결과 : {}'.format(sumResult))

    subsResult = calc.subs()
    print('뺄셈 결과 : {}'.format(subsResult))
    
    multResult = calc.mult()
    print('곱셈 결과 : {}'.format(multResult))

    divResult = calc.div()
    print('나눗셈 결과 : {}'.format(divResult))


    # 덧셈결과 : 8
    # 뺄셈결과 : 4
    # 곱셈결과 : 12
    # 나눗셈결과 : 3
=======
class Calculator:
    def __init__(self, num1, num2) : #init: 생성자 함수
        self.num1 = num1
        self.num2 = num2
        # 속성값
    
        #함수
    def sum(self):
        return self.num1 + self.num2
    
    def subs(self) :
        return self.num1 - self.num2

    def mult(self) :
        return self.num1 * self.num2
        
    def div(self) :
        return self.num1 // self.num2

    

if __name__=='__main__':
    calc = Calculator(6, 2) # num1 =6, num2 =2 클래스 이름 정의 Calculator
    sumResult = calc.sum()
    print('덧셈 결과 : {}'.format(sumResult))

    subsResult = calc.subs()
    print('뺄셈 결과 : {}'.format(subsResult))
    
    multResult = calc.mult()
    print('곱셈 결과 : {}'.format(multResult))

    divResult = calc.div()
    print('나눗셈 결과 : {}'.format(divResult))


    # 덧셈결과 : 8
    # 뺄셈결과 : 4
    # 곱셈결과 : 12
    # 나눗셈결과 : 3
>>>>>>> 28f04485b005846a6db96411bd8350614e91e898
