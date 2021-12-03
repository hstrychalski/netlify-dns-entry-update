import string, requests
from api.request import Request

class Client():

    def __init__(self, access_token: string, api_base_url: string):
        self._headers = {
            'Content-Type': 'application/json'
        }
        self._headers['Authorization'] = 'Bearer ' + access_token
        self._api_base_url = api_base_url

    def send_request(self, request: Request):
        response = None
        if request.method == 'GET':
            response = self.get(request.path)

        if request.method == 'POST':
            response = self.post(request.path, request.body)

        if request.method == 'DELETE':
            response = self.delete(request.path)

        if response is not None:
            return response.json()

        raise RuntimeError('Unsupported method: ' + request.method)


    def get(self, path: string):
        return requests.get(self._api_base_url + path, headers=self._headers)

    def post(self, path: string, data: dict):
        return requests.post(self._api_base_url + path, data, headers=self._headers)

    def delete(self, path):
        return requests.delete(self._api_base_url + path, headers=self._headers)
