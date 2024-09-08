from unittest import TestCase

from src.chexmate.endpoints.request_parameters.parameter_restriction import ParameterRestriction


class TestParameterRestriction(TestCase):

    def test_it(self):
        req_function = lambda x: x is True
        param_req = ParameterRestriction(req_function)
        self.assertTrue(param_req(True))
        self.assertFalse(param_req(False))