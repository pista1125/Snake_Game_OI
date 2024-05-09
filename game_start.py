from turtle import Turtle

art = '''               
                
                
                UP
               
LEFT    DOWN   RIGHT'''

art_2 = '''
2. Player control                     1. Player control
                 
         W                                           UP
               
A       S       D                  LEFT    DOWN   RIGHT'''

class GameStart(Turtle):
    def __init__(self):
        super().__init__()
        self.time = 3
        self.color("white")
        self.hideturtle()
        self.penup()
        self.button = art
        self.button_2 = art_2
    def Start(self):
        self.write(f"Game will be start at: {self.time}\n {self.button} ", False, "center", ("Arial", 12, "normal"))
        self.time -= 1

    def Start_2(self):
        self.write(f"         Game will be start at: {self.time}\n {self.button_2} ", False, "center", ("Arial", 12, "normal"))
        self.time -= 1


