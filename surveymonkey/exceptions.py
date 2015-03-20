
class SurveyMonkeyWarning(UserWarning):
    pass


class APIError(Exception):
    pass

    
class APIRequestError(APIError):
    """Problem with connection, parsing json, timeout or any other response with
    non 200 HTTP code

    """
    def __init__(self, response, error):
        self.response = response
        self.error = error
        super(APIRequestError, self).__init__(error.message)


class SurveyMonkeyAPIError(APIError):
    """"""
    error = "Unknown Error"
    error_code = None
    error_description = None

    def __init__(self, response, error_description):
        self.response = response
        if error_description:
            self.error_description = error_description
        super(SurveyMonkeyAPIError, self).__init__()

    def __str__(self):
        return "%s (%s): %s" % (self.error, self.error_code, self.error_description)


    def __repr__(self):
        return "<%s> %s" % (self.__class__.__name__, self)


class SurveyMonkeyNotAuthenticated(SurveyMonkeyAPIError):
    error = "Not Authenticated"
    error_code = 1
    
class SurveyMonkeyInvalidUserCredentials(SurveyMonkeyAPIError):
    error = "Invalid User Credentials"
    error_code = 2

class SurveyMonkeyInvalidRequest(SurveyMonkeyAPIError):
    error = "Invalid Request"
    error_code = 3
    
class SurveyMonkeyUnknownUser(SurveyMonkeyAPIError):
    error = "Unknown User"
    error_code = 4
    
class SurveyMonkeySystemError(SurveyMonkeyAPIError):
    error = "System Error"
    error_code = 5

