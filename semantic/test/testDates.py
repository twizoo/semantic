import datetime
import unittest
from freezegun import freeze_time
from semantic.dates import DateService


@freeze_time('2014-01-01 00:00')
class TestDate(unittest.TestCase):

    def compareDate(self, input, target):
        service = DateService()
        result = service.extractDate(input)
        self.assertEqual(target, result)

    def compareTime(self, input, target):
        service = DateService()
        result = service.extractTime(input)
        self.assertEqual(target, result)

    def compareDates(self, input, targets):
        service = DateService()
        results = service.extractDates(input)
        for (result, target) in zip(results, targets):
            self.assertEqual(target, result)

    def compareTimes(self, input, targets):
        service = DateService()
        results = service.extractDates(input)
        for (result, target) in zip(results, targets):
            self.assertEqual(target.time(), result.time())

    #
    #  Date Tests
    #

    def testExactWords(self):
        input = "Remind me on January Twenty Sixth"
        target = "2014-01-26"
        self.compareDate(input, target)

    def testExactWordsDash(self):
        input = "Remind me on January Twenty-Sixth"
        target = "2014-01-26"
        self.compareDate(input, target)

    def testExactNums(self):
        input = "Remind me on January 26"
        target = "2014-01-26"
        self.compareDate(input, target)

    def testOrdinalNums(self):
        input = "Remind me on January 2nd"
        target = "2014-01-02"
        self.compareDate(input, target)

    def testWeekFromExact(self):
        input = "Do x y and z a week from January 26"
        target = "2014-02-02"
        self.compareDate(input, target)

    def testMultipleWeeksFrom(self):
        input = "Do x y and z three weeks from January 26"
        target = "2014-02-16"
        self.compareDate(input, target)

    def testMultiWordDaysFrom(self):
        input = "Do x y and z twenty six days from January 26"
        target = "2014-02-21"
        self.compareDate(input, target)

    def testMultiWordAndDaysFrom(self):
        input = "Do x y and z one hundred and twelve days from January 26"
        target = "2014-05-18"
        self.compareDate(input, target)

    def testNextFriday(self):
        input = "Next Friday, go to the grocery store"
        target = "2014-01-10"
        self.compareDate(input, target)

    def testAmbiguousNext(self):
        input = "The next event will take place on Friday"
        target = "2014-01-03"
        self.compareDate(input, target)

    def testTomorrow(self):
        input = "Tomorrow morning, go to the grocery store"
        target = "2014-01-02"
        self.compareDate(input, target)

    def testToday(self):
        input = "Send me an email some time today if you can"
        target = "2014-01-01"
        self.compareDate(input, target)

    def testThis(self):
        input = "This morning, I went to the gym"
        target = "2014-01-01"
        self.compareDate(input, target)

    def testIllegalDate(self):
        input = "I have a meeting on February 29 at 12:15pm"
        self.assertRaises(ValueError, lambda: DateService().extractDate(input))

    def testNoDate(self):
        input = "It's a very nice day."
        target = None
        self.compareDate(input, target)

    def testNoDateButTime(self):
        input = "I have a meeting at 2pm"
        target = None
        self.compareDate(input, target)

    #
    #  Time Tests
    #

    def testExactTime(self):
        input = "Let's go to the park at 12:51pm"
        target = "12:51"
        self.compareTime(input, target)

    def testInExactTime(self):
        input = "I want to leave in two hours and twenty minutes"
        target = datetime.datetime.today() + \
            datetime.timedelta(hours=2, minutes=20)
        self.compareTime(input, target)

    def testTimeNoMinutes(self):
        input = "Let's go to the park at 8pm"
        target = "20:00"
        self.compareTime(input, target)

    def testTimeNoMinutesLater(self):
        input = "Let's go to the park at 10pm"
        target = "22:00"
        self.compareTime(input, target)

    def testTimeDotMinutes(self):
        input = "Let's go to the park at 6.20pm"
        target = "18:20"
        self.compareTime(input, target)

    def testTimeDotMinutesZeroMinutes(self):
        input = "Let's go to the park at 6.00am"
        target = "06:00"
        self.compareTime(input, target)

    def testAmbiguousTime(self):
        input = "Let's go to the park at 8"
        target = "20:00"
        self.compareTime(input, target)

    def testAmbiguousDotTime(self):
        input = "Let's go to the park at 8.45"
        target = "20:45"
        self.compareTime(input, target)

    def testMilitaryMorningTime(self):
        input = "Let's go to the park at 08:00"
        target = "08:00"
        self.compareTime(input, target)

    def testMilitaryAfternoonTime(self):
        input = "Let's go to the park at 20:00"
        target = "20:00"
        self.compareTime(input, target)

    def testThisEve(self):
        input = "Let's go to the park this eve."
        target = "20:00"
        self.compareTime(input, target)

    def testTonightTime(self):
        input = "Let's go to the park tonight."
        target = "20:00"
        self.compareTime(input, target)

    def testBeforeTenIsEveningTime(self):
        input = "Let's go to the park at 5."
        target = "17:00"
        self.compareTime(input, target)

    def testInThe(self):
        input = "I went to the park in the afternoon"
        target = "15:00"
        self.compareTime(input, target)

    def testBothDateAndTime(self):
        input = "Let's go to the park at 5 tomorrow."
        target_time = "17:00"
        target_date = "2014-01-02"
        self.compareTime(input, target_time)
        self.compareDate(input, target_date)

    def testNoTime(self):
        input = "It's a very nice day."
        target = None
        self.compareTime(input, target)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDate)
    unittest.TextTestRunner(verbosity=2).run(suite)
