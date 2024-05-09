from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.x = 0
        self.color(self.change_food_color())
        self.penup()
        self.possible_location = []
        self.x_pos = self.xcor()
        self.y_pos = self.ycor()
        self.food_number = 1


    def create_object(self):
        for x in range(-260, 260):
            if x % 20 == 0:
                self.possible_location.append(x)
        if self.food_number % 5 != 0:
            self.color(self.change_food_color())
            self.shapesize(1, 1)
            self.goto(random.choice(self.possible_location), random.choice(self.possible_location))
            self.x_pos = self.xcor()
            self.y_pos = self.ycor()
            self.food_number += 1
        elif self.food_number % 5 == 0:
            self.color("red")
            self.shapesize(stretch_wid=1.5, stretch_len=1.5)
            self.goto(random.choice(self.possible_location), random.choice(self.possible_location))
            self.x_pos = self.xcor()
            self.y_pos = self.ycor()
            self.food_number += 1

    def change_food_color(self):
        if self.x % 5 == 0:
            return "blue"
        elif self.x % 5 == 1:
            return "white"
        elif self.x % 5 == 2:
            return "green"
        elif self.x % 5 == 3:
            return "yellow"
        elif self.x % 5 == 4:
            return "orange"

    def change_color_button(self):
        self.x += 1
        self.color(self.change_food_color())





