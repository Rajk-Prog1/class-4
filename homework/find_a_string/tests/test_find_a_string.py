from homework.find_a_string.find_a_string import find_a_string


class TestFindAString:

    def test_basic(self):
        assert find_a_string("ABCDCDC", "CDC") == 2

    def test_case_sensitivity(self):
        assert find_a_string("I am an Indian, by birth.", "Birth") == 0

    def test_mixed_case(self):
        assert find_a_string("ThIsisCoNfUsInG", "is") == 1

    def test_overlapping_substrings(self):
        assert find_a_string("ininini", "ini") == 3

    def test_special_characters(self):
        assert find_a_string("WoW!ItSCoOWoWW", "oW") == 2

    def test_multiple_occurrences(self):
        assert find_a_string("AbBaAbBaAbBa", "Ab") == 3

    def test_substring_of_numbers(self):
        assert find_a_string("12jlka445kljakldfjlaksjdfdka3942", "3942") == 1

    def test_non_existing_substring(self):
        assert (
            find_a_string("In the convential world, it won't ever happen", "lD,") == 0
        )

    def test_mixed_types(self):
        assert find_a_string("BlUeBe1Bl*fjal9jkl", "Bl") == 2

    def test_partial_match(self):
        assert find_a_string("TestCaseTestCase", "CaseT") == 1

    def test_empty_string(self):
        assert find_a_string("", "abc") == 0

    def test_empty_substring(self):
        assert find_a_string("abc", "") == 0

    def test_both_empty(self):
        assert find_a_string("", "") == 0

    def test_substring_longer_than_string(self):
        assert find_a_string("abc", "abcdef") == 0

    def test_substring_equals_string(self):
        assert find_a_string("abc", "abc") == 1
