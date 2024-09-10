from unittest import TestCase
import os


class BaseTestEndpointSubclass(TestCase):

    def setUp(self):
        self.base_url = 'https://fake.seamlesschex.com'
        self.api_key = 'fake_seamless_chex_api_key'
