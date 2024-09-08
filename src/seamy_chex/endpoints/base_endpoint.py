import os
from abc import ABC, abstractmethod

import requests
from requests import Response
from urllib.parse import urljoin

from src.seamy_chex.endpoints.request_parameters.request_parameter import RequestParameter
from src.seamy_chex.endpoints.request_parameters.request_parameter_list import RequestParameterList
from src.seamy_chex.enums.content_type_enum import ContentType
from src.seamy_chex.enums.http_method_enum import HTTPMethod
from src.seamy_chex.enums.seamless_chex_base_url_enum import SeamlessChexBaseUrl


class BaseEndpoint(ABC):

    def __init__(self, url_tail: str, method: HTTPMethod, content_type: ContentType):
        self.url_tail = url_tail
        self.seamless_chex_environment = os.environ.get('SEAMLESS_CHEX_ENVIRONMENT')
        if self.seamless_chex_environment is None:
            raise ValueError(f'The "SEAMLESS_CHEX_ENVIRONMENT" environment variable needs to be set with a string representing either "PRODUCTION" for production mode or anything else for sandbox mode. It is currently {self.seamless_chex_environment}')
        self.is_sandbox_mode = self.seamless_chex_environment != 'PRODUCTION'
        self.base_url = SeamlessChexBaseUrl.SANDBOX_BASE_URL.value if self.is_sandbox_mode else SeamlessChexBaseUrl.PRODUCTION_BASE_URL.value
        self.api_key = os.environ.get('SEAMLESS_CHEX_API_KEY')
        if self.api_key is None:
            raise ValueError(f'The "SEAMLESS_CHEX_API_KEY" environment variable needs to be set with either the base sandbox or base production api key.')
        self.full_url = urljoin(self.base_url, self.url_tail)
        self.method = method
        self.content_type = content_type

    @abstractmethod
    def create_request_header_and_body_parameter_lists(self, **kwargs) -> tuple[RequestParameterList, RequestParameterList]:
        """Creates the list of parameters for the header and body of the request.
        Please refer to this method for documentation of each parameter."""
        pass

    def send_request(self, header_params: RequestParameterList, body_params: RequestParameterList) -> Response:
        header_params.validate()
        body_params.validate()
        new_request = requests.Request(
            method=self.method.value,
            url=self.full_url,
            headers=header_params.to_dict(),
            data=body_params.to_dict()
        )
        prepared_request = new_request.prepare()
        with requests.session() as sesh:
            resp = sesh.send(prepared_request)
        return resp
