import numpy as np
#import array
from sys import stdout
#import random
from math import *
import time
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import copy


########################
# Create hexagonal coordinates
A = [np.nan,np.nan,np.nan,[-5,5,0,0,np.nan,np.nan],[-5,4,1,0,np.nan,np.nan],[-5,3,2,0,np.nan,np.nan],[-5,2,3,0,np.nan,np.nan],[-5,1,4,0,np.nan,np.nan],[-5,0,5,0,np.nan,np.nan],np.nan,np.nan,np.nan]
B = [np.nan,np.nan,np.nan,[-4,5,-1,0,np.nan,np.nan],[-4,4,0,0,np.nan,np.nan],[-4,3,1,0,np.nan,np.nan],[-4,2,2,0,np.nan,np.nan],[-4,1,3,0,np.nan,np.nan],[-4,0,4,0,np.nan,np.nan],[-4,-1,5,0,np.nan,np.nan],np.nan,np.nan]
C = [np.nan,np.nan,[-3,5,-2,0,np.nan,np.nan],[-3,4,-1,0,np.nan,np.nan],[-3,3,0,0,np.nan,np.nan],[-3,2,1,0,np.nan,np.nan],[-3,1,2,0,np.nan,np.nan],[-3,0,3,0,np.nan,np.nan],[-3,-1,4,0,np.nan,np.nan],[-3,-2,5,0,np.nan,np.nan],np.nan,np.nan]
D = [np.nan,np.nan,[-2,5,-3,0,np.nan,np.nan],[-2,4,-2,0,np.nan,np.nan],[-2,3,-1,0,np.nan,np.nan],[-2,2,0,0,np.nan,np.nan],[-2,1,1,0,np.nan,np.nan],[-2,0,2,0,np.nan,np.nan],[-2,-1,3,0,np.nan,np.nan],[-2,-2,4,0,np.nan,np.nan],[-2,-3,5,0,np.nan,np.nan],np.nan]
E = [np.nan,[-1,5,-4,0,np.nan,np.nan],[-1,4,-3,0,np.nan,np.nan],[-1,3,-2,0,np.nan,np.nan],[-1,2,-1,0,np.nan,np.nan],[-1,1,0,0,np.nan,np.nan],[-1,0,1,0,np.nan,np.nan],[-1,-1,2,0,np.nan,np.nan],[-1,-2,3,0,np.nan,np.nan],[-1,-3,4,0,np.nan,np.nan],[-1,-4,5,0,np.nan,np.nan],np.nan]
F = [np.nan,[0,5,-5,0,np.nan,np.nan],[0,4,-4,0,np.nan,np.nan],[0,3,-3,0,np.nan,np.nan],[0,2,-2,0,np.nan,np.nan],[0,1,-1,0,np.nan,np.nan],[0,0,0,0,np.nan,np.nan],[0,-1,1,0,np.nan,np.nan],[0,-2,2,0,np.nan,np.nan],[0,-3,3,0,np.nan,np.nan],[0,-4,4,0,np.nan,np.nan],[0,-5,5,0,np.nan,np.nan]]
G = [np.nan,[1,4,-5,0,np.nan,np.nan],[1,3,-4,0,np.nan,np.nan],[1,2,-3,0,np.nan,np.nan],[1,1,-2,0,np.nan,np.nan],[1,0,-1,0,np.nan,np.nan],[1,-1,0,0,np.nan,np.nan],[1,-2,1,0,np.nan,np.nan],[1,-3,2,0,np.nan,np.nan],[1,-4,3,0,np.nan,np.nan],[1,-5,4,0,np.nan,np.nan],np.nan]
H = [np.nan,np.nan,[2,3,-5,0,np.nan,np.nan],[2,2,-4,0,np.nan,np.nan],[2,1,-3,0,np.nan,np.nan],[2,0,-2,0,np.nan,np.nan],[2,-1,-1,0,np.nan,np.nan],[2,-2,0,0,np.nan,np.nan],[2,-3,1,0,np.nan,np.nan],[2,-4,2,0,np.nan,np.nan],[2,-5,3,0,np.nan,np.nan],np.nan]
I = [np.nan,np.nan,[3,2,-5,0,np.nan,np.nan],[3,1,-4,0,np.nan,np.nan],[3,0,-3,0,np.nan,np.nan],[3,-1,-2,0,np.nan,np.nan],[3,-2,-1,0,np.nan,np.nan],[3,-3,0,0,np.nan,np.nan],[3,-4,1,0,np.nan,np.nan],[3,-5,2,0,np.nan,np.nan],np.nan,np.nan]
J = [np.nan,np.nan,np.nan,[4,1,-5,0,np.nan,np.nan],[4,0,-4,0,np.nan,np.nan],[4,-1,-3,0,np.nan,np.nan],[4,-2,-2,0,np.nan,np.nan],[4,-3,-1,0,np.nan,np.nan],[4,-4,0,0,np.nan,np.nan],[4,-5,1,0,np.nan,np.nan],np.nan,np.nan]
K = [np.nan,np.nan,np.nan,[5,0,-5,0,np.nan,np.nan],[5,-1,-4,0,np.nan,np.nan],[5,-2,-3,0,np.nan,np.nan],[5,-3,-2,0,np.nan,np.nan],[5,-4,-1,0,np.nan,np.nan],[5,-5,0,0,np.nan,np.nan],np.nan,np.nan,np.nan]

grid = [np.nan,A,B,C,D,E,F,G,H,I,J,K]

positions = ['A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B3', 'B4',
'B5', 'B6', 'B7', 'B8', 'B9', 'C2', 'C3', 'C4',
'C5', 'C6', 'C7', 'C8', 'C9', 'D2', 'D3', 'D4',
'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'E1', 'E2',
'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10',
'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',
'F9', 'F10', 'F11', 'G1', 'G2', 'G3', 'G4',
'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'H2', 'H3',
'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'I2',
'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'J3',
'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'K3', 'K4',
'K5', 'K6', 'K7','K8']


