import os
from abc import ABC, abstractmethod

import requests
from requests import Response
from urllib.parse import urljoin

from src.seamy_chex.endpoints.request_parameters.request_parameter import RequestParameter
from src.seamy_chex.enums.content_type_enum import ContentType
from src.seamy_chex.enums.http_method_enum import HTTPMethod


class BaseEndpoint(ABC):

    def __init__(self, url_tail: str, method: HTTPMethod, content_type: ContentType):
        self.url_tail = url_tail
        self.base_url = os.environ.get('SEAMLESS_CHEX_BASE_URL')
        if self.base_url is None:
            raise ValueError(f'The "SEAMLESS_CHEX_BASE_URL" environment variable needs to be set with either the base sandbox or base production url.')
        self.api_key = os.environ.get('SEAMLESS_CHEX_API_KEY')
        if self.api_key is None:
            raise ValueError(f'The "SEAMLESS_CHEX_API_KEY" environment variable needs to be set with either the base sandbox or base production api key.')
        self.full_url = urljoin(self.base_url, self.url_tail)
        self.method = method
        self.content_type = content_type

    @abstractmethod
    def create_request_parameters(self, **kwargs) -> tuple[tuple[RequestParameter, ...], tuple[RequestParameter, ...]]:
        """Creates the list of parameters for the header and body of the request.
        Please refer to this method for documentation of each parameter."""
        pass

    def send_request(self, header_params: tuple[RequestParameter, ...], body_params: tuple[RequestParameter, ...]) -> Response:
        self.validate_parameters(header_params)
        self.validate_parameters(body_params)
        requests_parameters = {
            'url': self.full_url,
            'headers': self.parameters_tuple_to_dict(header_params),
            'json': self.parameters_tuple_to_dict(body_params)
        }
        match self.method:
            case HTTPMethod.GET:
                resp = requests.get(**requests_parameters)
            case HTTPMethod.POST:
                resp = requests.post(**requests_parameters)
            case _:
                raise ValueError(f'Unsupported request method: {self.method.name}')
        return resp

    def parameters_tuple_to_dict(self, param_list: tuple[RequestParameter, ...]):
        result = {}
        for param in param_list:
            key, value = param.to_key_value_pair()
            if value is not None:
                result.update({key: value})
        return result

    def validate_parameters(self, param_list: tuple[RequestParameter, ...]):
        for param in param_list:
            param.validate()
