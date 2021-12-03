from api.request import Request
import string

class DnsRecordsDelete(Request):

    _path = '/dns_zones/{}/dns_records/{}'
    _method = 'DELETE'

    def __init__(self, zone_id: string, dns_record_id: string):
        path = self._path.format(zone_id, dns_record_id)
        super().__init__(path, self._method, None)