#################################
## Dictionaries mapping cell names to column indices and to coordinates
## Used for more efficient board search
#################################
map_from_alpha_to_index = {"A" : 1,"B" : 2,"C" : 3,"D" : 4,"E" : 5,"F" : 6,"G" : 7,"H" : 8,"I" : 9,"J" : 10,"K" : 11}
map_from_index_to_alpha = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K"}
map_coordinate_alpha = {
repr([-5,5,0]) : 'A3', repr([-5,4,1]) : 'A4', repr([-5,3,2]) : 'A5', repr([-5,2,3]) : 'A6', repr([-5,1,4]) : 'A7',
repr([-5,0,5]) : 'A8', repr([-4,5,-1]) : 'B3', repr([-4,4,0]) : 'B4', repr([-4,3,1]) : 'B5', repr([-4,2,2]) : 'B6',
repr([-4,1,3]) : 'B7', repr([-4,0,4]) : 'B8', repr([-4,-1,5]) : 'B9',repr([-3,5,-2]) : 'C2',repr([-3,4,-1]) : 'C3',
repr([-3,3,0]) : 'C4', repr([-3,2,1]) : 'C5',repr([-3,1,2]) : 'C6',repr([-3,0,3]) : 'C7',repr([-3,-1,4]) : 'C8',
repr([-3,-2,5]) : 'C9', repr([-2,5,-3]) : 'D2',repr([-2,4,-2]) : 'D3',repr([-2,3,-1]) : 'D4',repr([-2,2,0]) : 'D5',
repr([-2,1,1]) : 'D6', repr([-2,0,2]) : 'D7',repr([-2,-1,3]) : 'D8', repr([-2,-2,4]) : 'D9', repr([-2,-3,5]) : 'D10',
repr([-1,5,-4]) : 'E1', repr([-1,4,-3]) : 'E2',repr([-1,3,-2]) : 'E3',repr([-1,2,-1]) : 'E4',repr([-1,1,0]) : 'E5',
repr([-1,0,1]) : 'E6', repr([-1,-1,2]) : 'E7', repr([-1,-2,3]) : 'E8',repr([-1,-3,4]) : 'E9', repr([-1,-4,5]) : 'E10',
repr([0,5,-5]) : 'F1', repr([0,4,-4]) : 'F2',repr([0,3,-3]) : 'F3',repr([0,2,-2]) : 'F4',repr([0,1,-1]) : 'F5',
repr([0,0,0]) : 'F6', repr([0,-1,1]) : 'F7', repr([0,-2,2]) : 'F8',repr([0,-3,3]) : 'F9',repr([0,-4,4]) : 'F10',
repr([0,-5,5]) : 'F11', repr([1,4,-5]) : 'G1',repr([1,3,-4]) : 'G2',repr([1,2,-3]) : 'G3',repr([1,1,-2]) : 'G4',
repr([1,0,-1]) : 'G5', repr([1,-1,0]) : 'G6',repr([1,-2,1]) : 'G7', repr([1,-3,2]) : 'G8',repr([1,-4,3]) : 'G9',
repr([1,-5,4]) : 'G10', repr([2,3,-5]) : 'H2',repr([2,2,-4]) : 'H3',repr([2,1,-3]) : 'H4',repr([2,0,-2]) : 'H5',
repr([2,-1,-1]) : 'H6', repr([2,-2,0]) : 'H7',repr([2,-3,1]) : 'H8', repr([2,-4,2]) : 'H9', repr([2,-5,3]) : 'H10',
repr([3,2,-5]) : 'I2', repr([3,1,-4]) : 'I3',repr([3,0,-3]) : 'I4',repr([3,-1,-2]) : 'I5',repr([3,-2,-1]) : 'I6',
repr([3,-3,0]) : 'I7', repr([3,-4,1]) : 'I8', repr([3,-5,2]) : 'I9',repr([4,1,-5]) : 'J3',repr([4,0,-4]) : 'J4',
repr([4,-1,-3]) : 'J5', repr([4,-2,-2]) : 'J6',repr([4,-3,-1]) : 'J7',repr([4,-4,0]) : 'J8',repr([4,-5,1]) : 'J9',
repr([5,0,-5]) : 'K3', repr([5,-1,-4]) : 'K4',repr([5,-2,-3]) : 'K5',repr([5,-3,-2]) : 'K6',repr([5,-4,-1]) : 'K7',
repr([5,-5,0]) : 'K8'
}

class game_positions:

    def __init__(self, board, player = "black", history = [], gameover = False, player_positions = [], valid_moves = [], new_cell = [],
                    pieces_being_captured = [], pieces_capturing_enemy = [], depth =3, number_of_players_black = 9, number_of_players_white = 9,move_made = []):
        self.board = board
        self.player = player
        self.history = history
        self.gameover = gameover
        self.player_positions = player_positions
        self.valid_moves = valid_moves
        self.new_cell = new_cell
        self.pieces_being_captured = pieces_being_captured
        self.pieces_capturing_enemy = pieces_capturing_enemy
        self.depth = depth
        self.number_of_players_black = number_of_players_black
        self.number_of_players_white = number_of_players_white
        self.move = move_made

    def getboard(self):
        return self.board

    ###########################################################################
    ## Sets starting positions for all pieces
    ###########################################################################
    def setboard(self,board = None):
        board[map_from_alpha_to_index["F"]][1][3] = 0
        board[map_from_alpha_to_index["F"]][1][4] = "black"
        board[map_from_alpha_to_index["F"]][1][5] = "neutron"
        board[map_from_alpha_to_index["F"]][2][3]= -1
        board[map_from_alpha_to_index["F"]][2][4] = "black"
        board[map_from_alpha_to_index["F"]][3][3] = -1
        board[map_from_alpha_to_index["F"]][3][4] = "black"
        board[map_from_alpha_to_index["D"]][2][3] = -1
        board[map_from_alpha_to_index["D"]][2][4] = "black"
        board[map_from_alpha_to_index["E"]][1][3] = 1
        board[map_from_alpha_to_index["E"]][1][4] = "black"
        board[map_from_alpha_to_index["E"]][2][3] = 1
        board[map_from_alpha_to_index["E"]][2][4] = "black"
        board[map_from_alpha_to_index["H"]][2][3] = -1
        board[map_from_alpha_to_index["H"]][2][4] = "black"
        board[map_from_alpha_to_index["G"]][1][3] = 1
        board[map_from_alpha_to_index["G"]][1][4] = "black"
        board[map_from_alpha_to_index["G"]][2][3] = 1
        board[map_from_alpha_to_index["G"]][2][4] = "black"

        board[map_from_alpha_to_index["F"]][11][3] = 0
        board[map_from_alpha_to_index["F"]][11][4] = "white"
        board[map_from_alpha_to_index["F"]][11][5] = "neutron"
        board[map_from_alpha_to_index["F"]][10][3]= -1
        board[map_from_alpha_to_index["F"]][10][4] = "white"
        board[map_from_alpha_to_index["F"]][9][3] = -1
        board[map_from_alpha_to_index["F"]][9][4] = "white"
        board[map_from_alpha_to_index["D"]][10][3] = -1
        board[map_from_alpha_to_index["D"]][10][4] = "white"
        board[map_from_alpha_to_index["E"]][10][3] = 1
        board[map_from_alpha_to_index["E"]][10][4] = "white"
        board[map_from_alpha_to_index["E"]][9][3] = 1
        board[map_from_alpha_to_index["E"]][9][4] = "white"
        board[map_from_alpha_to_index["H"]][10][3] = -1
        board[map_from_alpha_to_index["H"]][10][4] = "white"
        board[map_from_alpha_to_index["G"]][10][3] = 1
        board[map_from_alpha_to_index["G"]][10][4] = "white"
        board[map_from_alpha_to_index["G"]][9][3] = 1
        board[map_from_alpha_to_index["G"]][9][4] = "white"
        self.board = board


    ###########################################################################
    ## Retrieve distance between two points on grid
    ###########################################################################
    def cube_distance(self, a, b):
        return (abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])) / 2


    ###########################################################################
    ## Retrieve player positions
    ###########################################################################

    def get_player_positions(self, board, player_turn):
        player_positions = []
        for i in range(1, len(board)):
            if str(board[i]) != 'nan':
                for j in range(1,len(board[i])):
                    if str(board[i][j]) != 'nan':
                        if board[i][j][4] == player_turn:
                            #player_coordinates.append(board[i][j][0:4])
                            player_positions.append(str(map_from_index_to_alpha[i])+str(j))
        self.player_positions = player_positions
        return player_positions

