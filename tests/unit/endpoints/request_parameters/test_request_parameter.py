from unittest import TestCase

from src.seamy_chex.endpoints.request_parameters.parameter_restriction import ParameterRestriction
from src.seamy_chex.endpoints.request_parameters.request_parameter import RequestParameter


class TestRequestParameter(TestCase):

    def setUp(self):
        self.req_param = RequestParameter(  # valid request parameter
            param_name='test_name',
            param_value='test_value',
            param_types=str,
            restrictions=[
                ParameterRestriction(lambda x: len(x) <= 128)
            ],
            description='This is a test description',
            required=True
        )

    def test_all_good(self):
        self.req_param.validate()

    def test_none_value_when_required_raises(self):
        self.req_param.param_value = None
        self.assertRaises(ValueError, self.req_param.validate)

    def test_invalid_param_restriction(self):
        self.req_param.restrictions = [
            ParameterRestriction(lambda x: False)
        ]
        self.assertRaises(ValueError, self.req_param.validate)

    def test_invalid_param_type(self):
        self.req_param.param_types = int
        self.assertRaises(ValueError, self.req_param.validate)
