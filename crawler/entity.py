from dataclasses import dataclass

@dataclass
class Entity:
    url : str = '/Users/USER/SbaProjects/crawler/data/'
    parser : str = ''
    path : str = ''
    api : str = ''
    apikey : str = ''