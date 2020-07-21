class Game:
    def __init__(self, scorecard):
        self.scorecard = scorecard

    def score(self):
        scorecard_as_list = [char for char in self.scorecard]
        scores = []


        roll_number = 0
        for _frame in range(10):

            score1 = scorecard_as_list[roll_number]
            current_frame_score = 0
            bonus_score = 0
            if self.is_strike(score1):
                current_frame_score = self.get_score(score1)
                bonus_score += self.get_score(scorecard_as_list[roll_number + 1])
                bonus_score += self.get_score(scorecard_as_list[roll_number + 2])
                roll_number += 1
            else:
                score2 = scorecard_as_list[roll_number + 1]
                current_frame_score = self.get_frame_score(score1, score2)

                if self.is_spare(score2):
                    bonus_score += self.get_score(scorecard_as_list[roll_number + 2])
            
                roll_number += 2
            scores.append(current_frame_score + bonus_score)
        return sum(scores) 

    def is_spare(self, score):
        return score == '/'

    def is_strike(self, score):
        return score == 'X'
    
    def is_miss(self, score):
        return score == '-'

    def get_frame_score(self, score1, score2):
        score1 = self.get_score(score1)
        score2 = self.get_score(score2)
        if self.is_spare(score2):
            score2 = 10 - score1
        return score1 + score2 

    def get_score(self, score_as_text):
        if self.is_miss(score_as_text):
            return 0
        if self.is_strike(score_as_text):
            return 10
        if self.is_spare(score_as_text):
            return '/'
        return int(score_as_text)