#******************************************************************************
# MOVEMENT FUNCTIONS
    ###########################################################################
    ## FUNCTION FOR REPLACING PIECES ON BOARD
    ###########################################################################
    def replace_pieces(self,board,moving_piece,destination):
        moving_piece_letter = moving_piece[0]
        moving_piece_number = moving_piece[1:]
        moving_piece_cell = board[map_from_alpha_to_index[moving_piece_letter]][int(moving_piece_number)]

        destination_letter = destination[0]
        destination_number = destination[1:]
        destination_cell = board[map_from_alpha_to_index[destination_letter]][int(destination_number)]

        board[map_from_alpha_to_index[destination_letter]][int(destination_number)][3] = board[map_from_alpha_to_index[moving_piece_letter]][int(moving_piece_number)][3]
        board[map_from_alpha_to_index[destination_letter]][int(destination_number)][4] = board[map_from_alpha_to_index[moving_piece_letter]][int(moving_piece_number)][4]
        board[map_from_alpha_to_index[destination_letter]][int(destination_number)][5] = board[map_from_alpha_to_index[moving_piece_letter]][int(moving_piece_number)][5]
        board[map_from_alpha_to_index[moving_piece_letter]][int(moving_piece_number)][3] = 0
        board[map_from_alpha_to_index[moving_piece_letter]][int(moving_piece_number)][4] = np.nan
        board[map_from_alpha_to_index[moving_piece_letter]][int(moving_piece_number)][5] = np.nan

        return board
    ###########################################################################
    ## Validate Vertical move
    ###########################################################################
    def move_vertical(self,board,old_coord, old_cell_letter, old_cell_number, new_coord, new_cell_letter, new_cell_number):
        valid = True
        distance = self.cube_distance(old_coord, new_coord)
        moves = []
        y_coord = []
        z_coord = []

        if int(old_cell_number) < int(new_cell_number):                                     ## Check for up vs down movement
            ## DOWNWARD MOVEMENT
            for y in range(int(old_coord[1]-1), int((old_coord[1] - 1) - (distance)),-1):   ## Iterate through every cell between starting point and destination
                y_coord.append(y)
            for z in range(int(old_coord[2]+1), int((old_coord[2]+1) + (distance))):
                z_coord.append(z)
            for i in range(0,len(y_coord)):
                move = [old_coord[0], y_coord[i], z_coord[i]]
                moves.append(move)
        if int(old_cell_number) > int(new_cell_number):
            ## UPWARD MOVEMENT
            for y in range(int(old_coord[1]+1), int((old_coord[1]+1) + (distance))):
                y_coord.append(y)
            for z in range(int(old_coord[2]-1), int((old_coord[2] - 1) - (distance)),-1):
                z_coord.append(z)
            for i in range(0,len(z_coord)):
                move = [old_coord[0], y_coord[i], z_coord[i]]
                moves.append(move)

        occupation = []
        colors = []
        for move in moves:
            alpha = map_coordinate_alpha[repr(move)]
            letter = map_from_alpha_to_index[alpha[0]]
            number = int(alpha[1:])
            occupation.append(board[letter][number][3])
            colors.append(board[letter][number][4])

        if sum(np.absolute(occupation)) != 0:                                               ## return a false valid vaiable if rules are broken
            valid = False
        if str(board[new_cell_letter][int(new_cell_number)][4]) != 'nan':
            valid = False
        colors = colors[1:]
        if ('black' in colors) or ('white' in colors):                                          ## test for occupation
            valid = False
        if [0,0,0] in moves[0:-1]:                                                              ## test for move through F6
            valid = False

        return valid

    ###########################################################################
    ## Validate South eastern MOVE
    ###########################################################################
    def move_se(self,board,old_coord, old_cell_letter, old_cell_number, new_coord, new_cell_letter, new_cell_number):   ## Same concept as vertical
        valid = True
        distance = self.cube_distance(old_coord, new_coord)
        moves = []
        x_coord = []
        y_coord = []

        for x in range(int(old_coord[0]+1), int((old_coord[0]+1) + (distance))):
            x_coord.append(x)
        for y in range(int(old_coord[1]-1), int((old_coord[1] - 1) - (distance)),-1):
            y_coord.append(y)
        for i in range(0,len(x_coord)):
            move = [x_coord[i],y_coord[i],old_coord[2]]
            moves.append(move)

        occupation = []
        colors = []
        for move in moves:
            alpha = map_coordinate_alpha[repr(move)]
            letter = map_from_alpha_to_index[alpha[0]]
            number = int(alpha[1:])
            occupation.append(board[letter][number][3])
            colors.append(board[letter][number][4])

        if sum(np.absolute(occupation)) != 0:
            valid = False
        if [0,0,0] in moves[0:-1]:
            valid = False
        if str(board[new_cell_letter][int(new_cell_number)][4]) != 'nan':
            valid = False
        colors = colors[1:]
        return valid


    ###########################################################################
    ## Validate North Eastern MOVE
    ###########################################################################
    def move_ne(self,board,old_coord, old_cell_letter, old_cell_number, new_coord, new_cell_letter, new_cell_number):
        valid = True
        distance = self.cube_distance(old_coord, new_coord)
        moves = []
        x_coord = []
        z_coord = []
        for x in range(int(old_coord[0]+1), int((old_coord[0]+1) + (distance))):
            x_coord.append(x)
        for z in range(int(old_coord[2]-1), int((old_coord[2] - 1) - (distance)),-1):
            z_coord.append(z)
        for i in range(0,len(x_coord)):
            move = [x_coord[i],old_coord[1], z_coord[i]]
            moves.append(move)
        occupation = []
        colors = []

        for move in moves:
            alpha = map_coordinate_alpha[repr(move)]
            letter = map_from_alpha_to_index[alpha[0]]
            number = int(alpha[1:])
            occupation.append(board[letter][number][3])
            colors.append(board[letter][number][4])

        if sum(np.absolute(occupation)) != 0:
            valid = False
        if [0,0,0] in moves[0:-1]:
            valid = False
        if str(board[new_cell_letter][int(new_cell_number)][4]) != 'nan':
            valid = False
        colors = colors[1:]
        return valid


    ###########################################################################
    ## Validate South Western
    ###########################################################################
    def move_sw(self,board,old_coord, old_cell_letter, old_cell_number, new_coord, new_cell_letter, new_cell_number):
        valid = True
        distance = self.cube_distance(old_coord, new_coord)
        moves = []
        x_coord = []
        z_coord = []
        for x in range(int(old_coord[0]-1), int((old_coord[0]-1) - (distance)), -1):
            x_coord.append(x)
        for z in range(int(old_coord[2]+1), int((old_coord[2] + 1) + (distance))):
            z_coord.append(z)
        for i in range(0,len(x_coord)):
            move = [x_coord[i],old_coord[1],z_coord[i]]
            moves.append(move)

        occupation = []
        colors = []
        for move in moves:
            alpha = map_coordinate_alpha[repr(move)]
            letter = map_from_alpha_to_index[alpha[0]]
            number = int(alpha[1:])
            occupation.append(board[letter][number][3])
            colors.append(board[letter][number][4])

        if sum(np.absolute(occupation)) != 0:
            valid = False
        if [0,0,0] in moves[0:-1]:
            valid = False
        if str(board[new_cell_letter][int(new_cell_number)][4]) != 'nan':
            valid = False

        return valid


    ###########################################################################
    ## Validate NORTH WESTERN MOVE
    ###########################################################################
    def move_nw(self,board,old_coord, old_cell_letter, old_cell_number, new_coord, new_cell_letter, new_cell_number):
        valid = True
        distance = self.cube_distance(old_coord, new_coord)
        moves = []
        x_coord = []
        y_coord = []
        for x in range(int(old_coord[0]-1), int((old_coord[0]-1) - (distance)), -1):
            x_coord.append(x)
        for y in range(int(old_coord[1]+1), int((old_coord[1] + 1) + (distance))):
            y_coord.append(y)
        for i in range(0,len(x_coord)):
            move = [x_coord[i],y_coord[i],old_coord[2]]
            moves.append(move)

        occupation = []
        colors = []
        for move in moves:
            alpha = map_coordinate_alpha[repr(move)]
            letter = map_from_alpha_to_index[alpha[0]]
            number = int(alpha[1:])
            occupation.append(board[letter][number][3])
            colors.append(board[letter][number][4])

        if sum(np.absolute(occupation)) != 0:
            valid = False
        if [0,0,0] in moves[0:-1]:
            valid = False
        if str(board[new_cell_letter][int(new_cell_number)][4]) != 'nan':
            valid = False
        colors = colors[1:]
        if ('black' in colors) or ('white' in colors):
            valid = False

        return valid


    ###########################################################################
    ##  USE DIRECTIONAL VALIDATION FUNCTIONS TO GET EVERY VALID MOVE FOR A GIVEN PIECE
    ###########################################################################
    def get_valid_moves(self, board, player_turn, old_cell, old_cell_letter, old_cell_number):
        valid_moves = []
        for pos in positions:
            pos_letter = map_from_alpha_to_index[pos[0]]
            pos_number = pos[1:]
            pos_cell = board[pos_letter][int(pos_number)]
            pos_coord = pos_cell[0:3]
            old_coord = old_cell[0:3]

            ## Find out which axis stays constant to deduct direction
            constant_axis = []
            for i in range(0,len(old_coord)):
                constant_axis.append(old_coord[i] == pos_coord[i])

            if pos_letter == map_from_alpha_to_index[old_cell_letter]:
                valid = self.move_vertical(board,old_coord, old_cell_letter, old_cell_number, pos_coord, pos_letter, pos_number)
                if valid == True:
                    valid_moves.append(pos)

            if pos_letter < map_from_alpha_to_index[old_cell_letter]:

                    #######################################################
                    #### NORTH WEST MOVE
                    #######################################################
                if str(constant_axis[2]) == 'True':
                    valid = self.move_nw(board,old_coord, old_cell_letter, old_cell_number, pos_coord, pos_letter, pos_number)
                    if valid == True:
                        valid_moves.append(pos)
                    #######################################################
                    #### SOUTH WEST MOVE
                    #######################################################
                if str(constant_axis[1]) == 'True':
                    valid = self.move_sw(board,old_coord, old_cell_letter, old_cell_number, pos_coord, pos_letter, pos_number)
                    if valid == True:
                        valid_moves.append(pos)

            if pos_letter > map_from_alpha_to_index[old_cell_letter]:

                if str(constant_axis[2]) == 'True':
                    #######################################################
                    #### SOUTH EAST MOVE
                    #######################################################
                    valid = self.move_se(board,old_coord, old_cell_letter, old_cell_number, pos_coord, pos_letter, pos_number)
                    if valid == True:
                        valid_moves.append(pos)
                if str(constant_axis[1]) == 'True':
                    #######################################################
                    #### NORTH EAST MOVE
                    #######################################################
                    valid = self.move_ne(board,old_coord, old_cell_letter, old_cell_number, pos_coord, pos_letter, pos_number)
                    if valid == True:
                        valid_moves.append(pos)

        self.valid_moves = valid_moves
        return valid_moves


    ###########################################################################
    ## MOVE FUNCTION FOR PLAYER (NOT AI)
    ###########################################################################
    def make_move(self, board, player_turn):
        #print(self.player_positions)
        legal_moves = []
        for i in range(0,len(self.player_positions)):
            old_cell_letter = self.player_positions[i][0]
            old_cell_number = self.player_positions[i][1:]
            old_cell = board[map_from_alpha_to_index[old_cell_letter]][int(old_cell_number)]
            valid_moves = self.get_valid_moves(board=board, player_turn=player_turn, old_cell=old_cell, old_cell_letter=old_cell_letter, old_cell_number = old_cell_number)
            #print("VALID MOVES FOR" + self.player_positions[i])
            #print(valid_moves)
            if len(valid_moves) >= 1:
                legal_moves.append(self.player_positions[i])
        print(legal_moves)
        ###################
        ## Input
        ###################
        while True:
            old_cell = input("Which cell would you like to play? Insert here: ")
            if old_cell not in legal_moves:
                print("INVALID")
                continue

            old_cell_letter = old_cell[0]
            old_cell_number = old_cell[1:]
            old_cell = board[map_from_alpha_to_index[old_cell_letter]][int(old_cell_number)]
            valid_moves = self.get_valid_moves(board=board, player_turn=player_turn, old_cell=old_cell, old_cell_letter=old_cell_letter, old_cell_number = old_cell_number)
            print(self.valid_moves)
            new_cell = input("Which cell would you like to move to? Insert here: ")
            if new_cell not in self.valid_moves:
                print("INVALID")
                continue
            new_cell_letter = new_cell[0]
            new_cell_number = new_cell[1:]
            new_cell = board[map_from_alpha_to_index[new_cell_letter]][int(new_cell_number)]
            self.new_cell = new_cell

            ## Update board
            self.board = self.replace_pieces(self.board,str(old_cell_letter+str(old_cell_number)),str(new_cell_letter+str(new_cell_number)))

            if (str(new_cell_letter) == 'F') and (int(new_cell_number) == 6):
                if self.board[map_from_alpha_to_index[new_cell_letter]][int(new_cell_number)][5] == 'neutron':
                    print(player_turn + " WINS")
                    print("Neutron reached middle of board")
                    self.gameover = True
            break

