import requests
from requests import Response
from urllib.parse import urljoin
from abc import ABC, abstractmethod

from src.seamy_chex.endpoints.request_parameters.request_parameter_list import RequestParameterList
from src.seamy_chex.enums.content_type_enum import ContentType
from src.seamy_chex.enums.http_method_enum import HTTPMethod


class BaseEndpoint(ABC):

    def __init__(self, base_url: str, url_tail: str, api_key: str, method: HTTPMethod, content_type: ContentType):
        self.base_url = base_url
        self.url_tail = url_tail
        self.full_url = urljoin(self.base_url, self.url_tail)
        self.api_key = api_key
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
