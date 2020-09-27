클래스 하나가 단위 unit이 됩니다.
이제 확장을 하겠습니다.
객체 지향에서는 디자인패턴이라는 개념이 존재합니다.
1994년 GoF 4인방 개발자 에릭 감마 .. 23가지 패턴으로 정의 (VScode 개발자)

패턴 조합을 통해 큰 개념의 패턴 -> MVC 패턴이라고 합니다.
model, view, controller 이렇게 조합합니다. -> Java, C언어에서 주로 사용하는 개념.

model : 데이터처리 -> API 서버 -> Python -> Tensorflow
view : 화면 UI 처리 -> UI 서버 -> Reactjs
controller : model + view를 연결 ---> 네트워크 처리 -> Flask (app.py) ->Restful

Backend Tier (API 서버 구축 담당 : Java, C, Python)
Frontend Tier (UI 서버 구축 담당 : Javascript, HTML, Reactjs)

모델을 제작하고 뷰를 만들어서 컨트롤러로 연결한다.
프로토타입 입니다.

독자적으로 움직이는 ---> 모듈
5개의 모듈(개인이 작성)을 합쳤을 때, 조립이 잘 되서 작동이 잘 되면 1 단계를 패스

캐글

dataset(test.csv, train.csv)를 모델에 추가했습니다.

titanic 폴더에
dataset(test.csv, train.csv)가 존재하고
entity (속성), service (기능) = 객체(object)

def __init__(self, ....) => 속성
def abc() : => 기능
결국 class는 객체를 정의하는 것이다.

class가 여러개 (entity, service) 모여서 다시 큰 개념의 객체를 이룬다. 그때, 이것은 클래스가 아닌 model이라고 한다.

패키지는 같은 컨셉을 공유하는 클래스의 집합... 모듈 --(진화)---> 모델
모델에 AI 개념이 없으면 web에서 말하는 모델이고
AI 개념이 존재하면 인공지능 모델이 된다.

여기서 AI 개념이라고 하면 결국, 머신러닝(기계학습) 코딩의 유무
dataset을 추가하면 이를 지도학습이라고 합니다.
dataset이 없으면 이를 비지도학습이라고 합니다.

지금 타이타닉은 dataset을 모델에 넣었으므로 이는 지도학습을 하겠다는 의미

