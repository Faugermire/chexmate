from unittest import TestCase

from chexmate.endpoints.request_parameters.parameter_requirement import ParameterRequirement


class TestParameterRequirement(TestCase):

    def test_it(self):
        req_function = lambda x: x is True
        param_req = ParameterRequirement(req_function)
        self.assertTrue(param_req(True))
        self.assertFalse(param_req(False))
