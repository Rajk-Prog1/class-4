from homework.minion_game.minion_game import minion_game


class TestMinionGame:

    def test_basic(self):
        assert minion_game("BANANA") == "Stuart 12"

    def test_kevin_wins(self):
        assert minion_game("BAANANAS") == "Kevin 19"

    def test_kevin_win_with_vowel(self):
        assert minion_game("ANANAS") == "Kevin 12"

    def test_draw_case(self):
        assert minion_game("BANANANAAAS") == "Draw"

    def test_another_draw_case(self):
        assert minion_game("BANAASA") == "Draw"

    def test_single_vowel_string(self):
        assert minion_game("A") == "Kevin 1"

    def test_single_consonant_string(self):
        assert minion_game("B") == "Stuart 1"

    def test_empty_string(self):
        assert minion_game("") == "Draw"

    def test_all_vowels(self):
        assert minion_game("AEIOU") == "Kevin 15"

    def test_all_consonants(self):
        assert minion_game("BCDFGH") == "Stuart 21"

    def test_long_string(self):
        assert minion_game("BANANANANANANANANA") == "Stuart 90"

    def test_mixed_case(self):
        assert minion_game("ABABABAB") == "Kevin 20"

    def test_large_input(self):
        large_string = "BANANA" * 100
        assert minion_game(large_string) == "Stuart 90300"
