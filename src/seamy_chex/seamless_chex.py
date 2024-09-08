import os

from src.seamy_chex.endpoints.create_a_check_endpoint import CreateACheckEndpoint
from src.seamy_chex.enums.seamless_chex_base_url_enum import SeamlessChexBaseUrl


class SeamlessChex:

    def __init__(self):
        self.seamless_chex_environment = os.environ.get('SEAMLESS_CHEX_ENVIRONMENT')
        if self.seamless_chex_environment is None:
            raise ValueError(f'The "SEAMLESS_CHEX_ENVIRONMENT" environment variable needs to be set with a string representing either "PRODUCTION" for production mode or anything else for sandbox mode. It is currently {self.seamless_chex_environment}')
        self.is_sandbox_mode = self.seamless_chex_environment != 'PRODUCTION'
        self.base_url = SeamlessChexBaseUrl.SANDBOX_BASE_URL.value if self.is_sandbox_mode else SeamlessChexBaseUrl.PRODUCTION_BASE_URL.value
        self.api_key = os.environ.get('SEAMLESS_CHEX_API_KEY')
        if self.api_key is None:
            raise ValueError(f'The "SEAMLESS_CHEX_API_KEY" environment variable needs to be set with either the base sandbox or base production api key.')

        self.endpoints = None
        # Initialize endpoints
        self.endpoints.create_a_check = CreateACheckEndpoint(self.base_url, self.api_key)