#*****************************************************************************
## FUNCTIONS WITH REGARDS TO CAPTURING


    ###########################################################################
    ## RETRIEVE ALL PIECES IN VIEW OF PLAYER PIECES
    ###########################################################################
    def get_captures(self, board, player_turn):
        pieces_being_captured = []
        pieces_capturing_enemy = []
        ## find which pieces to capture
        if player_turn == 'black':
            enemy = 'white'
        else:
            enemy = 'black'

        i = 0

        ## For every move, check what is in view.
        ## If opposite team piece is in view, check what is in view of that piece
        ## ifthe sum of charges around this piece is 0, append cell to captures list

        pos_cell = self.new_cell.copy()
        pos_coord = pos_cell[0:3]

        ##############################
        ## MOVE UP
        capture_piece = []
        capture_piece_alpha = []
        temp = pos_coord.copy()
        capsign = False
        while capsign == False:

            temp[1] = temp[1] + 1
            temp[2] = temp[2] - 1
            if (temp[1] > 5) or (temp[2] < -5): ## dont let search go above border
                break

            alpha = map_coordinate_alpha[repr(temp)]
            letter = map_from_alpha_to_index[alpha[0]]
            number = int(alpha[1:])
            if str(board[letter][number][4]) == enemy:
                capture_piece.append(board[letter][number])
                capture_piece_alpha.append(str(map_from_index_to_alpha[letter])+str(number))
                capsign = True

        ##############################
        ## MOVE Down
        temp = pos_coord.copy()
        capsign = False
        while capsign == False:
            temp[1] = temp[1] - 1
            temp[2] = temp[2] + 1
            if (temp[2] > 5) or (temp[1] < -5): ## dont let search go above border
                break
            alpha = map_coordinate_alpha[repr(temp)]
            letter = map_from_alpha_to_index[alpha[0]]
            number = int(alpha[1:])
            if str(board[letter][number][4]) == enemy:
                capture_piece.append(board[letter][number])
                capture_piece_alpha.append(str(map_from_index_to_alpha[letter])+str(number))
                capsign = True

        ##############################
        ## MOVE SE
        temp = pos_coord.copy()
        capsign = False
        while capsign == False:

            temp[0] = temp[0] + 1
            temp[1] = temp[1] - 1
            if (temp[0] > 5) or (temp[1] < -5): ## dont let search go above border
                break
            alpha = map_coordinate_alpha[repr(temp)]
            letter = map_from_alpha_to_index[alpha[0]]
            number = int(alpha[1:])
            if str(board[letter][number][4]) == enemy:
                capture_piece.append(board[letter][number])
                capture_piece_alpha.append(str(map_from_index_to_alpha[letter])+str(number))
                capsign = True


        ##############################
        ## MOVE NE
        temp = pos_coord.copy()
        capsign = False
        while capsign == False:

            temp[0] = temp[0] + 1
            temp[2] = temp[2] - 1
            if (temp[0] > 5) or (temp[2] < -5): ## dont let search go above border
                break
            alpha = map_coordinate_alpha[repr(temp)]
            letter = map_from_alpha_to_index[alpha[0]]
            number = int(alpha[1:])
            if str(board[letter][number][4]) == enemy:
                capture_piece.append(board[letter][number])
                capture_piece_alpha.append(str(map_from_index_to_alpha[letter])+str(number))
                capsign = True


        ##############################
        ## MOVE SW
        temp = pos_coord.copy()
        capsign = False
        while capsign == False:

            temp[0] = temp[0] - 1
            temp[2] = temp[2] + 1
            if (temp[2] > 5) or (temp[0] < -5): ## dont let search go above border
                break
            alpha = map_coordinate_alpha[repr(temp)]
            letter = map_from_alpha_to_index[alpha[0]]
            number = int(alpha[1:])
            if str(board[letter][number][4]) == enemy:
                capture_piece.append(board[letter][number])
                capture_piece_alpha.append(str(map_from_index_to_alpha[letter])+str(number))
                capsign = True

        ##############################
        ## MOVE NW
        temp = pos_coord.copy()
        capsign = False
        while capsign == False:

            temp[0] = temp[0] - 1
            temp[1] = temp[1] + 1
            if (temp[1] > 5) or (temp[0] < -5): ## dont let search go above border
                break
            alpha = map_coordinate_alpha[repr(temp)]
            letter = map_from_alpha_to_index[alpha[0]]
            number = int(alpha[1:])
            if str(board[letter][number][4]) == enemy:
                capture_piece.append(board[letter][number])
                capture_piece_alpha.append(str(map_from_index_to_alpha[letter])+str(number))
                capsign = True

        #######################################
        ## ITERATE OVER EACH PIECE IN SIGHT OF MOVE
        #######################################
        capturing_pieces_by_move = []
        capturing_pieces_by_move_alpha = []
        for i in range(0,len(capture_piece_alpha)):
            if capture_piece_alpha[i] == []:
                capturing_pieces_by_move.append([])
                capturing_pieces_by_move_alpha.append([])

            else:
                move = capture_piece_alpha[i]
                pos_letter = map_from_alpha_to_index[move[0]]
                pos_number = move[1:]
                pos_cell = board[pos_letter][int(pos_number)]
                pos_coord = pos_cell[0:3]

                ################################################################
                ## For the piece in sight, find pieces in sight of that

                ##############################
                ## MOVE UP
                capturing_piece = []
                capturing_piece_alpha = []
                temp = pos_coord.copy()
                capsign = False
                while capsign == False:

                    temp[1] = temp[1] + 1
                    temp[2] = temp[2] - 1
                    if (temp[1] > 5) or (temp[2] < -5): ## dont let search go above border
                        break
                    alpha = map_coordinate_alpha[repr(temp)]
                    letter = map_from_alpha_to_index[alpha[0]]
                    number = int(alpha[1:])
                    if str(board[letter][number][4]) != 'nan':
                        capturing_piece.append(board[letter][number])
                        capturing_piece_alpha.append(str(map_from_index_to_alpha[letter])+str(number))
                        capsign = True


                ##############################
                ## MOVE Down
                temp = pos_coord.copy()
                capsign = False
                while capsign == False:

                    temp[1] = temp[1] - 1
                    temp[2] = temp[2] + 1
                    if (temp[2] > 5) or (temp[1] < -5): ## dont let search go above border
                        break
                    alpha = map_coordinate_alpha[repr(temp)]
                    letter = map_from_alpha_to_index[alpha[0]]
                    number = int(alpha[1:])
                    if str(board[letter][number][4]) != 'nan':
                        capturing_piece.append(board[letter][number])
                        capturing_piece_alpha.append(str(map_from_index_to_alpha[letter])+str(number))
                        capsign = True

                ##############################
                ## MOVE SE
                temp = pos_coord.copy()
                capsign = False
                while capsign == False:

                    temp[0] = temp[0] + 1
                    temp[1] = temp[1] - 1
                    if (temp[0] > 5) or (temp[1] < -5): ## dont let search go above border
                        break
                    alpha = map_coordinate_alpha[repr(temp)]
                    letter = map_from_alpha_to_index[alpha[0]]
                    number = int(alpha[1:])
                    if str(board[letter][number][4]) != 'nan':
                        capturing_piece.append(board[letter][number])
                        capturing_piece_alpha.append(str(map_from_index_to_alpha[letter])+str(number))
                        capsign = True

                ##############################
                ## MOVE NE
                temp = pos_coord.copy()
                capsign = False
                while capsign == False:

                    temp[0] = temp[0] + 1
                    temp[2] = temp[2] - 1
                    if (temp[0] > 5) or (temp[2] < -5): ## dont let search go above border
                        break
                    alpha = map_coordinate_alpha[repr(temp)]
                    letter = map_from_alpha_to_index[alpha[0]]
                    number = int(alpha[1:])
                    if str(board[letter][number][4]) != 'nan':
                        capturing_piece.append(board[letter][number])
                        capturing_piece_alpha.append(str(map_from_index_to_alpha[letter])+str(number))
                        capsign = True

                ##############################
                ## MOVE SW
                temp = pos_coord.copy()
                capsign = False
                while capsign == False:

                    temp[0] = temp[0] - 1
                    temp[2] = temp[2] + 1
                    if (temp[2] > 5) or (temp[0] < -5): ## dont let search go above border
                        break
                    alpha = map_coordinate_alpha[repr(temp)]
                    letter = map_from_alpha_to_index[alpha[0]]
                    number = int(alpha[1:])
                    if str(board[letter][number][4]) != 'nan':
                        capturing_piece.append(board[letter][number])
                        capturing_piece_alpha.append(str(map_from_index_to_alpha[letter])+str(number))
                        capsign = True

                ##############################
                ## MOVE NW
                temp = pos_coord.copy()
                capsign = False
                while capsign == False:

                    temp[0] = temp[0] - 1
                    temp[1] = temp[1] + 1
                    if (temp[1] > 5) or (temp[0] < -5): ## dont let search go above border
                        break
                    alpha = map_coordinate_alpha[repr(temp)]
                    letter = map_from_alpha_to_index[alpha[0]]
                    number = int(alpha[1:])
                    if str(board[letter][number][4]) != 'nan':
                        capturing_piece.append(board[letter][number])
                        capturing_piece_alpha.append(str(map_from_index_to_alpha[letter])+str(number))
                        capsign = True

                capturing_pieces_by_move.append(capturing_piece)
                capturing_pieces_by_move_alpha.append(capturing_piece_alpha)


            temp_calc = []
            for i in range(0,len(capturing_pieces_by_move)):
                temp_sum = sum(x.count(player_turn) for x in capturing_pieces_by_move[i])
                if temp_sum > 1:
                    l = []
                    for j in range(0,len(capturing_pieces_by_move[i])):
                        l.append(capturing_pieces_by_move[i][j][3])
                else:
                    l = []
                    l.append([])
                temp_calc.append(l)


            for i in range(0,len(temp_calc)):
                if temp_calc[i] != [[]]:
                    temp_calc[i] = sum(temp_calc[i])

            pieces_being_captured = []
            pieces_capturing_enemy = []
            for i in range(0,len(temp_calc)):
                if temp_calc[i] != [[]]:
                    if temp_calc[i] == 0:
                        pieces_capturing_enemy.append(capturing_pieces_by_move_alpha[i])
                        pieces_being_captured.append(capture_piece_alpha[i])
                        #print(capture_piece_alpha[i])

        self.pieces_being_captured = pieces_being_captured
        self.pieces_capturing_enemy = pieces_capturing_enemy
        return pieces_being_captured, pieces_capturing_enemy




    ###########################################################################
    ## MAAKE CAPTURE AS HUMAN
    ###########################################################################
    def make_capture(self, board, player_turn):
        # THIS IS A SIMULTANEOUS CAPTURE
        if len(self.pieces_being_captured) > 1:
            print("Simultaneous capture")

            for k in range(0,len(self.pieces_being_captured)):
                available_pieces = []
                for i in range(0,len(self.pieces_capturing_enemy[k])):
                    pieces = self.pieces_capturing_enemy[k].copy()
                    piece = pieces[k][i]
                    #print(piece)
                    piece_letter = piece[0]
                    piece_number = piece[1:]
                    piece_cell = board[map_from_alpha_to_index[piece_letter]][int(piece_number)]
                    if str(piece_cell[4]) == player_turn:
                        available_pieces.append(piece)
                print("#### AVAILABLE PIECES")
                print(available_pieces)

                while True:
                    piece_to_use = input("Which piece would you like to capture with? ")
                    if piece_to_use not in available_pieces:
                        print("INVALID")
                        continue
                    break

                capturing = self.pieces_being_captured[k]
                capturing_letter = capturing[0]
                capturing_number = capturing[1:]
                capturing_cell = board[map_from_alpha_to_index[capturing_letter]][int(capturing_number)]
                if capturing_cell[5] == 'neutron':
                    print("GAME OVER")
                    print(player_turn + " captured your neutron")
                    print(player_turn + " WINS")
                    self.gameover = True

                self.board = replace_pieces(self.board,str(piece_letter+str(piece_number)),capturing)
                self.new_cell = piece_cell

        if len(self.pieces_being_captured) == 1:
            available_pieces = []
            for i in range(0,len(self.pieces_capturing_enemy[0])):
                pieces = self.pieces_capturing_enemy.copy()
                piece = pieces[0][i]
                print(piece)
                piece_letter = piece[0]
                piece_number = piece[1:]

                piece_cell = board[map_from_alpha_to_index[piece_letter]][int(piece_number)]
                if str(piece_cell[4]) == player_turn:
                    available_pieces.append(piece)
            print("##################AVAILABLE PIECES")
            print(available_pieces)

            while True:
                piece_to_use = input("Which piece would you like to capture with? ")
                if piece_to_use not in available_pieces:
                    print("INVALID")
                    continue
                break
            piece_letter = piece_to_use[0]
            piece_number = piece_to_use[1:]

            capturing = self.pieces_being_captured[0]
            capturing_letter = capturing[0]
            capturing_number = capturing[1:]
            capturing_cell = board[map_from_alpha_to_index[capturing_letter]][int(capturing_number)]
            if capturing_cell[5] == 'neutron':
                print("GAME OVER")
                print(player_turn + " captured your neutron")
                print(player_turn + " WINS")
                self.gameover = True

            self.board = self.replace_pieces(self.board,str(piece_letter+str(piece_number)),capturing)
            self.new_cell = piece_cell
        if len(self.pieces_being_captured) == 0:
            print("Nothing to capture")


    ###########################################################################
    ## CHECK IF BOARD IS GAME OVER
    ###########################################################################
    def check_board_for_go(self,board, player_turn):
        if player_turn == 'black':
            player2 = 'white'
        else:
            player2 = 'black'
        go = False
        if board[map_from_alpha_to_index['F']][int(6)][5] == 'neutron':
            go = True
            print('GAME OVER IN TREE')
            print("NEUTRON IN MIDDLE")

        neutrons = []
        electrons_p = 0
        electrons_p2 = 0
        positrons_p = 0
        positrons_p2 = 0
        for i in range(1,len(board)):
            if str(board[i]) != 'nan':
                for j in range(1,len(board)):
                    if str(board[i][j]) != 'nan':
                        if board[i][j][4] == player_turn:
                            if board[i][j][3] == -1:
                                electrons_p += 1
                            if board[i][j][3] == 1:
                                positrons_p += 1
                        if board[i][j][4] == player2:
                            if board[i][j][3] == -1:
                                electrons_p2 += 1
                            if board[i][j][3] == 1:
                                positrons_p2 += 1
                        if board[i][j][5] == 'neutron':
                            neutrons.append(board[i][j])
        if len(neutrons) < 2:
            go = True
            print('GAME OVER IN TREE')
            print('NOT ENOUGH NEUTRON')
        if (electrons_p <= 1) or (electrons_p2 <= 1) or (positrons_p <= 1) or (positrons_p2 <= 1):
            go = True
            print('GAME OVER IN TREE not enough pieces')
            print(electrons_p, electrons_p2, positrons_p, positrons_p2)

        return go

