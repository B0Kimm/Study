<<<<<<< HEAD
import sys
sys.path.insert(0, '/Users/USER/SbaProjects')

from crawler.entity import Entity
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame
import os, shutil

class Service :
    def __init__(self) :
        self.entity = Entity()

    def bugs_music(self) :
        pass

    def naver_movie(self) :
        pass


    def naver_cartoon(self, url) :
        parser = 'html.parser'
        url= 'https://comic.naver.com/webtoon/weekday.nhn'
        response = urlopen(url)
        soup = BeautifulSoup(response, parser)
        return soup


    def create_folder_by_week(self) :
        weekday_dict = dict()
        weekday_dict['mon'] ='월요일'
        weekday_dict['tue'] ='화요일'
        weekday_dict['wed'] ='수요일'
        weekday_dict['thu'] ='목요일'
        weekday_dict['fri'] ='금요일'
        weekday_dict['sat'] ='토요일'
        weekday_dict['sun'] ='일요일'
        
        myfolder = './simple/'

        try:
            if not os.path.exists(myfolder): 
                os.mkdir(myfolder)

            for mydir in weekday_dict.values() :
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                   
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)
        return myfolder

    @ staticmethod    
    def targets(this) :
        this = self.entity
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
    
    @ staticmethod
    def save_image_file(this,folder,src,key, title) :
        image_file = urlopen(mysrc)
        key = myweekday
        filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle +'.jpg'
        
        myfile = open(filename, mode='wb')
        myfile.write(image_file.read()) 
        myfile.close()

    @ staticmethod
    def create_csv_file(this,clist) :
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
=======
import sys
sys.path.insert(0, '/Users/USER/SbaProjects')

from crawler.entity import Entity
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame
import os, shutil

class Service :
    def __init__(self) :
        self.entity = Entity()

    def bugs_music(self) :
        pass

    def naver_movie(self) :
        pass


    def naver_cartoon(self, url) :
        parser = 'html.parser'
        url= 'https://comic.naver.com/webtoon/weekday.nhn'
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
        
        myfolder = 'c:\\simple\\'

        try:
            if not os.path.exists(myfolder): 
                os.mkdir(myfolder)

            for mydir in weekday_dict.values() :
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                   
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)
        return myfolder
    
    @ staticmethod
    def saveFile(folder,src,key, title) :
        image_file = urlopen(mysrc)
        key = myweekday
        filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle +'.jpg'
        
        myfile = open(filename, mode='wb')
        myfile.write(image_file.read()) 
        myfile.close()

    @ staticmethod    
    def targets(self) :
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

    @ staticmethod
    def create_csv_file(clist) :
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
>>>>>>> 88e3d89821e46f18a11e0022f1728d72e5a886b5
        print(filename + '파일로 저장됨')