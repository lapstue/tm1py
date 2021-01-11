# -*- coding: utf-8 -*-
import json
from typing import List

from TM1py.Services.ObjectService import ObjectService
from TM1py.Services.RestService import RestService, Response

class TM1ProjectService(ObjectService):
    """ Service to interact with TM1Project file
    """
    def __init__(self, rest: RestService):
        super().__init__(rest)

    def get_project(self, **kwargs):

        url = "/api/v1/!tm1project"
        body = json.dumps(kwargs)
        response = self._rest.GET(url=url, data=body)

    def set_project(self, **kwargs):

        url = "/api/v1/!tm1project"
        body = json.dumps(kwargs)
        response = self._rest.PUT(url=url, data=body)

        print(response.content)


