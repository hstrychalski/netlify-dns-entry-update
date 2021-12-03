from api.request import Request
import string


class DnsRecordAdd(Request):
    _path = '/dns_zones/{}/dns_records'
    _method = 'POST'

    def __init__(self, zone_id: string, value: string, hostname: string, ttl=360):
        data = {
            'type': 'A',
            'value': value,
            'hostname': hostname,
            'ttl': ttl
        }
        path = self._path.format(zone_id)
        super().__init__(path, self._method, data)
