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
            if response.status_code != 200:
                raise RuntimeError(response.json())

        if request.method == 'POST':
            response = self.post(request.path, data=request.body)
            if response.status_code != 201:
                raise RuntimeError(response.json())

        if request.method == 'DELETE':
            response = self.delete(request.path)
            if response.status_code != 204:
                raise RuntimeError(response.json())

        if response is not None:
            try:
                return response.json()
            except ValueError:
                return {}

        raise RuntimeError('Unsupported method: ' + request.method)


    def get(self, path: string):
        return requests.get(self._api_base_url + path, headers=self._headers)

    def post(self, path: string, data: dict):
        return requests.post(self._api_base_url + path, json=data, headers=self._headers)

    def delete(self, path):
        return requests.delete(self._api_base_url + path, headers=self._headers)
