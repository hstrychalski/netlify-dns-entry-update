import string, json, os, socket
from typing import List
from requests import get
from api.client import Client
from api.dns_record_delete import DnsRecordsDelete
from api.dns_record_add import DnsRecordAdd
from api.dns_records_get import DnsRecordsGet
from api.dns_zones_get import DnsZonesGet
from api.helper import get_absolute_path

class DnsRecordsUpdateRunner():

    def __init__(self):
        self._config = self.read_config()
        self._client = Client(self._config['accessToken'], self._config['baseApiUrl'])

    def read_config(self) -> dict:
        config_filename = get_absolute_path('config.json')
        with open(config_filename) as config:
            return json.load(config)

    def run(self):
        ip = self.get_current_ip()

        zone_id = self.get_dns_zone_id()
        dns_records = self.get_outdated_dns_records(zone_id, ip)
        self.remove_outdated_dns_records(zone_id, dns_records)
        self.push_new_dns_records(zone_id, ip, dns_records)

    def get_dns_zone_id(self) -> string:
        target_dns_zone = self._config['dnsZoneName']
        req = DnsZonesGet()
        zones = self._client.send_request(req)

        for zone in zones:
            if zone['name'] == target_dns_zone:
                return zone['id']

        raise RuntimeError('Target zone not found')

    def get_outdated_dns_records(self, zone_id: string, current_ip: string) -> List:
        req = DnsRecordsGet(zone_id)
        target_record_names = self._config['domains']

        outdated_records = []
        dns_records = self._client.send_request(req)
        for dns_record in dns_records:
            if dns_record['hostname'] in target_record_names and dns_record['value'] != current_ip:
                outdated_records.append({
                    'id': dns_record['id'],
                    'hostname': dns_record['hostname']
                })

        return outdated_records

    def remove_outdated_dns_records(self, zone_id: string, dns_records: []):
        for dns_record in dns_records:
            req = DnsRecordsDelete(zone_id, dns_record['id'])
            self._client.send_request(req)

    def push_new_dns_records(self, zone_id: string, value: string, records: []):
        for record in records:
            req = DnsRecordAdd(zone_id, value, record['hostname'])
            self._client.send_request(req)

    def get_current_ip(self) -> string:
        ip = get('https://api.ipify.org').content.decode('utf8')
        try:
            socket.inet_aton(ip)
            return ip
        except socket.error:
            raise RuntimeError("Invalid ip address received from api: " + ip)