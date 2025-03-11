from django.test import TestCase
from upload.test_runes import TestRunes
from upload.process_runes import calculate_efficiency

class TestProcessRunes(TestCase):
    def test_calculate_efficiency(self):
        output_runes = [calculate_efficiency(rune) for rune in TestRunes.runes]
        self.assertEqual(output_runes, [
            {"rune_id": 60739144488, "rune_set": 3, "current_efficiency": 27.69,},
            {"rune_id": 54267878655, "rune_set": 2, "current_efficiency": 98.47,},
            {"rune_id": 53664977198, "rune_set": 1, "current_efficiency": 61.27,},
            {"rune_id": 40709721092, "rune_set": 1, "current_efficiency": 74.67,},])