from turtle import Turtle

class Game_input:
    def __init__(self):
        self.menu = 0
        #This code is about a player count
        self.player_number = 0
        self.x_position = [30, -30]
        self.y_position = -100
        self.timmy_player =[]
        #This code is about a player speed
        self.speed = 0
        self.timmy_speed = []
        self.x_speed_position = [30, 0, -30]
        self.y_speed_position = -100
        self.choice_dif_level = ["hard", "normal", "easy"]
        #This code about a bounce wall
        self.bounce = ["Not bounce wall", "Bounce wall"]
        self.bounce_wall = 0
        self.timmy_wall = []
        #this code about a snake color setting
        self.x_color_position = [-100, -50, 0, 50, 100, 150]
        self.y_color_position = 30
        self.color_option = ["white", "red", "blue", "green", "yellow", "orange"]
        self.color = 0
        self.timmy_color = []
        self.color_choice = "white"
        #2. player_ color
        self.x_color_position_2 = [-100, -50, 0, 50, 100, 150]
        self.y_color_position_2 = -30
        self.color_2 = 0
        self.timmy_color_2 = []
        self.color_choice_2 = "white"
        #team, or not
        self.x_team_position = [-100, 100]
        self.y_team_position = 0
        self.timmy_team = []
        self.team_mode_option = ["1 V 1", "Team mode"]
        self.team_mode_choice = 0

    def player(self):
        for x in range(2):
            timmy = Turtle()
            timmy.color("white")
            timmy.hideturtle()
            timmy.penup()
            timmy.goto(self.y_position, self.x_position[x])
            timmy.write(f"{x+1} Player", False, "center", ("Arial", 12, "normal"))
            self.timmy_player.append(timmy)

    def choice_number(self, x, y):
        if -150 < x < -50 and 10 < y < 50:
            self.player_number = 1
        elif -150 < x < -50 and -50 < y < -10:
            self.player_number = 2

    def speed_turtle(self):
        for x in range(3):
            timmy = Turtle()
            timmy.color("white")
            timmy.hideturtle()
            timmy.penup()
            timmy.goto(self.y_speed_position, self.x_speed_position[x])
            timmy.write(f"{self.choice_dif_level[x]} Player", False, "center", ("Arial", 12, "normal"))
            self.timmy_speed.append(timmy)

    def choice_speed(self, x, y):
        if -150 < x < -50 and 25 < y < 50:
            self.speed = 0.05
        elif -150 < x < -50 and -25 < y < 25:
            self.speed = 0.1
        elif -150 < x < -50 and -50 < y < -25:
            self.speed = 0.2


    def wall_turtle(self):
        for x in range(2):
            timmy = Turtle()
            timmy.color("white")
            timmy.hideturtle()
            timmy.penup()
            timmy.goto(self.y_position, self.x_position[x])
            timmy.write(f"{self.bounce[x]} ", False, "center", ("Arial", 12, "normal"))
            self.timmy_wall.append(timmy)

    def choice_bounce(self, x, y):
        if 10 < y < 50:
            self.bounce_wall = 1
        elif -50 < y < -10:
            self.bounce_wall = 2

    def color_setting(self):
        timmy_2 = Turtle()
        timmy_2.color("white")
        timmy_2.hideturtle()
        timmy_2.penup()
        timmy_2.goto(0, 80)
        timmy_2.write(f"1. Player", False, "center", ("Arial", 12, "normal"))
        self.timmy_color.append(timmy_2)
        for x in range(6):
            timmy = Turtle()
            timmy.color("white")
            timmy.hideturtle()
            timmy.penup()
            timmy.goto(self.x_color_position[x], self.y_color_position)
            timmy.write(f"{self.color_option[x]}", False, "center", ("Arial", 12, "normal"))
            self.timmy_color.append(timmy)

    def choice_color(self, x, y):
        if 0 < y < 60 and -125 < x < -75:
            self.color_choice = self.color_option[0]
            self.color += 1
        elif 0 < y < 60 and -75 < x < -25:
            self.color_choice = self.color_option[1]
            self.color += 1
        elif 0 < y < 60 and -25 < x < 25:
            self.color_choice = self.color_option[2]
            self.color += 1
        elif 0 < y < 60 and 25 < x < 75:
            self.color_choice = self.color_option[3]
            self.color += 1
        elif 0 < y < 60 and 75 < x < 125:
            self.color_choice = self.color_option[4]
            self.color += 1
        elif 0 < y < 60 and 125 < x < 175:
            self.color_choice = self.color_option[5]
            self.color += 1

    def color_setting_2(self):
        timmy_2 = Turtle()
        timmy_2.color("white")
        timmy_2.hideturtle()
        timmy_2.penup()
        timmy_2.goto(0, -80)
        timmy_2.write(f"2. Player", False, "center", ("Arial", 12, "normal"))
        self.timmy_color_2.append(timmy_2)
        for x in range(6):
            timmy = Turtle()
            timmy.color("white")
            timmy.hideturtle()
            timmy.penup()
            timmy.goto(self.x_color_position_2[x], self.y_color_position_2)
            timmy.write(f"{self.color_option[x]}", False, "center", ("Arial", 12, "normal"))
            self.timmy_color_2.append(timmy)

    def choice_color_2(self, x, y):
        if -60 < y < 0 and -125 < x < -75:
            self.color_choice_2 = self.color_option[0]
            self.color_2 += 1
        elif -60 < y < 0 and -75 < x < -25:
            self.color_choice_2 = self.color_option[1]
            self.color_2 += 1
        elif -60 < y < 0 and -25 < x < 25:
            self.color_choice_2 = self.color_option[2]
            self.color_2 += 1
        elif -60 < y < 0 and 25 < x < 75:
            self.color_choice_2 = self.color_option[3]
            self.color_2 += 1
        elif -60 < y < 0 and 75 < x < 125:
            self.color_choice_2 = self.color_option[4]
            self.color_2 += 1
        elif -60 < y < 0 and 125 < x < 175:
            self.color_choice_2 = self.color_option[5]
            self.color_2 += 1

    def team_or_not(self):
        for x in range(2):
            timmy = Turtle()
            timmy.color("white")
            timmy.hideturtle()
            timmy.penup()
            timmy.goto(self.x_team_position[x], self.y_team_position)
            timmy.write(f"{self.team_mode_option[x]}", False, "center", ("Arial", 12, "normal"))
            self.timmy_team.append(timmy)

    def team_choice(self, x, y):
        if -150 < x < -50 and -30 < y < 30:
            self.team_mode_choice = 1
        elif 50 < x < 150 and -30 < y < 30:
            self.team_mode_choice = 2



    def timmy_clear_player(self):
        for timmy in self.timmy_player:
            timmy.clear()

    def timmy_clear_color(self):
        for timmy in self.timmy_color:
            timmy.clear()

    def timmy_clear_color_2(self):
        for timmy in self.timmy_color_2:
            timmy.clear()

    def timmy_clear_speed(self):
        for timmy in self.timmy_speed:
            timmy.clear()

    def timmy_clear_wall(self):
        for timmy in self.timmy_wall:
            timmy.clear()

    def timmy_clear_team(self):
        for timmy in self.timmy_team:
            timmy.clear()

