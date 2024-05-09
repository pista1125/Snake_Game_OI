from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.score_2 = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.eat_number = 1

    def update_score(self):
        self.write(f"Your score is: {self.score}", False, "center", ("Arial", 12, "normal"))

    def score_add(self):
        self.score += 1
        self.clear()
        self.update_score()

    def score_extra_add(self):
        self.score += 3
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", False, "center", ("Arial", 12, "normal"))

    def player_2_score_position(self):
        self.goto(0, -250)


    def player_2_score_1v1(self):
        self.write(f"2. Player score is: {self.score_2}", False, "center", ("Arial", 12, "normal"))

    def player_1_update(self):
        self.write(f"1. Player score is: {self.score}", False, "center", ("Arial", 12, "normal"))

    def player_2_score_team(self):
        self.write(f"Team score is: {self.score}", False, "center", ("Arial", 12, "normal"))


    def score_add_1player(self):
        self.score += 1
        self.clear()
        self.player_1_update()

    def score_extra_add_1player(self):
        self.score += 3
        self.clear()
        self.player_1_update()

    def score_add_2player(self):
        self.score_2 += 1
        self.clear()
        self.player_2_score_1v1()

    def score_extra_add_2player(self):
        self.score_2 += 3
        self.clear()
        self.player_2_score_1v1()

    def score_add_team(self):
        self.score += 1
        self.clear()
        self.player_2_score_team()

    def score_extra_add_team(self):
        self.score += 3
        self.clear()
        self.player_2_score_team()