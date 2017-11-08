from game_functions import *

player = 'black' # player white if ai is first, black if ai is second (bottom)
ai = "white" # keep ai white to circumvent evaluation bug

## Flip plot if AI plays 'white' or top
flip_plot = False
if player == 'white':
    flip_plot = True

b = game_positions(grid, player, None) ## create board
b.setboard(board = b.board)            ## set starting positions
ai_turn = 0

## Loop for playing.
## Loop breaks when game is over
while True:

    b.get_player_positions(board = b.board, player_turn = player)
    if player == 'black':
        b.number_of_players_black = len(b.player_positions)
    else:
        b.number_of_players_white = len(b.player_positions)
    print("MAKING MOVE")
    if ai == player:
        start = time.time()
        value, b.board = b.max_move(board = b.board, player_turn = player, depth = 3, a = -np.inf, b = np.inf)
        end = time.time()
        print("*******TIME******")
        print(end-start)
        #b.randomized_decision(board = b.board, player_turn = player)
        b.gameover = b.check_board_for_go(b.board, player_turn = player)
        ai_turn += 1
        print("############")
        print("############")
        print("AI moved from")
        print(b.move_made)
        print("############")

    else:
        b.make_move(board = b.board, player_turn = player)
        b.get_captures(board = b.board, player_turn = player)
        b.make_capture(board = b.board, player_turn = player)
        issues = input("Any issues? (n/y): ")
        if issues == 'y':
            piece = input("piece to move ")
            destination = input("where to move ")
            b.board = b.replace_pieces(b.board, piece, destination)

    plt.close()


    #########################################################
    ## PLOT INTERFACE
    ## Matplotlib solution courtesy of Stack Overflow
    ## https://stackoverflow.com/a/46526761/5310324
    #########################################################
    x = []
    y = []
    z = []
    color = []
    labels = []
    coord = []
    for i in range(0,len(b.board)):
        if str(b.board[i]) != 'nan':
            for j in range(0,len(b.board[i])):
                if str(b.board[i][j]) != 'nan':
                    x.append(b.board[i][j][0])
                    y.append(b.board[i][j][1])
                    z.append(b.board[i][j][2])
                    color.append(str(b.board[i][j][4]))
                    coord.append(b.board[i][j][0:3])
                    labels.append(b.board[i][j][3])

    hcoord = [c[0] for c in coord]
    vcoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) /3. for c in coord]

    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')

    for i in range(0,len(color)):
        if str(color[i]) == 'nan':
            color[i] = 'yellow'

    for x, y, c, l in zip(hcoord, vcoord, color, labels):
        color = c[0].lower()  # matplotlib understands lower case words for colours
        hexa = RegularPolygon((x, y), numVertices=6, radius=2. / 3.,
                             orientation=np.radians(30),
                             facecolor=color, alpha=0.4, edgecolor='k', gid = labels)
        ax.add_patch(hexa)
        ax.text(x, y, l, ha='center', va='center', size=20)
    # Also add scatter points in hexagon centres
    ax.scatter(hcoord, vcoord, c=[c[0].lower() for c in color])
    plt.ion()
    if flip_plot == True:
        plt.gca().invert_yaxis()
    plt.show()


    if b.gameover != True:
        print("NEXT MOVE")
        if player == "black":
            player = "white"
        else:
            player = "black"
        print("It is now player " + player + "s turn")
        continue
    else:
        print("Game over")
        break
