import random
import time


def dice_toss():
    """Generates two random integers between 1 and 6 (inclusive)
    and returns them as a list to simulate two dice tosses"""
    dice_lst = [random.randint(1, 6), random.randint(1, 6)]
    return dice_lst*2 if dice_lst[0] == dice_lst[1] else dice_lst


def display_dice(dice_lst):
    """Takes a list of max 2, min 1 element/s as an input and
    prints a graphical representation in the terminal"""

    # Possible die configurations:
    s = "+ - - - - +"
    m1 = "|  o   o  |"
    m2 = "|  o      |"
    m3 = "|    o    |"
    m4 = "|      o  |"
    m5 = "|         |"

    # all possible dice from 1 to 6 in a list
    dice = [[m5, m3, m5], [m2, m5, m4], [m2, m3, m4],
            [m1, m5, m1], [m1, m3, m1], [m1, m1, m1]]

    def die(i):
        """ Returns a dice from the dice list as a string of integers"""
        return [s, *dice[i-1], s]

    def join_row(*rows):
        """Zips the rows for the dice in ndice() in order to print the 
        dice next to eachother"""
        return ['   '.join(r) for r in zip(*rows)]

    def ndice(*ns):
        """Takes ns amount of args (dice) and prints them row by row"""
        for line in join_row(*map(die, ns)):
            print(line)

    if len(dice_lst) == 1:
        ndice(dice_lst[0])
    elif len(dice_lst) == 2:
        ndice(dice_lst[0], dice_lst[1])
    elif len(dice_lst) == 3:
        ndice(dice_lst[0], dice_lst[1], dice_lst[2])
    else:
        ndice(dice_lst[0], dice_lst[1], dice_lst[2], dice_lst[3])


def operating_sys():
    operating_system = input(
        "Which operating system are you player from? (Mac/Windows): ")
    if operating_system.lower().startswith('m'):
        m_full = "●"
        m_empty = "◯"
    else:
        m_full = "●"
        m_empty = "o"

    return m_full, m_empty


m_full, m_empty = operating_sys()

start_board = [
    [],  # Tommas ute
    [m_empty, m_empty, ' ', ' ', ' '],  # 1 - Ifylld Bo
    [' ', ' ', ' ', ' ', ' '],  # 2 - Ifylld Bo
    [' ', ' ', ' ', ' ', ' '],  # 3 - Ifylld Bo
    [' ', ' ', ' ', ' ', ' '],  # 4 - Ifylld Bo
    [' ', ' ', ' ', ' ', ' '],  # 5 - Ifylld Bo
    [m_full, m_full, m_full, m_full, m_full],  # 6 - Ifylld Bo
    [' ', ' ', ' ', ' ', ' '],  # 7
    [m_full, m_full, m_full, ' ', ' '],  # 8
    [' ', ' ', ' ', ' ', ' '],  # 9
    [' ', ' ', ' ', ' ', ' '],  # 10
    [' ', ' ', ' ', ' ', ' '],  # 11
    [m_empty, m_empty, m_empty, m_empty, m_empty],  # 12 - Slutet av bottendelen
    [m_full, m_full, m_full, m_full, m_full],  # 13
    [' ', ' ', ' ', ' ', ' '],  # 14
    [' ', ' ', ' ', ' ', ' '],  # 15
    [' ', ' ', ' ', ' ', ' '],  # 16
    [m_empty, m_empty, m_empty, ' ', ' '],  # 17
    [' ', ' ', ' ', ' ', ' '],  # 18
    [m_empty, m_empty, m_empty, m_empty, m_empty],  # 19 - Tommas Bo
    [' ', ' ', ' ', ' ', ' '],  # 20 - Tommas Bo
    [' ', ' ', ' ', ' ', ' '],  # 21 - Tommas Bo
    [' ', ' ', ' ', ' ', ' '],  # 22 - Tommas Bo
    [' ', ' ', ' ', ' ', ' '],  # 23 - Tommas Bo
    [m_full, m_full, ' ', ' ', ' '],  # 24 - Tommas Bo
    []  # 25 - Ifylldas ute
]


def fill_empty(lst):
    """Takes a row from the board as an input and returns the number of elements
    more than 5 to represent the amount of markers on each row"""
    if len(lst) > 5:
        return len(lst)-5
    else:
        return " "


