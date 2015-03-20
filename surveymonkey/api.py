import json, requests

from surveymonkey.exceptions import *
from surveymonkey.utils import cached_property

class APIResponse(object):
    data = None
    status = None
    upgrade_info = None
    _api_errors = (
        SurveyMonkeyNotAuthenticated,
        SurveyMonkeyInvalidUserCredentials,
        SurveyMonkeyInvalidRequest,
        SurveyMonkeyUnknownUser,
        SurveyMonkeySystemError
    )

    def __init__(self, response):
        self.response = response
        self.status = response.get('status')
        self.data = response.get('data')
        self.upgrade_info = response.get('upgrade_info')
        if self.status > 0:
            self._raise_from_code(self.status)

    def raise_from_code(self, error_code):
        try:
            error_class = self._api_errors[error_code-1]
        except KeyError:
            error_class = SurveyMonkeyAPIError
        raise error_class(self)
        

class SurveyMonkey(object):
    api_endpoint = "https://api.surveymonkey.net/v2/"

    def __init__(self, api_key, access_token=None, timeout=30, silent=False):
        self._api_key = api_key
        self._timeout = timeout
        self.silent = silent
        self.client = self._get_client(access_token)

    def _get_client(self, access_token):
        if access_token is not None:
            client = requests.session()
            client.headers = {
                "Authorization": "bearer %s" % access_token,
                "Content-Type": "application/json"
            }
            client.params = {
                "api_key": self.api_key
            }
            return client
        
    @cached_property
    def batch(self):
        return Batch(self)

    def call(self, uri, params=None, timeout=None, access_token=None):
        url = self.api_endpoint + uri
        data = json.dumps(params or {})
        timeout = timeout or self._timeout
        if access_token is None:
            client = self.client
        else:
            client = self._get_client(access_token)
        if client is None:
            raise TypeError("access_token is required to make an API call.")
        try:
            response = client.post(url, data=data, timeout=timeout).json()
        except requests.exceptions.RequestException as exc:
            raise SurveyMonkeyAPIConnectionError(exc)
        return APIResponse(response)
        
