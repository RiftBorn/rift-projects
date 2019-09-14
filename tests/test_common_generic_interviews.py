import unittest
from interview.common.generic_interviews import binary_to_decimal


class TestStringInterviews(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_isomorphic(self):
        """
        test interview.common.generic_interviews.binary_to_decimal
        """
        tests = [{
            "string": "0",
            "returned": 0,
        }, {
            "string": "111",
            "returned": 7,
        }, {
            "string": "11111",
            "returned": 31,
        }, {
            "string": "1010101",
            "returned": 85,
        }, {
            "string": "11111111",
            "returned": 255,
        }, {
            "string": "111111110101",
            "returned": 4085,
        }, {
            "string": "00000111",
            "returned": 7,
        }, {
            "string": "1111111111111111111111111111111",
            "returned": 2147483647,
        }]

        for test in tests:
            binary_string = test.get("string")
            expected = test.get("returned")
            returned = binary_to_decimal(binary_string)
            self.assertEqual(expected, returned)
