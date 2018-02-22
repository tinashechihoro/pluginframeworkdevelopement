from manager import Plugin

class CountHttp200(Plugin):
    def __init__(self,**kwargs):
        self.keywords = ['counter']