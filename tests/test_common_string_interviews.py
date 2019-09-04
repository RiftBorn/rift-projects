import unittest
from interview.common.string_interviews import is_isomorphic


class TestStringInterviews(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_isomorphic(self):
        """
        test interview.common.string_interview.is_isomorphic
        """
        tests = [{
            "string1": "egg",
            "string2": "add",
            "returned": True,
        }, {
            "string1": "Liyuan",
            "string2": "MuyShen",
            "returned": False,
        }]

        for test in tests:
            word_1 = test.get("string1")
            word_2 = test.get("string2")
            expected = test.get("returned")
            returned = is_isomorphic(word_1, word_2)
            self.assertEqual(expected, returned)