###############################################################################
## Functions pertaining to the search algorithm
###############################################################################

    ###########################################################################
    ## EVALUATE BOARD FOR MINIMAX
    ###########################################################################
    def evaluate_move(self,board, player_turn, player_type):
        #does it lead to a capture?
        if player_turn == 'black':
            player2 = 'white'
            number_player_turn_pieces = self.number_of_players_black
            number_player2_pieces = self.number_of_players_white
        else:
            player2 = 'black'
            number_player2_pieces = self.number_of_players_black
            number_player_turn_pieces = self.number_of_players_white

        score = 0
        if player_type == 'max':
            # Check for neutrons and for captures
            player_count = 0
            player2_count = 0
            electrons_p = 0
            electrons_p2 = 0
            positrons_p = 0
            positrons_p2 = 0
            neutrons_p = []
            neutrons_p2 = []

            p_freedom_cell = []
            p_freedom_alpha = []
            p2_freedom_cell = []
            P2_freedom_alpha = []
            for i in range(1,len(board)):
                if str(board[i]) != 'nan':
                    for j in range(1,len(board)):
                        if str(board[i][j]) != 'nan':
                            if str(board[i][j][4]) == player_turn:
                                p_freedom_cell.append(board[i][j])
                                p_freedom_alpha.append(str(map_from_index_to_alpha[i]) + str(j))         ## Getplayer 1 positions
                                player_count += 1
                                if board[i][j][3] == -1:
                                    electrons_p += 1
                                if board[i][j][3] == 1:
                                    positrons_p += 1
                                if str(board[i][j][5]) == 'neutron':
                                    neutrons_p.append(board[i][j])
                            if str(board[i][j][4]) == player2:
                                p2_freedom_cell.append(board[i][j])
                                P2_freedom_alpha.append(str(i) + str(j))        ## Get player 2 positions
                                player2_count += 1
                                if board[i][j][3] == -1:
                                    electrons_p2 += 1
                                if board[i][j][3] == 1:
                                    positrons_p2 += 1
                                if str(board[i][j][5]) == 'neutron':
                                    neutrons_p2.append(board[i][j])

            open_cells_count = []
            #for i in range(0, len(p_freedom_cell)):
            #    temp = self.get_valid_moves(board, player_turn, p_freedom_cell[i], p_freedom_alpha[i][0], p_freedom_alpha[i][1:])
            #    open_cells_count.append(len(temp))
            #temp = sum(open_cells_count)
            #score += 0.05*temp

            if (electrons_p < 1) or  (positrons_p < 1):
                score -= 100
            if (electrons_p2 < 1) or (positrons_p2 < 1):
                score += 100

            if len(neutrons_p) == 0:
                print("Lost Neutron")
                score -= 100
            if len(neutrons_p2) == 0:
                score += 100
                print("Killed enemy Neutron")
                print("enemy Neutron in middle")
            if int(player_count) < int(number_player_turn_pieces):
                print(player_turn)
                print(player_count)
                print(number_player_turn_pieces)
                score -= 20
            if int(player2_count) < int(number_player2_pieces):
                score += 20
                print(player2_count)
                print(number_player2_pieces)
            if (str(board[6][6][4]) == player_turn) and (str(board[6][6][5]) == 'neutron'):
                score += 100
                print("Netron in middle")
            if (str(board[6][6][4]) == player2) and (str(board[6][6][5]) == 'neutron'):
                score -= 100
                print("enemy Neutron in middle")


        if player_type == 'min':
            # Check for neutrons and for captures
            player_count = 0
            player2_count = 0
            electrons_p = 0
            electrons_p2 = 0
            positrons_p = 0
            positrons_p2 = 0
            neutrons_p = []
            neutrons_p2 = []

            p_freedom_cell = []
            p_freedom_alpha = []
            p2_freedom_cell = []
            P2_freedom_alpha = []
            for i in range(1,len(board)):
                if str(board[i]) != 'nan':
                    for j in range(1,len(board)):
                        if str(board[i][j]) != 'nan':
                            if str(board[i][j][4]) == player_turn:
                                player_count += 1
                                p_freedom_cell.append(board[i][j])
                                p_freedom_alpha.append(str(map_from_index_to_alpha[i]) + str(j))
                                if board[i][j][3] == -1:
                                    electrons_p += 1
                                if board[i][j][3] == 1:
                                    positrons_p += 1
                                if str(board[i][j][5]) == 'neutron':
                                    neutrons_p.append(board[i][j])
                            if str(board[i][j][4]) == player2:
                                player2_count += 1
                                if board[i][j][3] == -1:
                                    electrons_p2 += 1
                                if board[i][j][3] == 1:
                                    positrons_p2 += 1
                                if str(board[i][j][5]) == 'neutron':
                                    neutrons_p2.append(board[i][j])

            open_cells_count = []
            #for i in range(0, len(p_freedom_cell)):
            #    temp = self.get_valid_moves(board, player_turn, p_freedom_cell[i], p_freedom_alpha[i][0], p_freedom_alpha[i][1:])
            #    open_cells_count.append(len(temp))
            #temp = sum(open_cells_count)
            #score -= 0.05*temp

            if (electrons_p < 1) or  (positrons_p < 1):
                score += 100
            if (electrons_p2 < 1) or (positrons_p2 < 1):
                score -= 100
            if len(neutrons_p) == 0:
                score += 100
                print("Lost Neutron")
            if len(neutrons_p2) == 0:
                score -= 100
                print("Killed enemy Neutron")
            if int(player_count) < number_player_turn_pieces:
                score += 20
            if int(player2_count) < number_player2_pieces:
                score -= 20
            if (str(board[6][6][4]) == player_turn) and (str(board[6][6][5]) == 'neutron'):
                score -= 100
                print("Netron in middle")
            if (str(board[6][6][4]) == player2) and (str(board[6][6][5]) == 'neutron'):
                score += 100
                print("enemy Neutron in middle")
        return score