def display_board(board):
    """Takes the board and prints the board into the terminal"""
    print('\n')
    print(f"P1 Finished Checkers: {len(fin_p1_full_list)}")
    print("  ₁ ₁ ₁ ₁ ₁ ₁   ₁ ₂ ₂ ₂ ₂ ₂  ")
    print("  ³ ⁴ ⁵ ⁶ ⁷ ⁸   ⁹ ⁰ ¹ ² ³ ⁴  ")
    print("|━━━━━━━━━━━━━━━━━━━━━━━━━━━|")
    print("| {} {} {} {} {} {} | {} {} {} {} {} {} | {}".format(board[13][0], board[14][0], board[15][0], board[16][0], board[17]
          [0], board[18][0], board[19][0], board[20][0], board[21][0], board[22][0], board[23][0], board[24][0], " ".join(board[25])))
    print("| {} {} {} {} {} {} | {} {} {} {} {} {} |".format(board[13][1], board[14][1], board[15][1], board[16][1],
          board[17][1], board[18][1], board[19][1], board[20][1], board[21][1], board[22][1], board[23][1], board[24][1]))
    print("| {} {} {} {} {} {} | {} {} {} {} {} {} |".format(board[13][2], board[14][2], board[15][2], board[16][2],
          board[17][2], board[18][2], board[19][2], board[20][2], board[21][2], board[22][2], board[23][2], board[24][2]))
    print("| {} {} {} {} {} {} | {} {} {} {} {} {} |".format(board[13][3], board[14][3], board[15][3], board[16][3],
          board[17][3], board[18][3], board[19][3], board[20][3], board[21][3], board[22][3], board[23][3], board[24][3]))
    print("| {} {} {} {} {} {} | {} {} {} {} {} {} |".format(board[13][4], board[14][4], board[15][4], board[16][4],
          board[17][4], board[18][4], board[19][4], board[20][4], board[21][4], board[22][4], board[23][4], board[24][4]))
    print("| {} {} {} {} {} {} | {} {} {} {} {} {} |".format(fill_empty(board[13]), fill_empty(board[14]), fill_empty(board[15]), fill_empty(board[16]), fill_empty(
        board[17]), fill_empty(board[18]), fill_empty(board[19]), fill_empty(board[20]), fill_empty(board[21]), fill_empty(board[22]), fill_empty(board[23]), fill_empty(board[24])))
    print("|━━━━━━━━━━━━━━━━━━━━━━━━━━━|")
    print("| {} {} {} {} {} {} | {} {} {} {} {} {} |".format(fill_empty(board[12]), fill_empty(board[11]), fill_empty(board[10]), fill_empty(board[9]), fill_empty(
        board[8]), fill_empty(board[7]), fill_empty(board[6]), fill_empty(board[5]), fill_empty(board[4]), fill_empty(board[3]), fill_empty(board[2]), fill_empty(board[1])))
    print("| {} {} {} {} {} {} | {} {} {} {} {} {} |".format(board[12][4], board[11][4], board[10][4], board[9]
          [4], board[8][4], board[7][4], board[6][4], board[5][4], board[4][4], board[3][4], board[2][4], board[1][4]))
    print("| {} {} {} {} {} {} | {} {} {} {} {} {} |".format(board[12][3], board[11][3], board[10][3], board[9]
          [3], board[8][3], board[7][3], board[6][3], board[5][3], board[4][3], board[3][3], board[2][3], board[1][3]))
    print("| {} {} {} {} {} {} | {} {} {} {} {} {} |".format(board[12][2], board[11][2], board[10][2], board[9]
          [2], board[8][2], board[7][2], board[6][2], board[5][2], board[4][2], board[3][2], board[2][2], board[1][2]))
    print("| {} {} {} {} {} {} | {} {} {} {} {} {} |".format(board[12][1], board[11][1], board[10][1], board[9]
          [1], board[8][1], board[7][1], board[6][1], board[5][1], board[4][1], board[3][1], board[2][1], board[1][1]))
    print("| {} {} {} {} {} {} | {} {} {} {} {} {} | {}".format(board[12][0], board[11][0], board[10][0], board[9][0], board[8]
          [0], board[7][0], board[6][0], board[5][0], board[4][0], board[3][0], board[2][0], board[1][0], " ".join(board[0])))
    print("|━━━━━━━━━━━━━━━━━━━━━━━━━━━|")
    print("  ₁ ₁ ₁ ₀ ₀ ₀   ₀ ₀ ₀ ₀ ₀ ₀  ")
    print("  ² ¹ ⁰ ⁹ ⁸ ⁷   ⁶ ⁵ ⁴ ³ ² ¹  ")
    print(f"P2 Finished Checkers: {len(fin_p2_empty_list)}")
    print('\n')


def has_out(lst, marker):
    """Takes the list of OUT pieces and returns True if there are elements in
    the list"""
    if lst.count(marker) > 0:
        return True
    else:
        return False


