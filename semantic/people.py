import re


class PeopleService(object):

    __numberDescriptors__ = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20
    }

    _peopleRegex = re.compile(r""".*?(for|of)[\s]*(\d[\s]+|\w+)""")

    def extractNumberOfPeople(self, input):
        matchObj = self._peopleRegex.findall(input)

        for match in matchObj:
            try:
                number = int(match[1])
                return number
            except ValueError:
                if match[1] in self.__numberDescriptors__:
                    return self.__numberDescriptors__[match[1]]
            except IndexError:
                return None
