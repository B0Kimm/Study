from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
db = SQLAlchemy

config = {
    'user' : 'root',
    'password' : '1793456',
    'host' : 'localhost',
    'port': '3306',
    'database' : 'mariadb'

}

charset = {'utf8' : 'utf8'}
url = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset=utf8"
('mysql+mysqlconnector://root:1793456@127.0.0.1/mariadb?charset=utf8', encoding='utf8', echo=True)


# root에 정의하면 static 객체가 된다.