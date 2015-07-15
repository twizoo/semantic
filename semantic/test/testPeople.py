import unittest
from semantic.people import PeopleService


class TestPeople(unittest.TestCase):
    def compareNumberOfPeople(self, input, target):
        service = PeopleService()
        result = service.extractNumberOfPeople(input)
        self.assertEqual(target, result)

    # TESTS

    def testCardinalNumber(self):
        input = "This car is for 4 people."
        target = 4
        self.compareNumberOfPeople(input, target)

    def testCardinalNumberEndoOfSentence(self):
        input = "The hotel room for 2."
        target = 2
        self.compareNumberOfPeople(input, target)

    def testWrittenCardinalNumber(self):
        input = "The venue has capacity for ten people."
        target = 10
        self.compareNumberOfPeople(input, target)

    def testDoubleFor(self):
        input = "BBQ for Wednesday late afternoon for six friends."
        target = 6
        self.compareNumberOfPeople(input, target)

    def testOfPhrase(self):
        input = "Total number of nine ppl."
        target = 9
        self.compareNumberOfPeople(input, target)

    def testNoNumberOfPeople(self):
        input = "It's a nice weather in London today."
        target = None
        self.compareNumberOfPeople(input, target)
