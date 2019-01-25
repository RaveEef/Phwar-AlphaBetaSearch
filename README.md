# Search Algorithms Applied to PHWAR
Cedric Oeldorf
Student Number: i6167918
Department of Data Science and Knowledge Engineering, Maastricht University




# Table of Contents


1. Phwar	3
2. Methodology	4
2.1 Prerequisites	4
2.2 Gameplay	4
2.3 Data Structure	6
2.4 Game Mechanics	7
2.4.1 Movement Functions	7
2.4.2 Capturing Functions	7
2.5 Search Algorithm	8
2.5.1 Alpha-Beta Pruning	8
2.5.2 Evaluation	9
3. Test results	10
4. Conclusion	11

## 1. Phwar

Phwar, which is the shortened term for Phase War, is a board game based on a hexagonal layout consisting of individual hexagons.

![alt text][1]

The aim of the game is to either ‘capture’ all electrons, positrons or neutrons of the enemy player, or to move one's own neutron to the middle of the board. The set of rules implemented for this algorithm are as follows:

Particles can move in any of the six hexagonal directions in an unobstructed line
Pieces cannot pass through F6, only enter and exit it.
Pieces are captured in the following fashion:
Current player moves piece into victim's line of sight
Capture initiates only involving enemy pieces in the line of site of the current players last moved piece.
Simultaneous captures are possible
Sequential captures are not possible.

## 2. Methodology

This section will start out by listing the prerequisites for running this code on a machine. This will be followed by a short description on how to work the game interface and then moves onto exploring how the state of the game is saved and accessed. Lastly the functions pertaining to the game mechanics and then search algorithm will be discussed.


### 2.1 Prerequisites

The programming language chosen for this assignment is Python 3.5.2 using the IPython3 command shell. The code is split into two files, namely game_functions.py and  phwar.py. The former holds a class that contains all movement, capture and search functions needed for Phwar. The latter script is focused on initializing the game and visualizing the board.
The following packages are needed in order to run the above scripts:

- numpy 1.13.3
- sys 3.5.2
- random On board with Python 3.5
- math On board with Python 3.5
- time On board with Python 3.5
- matplotlib 2.0.2
- copy 2.5

In order to run the game, please navigate to the directory holding the two scripts, enter IPython3 and run phwar.py.

### 2.2 Gameplay

By default, the AI plays white and the player, who is black, takes the first turn. Changing line 3 in phwar.py to ’white’ will have the AI play black.
Running phwar.py will print the following in the terminal:

![alt text][2]

A list of board coordinates representing the current positions of the players pieces is depicted. Please select a piece by typing the coordinate into the command line as it appears in the list.  After this selection, a second list appears, depicting all coordinates that result in valid moves for the selected piece. In this example we will move from ‘F3’ to ‘F5’.

![alt text][3]

The terminal will print ‘nothing to capture’ and ask if there were any issues. The issues question was implemented as a way to let the player manipulate the board in order to do a sequential capture. To continue through the issues line, enter ‘n’. If there was an issue and you would like to update a position on the board, enter ‘y’.
In the event of a capture, you will be prompted to select a piece to capture as depicted below. In this case, please select a cell from the list printed above the input query.

![alt text][4]

Now a board will appear represented in the format of fig. 2 and the ai will start calculating its move.
Once it is done, the plot will close and a new one with an updated board will appear. The terminal will now revert back to giving the player the chance to select his/her next move.
Please note, in order to start a new game, fully exit IPython and re-enter it. Else old board positions might carry over into the new game.

![alt text][5]

2.3 Data Structure

The data structure is a list of lists created in lines 12 - 26 of game_functions.py.

![alt text][6]

The list named ‘grid’ in line 26 is the list that holds the whole board. It is comprised of an empty value and 11 sub-lists. The empty value serves to make indexing more intuitive by letting the content start at index 1 as opposed to 0.
Each of these sub-lists represents one ‘column’ of the hexagon, here labelled from A to K. A sub-list holds the state of every cell in its respective column. A cell’s state is also stored in a list, for which the entries represent the values  [x,y,z,charge,player,neutron]

- X, y and z represent the hexagonal coordinates which are used for calculations and traversing the board.
- ‘Charge’ can take on -1,0 or 1 and represents the type of piece
- ‘Player’ holds the color the piece belongs to
- ‘Neutron’ holds whether or not an occupied cell is a neutron.

Because looping over lists is very inefficient in Python, a set of dictionaries serving as mappings were created (lines 42 - 46). These allow access to a cell by using the traditional game coordinates (e.g. ‘F6’) and also allow access to the hexagonal coordinate system via the traditional game coordinates. This minimizes the need to loop through the board in order to search for information.  


### 2.4 Game Mechanics

The game lives within a class called “game_positions” created at line 70 of game_functions.py. We won’t be covering the small helper functions in the report, but these are described in the script via commentary.

#### 2.4.1 Movement Functions

When selecting a piece to move, the script returns all valid cells to which the selected piece can move. This search is done via the movement functions created in lines 160 to 487. Each movement direction has it’s own function, but the principle is the same across the board. The directional functions follow these steps:

