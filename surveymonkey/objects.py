import re

__all__ = [
    'Survey', 'Recipient', 'Collector', 'EmailMessage'
]

class Survey(dict):

    def __init__(self, survey_title, template_id=None, from_survey_id=None):
        params = {
            'survey_title': survey_title
        }
        if template_id:
            params['template_id'] = template_id
        if from_survey_id:
            params['from_survey_id'] = from_survey_id
            assert not template_id, \
                "template_id and form_survey_id cannot be specified together"
        super(Survey, self).__init__(params)


class Recipient(dict):
    
    def __init__(self, email, first_name=None, last_name=None, custom_id=None):
        params = {
            'email': email
        }
        if first_name:
            params['first_name'] = first_name
        if last_name:
            params['last_name'] = last_name
        if custom_id:
            params['custom_id'] = custom_id
        super(Recipient, self).__init__(params)


class Collector(dict):
    
    def __init__(self, type, name=None, recipients=None, send=None):
        params = {
            'type': type
        }
        if name:
            params['name'] = name
        if recipients:
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
        if body_text:
            assert self.re_survey_link.search(body_text), \
                "%s has to be inside the 'body_text'" % self.survey_link
            assert self.re_remove_link.search(body_text), \
                "%s has to be inside the 'body_text'" % self.remove_link
            params['body_text'] = body_text
        super(EmailMessage, self).__init__(params)
        
