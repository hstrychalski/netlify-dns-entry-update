import string

class Request:

    def __init__(self, path: string, method: string, body: dict):
        self._path = path
        self._method = method
        self._body = body
        pass

    @property
    def path(self):
        return self._path

    @property
    def method(self):
        return self._method

    @property
    def body(self):
        return self._body
