# 프로퍼티는 url, parser, path, api, apikey 전부 str 타입

from dataclasses import dataclass

@dataclass
class Entity:
    url : str = '/Users/USER/SbaProjects/crawler/data/'
    parser : str = ''
    path : str = ''
    api: str = ''
    apikey : str = ''