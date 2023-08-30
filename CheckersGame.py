# Author: Hailey Stoudt
# GitHub username: stoudth
# Date: 3/19/2024
# Description: Program that represents a checkers game. Will initialize a game and players and move according
#              to player input. It validates moves based on the specifications of the README and Ed Discussion.
#              It keeps track of the moves using data members which includes the board and different piece counts. A winner
#              is declared once a player captures all of their opponent's pieces.

class OutofTurn(Exception):
    """User-defined exception that is raised if a player tries ot make a move out of turn."""
    pass


class InvalidSquare(Exception):
    """User-defined exception that is raised if the coordinates of a square are not valid."""
    pass


class InvalidPlayer(Exception):
    """User-defined exception that is raised if data passed to a method is not valid regarding a player."""
    pass


class Player:
    """Represents a checker player. Used by the Checkers class."""

    def __init__(self, player_name, checker_color):
        """
        Initializes Player object with required private data members. Takes player name and checker color as
        parameters. Private data members include count of king pieces, count of triple king pieces, and count of
        captured pieces along with the player's name and checker color.
        """
        self._player_name = player_name
        self._checker_color = checker_color
        self._king_count = 0
        self._triple_king_count = 0
        self._captured_pieces_count = 0

    def get_king_count(self):
        """Takes no parameters. Returns the number of king pieces that the player has."""
        return self._king_count

    def append_king_count(self, num):
        """Adds the number passed as a parameter to the self._king_count data member."""
        self._king_count += num

    def get_triple_king_count(self):
        """Takes no parameters. Returns the number of king pieces that the player has."""
        return self._triple_king_count

    def append_triple_king_count(self, num):
        """Adds the number passed as a parameter to the self._triple_king_count data member."""
        self._triple_king_count += num

    def get_captured_pieces_count(self):
        """Takes no parameters. Returns the number of opponent pieces that the player has captured."""
        return self._captured_pieces_count

    def append_captured_pieces_count(self, num):
        """Add the number passed as a parameter to the self._captured_pieces count data member."""
        self._captured_pieces_count += num