def is_valid_move_dice(start_pos, end_pos, dice_lst):
    """Takes start_position, end_position, and dice_list and returns if the desired move
    is possible with the given dice_lst"""
    # Since we can go in either direction, we have to take the absolute value and check if it's
    # in the dice_list
    val = abs(start_pos - end_pos) in dice_lst
    if not val:
        print("You don't have the dice for that")
    return val


def is_valid_move_marker(board, end_pos, marker):
    """Takes the board, an end position and a marker and returns true if the marker can be moved to
    the position (based on the current markers in the position), otherwise false"""
    # Check what marker it is
    if marker == m_empty:
        # Checks if there are more than 1 marker of the other kind there, if so, return false
        if board[end_pos].count(m_full) > 1:
            print(f'Row {end_pos} is full, move somewhere else.')
            return False
    else:
        # Checks if there are more than 1 marker of the other kind there, if so, return false
        if board[end_pos].count(m_empty) > 1:
            print(f'Row {end_pos} is full, move somewhere else.')
            return False

    return True


def marker_knocked_out(board):
    """Takes a board and returns true if any marker should be remove because it's been knocked out"""
    # Create index
    index = 1
    # Walk through all of the rows with markers in the playing board
    for row in board[1:25]:
        # Checks if there is a marker on top of an empty marker of the other kind, then it is knocked out
        if (row[0] == m_empty and row[1] == m_full) or (row[0] == m_full and row[1] == m_empty):
            # We return true along with the row number of the knocked out marker
            return (True, index)
        else:
            index += 1
    return (False, None)


def remove_knocked_marker(board, position):
    """Takes the board and a position of a knocked marker, moves the marker from the position 
    on the board to the out_list"""
    marker = board[position].pop(0)  # Retrieves marker
    board[position].append(" ")  # Fills the row
    if marker == m_full:  # Makes sure that the marker gets appended to correct out list
        board[25].append(marker)
    else:
        board[0].append(marker)


def all_in_home_check(board, finished_m_list, marker):
    """Takes two arguments, the playing board and a marker, and returns true if 
    that marker has won the game, otherwise false"""
    # Starts by checking which marker we got as input
    if marker == m_full:
        # If we have a filled marker, we flatten all of the rows in the filled markers "home", i.e. rows 1-6.
        # We then count the number of occurrences of the marker in the list, if == 15,
        # all are home and we return true
        if ([element for row in board[1:7] for element in row].count(m_full) + len(finished_m_list)) == 15:
            return True
        # If we have a empty marker, we flatten all of the rows in the empty markers "home", i.e. rows 19-24.
        # We then count the number of occurrences of the marker in the list, if == 15,
        # all are home and we return true
    if marker == m_empty:
        if ([element for row in board[19:25] for element in row].count(m_empty) + len(finished_m_list)) == 15:
            return True

    return False


def player_input_normal():
    """Player input function for normal play. Takes no arguments and return (start_position, end_positions)"""
    start = ""  # Declare variables for while loop
    end = ""  # Declare variables for while loop
    # While loop to get a valid input for START_POS from player
    while start not in list(range(1, 25)) or start == "Q":
        start = input('From which row do you want to move a marker? (1-24): ')
        if start == "Q":  # Player Quit out mode
            return
        try:
            start = int(start)
        except:
            print('Please input a valid integer')

    while end not in list(range(1, 25)):  # Loop to get correct END_POS from player
        end = input('To where do you want to move the marker? (1-24): ')
        if end == "Q":
            return
        try:
            end = int(end)
        except:
            print('Please input a valid integer')

    return start, end  # Returns from where to where the players wishes to move


def player_input_has_out(marker):
    """Takes TURN as variable to check if current player has markers that are out of play"""
    if marker not in [m_full, m_empty]:  # Internal error checking
        print('Invalid marker')
        return 'Invalid Marker'

    start = ""  # Declaring variables for loop
    end = ""  # Declaring variables for loop

    # If m_fill has to enter the board
    if marker == m_full:
        start = 25  # Force the start to have index 25
        # Loop to only accept valid input from player
        while end not in list(range(19, 25)):
            end = input('To where do you want to move the marker? (19-24): ')
            if end == "Q":
                return
            try:
                end = int(end)
            except:
                print('Please input a valid integer')
        return start, end

    # If m_empty has to enter the board
    elif marker == m_empty:
        start = 0  # Force the start to have index 0
        while end not in list(range(1, 7)):  # While loop until valid input
            end = input('To where do you want to move the marker? (1-6): ')
            if end == "Q":
                return
            try:
                end = int(end)
            except:
                print('Please input a valid integer')
        return start, end


