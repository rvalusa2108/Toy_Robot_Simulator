# Toy Robot Simulator

## Features:
 - Yaml config for defining the initial Robot grid environment setup, logger, log level
 - Package, Classes, Methods implementation for easy usability, scalability
 - Exception handling with integrating with logger
 - Pytest test cases to check the different movements, rotations of the Robot

## Requirements:

1. Robot is always facing one of the following directions: NORTH, EAST,SOUTH or WEST.
2. Robot can turn left, right, and move one step at a time.
3. Robot cannot move off the board and ignores a command forcing it to do it.
4. Robot can report its current position on the board and direction.
5. A newly created robot must be placed into location x=0 y=0 and face NORTH.
6. The board is aligned with Cartesian coordinate system. Its bottom left corner has coordinate (0,0) and top right (n-1, m-1).
 
The solution will receive commands as a text file and outputs robot's reports into STDOUT. Below are the only commands that robot understands:

PLACE x y direction     -- places robot into specified location on a board and set initial direction  
MOVE                    -- moves robot one step in the current direction  
LEFT                    -- turns robot 90 degrees anticlockwise  
RIGTH                   -- turns robot 90 degrees clockwise  
REPORT                  -- outputs current state into STDOUT  

## Execution
1. Define input commands in ./toy_robot/input_commands.txt
2. cd ./<project_repo_directory>
3. Application execution
    python ./toy_robot/main.py
4. Pytest test cases execution
    python ./toy_robot/test/test_main.py

