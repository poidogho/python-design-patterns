class Adapter:
    def __init__(self, object, **adaptedMethod):
        self._object = object
        self.__dict__.update(adaptedMethod)

    def __getattr__(self, attr):
        return getattr(self._object, attr)
