객체(Object) = 기능(function) + 속성(Property, Attribute, Feature) => 파라미터( AI 파트 )
하나의 {..}에 같이 있음

brace 의 종류 : () round/{}curl/[]square brace 총 3가지(전 프로그래밍 공통)
() 컨디션, 파라미터존, 튜플
{} 블락, JSON, Dict
[] array,
[[]] matrix
 ====> notation이라고 합니다.
 ====> 언어기호학


기본적으로 컴공 0,1만이 존재합니다. 이진수 binary code

George Boole https://en.wikipedia.org/wiki/George_Boole
T,F로 판단 1850 ----> 전선 (모스부호) ----> 컴퓨터

선택지는 하상 두가지 중에 하나를 선택하는 구조 -> 컴공의 해법

on, off의 개념이다. 
요소가 존재와 비존재로 종류가 나뉜다. -> Deicision Tree(Origin AI Algorithm)

Q 객체지향 vs 함수형 프로그래밍을 구분하는 기분은 무엇이 있고 없고인가?
속성이 있으면 객체지향, 없으면 함수형 프로그래밍

__init__: 생성자 함수 --> 인스턴스(객체) 만드는 함수 
    __(underscore) 2개 사용 = 접근제한(private)

객체 지향


Conclusion : 객체 지향은 속성이 존재해야 한다. 그리고 속성을 정의하는 곳(define)은 __init__(속성 파라미터)이다.
(parameter = input value)
self는 객체내부의 속성에 접근하는 키워드
속성은 은닉화때문에 반드시 self. 로만 접근할 수 있다.
보안의 기본처리이다(은닉화). __init__은 클래스 내부에서만 접근한다.


클래스 내부에서 메소드의 종류?
기준 : self
self exist dynamic -> 데이터를 메모리에서 메소드가 유효한 시간동안만 존재, 그 메소드가 소멸된 후 값은 self에 저장
self !exist static -> 반 영속적으로 저장됨 

Dynamic(동적) , Static(정적)
def print_info(self) - dynamic
@staticmethod (anotation) - static