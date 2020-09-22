<<<<<<< HEAD
# 프로퍼티는 url, parser, path, api, apikey 전부 str 타입

from dataclasses import dataclass

@dataclass
class Entity:
    url : str = '/Users/USER/SbaProjects/crawler/data/'
    parser : str = ''
    path : str = ''
    api: str = ''
=======
# 프로퍼티는 url, parser, path, api, apikey 전부 str 타입

from dataclasses import dataclass

@dataclass
class Entity:
    url : str = '/Users/USER/SbaProjects/crawler/data/'
    parser : str = ''
    path : str = ''
    api: str = ''
>>>>>>> 28f04485b005846a6db96411bd8350614e91e898
    apikey : str = ''