def player_input_endgame(marker):
    """Takes TURN/MARKER as input. Special condition for end play needed since players can now play out their marker"""
    start = ""  # Declaring variables for loops
    end = ""  # Declaring variables for loops
    if marker == m_full:  # Check whos turn it is
        while start not in list(range(1, 7)):  # Loop until valid input
            start = input(
                'From which row do you want to move a marker? (1-6): ')
            if start == "Q":
                return
            try:
                start = int(start)
            except:
                print('Please input a valid integer')

        # Loop until valid input. Additional option for player (OUT)
        while end not in list(range(1, 7)) or end != "OUT":
            end = input(
                'To where do you want to move the marker? (1-6 or OUT): ')
            if end == "Q":
                return
            elif end.upper().startswith('O'):  # If player wants to play out
                return start, 0  # We return the end position as outside of the board
            else:
                try:
                    end = int(end)
                    return start, end
                except:
                    print('Please input a valid integer or "OUT"')

    else:  # Player 2's player input
        while start not in list(range(19, 25)):
            start = input(
                'From which row do you want to move a marker? (19-24): ')
            if start == "Q":
                return
            try:
                start = int(start)
            except:
                print('Please input a valid integer')

        while end not in list(range(19, 25)) or end != "OUT":
            end = input(
                'To where do you want to move the marker? (19-24 or OUT): ')
            if end == "Q":
                return
            elif end.upper().startswith('O') == "OUT":
                return start, 25  # Give index outside of board if player wishes to play out
            else:
                try:
                    end = int(end)
                    return start, end
                except:
                    print('Please input a valid integer or "OUT"')

    return start, end


def move_out(board, start_pos, marker):
    """Takes board, start_pos, and marker in order to take a marker from given Start_pos and move 
    it to players list of finished markers"""
    marker_ = board[start_pos].pop(0)  # Take the marker off the board

    if len(board[start_pos]) < 5:  # If there are less than or equal to five
        # We have to append additional blankspace for display function
        board[start_pos].append(" ")

    if marker == m_full:  # Check if player 1
        fin_p1_full_list.append(marker_)  # Append to players 1 final list
    else:  # If not player 1, therfore, player 2
        fin_p2_empty_list.append(marker_)


def is_right_direction_check(start_pos, end_pos, marker):
    """Takes start_pos, end_pos, and marker to check if player is trying
    to move the marker in the right direction."""
    if marker == m_full:  # Player 1
        if start_pos - end_pos > 0:  # They are moving in the positive integer direction
            return True
        else:
            print('Wrong direction')
            return False
    else:  # Player 2
        if start_pos - end_pos < 0:  # Move in the negative integer direction
            return True
        else:
            print('Wrong direction')
            return False


def is_movable_marker(board, start_pos, marker):
    """ Takes board, start_pos, and marker to check if there is a marker
    and if it's the right marker"""
    if board[start_pos][0] == marker:
        return True
    else:
        if board[start_pos][0] == " ":
            print('You selected an empty row')
        else:
            print(f"{board[start_pos][0]} isn't your marker.")
        return False


def is_entry_possible(board, marker, dice_lst):
    """Takes board, marker, dice_lst and returns if there is a valid entry given
    the dice_lst"""
    if marker == m_full:  # Player 1
        for i in dice_lst:  # Loop through all dices
            # Check if entry NOT possible with current dice
            if (board[25-i][0] == m_empty and board[25-i][1] == m_empty):
                pass  # Then pass
            else:  # If there IS a possible entry
                return True  # Stops the loop and function, since we have a possible entry
    else:  # Player 2
        for i in dice_lst:  # Loop through all dices
            # Check if entry NOT possible with current dice
            if (board[i][0] == m_full and board[i][1] == m_full):
                pass  # Then pass
            else:  # If there IS a possible entry
                return True  # Stops the loop and function, since we have a possible entry
    return False  # If loops don't return anything, that means it isn't possible to enter with rolled dice


def move_marker(board, start_pos, end_pos):  # COULD PROBABLY MAKE EASIER
    """Must check if the len(row) is greater than 5 since all rows need a 
    minimum of 5 elements in order to display_board correctly (we are using indeces there)."""
    marker = board[start_pos].pop(0)  # Pop the marker

    # only need to append blankspace if there are less than five OR we need to enter
    if len(board[start_pos]) < 5 and start_pos not in [0, 25]:
        board[start_pos].append(" ")  # Append blankspace if needed

    if board[end_pos].count(" ") > 0:  # If there are any whitespaces
        # Place marker in FIRST whitespace
        board[end_pos][board[end_pos].index(" ")] = marker
    else:
        # If there are no blankspaces, just append it
        board[end_pos].append(marker)


def win_check(fin_lst_marker):
    # If player has 15 markers in finish_list, they win
    return len(fin_lst_marker) == 15


