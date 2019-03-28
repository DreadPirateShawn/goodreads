from tests.base import TestBase


class TestGroup(TestBase):

    def setUp(self):
        self.group = self.client.group(1)

    def test_group_title(self):
        self.assertEqual(self.group.title, 'Goodreads Feedback')
