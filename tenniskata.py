import unittest

class TennisGame:
    def __init__(self):
        self.finish = False
        self.who_is_the_winner = 0
        self.player_1_score = 0
        self.player_2_score = 0

    def player_1_scores(self):
        if self.player_1_score == 0:
            self.player_1_score = 15
        elif self.player_1_score == 15:
            self.player_1_score = 30
        elif self.player_1_score == 30:
            self.player_1_score = 40
        else:
            self.finish = True
            self.who_is_the_winner = 1

    def player_2_scores(self):
        if self.player_2_score == 0:
            self.player_2_score = 15
        elif self.player_2_score == 15:
            self.player_2_score = 30
        elif self.player_2_score == 30:
            self.player_2_score = 40
        else:
            self.finish = True
            self.who_is_the_winner = 2

    def winner(self):
        if self.finish:
            return self.who_is_the_winner

    def start(self, p1, p2):
        p1.score = 0
        p2.score = 0

class TennisTests(unittest.TestCase):

    def __init__(self):
        self.g = TennisGame()
        
    def test_when_game_starts_player_1_scores_zero(self):
        self.assertEqual(0, self.g.player_1_score)
    
    def test_when_game_starts_player_2_scores_zero(self):
        self.assertEqual(0, self.g.player_2_score)

    def test_when_player_1_win_the_first_ball_his_score_is_15(self):
        self.g.player_1_scores()
        self.assertEqual(15, self.g.player_1_score)

    def test_when_player_1_win_two_first_balls(self):
        self.g.player_1_scores()
        self.g.player_1_scores()
        self.assertEqual(self.g.player_1_score, 30)

    def test_when_player1_win_three_first_balls(self):
        self.g.player_1_scores()
        self.g.player_1_scores()
        self.g.player_1_scores()
        self.assertEqual(self.g.player_1_score, 40)

    def test_when_player2_win_first_balls(self):
        self.g.player_2_scores()
        self.assertEqual(self.g.player_2_score, 15)

    def test_when_player_2_win_two_first_balls(self):
        self.g.player_2_scores()
        self.g.player_2_scores()
        self.assertEqual(self.g.player_2_score, 30)

    def test_when_player2_win_three_first_balls(self):
        self.g.player_2_scores()
        self.g.player_2_scores()
        self.g.player_2_scores()
        self.assertEqual(self.g.player_2_score,40)

    def test_when_player1_six_balls_and_player2_four_ball(self):
        self.g.player_1_scores()
        self.g.player_1_scores()
        self.g.player_1_scores()
        self.g.player_2_scores()
        self.g.player_2_scores()
        self.g.player_2_scores()
        self.g.player_1_scores()
        self.g.player_2_scores()
        self.g.player_1_scores()
        self.g.player_1_scores()
        self.assertEqual(self.g.winner(), 1)

    def test_when_player_2_six_balls_and_player_1_four_balls(self):
        g = TennisGame()
        self.g.player_2_scores()
        self.g.player_2_scores()
        self.g.player_2_scores()
        self.g.player_1_scores()
        self.g.player_1_scores()
        self.g.player_1_scores()
        self.g.player_2_scores()
        self.g.player_1_scores()
        self.g.player_2_scores()
        self.g.player_2_scores()
        self.assertEqual(self.g.winner(), 2)

        
if __name__ == "__main__":
    unittest.main()