def is_valid_move_fin(start_pos, marker, dice_lst):
    """Takes start position, marker and dice and checks whether marker can go out or not. Return True True if
    it can out cleanly, True False fo out with behind check, False False cannot go out"""
    state = (
        False, False)  # Default case that player cannot move out and needs to check behind
    if marker == m_full:  # Player 1
        # (Can go out, Without checking behind)
        for die in dice_lst:  # Check all dice
            if die - start_pos == 0:  # If you can go out cleanly
                return True, True  # Return TRUE for able to go out, TRUE for not needing another check
            elif die - start_pos > 0:  # If dice has more moves than are spaces left
                # - TRUE marker can go out, FALSE because does need a is_any_behind_check # Update state, since next dice MIGHT give (TRUE TRUE)
                state = (True, False)
        else:
            return state  # Return state either (FALSE, FALSE) or (TRUE, FALSE)
    else:  # Same thing for player 2
        for die in dice_lst:
            if die + start_pos == 25:
                return True, True
            elif die + start_pos > 25:
                state = (True, False)
        else:
            return state


def is_any_behind(board, start_pos, marker):  # IS ANY BEHIND
    """Takes board, start_pos, and marker in order to check if there are any markers behind the marker that a move has been initiated
    Used in conjunction with is_valid_move_fin()"""
    if marker == m_full:  # Player 1
        # Flattens the rows BEHIND the marker and if there are any markers behind
        if [element for row in board[start_pos+1:7] for element in row].count(marker) > 0:
            return True  # There are any
        else:
            return False
    else:  # Player 2
        # Flattens the rows BEHIND the marker and if there are any markers behind
        if [element for row in board[19:start_pos] for element in row].count(marker) > 0:
            return True
        else:
            return False


def display_no_valid_entry():
    """If there is no valid entry for player, print feedback"""
    print('\n')
    print('=======================================')
    print('!!! NO VALID MOVE, SWITCHING TURNS !!!')
    print('=======================================')
    print('\n')


def display_player_turn(player):
    """Takes player (marker) as input and displays whos turn it is"""
    if player == m_full:
        print("\n")
        print("\n")
        print("_______________________________________________________________")
        print("\n")
        print(f"Player 1 ({player}), your turn.")
    else:
        print("\n")
        print("\n")
        print("_______________________________________________________________")
        print("\n")
        print(f"Player 2 ({player}), your turn.")


def initial_roll():
    """Takes no arguments, players roll for highest to determine who starts"""
    p1_dice = 0  # Declare variables for loop
    p2_dice = 0  # Declare variables for loop

    while p1_dice == p2_dice:  # While none has higher, make players roll
        input("Player 1, press enter to roll die: ")
        p1_dice = random.randint(1, 6)
        display_dice([p1_dice])
        input("Player 2, press enter to roll die: ")
        p2_dice = random.randint(1, 6)
        display_dice([p2_dice])

        if p1_dice == p2_dice:  # Give feedback that they got the same variable
            print("You got the same number, roll again!")

    if p1_dice > p2_dice:  # If player 1 rolls higher
        print("Player 1, you start!")
        return ([p1_dice, p2_dice], m_full)
    else:  # If player 2 rolls higher
        print("Player 2, you start!")
        return ([p1_dice, p2_dice], m_empty)


def display_winner(player):
    """Takes player (marker) and displays winner message"""
    if player == m_full:
        print('\n')
        print('============================================')
        print('Congratulations Player 1, you won the game!')
        print('============================================')
        print('\n')
    else:
        print('\n')
        print('============================================')
        print('Congratulations Player 2, you won the game!')
        print('============================================')
        print('\n')


def move_is_possible(board, marker, dice_lst):
    """Takes board, marker and dice_list and checks whether any moves are possible or not. Returns boolean"""
    index = 0  # Create index
    for row in board[1:25]:  # Walks through every row in the board
        index += 1  # adds to index
        if marker == m_full:  # checks marker type
            if row[0] == marker:  # checks if row contain marker
                for die in dice_lst:  # goes through dice
                    if index - die > 0:  # if move is not going "off" table
                        # checks is move possible
                        if not (board[index - die][0] == m_empty and board[index - die][1] == m_empty):
                            return True  # if move possible
        else:  # same for other marker type
            if row[0] == marker:
                for die in dice_lst:
                    if index + die < 25:
                        if not (board[index + die][0] == m_full and board[index + die][1] == m_full):
                            return True
    else:
        return False  # if no return true, return false


