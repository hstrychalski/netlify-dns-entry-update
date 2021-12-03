from api.request import Request

class DnsZonesGet(Request):

    _path ='dns_zones'
    _method = 'GET'

    def __init__(self):
        super().__init__(self._path, self._method, None)
