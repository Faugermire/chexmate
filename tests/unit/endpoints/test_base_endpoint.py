from chexmate.endpoints.base_endpoint import BaseEndpoint
from chexmate.endpoints.request_parameters.request_parameter_list import RequestParameterList
from tests.unit.endpoints.base_endpoint_test_subclass import BaseTestEndpointSubclass


class BaseEndpointTestWrapper(BaseEndpoint):
    """wrapper that allows us to instantiate a representational object of the base endpoint, which we can't
    do normally because of its ABC lineage and presence of abstract methods."""

    def create_request_header_and_body_parameter_lists(self, **kwargs) -> tuple[RequestParameterList, RequestParameterList]:
        return RequestParameterList(), RequestParameterList()


class TestBaseEndpoint(BaseTestEndpointSubclass):
    pass
