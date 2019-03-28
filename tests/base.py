import unittest
from goodreads import apikey
from goodreads.client import GoodreadsClient


class TestBase(unittest.TestCase):

    _client = None

    @property
    def client(self):
        if not self._client:
            self._client = GoodreadsClient(apikey.key, apikey.secret)
            self._client.authenticate(apikey.oauth_access_token,
                                      apikey.oauth_access_token_secret)
        return self._client

    def assertStartsWith(self, actual, expected):
        self.assertTrue(
            actual.startswith(expected),
            msg="\n" \
                "Expect ~> {expected}\n" \
                "Actual ~> {actual}".format(
                    expected=expected,
                    actual=actual
                )
            )

    def assertEndsWith(self, actual, expected):
        self.assertTrue(
            actual.endswith(expected),
            msg="\n" \
                "Expect ~> {expected}\n" \
                "Actual ~> {actual}".format(
                    expected=expected,
                    actual=actual
                )
            )

    def assertIsDigit(self, actual):
        self.assertTrue(actual.isdigit(),
                        msg="Value is not a digit: %s" % actual)
