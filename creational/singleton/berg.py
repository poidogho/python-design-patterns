# this class will make its attributes global
class Berg:
    _orezimeEmployees = {}

    def __init__(self):
        self.__dict__ = self._orezimeEmployees
        pass
