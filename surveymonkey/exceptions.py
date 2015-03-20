
class SurveyMonkeyWarning(UserWarning):
    pass


class SurveyMonkeyError(Exception):
    pass

    
class SurveyMonkeyAPIConnectionError(SurveyMonkeyError):
    """Problem with connection, parsing json, timeout or any other response with
    non 200 HTTP code

    """
    def __init__(self, error):
        self.error = error
        super(SurveyMonkeyAPIConnectionError, self).__init__(error.message)


class SurveyMonkeyAPIError(SurveyMonkeyError):
    """"""
    message = "Unknown Error"
    error_code = None

    def __init__(self, response):
        self.response = response


class SurveyMonkeyNotAuthenticated(SurveyMonkeyAPIError):
    message = "Not Authenticated"
    error_code = 1
    
class SurveyMonkeyInvalidUserCredentials(SurveyMonkeyAPIError):
    message = "Invalid User Credentials"
    error_code = 2

class SurveyMonkeyInvalidRequest(SurveyMonkeyAPIError):
    message = "Invalid Request"
    error_code = 3
    
class SurveyMonkeyUnknownUser(SurveyMonkeyAPIError):
    message = "Unknown User"
    error_code = 4
    
class SurveyMonkeySystemError(SurveyMonkeyAPIError):
    message = "System Error"
    error_code = 5