#*******************************************************************************
## MINIMAX IMPLEMENTATION WITH ALPHA BETA PRUNING
    def count_pieces(self,board, player_turn, positions, positions2):
        if player_turn == 'black':
            player2 = 'white'
        else:
            player2 = 'black'

        p = positions
        p2 =  positions2
        if player_turn == 'black':
            self.number_of_players_black = len(p)
        else:
            self.number_of_players_white = len(p2)

        if player_turn == 'white':
            self.number_of_players_white = len(p)
        else:
            self.number_of_players_black = len(p2)


######################################
## Alpha-Beta search
######################################

    #########################################################
    ## Max player
    ########################################################
    def max_move(self, board, player_turn, depth, a, b):

        best_score = a      ## For the max player, let alpha be the best score

        ###################
        ## if the last play has been reached, evaluate the board
        if depth == 0:
            best_score = self.evaluate_move(board = board,player_turn= player_turn,player_type = 'max')
            best_move = board

        else:
            ## set the player turn colors
            if player_turn == 'black':
                player2 = 'white'
            else:
                player2 = 'black'

            ###################
            ## Check if current position is game over, if yes then evaluate the board.
            go = self.check_board_for_go(board, player_turn)
            if go == True:
                best_score = self.evaluate_move(board = board,player_turn= player_turn,player_type= 'max')
                best_move = board

            else:
                best_move = []
                positions = self.get_player_positions(board, player_turn)       ## get the player positions for both players
                positions2 = self.get_player_positions(board, player2)
                self.count_pieces(board, player_turn, positions, positions2)    ## count pieces, feeds into evaluation function

                ###########################
                ## Find pieces that have valid moves
                legal_moves = []
                for i in range(0,len(positions)):
                    old_cell_letter = positions[i][0]
                    old_cell_number = positions[i][1:]
                    old_cell = board[map_from_alpha_to_index[old_cell_letter]][int(old_cell_number)]
                    valid_moves = self.get_valid_moves(board=board, player_turn=player_turn, old_cell=old_cell, old_cell_letter=old_cell_letter, old_cell_number = old_cell_number)
                    if len(valid_moves) >= 1:
                        legal_moves.append(positions[i])
                counter = 0

                ############################
                ## For each movable piece, get its moves
                for valid in legal_moves:
                    breakloop = False
                    valid = str(valid)
                    old_cell_letter = str(valid[0])
                    old_cell_number = int(valid[1:])
                    old_cell = board[map_from_alpha_to_index[old_cell_letter]][int(old_cell_number)]
                    valid_moves = self.get_valid_moves(board=board, player_turn=player_turn, old_cell=old_cell, old_cell_letter=old_cell_letter, old_cell_number = old_cell_number)

                    ##################################
                    ## Iterate over every move of current piece
                    ## FOR THAT PIECE EACH CHILD
                    for move in valid_moves:
                        breakloop = False

                        ## get characteristics of destination cell
                        temp_board = copy.deepcopy(board)
                        new_cell_letter = str(move[0])
                        new_cell_number = int(move[1:])
                        new_cell = board[map_from_alpha_to_index[new_cell_letter]][int(new_cell_number)]
                        self.new_cell = new_cell

                        ## Update board with new move
                        temp_board = self.replace_pieces(temp_board,str(old_cell_letter+str(old_cell_number)),str(new_cell_letter+str(new_cell_number)))

                        ## search for captures
                        pieces_being_captured, pieces_capturing_enemy = self.get_captures(board = temp_board, player_turn = player_turn)
                        if len(pieces_being_captured) >= 1:
                            all_available = []
                            legal_captures = []
                            for h in range(0,len(pieces_being_captured)):
                                available_pieces = []
                                # For each piece being captured, iterate over insight pieces and see if any player turn
                                for i in range(0,len(pieces_capturing_enemy[h])):
                                    piece = pieces_capturing_enemy[h][i]
                                    piece_cell = temp_board[map_from_alpha_to_index[str(piece[0])]][int(piece[1:])]
                                    if str(piece_cell[4]) == player_turn:
                                        available_pieces.append(piece)
                                if len(available_pieces) > 1:
                                    all_available.append(available_pieces)
                                    legal_captures.append(pieces_being_captured[h])

                                ############################
                                # If there are pieces to be captured, iterate over each
                                ## Note there are different loops depending on how many pieces are available for captured

                                #####
                                ## Simultaenous Capture
                                if len(all_available) > 1:
                                    # for each capture, create a new board
                                    for piece in all_available[0]:
                                        temp_board2 = copy.deepcopy(temp_board)
                                        temp = all_available[1]
                                        temp_board2 = self.replace_pieces(temp_board2,piece,legal_captures[0])
                                        if piece in temp:
                                            temp.remove(piece)
                                            ## for each simultaenous capture, create a board with differrent combinations of capturing sequences
                                            for piece2 in temp:
                                                temp_board2 = self.replace_pieces(temp_board2,piece2,legal_captures[1])
                                                b_pos = self.get_player_positions(temp_board2,player2)
                                                self.count_pieces(board, player_turn, positions, b_pos)
                                                ## feed resulting board into min player function
                                                value, new_move = self.min_move(temp_board2,player2, depth = depth-1,  a = a, b = b)

                                                ############
                                                ## if the value coming from min player is larger than a, stop searching
                                                if value > a:
                                                    best_move =  copy.deepcopy(temp_board2)
                                                    self.move_made = [valid,move]
                                                a = max(a, value)
                                                best_score = a ## save max

                                                ## if alpha > beta, stop searching here
                                                if a >= b:
                                                    breakloop = True
                                                    break
                                        if breakloop == True:
                                            break


                                ###############################
                                ## Loop for if only one piece to be captured, same principle as above
                                if len(all_available) == 1:
                                    for piece in all_available[0]:
                                        temp_board2 = copy.deepcopy(temp_board)
                                        temp_board2 = self.replace_pieces(temp_board2,piece,legal_captures[0])
                                        b_pos = self.get_player_positions(temp_board2,player2)
                                        self.count_pieces(board, player_turn, positions, b_pos)

                                        value, new_move = self.min_move(temp_board2,player2, depth = depth-1, a = a, b = b)

                                        if value > a:
                                            best_move =  copy.deepcopy(temp_board2)
                                            self.move_made = [valid,move]
                                        a = max(a, value)
                                        best_score = a

                                        ## if alpha > beta, break loop
                                        if a >= b:
                                            breakloop = True
                                            break

                                ##############################
                                ## loop if move does not result in capture
                                if len (all_available) == 0:
                                    value, new_move = self.min_move(temp_board,player2, depth = depth-1, a = a, b = b)
                                    if value > a:
                                        best_move =  copy.deepcopy(temp_board)
                                        self.move_made = [valid,move]
                                    a = max(a, value)
                                    best_score = a

                                    if a >= b:
                                        breakloop = True
                                        break
                                if breakloop == True:
                                    break

                        ######################################
                        ## If no capture was suspected, do this
                        else:
                            value, new_move = self.min_move(temp_board,player2, depth = depth-1,  a = a, b = b)
                            if value > a:
                                best_move =  copy.deepcopy(temp_board)
                                self.move_made = [valid,move]
                            a = max(a, value)
                            best_score = a
                            if a >= b:
                                breakloop = True
                                break
                        if breakloop == True:
                            break

        return best_score, best_move


    ########################################
    ## Min player follows the same code as above just with minimal changes as the minimzing player.

    def min_move(self, board, player_turn, depth, a, b):

        best_score = b
        breakloop = False
        if depth == 0:
            best_score = self.evaluate_move(board = board,player_turn= player_turn, player_type= 'min')
            best_move = board

        else:
            best_move = []
            if player_turn == 'black':
                player2 = 'white'
            else:
                player2 = 'black'

            go = self.check_board_for_go(board, player_turn)
            if go == True:
                best_score = self.evaluate_move(board = board, player_turn= player_turn, player_type = 'min')
                best_move = board
            else:

                positions = self.get_player_positions(board, player_turn)
                positions2 = self.get_player_positions(board, player2)
                self.count_pieces(board, player_turn, positions, positions2)
                legal_moves = []
                for i in range(0,len(positions)):
                    old_cell_letter = positions[i][0]
                    old_cell_number = positions[i][1:]
                    old_cell = board[map_from_alpha_to_index[old_cell_letter]][int(old_cell_number)]
                    valid_moves = self.get_valid_moves(board=board, player_turn=player_turn, old_cell=old_cell, old_cell_letter=old_cell_letter, old_cell_number = old_cell_number)
                    if len(valid_moves) >= 1:
                        legal_moves.append(positions[i])

                for valid in legal_moves:
                    breakloop = False
                    old_cell_letter = str(valid[0])
                    old_cell_number = int(valid[1:])
                    old_cell = board[map_from_alpha_to_index[old_cell_letter]][int(old_cell_number)]
                    valid_moves = self.get_valid_moves(board=board, player_turn=player_turn, old_cell=old_cell, old_cell_letter=old_cell_letter, old_cell_number = old_cell_number)
                    for move in valid_moves:
                        breakloop = False

                        temp_board = copy.deepcopy(board)
                        new_cell_letter = move[0]
                        new_cell_number = move[1:]
                        new_cell = board[map_from_alpha_to_index[new_cell_letter]][int(new_cell_number)]
                        ## Update board
                        temp_board = self.replace_pieces(temp_board,str(old_cell_letter+str(old_cell_number)),str(new_cell_letter+str(new_cell_number)))
                        pieces_being_captured, pieces_capturing_enemy = self.get_captures(board = temp_board, player_turn = player_turn)

                        # If there are pieces to be captures, iterate over each
                        if len(pieces_being_captured) >= 1:
                            all_available = []
                            legal_captures = []
                            for h in range(0,len(pieces_being_captured)):
                                available_pieces = []
                                # For each piece being captured, iterate over insight pieces and see if any player turn
                                for i in range(0,len(pieces_capturing_enemy[h])):
                                    piece = pieces_capturing_enemy[h][i]
                                    piece_cell = temp_board[map_from_alpha_to_index[str(piece[0])]][int(piece[1:])]
                                    if str(piece_cell[4]) == player_turn:
                                        available_pieces.append(piece)
                                if len(available_pieces) > 1:
                                    all_available.append(available_pieces)
                                    legal_captures.append(pieces_being_captured[h])


                                if len(all_available) > 1:
                                    for piece in all_available[0]:
                                        temp_board2 = copy.deepcopy(temp_board)
                                        temp = all_available[1]
                                        temp_board2 = self.replace_pieces(temp_board2,piece,legal_captures[0])
                                        if piece in temp:
                                            temp.remove(piece)
                                            for piece2 in temp:
                                                temp_board2 = self.replace_pieces(temp_board2,piece2,legal_captures[1])
                                                b_pos = self.get_player_positions(temp_board2,player2)
                                                self.count_pieces(board, player_turn, positions, b_pos)
                                                value, new_move = self.max_move(temp_board2,player2, depth = depth-1,  a = a, b = b)
                                                b = min(b, value)
                                                if value < b:
                                                    best_move = copy.deepcopy(temp_board2)
                                                best_score = b

                                                if a >= b:
                                                    breakloop = True
                                                    break
                                        if breakloop == True:
                                            break

                                elif len(all_available) == 1:
                                    for piece in all_available[0]:
                                        temp_board2 = copy.deepcopy(temp_board)
                                        temp_board2 = self.replace_pieces(temp_board2,piece,legal_captures[0])
                                        b_pos = self.get_player_positions(temp_board2,player2)
                                        self.count_pieces(board, player_turn, positions, b_pos)
                                        value, new_move = self.max_move(temp_board2,player2, depth = depth-1,  a = a, b = b)
                                        if value < b:
                                            best_move = copy.deepcopy(temp_board2)
                                        b = min(b, value)
                                        best_score = b

                                        if a >= b:
                                            breakloop = True
                                            break

                                elif len(all_available) == 0:
                                    value, new_move = self.max_move(temp_board,player, depth = depth-1,  a = a, b = b)
                                    if value < b:
                                        best_move = copy.deepcopy(temp_board)

                                    b = min(b, value)
                                    best_score = b

                                    if a >= b:
                                        breakloop = True
                                        break
                                if breakloop == True:
                                    break


                        else:
                            value, new_move = self.max_move(temp_board,player2, depth = depth-1, a = a, b = b)
                            if value < b:
                                best_move = copy.deepcopy(temp_board)
                            b = min(b, value)
                            best_score = b

                            if a >= b:
                                breakloop = True
                                break
                        if breakloop == True:
                            break

        return best_score, best_move
