from surveymonkey.calls.base import Call


class Surveys(Call):

    def __get_survey_list(self, **kwargs):
        return self.make_call(self.__get_survey_list, {}, kwargs)
    __get_survey_list.allowed_params = [
        'page', 'page_size', 'start_date', 'end_date', 'title', 'recipient_email',
        'order_asc', 'fields'
    ]
    get_survey_list = __get_survey_list

    def __get_survey_details(self, survey_id, **kwargs):
        params = {
            'survey_id': survey_id
        }
        return self.make_call(self.__get_survey_details, params, kwargs)
    __get_survey_details.allowed_params = [
        'survey_id'
    ]
    get_survey_details = __get_survey_details
    
    def __get_collector_list(self, survey_id, **kwargs):
        params = {
            'survey_id': survey_id
        }
        return self.make_call(self.__get_collector_list, params, kwargs)
    __get_collector_list.allowed_params = [
        'survey_id', 'page', 'page_size', 'start_date', 'end_date', 'name',
        'order_asc', 'fields'
    ]
    get_collector_list = __get_collector_list

    def __get_respondent_list(self, survey_id, **kwargs):
        params = {
            'survey_id': survey_id
        }
        return self.make_call(self.__get_respondent_list, params, kwargs)
    __get_respondent_list.allowed_params = [
        'survey_id', 'collector_id', 'page', 'page_size', 'start_date', 'end_date', 
        'start_modified_date', 'end_modified_date', 'order_asc', 'order_by', 'fields'
    ]
    get_respondent_list = __get_respondent_list
    
    def __get_responses(self, respondent_ids, survey_id, **kwargs):
        params = {
            'respondent_ids': respondent_ids,
            'survey_id': survey_id
        }
        return self.make_call(self.__get_responses, params, kwargs)
    __get_responses.allowed_params = [
        'respondent_ids', 'survey_id'
    ]
    get_responses = __get_responses

    def __get_response_counts(self, collector_id, **kwargs):
        params = {
            'collector_id': collector_id
        }
        return self.make_call(self.__get_response_counts, params, kwargs)
    __get_response_counts.allowed_params = [
        'collector_id'
    ]
    get_response_counts = __get_response_counts
    
