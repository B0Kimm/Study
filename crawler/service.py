<<<<<<< HEAD
import sys
sys.path.insert(0, '/Users/USER/SbaProjects')

from crawler.entity import Entity
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame


class Service:
    def __init__(self) :
        self.entity = Entity()
    
    def bugs_music(self) :
        pass

    def naver_movie(self) :
        pass


    def naver_cartoon(self, url) :
        parser = 'html.parser'
        url = 'https://comic.naver.com/webtoon/weekday.nhn'
        response = urlopen(url)
        soup = BeautifulSoup(response, parser)
        return soup

    
    def create_folder_week(self) :
        weekday_dict = dict()
        weekday_dict['mon'] ='월요일'
        weekday_dict['tue'] ='화요일'
        weekday_dict['wed'] ='수요일'
        weekday_dict['thu'] ='목요일'
        weekday_dict['fri'] ='금요일'
        weekday_dict['sat'] ='토요일'
        weekday_dict['sun'] ='일요일'

        import os, shutil
        myfolder = 'c:\\sample\\'

        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)
            
            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath) :
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)

    
    def save_img(self) :
        image_file = urlopen(mysrc)
        filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle +'.jpg'
        
        myfile = open(filename, mode='wb')
        myfile.write(image_file.read()) 
        myfile.close()
        
        mytarget = soup.find_all('div', attrs = {'class':'thumb'})
        mylist = []

        for abcd in mytarget :
            myhref = abcd.find('a').attrs['href']
            myhref = myhref.replace('/webtoon/list.nhn?', '')
            result = myhref.split('&')
        
            mytitleid=result[0].split('=')[1]
            myweekday = result[1].split('=')[1]

            imgtag = abcd.find('img')
            mytitle = imgtag.attrs['title'].strip()
            mytitle = mytitle.replace('?','').replace(':','')
    

            mysrc = imgtag.attrs['src']
            saveFile(mysrc, myweekday, mytitle)

    def create_csv_file(self, clist) :
        sublist = []
        sublist.append(mytitleid)
        sublist.append(myweekday)
        sublist.append(mytitle)
        sublist.append(mysrc)
        clist.append(sublist)

        mycolumns = ['타이틀 번호','요일','제목','링크']
        myframe = DataFrame(mylist, columns=mycolumns)

        filename ='cartoon.csv'

        myframe.to_csv(filename, encoding = 'utf-8', index = False)
        print(filename + '파일로 저장됨')
=======
import sys
sys.path.insert(0, '/Users/USER/SbaProjects')

from crawler.entity import Entity
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame


class Service:
    def __init__(self) :
        self.entity = Entity()
    
    def bugs_music(self) :
        pass

    def naver_movie(self) :
        pass


    def naver_cartoon(self, url) :
        parser = 'html.parser'
        url = 'https://comic.naver.com/webtoon/weekday.nhn'
        response = urlopen(url)
        soup = BeautifulSoup(response, parser)
        return soup

    
    def create_folder_week(self) :
        weekday_dict = dict()
        weekday_dict['mon'] ='월요일'
        weekday_dict['tue'] ='화요일'
        weekday_dict['wed'] ='수요일'
        weekday_dict['thu'] ='목요일'
        weekday_dict['fri'] ='금요일'
        weekday_dict['sat'] ='토요일'
        weekday_dict['sun'] ='일요일'

        import os, shutil
        myfolder = 'c:\\sample\\'

        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)
            
            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath) :
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)

    
    def save_img(self) :
        image_file = urlopen(mysrc)
        filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle +'.jpg'
        
        myfile = open(filename, mode='wb')
        myfile.write(image_file.read()) 
        myfile.close()
        
        mytarget = soup.find_all('div', attrs = {'class':'thumb'})
        mylist = []

        for abcd in mytarget :
            myhref = abcd.find('a').attrs['href']
            myhref = myhref.replace('/webtoon/list.nhn?', '')
            result = myhref.split('&')
        
            mytitleid=result[0].split('=')[1]
            myweekday = result[1].split('=')[1]

            imgtag = abcd.find('img')
            mytitle = imgtag.attrs['title'].strip()
            mytitle = mytitle.replace('?','').replace(':','')
    

            mysrc = imgtag.attrs['src']
            saveFile(mysrc, myweekday, mytitle)

    def create_csv_file(self, clist) :
        sublist = []
        sublist.append(mytitleid)
        sublist.append(myweekday)
        sublist.append(mytitle)
        sublist.append(mysrc)
        clist.append(sublist)

        mycolumns = ['타이틀 번호','요일','제목','링크']
        myframe = DataFrame(mylist, columns=mycolumns)

        filename ='cartoon.csv'

        myframe.to_csv(filename, encoding = 'utf-8', index = False)
        print(filename + '파일로 저장됨')
>>>>>>> 28f04485b005846a6db96411bd8350614e91e898
