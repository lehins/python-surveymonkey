import re

__all__ = [
    'Survey', 'Recipient', 'Collector', 'EmailMessage'
]

class Survey(dict):

    def __init__(self, survey_title, template_id=None, from_survey_id=None):
        params = {
            'survey_title': survey_title
        }
        if template_id is not None:
            params['template_id'] = template_id
        if from_survey_id is not None:
            params['from_survey_id'] = from_survey_id
        super(Survey, self).__init__(params)


class Recipient(dict):
    
    def __init__(self, email, first_name=None, last_name=None, custom_id=None):
        params = {
            'email': email
        }
        if first_name is not None:
            params['first_name'] = first_name
        if last_name is not None:            
            params['last_name'] = last_name
        if custom_id is not None:
            params['custom_id'] = custom_id
        super(Recipient, self).__init__(params)


class Collector(dict):
    
    def __init__(self, type, name=None, recipients=None, send=None):
        params = {
            'type': type
        }
        if name is not None:
            params['name'] = name
        if recipients is not None:
            params['recipients'] = recipients
        if send is not None:
            params['send'] = send
        super(Collector, self).__init__(params)


class EmailMessage(dict):
    survey_link = "[SurveyLink]"
    remove_link = "[RemoveLink]"
    re_survey_link = re.compile(re.escape(survey_link))
    re_remove_link = re.compile(re.escape(remove_link))

    def __init__(self, reply_email, subject, body_text=None):
        params = {
            'reply_email': reply_email,
            'subject': subject
        }
        if body_text is not None:
            assert self.re_survey_link.search(body_text), \
                "%s has to be inside the 'body_text'" % self.survey_link
            assert self.re_remove_link.search(body_text), \
                "%s has to be inside the 'body_text'" % self.remove_link
            params['body_text'] = body_text
        super(EmailMessage, self).__init__(params)
        
