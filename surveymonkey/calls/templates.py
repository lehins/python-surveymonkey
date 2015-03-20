from surveymonkey.calls.base import Call


class Templates(Call):

    def __get_template_list(self, **kwargs):
        return self.make_call(self.__get_template_list, {}, kwargs)
    __get_template_list.allowed_params = [
        'page', 'page_size', 'language_id', 'category_id',
        'show_only_available_to_current_user', 'fields'
    ]
    get_template_list = __get_template_list
