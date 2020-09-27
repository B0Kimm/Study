<<<<<<< HEAD
<<<<<<<< HEAD:util/file_handler.py
from dataclasses import dataclass
'''
context = '/Users/USER/SbaProjects/...'
fname = /titanic/data

'''
@dataclass
class FileReader:

    context : str = ''
    fname : str = ''
    train : object = None
    test: object = None
    id : str = ''
    label : str = ''
========
from dataclasses import dataclass

@dataclass
class Entity:
    context : str = '/Users/USER/SbaProjects/titanic/data/'
=======
from dataclasses import dataclass
'''
context = '/Users/USER/SbaProjects/...'
fname = /titanic/data

'''
@dataclass
class FileReader:

    context : str = ''
>>>>>>> 24429448bf9c9728c794e7114a5128e1fe34e689
    fname : str = ''
    train : object = None
    test: object = None
    id : str = ''
<<<<<<< HEAD
    label : str = ''
>>>>>>>> 24429448bf9c9728c794e7114a5128e1fe34e689:titanic/entity.py
=======
    label : str = ''
>>>>>>> 24429448bf9c9728c794e7114a5128e1fe34e689