def main():
    while game_on:  # While loop keeping the game running, while game_on
        if turn == p1_full:  # Checks if it is player 1's turn, else player 2's
            # Displays some text indicating who's supposed to make a move
            display_player_turn(turn)
            if not dice_lst:  # Make sures player can roll dice if there are no dice in the dice_lst
                roll = input('Press enter to roll dice:')  # roll dice prompt
                if roll == "Q":
                    break
                dice_lst = dice_toss()  # Generate the dice for the players turn
            while len(dice_lst) > 0:  # While we have moves left to do
                print('Remaining die/dice:')  # Prints remaining dice to player
                display_dice(dice_lst)
                # Prints current playing board to player
                print('Current board:')
                display_board(board)
                if has_out(board[25], turn):  # If we have a marker that is out
                    # We cannot come in with out marker
                    if not is_entry_possible(board, turn, dice_lst):
                        dice_lst = []  # Sets the dice list to false, will break out of the turn loop
                        turn = p2_empty  # Switches the turn to Player 2 so that initial condition in while game_on goes to the other player
                        display_no_valid_entry()

                        break  # Breaks out of current while len(dice_list) > 0

                    else:  # We have marker outside and HAVE a possible entry
                        valid_move = False  # Sets valid_move to false for the loop
                        while valid_move == False:  # Starts the while loop until we give a valid move
                            # Take input from player with Entry=True and sends the marker
                            start_pos, end_pos = player_input_has_out(turn)
                            valid_move = all([is_valid_move_dice(
                                start_pos, end_pos, dice_lst), is_valid_move_marker(board, end_pos, turn)])
                            #             ^   all checks if ALL of the validations (2) are True
                            if not valid_move:  # If not valid move, redo loop to get a valid move
                                print('Invalid move')
                            else:  # We did get a valid move
                                # Moves the marker
                                move_marker(board, start_pos, end_pos)
                                # Pops off the dice we just used from the DICE_LIST
                                dice_lst.pop(dice_lst.index(
                                    abs(start_pos-end_pos)))

                                # Checks if there are any markers that should be knocked out.
                                knocked, index_knocked = marker_knocked_out(
                                    board)
                                if knocked:  # If we found any
                                    # Remove the knocked out marker
                                    remove_knocked_marker(board, index_knocked)

                # Checks if player can play out markers, i.e. endgame
                elif all_in_home_check(board, fin_p1_full_list, turn):
                    valid_move = False  # Sets valid_move to false for the loop
                    while valid_move == False:  # Starts the while loop until we give a valid move
                        # sets start and end_pos using player_input_endgame
                        start_pos, end_pos = player_input_endgame(turn)
                        if end_pos == 0:  # if player chooses to "out" a marker
                            # checks if marker can be taken out, returns bool tup
                            can_out, doesnt_need_behind_check = is_valid_move_fin(
                                start_pos, turn, dice_lst)
                            # if (true, true), marker can be taken out straight away
                            if can_out and doesnt_need_behind_check:
                                # takes out marker
                                move_out(board, start_pos, turn)
                                # Pops off the dice we just used from the DICE_LIST
                                dice_lst.pop(dice_lst.index(
                                    abs(start_pos-end_pos)))
                                valid_move = True  # change to true to break loop
                                if win_check(fin_p1_full_list):  # checks if player won
                                    display_winner(turn)  # displays winner
                                    dice_lst = []  # break turn
                                    game_on = False  # if won, breaks game loop
                                    break
                            # if (true, false)
                            elif can_out and not doesnt_need_behind_check:
                                # checks if there are no markers in the home behind chosen marker
                                if not is_any_behind(board, start_pos, turn):
                                    # if no, takes out marker
                                    move_out(board, start_pos, turn)
                                    # Pops off the dice we just used from the DICE_LIST
                                    dice_lst.pop(dice_lst.index(max(dice_lst)))
                                    valid_move = True  # breaks loop
                                    if win_check(fin_p1_full_list):  # checks if player won
                                        display_winner(turn)  # displays winner
                                        dice_lst = []  # break turn
                                        game_on = False  # breaks game loop
                                        break
                                else:
                                    # Error message for player move
                                    print(
                                        "You cannot move this marker out, there are markers behind.")
                            else:
                                # Error message for player move, (false,false)
                                print(
                                    f"You don't have the dice to move marker from line {start_pos} out.")
                        else:  # not outing marker, then normal move
                            if move_is_possible(board, turn, dice_lst):
                                valid_move = all([                          # Check if ALL of the validations are True
                                    is_valid_move_dice(
                                        start_pos, end_pos, dice_lst),
                                    is_valid_move_marker(board, end_pos, turn),
                                    is_movable_marker(board, start_pos, turn),
                                    is_right_direction_check(
                                        start_pos, end_pos, turn)
                                ])
                                if not valid_move:  # Invalid move, print to user
                                    print('Invalid move')
                                else:  # We have a valid move
                                    # Moves the marker
                                    move_marker(board, start_pos, end_pos)
                                    # Pops off the dice we just used from the DICE_LIST
                                    dice_lst.pop(dice_lst.index(
                                        abs(start_pos-end_pos)))

                                    # Checks if there are any markers that should be knocked out.
                                    knocked, index_knocked = marker_knocked_out(
                                        board)
                                    if knocked:
                                        # Remove the knocked out marker
                                        remove_knocked_marker(
                                            board, index_knocked)
                            else:
                                display_no_valid_entry()
                                dice_lst = []
                                turn = p2_empty
                                time.sleep(2)
                                break

                else:  # If no marker is out, normal play
                    if move_is_possible(board, turn, dice_lst):
                        valid_move = False   # Same as before, variable for loop
                        while valid_move == False:  # Run this loop untill we have a valid move
                            start_pos, end_pos = player_input_normal()  # Take player input
                            valid_move = all([                          # Check if ALL of the validations are True
                                is_valid_move_dice(
                                    start_pos, end_pos, dice_lst),
                                is_valid_move_marker(board, end_pos, turn),
                                is_movable_marker(board, start_pos, turn),
                                is_right_direction_check(
                                    start_pos, end_pos, turn)
                            ])
                            if not valid_move:  # Invalid move, print to user
                                print('Invalid move')
                            else:  # We have a valid move
                                # Moves the marker
                                move_marker(board, start_pos, end_pos)
                                # Pops off the dice we just used from the DICE_LIST
                                dice_lst.pop(dice_lst.index(
                                    abs(start_pos-end_pos)))

                                # Checks if there are any markers that should be knocked out.
                                knocked, index_knocked = marker_knocked_out(
                                    board)
                                if knocked:
                                    # Remove the knocked out marker
                                    remove_knocked_marker(board, index_knocked)
                    else:
                        display_no_valid_entry()
                        dice_lst = []
                        turn = p2_empty
                        time.sleep(2)
                        break
            else:
                # displays the boards current state after the player have performed all moves
                time.sleep(1)
                display_board(board)
                turn = p2_empty  # changes turn

        else:  # next player
            display_player_turn(turn)
            if not dice_lst:
                roll = input('Press enter to roll dice:')
                if roll == "Q":
                    break
                dice_lst = dice_toss()  # Generate the dice for the players turn
            while len(dice_lst) > 0:  # While we have moves left to do
                print('Remaining die/dice:')  # print remaining dice to player
                display_dice(dice_lst)
                print('Current board:')  # prints current board
                display_board(board)
                if has_out(board[0], turn):  # If we have a marker that is out
                    # We cannot come in with out marker
                    if not is_entry_possible(board, turn, dice_lst):
                        dice_lst = []  # In order to stop loop next time
                        turn = p1_full  # Switch the turns
                        display_no_valid_entry()

                        break  # Break out of current loop

                    else:  # We have marker outside of board and a possible entry
                        valid_move = False  # Variable to control valid move loop
                        while valid_move == False:  # Starts the loopo
                            start_pos, end_pos = player_input_has_out(
                                turn)  # Player input with True and Marker
                            valid_move = all([is_valid_move_dice(
                                start_pos, end_pos, dice_lst), is_valid_move_marker(board, end_pos, turn)])
                            #             ^  checks ALL validations for entry
                            if not valid_move:  # Invalid move for player, another loop
                                print('Invalid move')
                            else:  # Valid move from player
                                # Move marker according to input
                                move_marker(board, start_pos, end_pos)
                                # Pops off the dice we just used from the DICE_LIST
                                dice_lst.pop(dice_lst.index(
                                    abs(start_pos-end_pos)))

                                # Checks if there are any markers that should be knocked out.
                                knocked, index_knocked = marker_knocked_out(
                                    board)
                                if knocked:
                                    # Remove the knocked out marker
                                    remove_knocked_marker(board, index_knocked)

                # if player can play out markers, i.e. all in home
                elif all_in_home_check(board, fin_p2_empty_list, turn):
                    valid_move = False  # sets bool for loop
                    while valid_move == False:  # starts loop for valid input from player
                        start_pos, end_pos = player_input_endgame(
                            turn)  # takes input
                        if end_pos == 25:  # if player chooses to out marker
                            can_out, doesnt_need_behind_check = is_valid_move_fin(
                                start_pos, turn, dice_lst)  # checks if move valid, return bool tuple
                            # (true, true), marker can out of board straight away
                            if can_out and doesnt_need_behind_check:
                                # move out marker from board
                                move_out(board, start_pos, turn)
                                # Pops off the dice we just used from the DICE_LIST
                                dice_lst.pop(dice_lst.index(
                                    abs(start_pos-end_pos)))
                                valid_move = True  # breaks input loop
                                if win_check(fin_p2_empty_list):  # checks if player won
                                    display_winner(turn)  # displays winner
                                    dice_lst = []  # break turn
                                    game_on = False  # breaks game loop
                                    break
                            # (true, false), we need to check if there are markers behind
                            elif can_out and not doesnt_need_behind_check:
                                # no markers behind in the home
                                if not is_any_behind(board, start_pos, turn):
                                    # move out marker
                                    move_out(board, start_pos, turn)
                                    # Pops off the dice we just used from the DICE_LIST
                                    dice_lst.pop(dice_lst.index(max(dice_lst)))
                                    valid_move = True  # move is valid, break input loop
                                    if win_check(fin_p2_empty_list):  # check if player won
                                        display_winner(turn)  # displays winner
                                        dice_lst = []  # break turn
                                        game_on = False  # break game
                                        break
                                else:
                                    # error for (true, false) case
                                    print(
                                        "You cannot move this marker out, there are markers behind.")
                            else:
                                # error for (false, false) case
                                print(
                                    f"You don't have the dice to move marker from line {start_pos} out.")
                        else:  # normal move
                            if move_is_possible(board, turn, dice_lst):
                                valid_move = all([                          # Check if ALL of the validations are True
                                    is_valid_move_dice(
                                        start_pos, end_pos, dice_lst),
                                    is_valid_move_marker(board, end_pos, turn),
                                    is_movable_marker(board, start_pos, turn),
                                    is_right_direction_check(
                                        start_pos, end_pos, turn)
                                ])
                                if not valid_move:  # Invalid move, print to user
                                    print('Invalid move')
                                else:  # We have a valid move
                                    # Moves the marker
                                    move_marker(board, start_pos, end_pos)
                                    # Pops off the dice we just used from the DICE_LIST
                                    dice_lst.pop(dice_lst.index(
                                        abs(start_pos-end_pos)))

                                    # Checks if there are any markers that should be knocked out.
                                    knocked, index_knocked = marker_knocked_out(
                                        board)
                                    if knocked:
                                        # Remove the knocked out marker
                                        remove_knocked_marker(
                                            board, index_knocked)
                            else:
                                display_no_valid_entry()
                                dice_lst = []
                                turn = p1_full
                                time.sleep(1)
                                break
                else:  # If no marker is out, normal play
                    if move_is_possible(board, turn, dice_lst):
                        valid_move = False  # Variable for while loop
                        while valid_move == False:  # Run untill we have valid move
                            start_pos, end_pos = player_input_normal()  # Take input from player
                            valid_move = all([      # Check if all checks are valid
                                is_valid_move_dice(
                                    start_pos, end_pos, dice_lst),
                                is_valid_move_marker(board, end_pos, turn),
                                is_movable_marker(board, start_pos, turn),
                                is_right_direction_check(
                                    start_pos, end_pos, turn)
                            ])
                            if not valid_move:  # Not valid, tell player, rerun looop
                                print('Invalid move')
                            else:  # We have a valid move
                                # Move marker according to input
                                move_marker(board, start_pos, end_pos)
                                # Pops off the dice we just used from the DICE_LIST
                                dice_lst.pop(dice_lst.index(
                                    abs(start_pos-end_pos)))

                                # Checks if there are any markers that should be knocked out.
                                knocked, index_knocked = marker_knocked_out(
                                    board)
                                if knocked:
                                    # Remove the knocked out marker
                                    remove_knocked_marker(board, index_knocked)
                    else:
                        display_no_valid_entry()
                        dice_lst = []
                        turn = p1_full
                        time.sleep(1)
                        break

            else:  # Once dice list is empty
                time.sleep(1)
                display_board(board)
                turn = p1_full  # Change the turn


if __name__ == '__main__':
    # Declaration of necessary variables
    board = start_board
    p1_full = m_full  # player 1 marker
    p2_empty = m_empty  # player 2 marker
    fin_p1_full_list = []  # list of finished markers for player 1
    fin_p2_empty_list = []  # list of finished markers for player 2

    # Welcoming text
    print("Hello and welcome to the beautiful game of backgammon! Lets play! \n")
    print("This is what the starting board looks like: ")
    display_board(board)

    # Game is on
    game_on = True

    # Print players and their individual markers
    print(f"Player 1, you are: {p1_full}")
    print(f"Player 2, you are: {p2_empty}")

    dice_lst, turn = initial_roll()

    #dice_lst = [p1_dice,p2_dice]
    display_board(board)
    time.sleep(2)

    main()
