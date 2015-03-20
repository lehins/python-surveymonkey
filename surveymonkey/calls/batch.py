from surveymonkey.calls.base import Call


class Survey(dict):

    def __init__(self, survey_title, **kwargs):
        self.survey_title = survey_title
        self.template_id = kwargs.get('template_id')
        self.from_survey_id = kwargs('from_survey_id')
        super(Survey, self).__init__(survey_title=survey_title, **kwargs)


class Recipient(dict):
    
    def __init__(self, email, **kwargs):
        self.email = email
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.custom_id = kwargs('custom_id')
        super(Survey, self).__init__(email=email, **kwargs)


class Collector(dict):
    
    def __init__(self, type, **kwargs):
        self.type = type
        self.name = kwargs.get('name')
        self.recipients = kwargs.get('recipients')
        super(Survey, self).__init__(type=type, **kwargs)


class EmailMessage(dict):

    def __init__(self, reply_email, subject, **kwargs):
        self.reply_email = reply_email
        self.subject = subject
        self.body_text = kwargs('body_text')
        super(Survey, self).__init__(reply_email=reply_email, subject=subject, **kwargs)
        
        
class Batch(Call):

    def __create_flow(self, survey, collector, email_message):
        params = {
            'survey': survey,
            'collector': collector,
            'email_message': email_message
        }
        return self.make_call(self.__create_flow, params, {})
    __create_flow.allowed_params = [
        'survey', 'collector', 'email_message'
    ]
