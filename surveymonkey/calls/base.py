import warnings, datetime

from surveymonkey.exceptions import SurveyMonkeyWarning



class Call(object):
    """ Base class for all API calls """

    _api = None
    date_params = (
        'start_date', 'end_date', 'start_modified_date', 'end_modified_date'
    )

    @property
    def call_name(self):
        return self.__class__.__name__.lower()

    def __init__(self, api):
        self._api = api

    def _update_params(self, params, extra_kwargs):
        control_kwargs = {}
        for key in ('access_token', 'timeout'):
            if key in extra_kwargs:
                control_kwargs[key] = extra_kwargs.pop(key)
        params.update(extra_kwargs)
        return control_kwargs

    def make_call(self, func, params, extra_kwargs):
        if hasattr(func, '__name__'):
            uri = '/%s/%s' % (self.call_name, func.__name__[2:])
        else:
            uri = '/%s' % self.call_name
        control_kwargs = self._update_params(params, extra_kwargs)
        if not self._api.silent:
            unrecognized_params = set(params) - set(func.allowed_params)
            if unrecognized_params:
                err_msg = (
                    "At least one of the parameters to the api call: '%s' is "
                    "unrecognized. Allowed parameters are: '%s'. Unrecognized "
                    "parameters are: '%s'." % (uri, ', '.join(func.allowed_params), 
                                               ', '.join(unrecognized_params)))
                warnings.warn(err_msg, SurveyMonkeyWarning)
        for name in self.date_params:
            value = params.get(name)
            if value is not None and isinstance(datetime.date):
                params[name] = value.strftime("%Y-%m-%d %H:%M:%S")
        return self._api.call(uri, params=params, **control_kwargs)
