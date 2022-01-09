from berg import Berg


class Singleton(Berg):
    def __init__(self, **kwargs):
        Berg.__init__(self)
       #  update the dictionary of employees with new wmployees
        self._orezimeEmployees.update(kwargs)

    def __str__(self):
        return str(self._orezimeEmployees)
