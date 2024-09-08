from unittest import TestCase
import os


class BaseTestEndpointSubclass(TestCase):

    def setUp(self):
        self.base_url = 'https://test.seamlesschex.com'
        self.api_key = 'test_seamless_chex_api_key'