- Calculate distance between the origin and destination cells.
This accesses the function cube_distance (line 140)
Depending on the direction, add and subtract 1 from two of the three hexagonal coordinates, each time saving the new cell into a list until either a piece or the edge of the board is encountered.
- Detection of pieces is done by using the new coordinate, entering it into the dictionary mapping and accessing the cell on the board list.

Each of these functions are called in the functions get_valid_moves and in get_captures. Thus they form the core for traversing the board. This leads us to the next function, capturing.

#### 2.4.2 Capturing Functions

The capturing functions are constructed in game_functions.py in lines 489 to 873.
get_captures (line 496) makes heavy use of the movement functions. It processes the board in the following fashion:
Use principle of the movement functions to search the board and return any enemy pieces in the line of sight of the piece that was just moved.
Use the movement function principles a second time in order to check what pieces are in the line of sight of the detected enemy pieces.
The charge for these pieces is then calculated and a list of capturable pieces is returned.
Make_capture (line 797) checks if there is a simultaneous capture and lets the player choose with which piece to initiate the capture.


### 2.5 Search Algorithm

For this assignment, the adversarial search algorithm “Alpha-Beta Pruning” was implemented. First, a minimax algorithm was implemented. This was then improved by implemented the alpha-beta framework. The change from minimax to alpha-beta was not a drastic one, merely a heuristic and two variables were added to each function to alter the behaviour of the search algorithm.

#### 2.5.1 Alpha-Beta Pruning

The functions min_move and max_move initiate the search algorithm and call one another recursively. They are constructed from line 1106 until the end of the games_functions.py script. The max_move and the min_move functions are mostly the same except for a minor change. The former tries to maximise its score whereas the latter tries to minimize it.
Each function takes the arguments board, player_turn, depth, a and b. The board is the list containing the current state, depth represents the search depth, a represents alpha and b represents beta.

The first thing both functions do is check whether the maximum search depth has been reached. If this is the case, the current state of the board gets evaluated and returned.
After the above check, the board is tested for whether or not it is in a “game over’ state. If this is the case, the current board gets evaluated and returned.
If the above tests are passed, the two players positions are recorded. In line 1146, the current player's pieces are filtered into a list named “legal_moves”, that holds only pieces that are eligible to be moved.
The next step (line 1157) is to return a list of cells that each of the selected pieces can move to. This list is returned as “valid_moves” in line 1163.
In line 1168 we iterate over every valid move for the current piece. A new board holding the updated move is created in the process. In line 1182 it is then investigated whether this leads to a capture or not.

Now this get a little tricky. If there are captures, new boards need to be created with every capture combination. There are 4 loops that initialize depending on how many captures can be made. Each of them ends up feeding a new board into either the min_move or the max_move function.

Simultaneous capture
These boards are created from lines 1203 - 1233. For the available captures, every combination of selected pieces to undergo the action of capturing creates a new board. This is achieved with a nested loop.
Single capture
At least two boards are created, each representing a capture done by a different piece of the player. (lines 1238 - 1256).
No capture
The board stays as is and is fed into the minimizing or maximizing function.

The principle for all these loops is the same:

A new board is created.
The board is fed into the max_move or min_move function.
A value and a board is returned (representing the choice of the player one ply deeper)
best_move and best_score gets updated when
Returned value is greater than alpha (Maximizing player)
Returned value is smaller than beta (Minimizing player)
If alpha is larger than beta, the current loop breaks and the next set of children is traversed.

After the recursive process has run through all needed children, a new board is returned. This board represents the move the AI decided to make.

#### 2.5.2 Evaluation

Line 929 constructs the function that serves to evaluate a board and give it a score. The function can be split into two parts, one part for a maximizing player and the other for a minimizing player. They are identical except for that the scoring signs are inverted.

The heuristics are represented in the following table:

##### Heuristic and Score:
- Has the current player captured any pieces / been captured +20 / -20
- Has the player captured/lost all positrons/electrons/neutrons? +100 / -100
- Did the move result in more freedom of movement? (Commented out for tournament) +(0.05*cells_reachable)
- Is the player’s/enemy player’s neutron in the center of the board? -100/+100


## 3. Test results

When minimax was implemented, the script was littered with nested for loops for traversing the board. This resulted in very inefficient game mechanics and searches. Although alpha-beta pruning brought a great improvement in speed, it was still not fast enough for implementation on the tournament day. Thus the dictionaries in lines 42 - 67 of game_functions.py were created to circumvent slow for loops.

Framework
Search Depth
Opening move time
Minimax (non-optimized board traversal)
3
> 10 -15 minutes
Alpha-Beta (non-optimized board traversal)
3
~ 5 minutes
Alpha-Beta (optimized)
3
~ 15 seconds


The above table clearly supports the notion of how great of an improvement alpha-beta pruning can be. In the non-optimized code, this addition performed in more or less a third of the time compared to traditional minimax search.

Another interesting fact was that replacing python loops with other methods came as such a vast improvement.

## 4. Conclusion
Phwar was a challenging game to implement. Due to a lack of time and a shift of focus onto code optimization, the rule of sequential capturing was left out by the AI. Unfortunately this led to several losses by default in the tournament.
Besides being a challenging game to implement, it was actually a challenging game to play. The kind of moves the implemented search algorithms come up with would be near impossible for a human to detect in such a brief period of time without prior training.
