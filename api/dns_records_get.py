from api.request import Request
import string

class DnsRecordsGet(Request):

    _path ='dns_zones/{}/dns_records'
    _method = 'GET'

    def __init__(self, zone_id: string):
        path = self._path.format(zone_id)
        super().__init__(path, self._method, None)
