from crawler.entity import Entity

from crawler.service import Service

# 내부에서는 모듈의 객체를 인스턴스화해야 한다.
# 대문자는 클래스
# 소문자는 인스턴스= (객체)
# 라운드 브레이스가 있는 클래스는 생성자이다.
# 결론.. 객체지향(OOP)에서는 속성과 기능을 호출하는 구조로 
# 두가지 방식이 있는데
# (스태틱)클래스 객체
# (다이나믹) 인스턴스 객체

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def naver_cartoon(self):
        service = self.service
        this = self.entity
        soup=service.get_url(this)
        myfolder=service.create_folder_from_dict(this)
        mytarget = service.setting_targets(soup,this)
        service.loop_fun(mytarget,this, myfolder)

    def movie_csv(self):
        service = self.service
        this = self.entity
        print(this.url)
        soup=service.get_url(this)

        target= service.setting_targets(soup,this)
        self.service.loop_fun2(target,this)

if __name__=='__main__':

    api = Controller()

    api.entity.dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}
    api.entity.columns = ['타이틀 번호', '요일', '제목', '링크']
    api.entity.filename = 'cartoon.csv'
    api.entity.url = 'https://comic.naver.com/webtoon/weekday.nhn'
    api.entity.new_folder_name='newfile'
    api.entity.tag='div'
    api.entity.attrs='thumb'
    api.entity.replace_str ='/webtoon/list.nhn?'

    api.naver_cartoon()

    api.entity.columns = ['순위', '제목', '변동', '변동폭']
    api.entity.url = "http://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    api.entity.tag ='tr'
    api.entity.attrs = ''
    api.entity.filename = 'naverMovieRank.csv'

    api.movie_csv()