class BaseModel(object):
    ''' base model '''
    def __init__(self):
        pass

class User(BaseModel):
    ''' user model '''
    name:str
    age:int
    address:str
    wxid:str
    remain:int

    def __init__(self):
        pass
