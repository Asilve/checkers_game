# Checkers game
A Checkers game with an option to play against a cpu opponent. 

## Programming Language
Python. This is due to me knowing python more than other languages. If i had time to learn another language, I would have made the game in C#/C++/Java.

## Tools
* Pygame. The most used library to create games with Python. This Library is specifically for creating games, therefore the natural choice to create this game.

## Design
Below is a Diagram of how I will break up making the checkers game into smaller, manageable tasks

<img width="625" alt="CheckersStep" src="https://github.com/Asilve/checkers_game/assets/115579581/97b52df9-19c0-4532-9da7-f9fe6419c8b4">

### - Game Display and Navigation
This mainly involves the visual aspects of the game, but also navigation between the 1 player, and 2 player game formats of checkers. I believe the best way to incorporate this would be a start menu that allows you to pick between playing against the computer or against another (local) player.

### - Game pieces
The game will require the program to calculate the valid moves the player can make, and to be able to move, capture and king pieces.

### - Computer Opponent
To make a computer opponent, We need the computer to behave with some intelligence. A good algorithm to achieve this is a minimax algorithm. This will simulate the available moves the computer can make, and a number of future turns, and assign each of the simulations with a value based on the outcome. If we make the computer the MAX player, the computer will want a higher simulation value. We calculate the value by increasing the value if the computer takes a piece, and decreasing the value if they lose a piece. After every simulation has ran, it will pick the best simulation outcome and move the piece accordingly. We however must limit the amout of turns the simulation will go through due to memory and time efficency.




