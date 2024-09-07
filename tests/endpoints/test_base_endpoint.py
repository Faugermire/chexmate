from src.seamy_chex.endpoints.base_endpoint import BaseEndpoint
from src.seamy_chex.endpoints.request_parameters.request_parameter import RequestParameter
from src.seamy_chex.enums.content_type_enum import ContentType
from src.seamy_chex.enums.http_method_enum import HTTPMethod
from tests.endpoints.base_endpoint_test_subclass import BaseTestEndpointSubclass


class BaseEndpointTestWrapper(BaseEndpoint):
    """wrapper that allows us to instantiate a representational object of the base endpoint, which we can't
    do normally because of its ABC lineage and presence of abstract methods."""

    def create_request_parameters(self, **kwargs) -> tuple[tuple[RequestParameter, ...], tuple[RequestParameter, ...]]:
        return (), ()


class TestBaseEndpoint(BaseTestEndpointSubclass):

    def setUp(self):
        super().setUp()
        self.base_endpoint = BaseEndpointTestWrapper(
            url_tail='/test/url/tail',
            method=HTTPMethod.POST,
            content_type=ContentType.APPLICATION_JSON
        )

    def test_parameter_tuple_to_dict(self):
        test_parameter_tuple = (
            RequestParameter(
                param_name='test_name_1',
                param_types=str,
                param_value='test_val_1',
                restrictions=[],
                description='test description 1',
                required=True
            ),
            RequestParameter(
                param_name='test_name_2',
                param_types=str,
                param_value=None,
                restrictions=[],
                description='test description 2',
                required=False
            ),
            RequestParameter(
                param_name='test_name_3',
                param_types=str,
                param_value='test_val_3',
                restrictions=[],
                description='test description 3',
                required=True
            ),
        )
        result = self.base_endpoint.parameters_tuple_to_dict(test_parameter_tuple)
        self.assertEqual(len(result), 2)
        self.assertEqual(result['test_name_1'], 'test_val_1')
        self.assertEqual(result['test_name_3'], 'test_val_3')
