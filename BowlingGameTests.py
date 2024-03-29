from unittest import TestCase
from BowlingGame import BowlingGame

# SCENARIUSZE TESTOWE
# 1. Jeśli wszystkie twoje rzuty (ang. roll/throw) były chybione to wynik końcowy wynosi zero
# 2. W każdym rzucie został strącony tylko jeden kręgiel (ang. pin). Wynik końcowy wynosi 20.
# 3. W pierwszej turze (ang. frame) został trafiony spare, następnie zostały strącone trzy kręgle. Wynik końcowy wynosi 16.
# 4. W pierwszej turze został trafiony strike, następnie zostały strącone trzy i cztery kręgle. Reszta rzutów była chybiona. Wynik końcowy wynosi 24.
# 5. Wszystkie rzuty to strikes. Wynik końcowy wynosi 300.


class BowlingGameTests(TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def test_all_gutter(self):

        for i in range(20):
            self.game.roll(0)

        self.assertEqual(0, self.game.score, "All gutters should get final score 0")

    def test_all_ones(self):

        for i in range(20):
            self.game.roll(1)

        self.assertEqual(20, self.game.score, "All ones should get 20 final score")

    def test_spare_then_3_pins(self):
        self.game.roll(9)
        self.game.roll(1)
        self.game.roll(3)

        for i in range(17):
            self.game.roll(0)

        self.assertEqual(16, self.game.score, "Should be 16 - spare then 3 pins down")

    def test_strike_then_3_4_pins(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)

        for i in range(17):
            self.game.roll(0)

        self.assertEqual(24, self.game.score, "Should be 24 - strike then 3 and 4 pins down")

    def test_all_strikes(self):

        for i in range(12):
            self.game.roll(10)

        self.assertEqual(300, self.game.score, "All ones should get 300 final score")