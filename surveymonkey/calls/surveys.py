from surveymonkey.calls.base import Call


class Surveys(Call):
    survey_fields = [
        'title', 'analysis_url', 'preview_url', 'date_created', 'date_modified',
        'language_id', 'question_count', 'num_responses'
    ]
    collector_fields = [
        'url', 'open', 'type', 'name', 'date_created', 'date_modified'
    ]
    respondent_fields = [
        'date_start', 'date_modified', 'collector_id', 'collection_mode',
        'custom_id', 'email', 'first_name', 'last_name', 'ip_address', 'status',
        'analysis_url', 'recipient_id'
    ]

    def __get_survey_list(self, **kwargs):
        fields = kwargs.get('fields', None)
        if fields is not None and not fields:
            kwargs['fields'] = self.survey_fields
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
        fields = kwargs.get('fields', None)
        if fields is not None and not fields:
            kwargs['fields'] = self.colector_fields
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
        fields = kwargs.get('fields', None)
        if fields is not None and not fields:
            kwargs['fields'] = self.respondent_fields
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
    
