from surveymonkey.calls.base import Call


class Collectors(Call):

    def __create_collector(self, survey_id, collector, **kwargs):
        params = {
            'survey_id': survey_id,
            'collector': collector
        }
        assert collector.get('type') == 'weblink', \
            "Only supported collector type for this call is 'weblink'"
        return self.make_call(self.__create_collector, params, kwargs)
    __create_collector.allowed_params = [
        'survey_id', 'collector'
    ]
    create_collector = __create_collector
    