class Checkers:
    """
    A class representing a game of checkers played by two people. The player with black checkers will always move
    first. Uses Player class to initialize a Player object.
    """

    def __init__(self):
        """
        Initializes a Checkers object that represents a game as it is played. Takes no parameters and initializes
        the board which is a private data member. It also initializes private data members to keep track of
        whose turn it is, the data of the players (checker_color, name, Player Object), the winner, which was the
        last piece moved, if the last move resulted in a capture, and if the last move resulted in the creation of
        a king.
        """
        self._board = [[None, "White", None, "White", None, "White", None, "White"],
                       ["White", None, "White", None, "White", None, "White", None],
                       [None, "White", None, "White", None, "White", None, "White"],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       ["Black", None, "Black", None, "Black", None, "Black", None],
                       [None, "Black", None, "Black", None, "Black", None, "Black"],
                       ["Black", None, "Black", None, "Black", None, "Black", None]]
        self._current_turn = None
        self._players = {}
        self._winner = None
        self._last_piece = None
        self._last_move_capture = None
        self._last_move_king_creation = None

    def create_player(self, player_name, checker_color):
        """
        Takes the parameters passed to it and creates a Player object using the Player class. Will set player
        using checker color “Black” to the person with the current turn. Returns Player object that was created.
        If checker color is already in use or exact name is already in use checker color is not "Black" or "White"
        or if there are already two players, InvalidPlayer exception will be raised.
        """
        if checker_color in self._players:
            raise InvalidPlayer
        if "Black" in self._players and "White" in self._players:
            raise InvalidPlayer
        if checker_color != "Black" and checker_color != "White":
            raise InvalidPlayer
        if "Black" in self._players:
            temp_dict = self._players["Black"]
            if temp_dict["Name"] == player_name:
                raise InvalidPlayer
        if "White" in self._players:
            temp_dict = self._players["White"]
            if temp_dict["Name"] == player_name:
                raise InvalidPlayer
        if checker_color == "Black":
            player_black = Player(player_name, checker_color)
            self._players["Black"] = {"Name"   : player_name,
                                      "Player" : player_black}
            self._current_turn = player_name
            return player_black
        if checker_color == "White":
            player_white = Player(player_name, checker_color)
            self._players["White"] = {"Name"   : player_name,
                                      "Player" : player_white}
            return player_white

    def get_player_name(self, checker_color):
        """Takes checker color as a parameter and returns the player's name listed playing that color."""
        if checker_color not in self._players:
            return "Player does not exist"
        else:
            temp_dict = self._players[checker_color]
            return temp_dict["Name"]

    def get_checker_details(self, square_location):
        """
        Takes a square location as a parameter and returns the type of piece on that square. If no
        piece is on the square, it returns None. If square does not exist it raises an InvalidSquare exception.
        """
        row_index = square_location[0]
        column_index = square_location[1]
        if row_index > 7 or column_index > 7:
            raise InvalidSquare
        if row_index < 0 or column_index < 0:
            raise InvalidSquare
        board_row = self._board[row_index]
        checker_details = board_row[column_index]
        return checker_details

    def get_player_color(self, player_name):
        """Takes a player's name as parameter and returns the checker color that player is using."""
        temp_dict_white = self._players["White"]
        temp_dict_black = self._players["Black"]
        if player_name == temp_dict_white["Name"]:
            return "White"
        if player_name == temp_dict_black["Name"]:
            return "Black"

    def get_player_object(self, checker_color):
        """Takes checker color as a parameter and returns the player's Player object listed playing that color."""
        if checker_color not in self._players:
            return "Player does not exist"
        else:
            temp_dict = self._players[checker_color]
            return temp_dict["Player"]

    def get_opponent_color(self, player_name):
        """Takes a player_name as a parameter and returns the opponent player's checker color. """
        temp_dict_white = self._players["White"]
        temp_dict_black = self._players["Black"]
        if player_name == temp_dict_white["Name"]:
            return "Black"
        if player_name == temp_dict_black["Name"]:
            return "White"

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """
        Takes as parameters the player's name, the starting square location of the piece they want to move,
        the destination they want to move it to. Square locations will be passed in (x,y) tuple format. First
        it validates that player is not making a move out of turn. Then it validates the starting square and
        destination square utilizing the validate_starting_square and validate_destination_square methods.
        Next it gets the coordinates of any pieces captured using the get_jumped_squares method. If this is a
        continued move, it then checks to make sure another capture was made otherwise an OutofTurn exception is
        made. Finally, it sends all the data it gathered to the perform_move method to make all necessary updates.
        That method returns the number of captured pieces which play_game then also returns.
        """
        #Initializes variables for use
        opponent_color = self.get_opponent_color(player_name)
        player_color = self.get_player_color(player_name)
        name_white = self.get_player_name("White")
        name_black = self.get_player_name("Black")

        #Tests for Player exception
        if player_name is not name_white and player_name is not name_black:
            raise InvalidPlayer
        if player_name not in self._current_turn and self._last_piece != starting_square_location:
            raise OutofTurn
        if player_name not in self._current_turn and self._last_move_capture is not True:
            raise OutofTurn
        if player_name not in self._current_turn and self._last_move_king_creation is True:
            raise OutofTurn

        #Gathers info for move and checks squares
        starting_checker = self.validate_starting_square(player_name, starting_square_location)
        self.validate_destination_square(destination_square_location)
        jumped_pieces = self.get_jumped_squares(starting_square_location, destination_square_location, opponent_color)
        if self._last_piece == starting_square_location and jumped_pieces == []:  # checks final player exception that further info was needed for
            raise OutofTurn

        #Performs move and returns
        num_captured = self.perform_move(starting_square_location, destination_square_location, starting_checker, jumped_pieces, player_color)
        return num_captured

    def validate_starting_square(self, player_name, start):
        """
        Takes a player's name and a set of coordinates as parameters. It checks to makes sure the
        coordinates are within the specified range of the checkers' board. It then checks that the square
        with those coordinates is not empty or does not contain a piece that does not belong to the player.
        If it finds either of those things are not true, it raises the InvalidSquare exception. Otherwise, it
        returns the details of the checkers piece that is located on that square. Utilized by the play_game method.
        Utilizes the get_player_color method.
        """
        row_index = start[0]
        column_index = start[1]
        if row_index > 7 or column_index > 7:
            raise InvalidSquare
        if row_index < 0 or column_index < 0:
            raise InvalidSquare
        starting_row = self._board[row_index]
        starting_checker = starting_row[column_index]
        if starting_checker is None:
            raise InvalidSquare
        checker_color = self.get_player_color(player_name)
        if checker_color not in starting_checker:
            raise InvalidSquare
        return starting_checker

    def validate_destination_square(self, destination):
        """
        Takes coordinates as a parameter. It checks that these coordinates are within the specified range
        of the checkers' board and that there is nothing on the square. If it finds that one of those things is not
        true, it raises and InvalidSquare exception. Utilized by the play_game method.
         """
        row_index = destination[0]
        column_index = destination[1]
        if row_index > 7 or column_index > 7:
            raise InvalidSquare
        if row_index < 0 or column_index < 0:
            raise InvalidSquare
        destination_row = self._board[row_index]
        destination_space = destination_row[column_index]
        if destination_space is not None:
            raise InvalidSquare

    def get_jumped_squares(self, start, destination, opponent_color):
        """
        Takes coordinates for the starting square and destination square and the color of the opponent as parameters.
        Determines which direction the player is moving. Based on this, one of the four methods is called:
        move_up_left, move_up_right, move_down_left, move_down_right. Method then returns a list of coordinates
        containing captured pieces. Utilized by the play_game method.
        """
        jumped_pieces = []
        start_x = start[0]
        start_y = start[1]
        destination_x = destination[0]
        destination_y = destination[1]
        if start_x > destination_x:
            if start_y > destination_y:  # move up left
                jumped_pieces = self.move_up_left(start, destination, opponent_color)
            if start_y < destination_y:  # move up right
                jumped_pieces = self.move_up_right(start, destination, opponent_color)
        if start_x < destination_x:
            if start_y > destination_y:  # move down left
                jumped_pieces = self.move_down_left(start, destination, opponent_color)
            if start_y < destination_y:  # move down right
                jumped_pieces = self.move_down_right(start, destination, opponent_color)
        return jumped_pieces

    def move_up_left(self, start, destination, opponent_color):
        """
        Utilized by the get_jumped_squares method. Takes the starting and destination squares as parameters
        along with the opponent player's color. Looks at all the squares between the start and destination squares (Only
        moves up and to the left). If the square contains an opponent's piece, it adds the coordinates of that square
        to a list. If square has piece of the current player's or contains None, it skips over these squares. Method
        returns list of coordinates once complete.
        """
        jumped_pieces = []
        start_x = start[0]
        start_y = start[1]
        destination_x = destination[0]
        count = abs(start_x - destination_x)
        for num in range(count - 1):
            jumped_square = (start_x - num - 1, start_y - num - 1)
            square_details = self.get_checker_details(jumped_square)
            if square_details is not None:
                if opponent_color in square_details :
                    jumped_pieces.append(jumped_square)
        return jumped_pieces

    def move_up_right(self, start, destination, opponent_color):
        """
        Utilized by the get_jumped_squares method. Takes the starting and destination squares as parameters
        along with the opponent player's color. Looks at all the square between the start and destination squares (Only
        moves up and to the right). If the square contains an opponent's piece, it adds the coordinates of that square
        to a list. If square has piece of the current player's or contains None, it skips over these squares. Method
        returns list of coordinates once complete.
        """
        jumped_pieces = []
        start_x = start[0]
        start_y = start[1]
        destination_x = destination[0]
        count = abs(start_x - destination_x)
        for num in range(count - 1):
            jumped_square = (start_x - num - 1, start_y + num + 1)
            square_details = self.get_checker_details(jumped_square)
            if square_details is not None:
                if opponent_color in square_details:
                    jumped_pieces.append(jumped_square)
        return jumped_pieces

    def move_down_left(self, start, destination, opponent_color):
        """
        Utilized by the get_jumped_squares method. Takes the starting and destination squares as parameters
        along with the opponent player's color. Looks at all the square between the start and destination squares (Only
        moves down and to the left). If the square contains an opponent's piece, it adds the coordinates of that square
        to a list. If square has piece of the current player's or contains None, it skips over these squares. Method
        returns list of coordinates once complete.
        """
        jumped_pieces = []
        start_x = start[0]
        start_y = start[1]
        destination_x = destination[0]
        count = abs(start_x - destination_x)
        for num in range(count - 1):
            jumped_square = (start_x + num + 1, start_y - num - 1)
            square_details = self.get_checker_details(jumped_square)
            if square_details is not None:
                if opponent_color in square_details:
                    jumped_pieces.append(jumped_square)
        return jumped_pieces

    def move_down_right(self, start, destination, opponent_color):
        """
        Utilized by the get_jumped_squares method. Takes the starting and destination squares as parameters
        along with the opponent player's color. Looks at all the square between the start and destination squares (Only
        moves down and to the right). If the square contains an opponent's piece, it adds the coordinates of that square
        to a list. If square has piece of the current player's or contains None, it skips over these squares. Method
        returns list of coordinates once complete.
        """
        jumped_pieces = []
        start_x = start[0]
        start_y = start[1]
        destination_x = destination[0]
        count = abs(start_x - destination_x)
        for num in range(count - 1):
            jumped_square = (start_x + num + 1, start_y + num + 1)
            square_details = self.get_checker_details(jumped_square)
            if square_details is not None:
                if opponent_color in square_details:
                    jumped_pieces.append(jumped_square)
        return jumped_pieces

    def perform_move(self, start, destination, starting_checker, jumped_pieces, player_color):
        """
        Takes as parameters coordinates for the start square and destination squares, the contents of the
        starting square, a list of any captured pieces, and the player's color. It then updates the starting square
        to contain None. It updates the destination square to contain the contents from the starting_checker or a
        king or triple king if applicable. It updates any counts within the Player's king or triple king counts and
        sets the self._last_piece to the destination coordinates. If a king or triple king is made, it sets the
        self._last_move_king_creation data member to True, otherwise it sets this to False. It then goes to the
        list of captured squares. If the list is empty it sets the self._last_move_capture data member to False.
        If the list is not empty, it goes through the self._board data member and set the squares in the list to
        None. As it does this it checks if any of the squares contain kings or triple kings to append the opponent's
        counts accordingly. It also updates a variable for the number of captured pieces and sets self._last_move_capture
        to True. Finally, it sets self._current_turn to the opponent, updates the player's number of captured pieces
        with the total from the list, and checks for a winner and sets the self._winner data member to that players
        name. It then returns the total number of captured pieces. This is utilized by the play_game method. It calls
        the update_square, get_player_object, get_player_name, get_checker_details, append_king_count,
        append_triple_king_count, append_captured_pieces_count, and get_captured_pieces_count methods.
        """
        #Set-up necessary variables
        captured_pieces = 0
        player_object = self.get_player_object(player_color)
        player_name = self.get_player_name(player_color)
        if player_color == "White":
            opponent_object = self.get_player_object("Black")
            opponent_name = self.get_player_name("Black")
        else:
            opponent_object = self.get_player_object("White")
            opponent_name = self.get_player_name("White")
        destination_x = destination[0]

        #Update starting square
        self.update_square(start, None)

        #Update destination square
        if player_color == "Black":
            if starting_checker == "Black" and destination_x == 0:
                self.update_square(destination, "Black_king")
                player_object.append_king_count(1)
                self._last_move_king_creation = True
            elif starting_checker == "Black_king" and destination_x == 7:
                self.update_square(destination, "Black_Triple_King")
                player_object.append_triple_king_count(1)
                self._last_move_king_creation = True
            else:
                self.update_square(destination, starting_checker)
                self._last_move_king_creation = False
        if player_color == "White":
            if starting_checker == "White" and destination_x == 7:
                self.update_square(destination, "White_king")
                player_object.append_king_count(1)
                self._last_move_king_creation = True
            elif starting_checker == "White_king" and destination_x == 0:
                self.update_square(destination, "White_Triple_King")
                player_object.append_triple_king_count(1)
                self._last_move_king_creation = True
            else:
                self.update_square(destination, starting_checker)
                self._last_move_king_creation = False
        self._last_piece = destination

        #Update captured pieces
        if jumped_pieces == []:
            self._last_move_capture = False
        else:
            for index in jumped_pieces:
                temp_checker = self.get_checker_details(index)
                if "king" in temp_checker:
                    opponent_object.append_king_count(-1)
                if "Triple" in temp_checker:
                    opponent_object.append_triple_king_count(-1)
                captured_pieces += 1
                self.update_square(index, None)
                self._last_move_capture = True

        #Update necessary data members and return
        self._current_turn = opponent_name
        player_object.append_captured_pieces_count(captured_pieces)
        if player_object.get_captured_pieces_count() == 12:
            self._winner = player_name
        return captured_pieces

    def update_square(self, square_location, checker_on_square):
        """
        Takes a set of coordinates and checker piece/None as parameter. It then goes into the self._board data member
        and places the checker piece/None on the square of the coordinates. Utilized by perform_move method.
        """
        row = square_location[0]
        column = square_location[1]
        board_row = self._board[row]
        board_row[column] = checker_on_square

    def print_board(self):
        """Takes no parameters and prints what the current board looks like in the form of an array."""
        print(self._board)

    def pretty_print_board(self):
        """
        Takes no parameters and prints what the current board looks like in the form of an array that is easily readable.
        """
        for index in range(len(self._board)):
            print(self._board[index])

    def game_winner(self):
        """Returns the game winner. If no game winner exists, returns 'Game has not ended'."""
        if self._winner is None:
            return "Game has not ended"
        else:
            return self._winner
