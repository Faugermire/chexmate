import os
from unittest import TestCase

from chexmate.seamless_chex import SeamlessChex


class TestE2ECreateACheckEndpoint(TestCase):

    def test_e2e_create_a_check_endpoint_success(self):
        print(f'API KEY: {os.environ['SEAMLESS_CHEX_API_KEY']}')
        print(f'SEAMLESS CHEX ENVIRONMENT: {os.environ['SEAMLESS_CHEX_ENVIRONMENT']}')
        seamless_chex = SeamlessChex()
        print(f'SEAMLESS CHEX SANDBOX MODE ACTIVATED: {seamless_chex.is_sandbox_mode}')
        request_body_params = {
            "number": None,
            "amount": 100,
            "memo": "Law Office Robert Aaron, FL" ,
            "name": "Robert Aaron",
            "email": "robertaaron@gmail.com",
            "authorization_date": "2345-01-01" ,
            "label": "Label" ,
            "phone": "1728514288" ,
            "sender_address": "3881 Coquina Ave" ,
            "sender_city": "North Port" ,
            "sender_state": "FL" ,
            "sender_zip": "34286" ,
            "bank_account": "5354070829" ,
            "bank_routing": "021000021" ,
            "token": None,
            "store": None,
            "type_info": "Service #1" ,
            "recurring": 1 ,
            "recurring_cycle": "week" ,
            "recurring_start_date": "2345-01-02" ,
            "recurring_installments": 3 ,
            "verify_before_save": True ,
            "fund_confirmation": False
        }
        header_parameters = seamless_chex.endpoints.create_a_check.create_request_header_list()
        body_parameters = seamless_chex.endpoints.create_a_check.create_request_body_list(**request_body_params)
        # print(f'HEADER PARAMETERS: {str(header_parameters)}')
        # print(f'BODY PARAMETERS: {str(body_parameters)}')
        # print(body_parameters.to_dict())
        resp = seamless_chex.endpoints.create_a_check.send_request(header_parameters, body_parameters)
        print('RESPONSE:')
        print(resp.json())
