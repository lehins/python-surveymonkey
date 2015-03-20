from surveymonkey.calls.base import Call


class User(Call):

    def __get_user_details(self, **kwargs):
        return self.make_call(self.__get_user_details, {}, kwargs)
    __get_user_details.allowed_params = []
    get_user_details = __get_user_details

