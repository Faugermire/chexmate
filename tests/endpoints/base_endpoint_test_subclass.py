from unittest import TestCase
import os


class BaseTestEndpointSubclass(TestCase):

    def setUp(self):
        os.environ['SEAMLESS_CHEX_BASE_URL'] = 'https://test.seamlesschex.com'
        os.environ['SEAMLESS_CHEX_API_KEY'] = 'test_seamless_chex_api_key'
