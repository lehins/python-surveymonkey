from surveymonkey.calls.base import Call


class Batch(Call):

    def __create_flow(self, survey, collector, email_message, **kwargs):
        params = {
            'survey': survey,
            'collector': collector,
            'email_message': email_message
        }
        assert collector.get('type') == 'email', \
            "Only supported collector type for this call is 'email'"
        return self.make_call(self.__create_flow, params, kwargs)
    __create_flow.allowed_params = [
        'survey', 'collector', 'email_message'
    ]
    create_flow = __create_flow

    def __send_flow(self, survey_id, collector, email_message, **kwargs):
        params = {
            'survey_id': survey_id,
            'collector': collector,
            'email_message': email_message
        }
        assert collector.get('type') == 'email', \
            "Only supported collector type for this call is 'email'"
        return self.make_call(self.__send_flow, params, kwargs)
    __send_flow.allowed_params = [
        'survey_id', 'collector', 'email_message'
    ]
    send_flow = __send_flow
    
