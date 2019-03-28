from tests.base import TestBase
from goodreads.event import GoodreadsEvent


class TestEvent(TestBase):

    def setUp(self):
        self.events = self.client.list_events('21244')

    def test_list_events(self):
        self.assertGreater(len(self.events), 0)
        for e in self.events:
            self.assertIsInstance(e, GoodreadsEvent)
