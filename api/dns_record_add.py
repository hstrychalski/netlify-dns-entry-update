from api.request import Request
import string


class DnsRecordAdd(Request):
    _path = '/dns_zones/{}/dns_records'
    _method = 'POST'

    def __init__(self, zone_id: string, value: string, hostname: string, ttl = 360):
        data = {
            "value": value,
            "hostname": hostname,
            "ttl": ttl,
            # "priority": 0,
            # "weight": 0,
            # "port": 0,
            # "flag": 0,
            # "tag": "string"
        }
        path = self._path.format(zone_id)
        super().__init__(path, self._method, data)
