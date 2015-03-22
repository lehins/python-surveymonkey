import json, requests

from surveymonkey.calls import *
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
        try:
            self.response_json = response.json()
        except ValueError as exc:
            raise APIRequestError(response, exc)
        self.status = self.response_json.get('status')
        self.data = self.response_json.get('data')
        self.upgrade_info = self.response_json.get('upgrade_info')
        if self.status > 0:
            self._raise_from_code(self.status)

    def _raise_from_code(self, error_code):
        try:
            error_class = self._api_errors[error_code-1]            
        except IndexError:
            error_class = SurveyMonkeyAPIError
        raise error_class(self, self.response_json.get('errmsg'))        

        
class SurveyMonkey(object):
    api_endpoint = "https://api.surveymonkey.net/v2"

    def __init__(self, api_key, access_token=None, timeout=30, silent=False):
        self._api_key = api_key
        self._access_token = access_token
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
                "api_key": self._api_key
            }
            return client
        
    @cached_property
    def batch(self):
        return Batch(self)

    @cached_property
    def surveys(self):
        return Surveys(self)
        
    @cached_property
    def collectors(self):
        return Collectors(self)
        
    @cached_property
    def templates(self):
        return Templates(self)
        
    @cached_property
    def user(self):
        return User(self)
        
    def call(self, uri, params=None, timeout=None, access_token=None):
        url = self.api_endpoint + uri
        params = params or {}
        data = json.dumps(params)
        timeout = timeout or self._timeout
        client = self.client if access_token is None \
                 else self._get_client(access_token)
        if client is None:
            raise TypeError("access_token is required to make an API call.")
        try:
            response = client.post(url, data=data, timeout=timeout)
            response.url = url
            response.params = params
        except requests.exceptions.RequestException as exc:
            raise APIRequestError(exc.response, exc)
        return APIResponse(response)
        
