from tests.base import TestBase
from goodreads.comment import GoodreadsComment


class TestComment(TestBase):

    def setUp(self):
        self.comments = self.client.list_comments('user', '1')

    def test_list_comments(self):
        self.assertGreater(len(self.comments), 0)
        for c in self.comments:
            self.assertIsInstance(c, GoodreadsComment)
