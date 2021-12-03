import string
from typing import Optional

class Request:

    def __init__(self, path: string, method: string, body: Optional[dict]):
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
