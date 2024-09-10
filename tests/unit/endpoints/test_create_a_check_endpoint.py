from chexmate.endpoints.create_a_check_endpoint import CreateACheckEndpoint
from tests.unit.endpoints.base_endpoint_test_subclass import BaseTestEndpointSubclass


class TestCreateACheckEndpoint(BaseTestEndpointSubclass):

    def setUp(self):
        super().setUp()
        self.create_a_check_endpoint = CreateACheckEndpoint(self.base_url, self.api_key)
        self.valid_long_setup_request_params = {
            'number': None,
            'amount': 1000.69,
            'memo': 'test memo',
            'name': 'test name',
            'email': 'test@email.com',
            'authorization_date': '2024-01-01',
            'label': 'test label',
            'phone': '1234567890',
            'sender_address': None,
            'sender_city': None,
            'sender_state': None,
            'sender_zip': None,
            'bank_account': '12345',
            'bank_routing': '123456789',
            'token': None,
            'store': None,
            'type_info': 'test type info',
            'recurring': 0,
            'recurring_cycle': 'day',
            'recurring_start_date': 'NULL',
            'recurring_installments': 0,
            'verify_before_save': True,
            'fund_confirmation': False
        }
        self.valid_short_setup_request_params_1 = {
            'amount': 1000.69,
            'memo': 'test memo',
            'name': 'test name',
            'email': 'test@email.com',
            'bank_account': '12345',
            'bank_routing': '123456789',
        }
        self.valid_short_setup_request_params_2 = {
            'amount': 1000.69,
            'memo': 'test memo',
            'name': 'test name',
            'email': 'test@email.com',
            'token': '123456789012345678901234567890123456',
            'store': 'test.site.com',
        }

    def test_long_valid_create_a_check_endpoint(self):
        header_params = self.create_a_check_endpoint.create_request_header_list()
        body_params = self.create_a_check_endpoint.create_request_body_list(**self.valid_long_setup_request_params)
        header_params.validate()
        body_params.validate()

    def test_short_valid_create_a_check_endpoint(self):
        header_params = self.create_a_check_endpoint.create_request_header_list()
        body_params = self.create_a_check_endpoint.create_request_body_list(**self.valid_short_setup_request_params_1)
        header_params.validate()
        body_params.validate()

        body_params = self.create_a_check_endpoint.create_request_body_list(**self.valid_short_setup_request_params_2)
        body_params.validate()
