# Snake Game Documentation
This documentation describes the code for a classic Snake Game implemented in Python using the Turtle graphics library.

## Prerequisites
To run the game, the following packages must be installed:

* Python 3
* Turtle graphics library

## Game Overview
The Snake game is a simple game where the player controls a snake that moves around the screen and eats food. As the snake eats more food, it grows in size, making it harder to avoid obstacles on the screen. If the snake collides with any obstacles, such as the boundaries of the screen or its own body, the game ends. The goal is to eat as much food as possible without colliding with anything.

## Code Overview
The code is structured in several modules:

* snake.py
* food.py
* score.py
* game_start.py
* game_input.py

The main game code is in the file main.py.

## Main
The main.py file contains the main game loop. It imports the required modules, creates a new screen using the Turtle graphics library, and sets up the game objects. The game loop runs until the player either quits the game or loses by colliding with an obstacle.

## Snake
The 'snake.py' module defines the Snake class, which represents the snake in the game. The Snake class has several methods, including:

* __init__: Initializes the snake with an initial size and position.
* move: Moves the snake in the direction it is facing.
* plus_snake: Increases the size of the snake.
* robot_pilot_move: Moves the snake automatically. 

## Food
The 'food.py' module defines the Food class, which represents the food that the snake eats. The Food class has several methods, including:

* __init__: Initializes the food with a random position on the screen.
* create_object: Creates a new food object at a random position on the screen.

## Score
The 'score.py' module defines the Score class, which keeps track of the player's score. The Score class has several methods, including:

* __init__: Initializes the score to zero.
* score_add: Increases the score by one.

## Game Start
The 'game_start.py' module defines the GameStart class, which displays the game start screen. The GameStart class has several methods, including:

* __init__: Initializes the game start screen.
* press_start: Waits for the player to press the "start" button.

## Game Input
The 'game_input.py' module defines the Game_input class, which handles the user input during the game. The Game_input class has several methods, including:

* __init__: Initializes the game input.
* left: Changes the direction of the snake to the left.
* right: Changes the direction of the snake to the right.
* up: Changes the direction of the snake to upwards.
* down: Changes the direction of the snake to downwards.

## Robot and Robot_2
The main.py file also includes two functions: robot and robot_2. These functions move the snake automatically towards the food object. The robot function moves the snake in a pattern that resembles a "Z", while robot_2 moves the snake directly towards the food object.

## Conclusion
The Snake Game implemented in Python using the Turtle graphics library is a simple yet entertaining game. This documentation describes the code structure and the functions used to create the game. With this information, users can modify and extend the game as needed