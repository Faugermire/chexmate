from src.seamy_chex.endpoints.base_endpoint import BaseEndpoint
from src.seamy_chex.endpoints.request_parameters.request_parameter import RequestParameter
from src.seamy_chex.enums.content_type_enum import ContentType
from src.seamy_chex.enums.http_method_enum import HTTPMethod
from tests.unit.endpoints.base_endpoint_test_subclass import BaseTestEndpointSubclass


class BaseEndpointTestWrapper(BaseEndpoint):
    """wrapper that allows us to instantiate a representational object of the base endpoint, which we can't
    do normally because of its ABC lineage and presence of abstract methods."""

    def create_request_header_and_body_parameter_lists(self, **kwargs) -> tuple[tuple[RequestParameter, ...], tuple[RequestParameter, ...]]:
        return (), ()


class TestBaseEndpoint(BaseTestEndpointSubclass):

    def setUp(self):
        super().setUp()
        self.base_endpoint = BaseEndpointTestWrapper(
            url_tail='/test/url/tail',
            method=HTTPMethod.POST,
            content_type=ContentType.APPLICATION_JSON
        )
