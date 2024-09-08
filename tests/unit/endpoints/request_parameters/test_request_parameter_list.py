from unittest import TestCase

from src.seamy_chex.endpoints.request_parameters.request_parameter import RequestParameter
from src.seamy_chex.endpoints.request_parameters.request_parameter_list import RequestParameterList


class TestRequestParameterList(TestCase):

    def test_request_parameter_list_to_dict(self):
        test_parameter_list = RequestParameterList(
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
        result = test_parameter_list.to_dict()
        self.assertEqual(len(result), 2)
        self.assertEqual(result['test_name_1'], 'test_val_1')
        self.assertEqual(result['test_name_3'], 'test_val_3')

    def test_validate_request_parameter_list_success(self):
        test_parameter_list = RequestParameterList(
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
        test_parameter_list.validate()

    def test_validate_request_parameter_list_fail(self):
        test_parameter_list = RequestParameterList(
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
                required=True
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
        self.assertRaises(ValueError, test_parameter_list.validate)
