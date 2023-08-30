# Author: Hailey Stoudt
# GitHub username: stoudth
# Date: 3/19/2024
# Description: Unit Testing File for CheckersGame.py (Portfolio Project - CS 162). Tests for applicable exceptions
#              specified in the README and Ed Discussions.

import unittest

from CheckersGame import Checkers, Player, OutofTurn, InvalidPlayer, InvalidSquare


class TestInvalidPlayer(unittest.TestCase):
    """Contains unit tests for InvalidPlayer exception."""

    def test_1(self):
        """Tests that InvalidPlayer Exception is raised."""
        game_1 = Checkers()

        #Tests that checker color must be "Black" or "White"
        with self.assertRaises(InvalidPlayer):
            game_1.create_player("Reggie", "Green")
        with self.assertRaises(InvalidPlayer):
            game_1.create_player("Bilal", "Blue")

        #Tests that only two people are allowed to play and both people can't be the same color or same name
        game_1.create_player("Reggie", "White")
        with self.assertRaises(InvalidPlayer):
            game_1.create_player("Vera", "White")
        with self.assertRaises(InvalidPlayer):
            game_1.create_player("Reggie", "Black")
        game_1.create_player("Bilal", "Black")
        with self.assertRaises(InvalidPlayer):
            game_1.create_player("Ali", "Black")

        #Tests that player names must be accurate to perform move
        game_1.play_game("Bilal", (5, 2), (4, 1))
        game_1.play_game("Reggie", (2, 7), (3, 6))
        with self.assertRaises(InvalidPlayer):
            game_1.play_game("Joan", (5, 4), (4, 3))
        with self.assertRaises(InvalidPlayer):
            game_1.play_game("Morina", (2, 5), (3, 4))


class TestInvalidSquare(unittest.TestCase):
    """Contains unit tests for InvalidSquare exception."""

    def test_2(self):
        """Tests that InvalidSquare exception is raised for starting square."""
        game_2 = Checkers()
        game_2.create_player("Stacy", "White")
        game_2.create_player("Mark", "Black")

        #Tests starting square off of board
        with self.assertRaises(InvalidSquare):
            game_2.play_game("Mark", (5, 8), (4, 7))
        game_2.play_game("Mark", (5, 6), (4, 7))
        with self.assertRaises(InvalidSquare):
            game_2.play_game("Stacy", (2, -1), (3, 0))
        game_2.play_game("Stacy", (2, 1), (3, 0))

        #Tests starting square with opponent piece
        with self.assertRaises(InvalidSquare):
            game_2.play_game("Mark", (2, 1), (3, 0))
        game_2.play_game("Mark", (5, 4), (4, 5))
        with self.assertRaises(InvalidSquare):
            game_2.play_game("Stacy", (5, 6), (4, 5))
        game_2.play_game("Stacy", (2, 3), (3, 2))

        #Tests starting square with no piece
        with self.assertRaises(InvalidSquare):
            game_2.play_game("Mark", (4, 1), (3, 2))
        game_2.play_game("Mark", (5, 2), (4, 1))
        with self.assertRaises(InvalidSquare):
            game_2.play_game("Stacy", (3, 4), (4, 3))

    def test_3(self):
        """Tests that InvalidSquare exception is raised for destination square."""
        game_3 = Checkers()
        game_3.create_player("Tom", "White")
        game_3.create_player("Fran", "Black")

        #Tests destination square off board
        with self.assertRaises(InvalidSquare):
            game_3.play_game("Fran", (6, 7), (5, 8))
        game_3.play_game("Fran", (5, 6), (4, 5))
        with self.assertRaises(InvalidSquare):
            game_3.play_game("Tom", (2, 1), (3, -1))

        # Tests destination square containing own piece
        with self.assertRaises(InvalidSquare):
            game_3.play_game("Tom", (1, 2), (2, 1))
        game_3.play_game("Tom", (2, 1), (3, 2))
        with self.assertRaises(InvalidSquare):
            game_3.play_game("Fran", (6, 5), (5, 4))

        # Tests destination square containing opponent piece
        game_3.play_game("Fran", (5, 2), (4, 3))
        with self.assertRaises(InvalidSquare):
            game_3.play_game("Tom", (3, 2), (4, 3))
        game_3.play_game("Tom", (1, 2), (2, 1))
        with self.assertRaises(InvalidSquare):
            game_3.play_game("Fran", (4, 3), (3, 2))

    def test_4(self):
        """Tests that InvalidSquare is raised for get_checker_details method."""
        game_3 = Checkers()
        game_3.create_player("Tom", "White")
        game_3.create_player("Fran", "Black")

        with self.assertRaises(InvalidSquare):
            game_3.get_checker_details((-1, 7))
        with self.assertRaises(InvalidSquare):
            game_3.get_checker_details((1, 8))


class TestOutofTurn(unittest.TestCase):
    """Contains unit tests for OutofTurn exception."""
    def test_5(self):
        """
        Tests that OutofTurn is raised when a player moves when they are not listed under the
        self._current_turn data member.
        """
        game_4 = Checkers()
        game_4.create_player("Isidora", "White")
        game_4.create_player("Xena", "Black")

        with self.assertRaises(OutofTurn):
            game_4.play_game("Isidora", (2, 3), (3, 4))

    def test_6(self):
        """
        Tests that OutofTurn is raised when a player has just made a capturing move and uses the last piece played but
        does not make another capturing move.
        """
        game_4 = Checkers()
        game_4.create_player("Isidora", "White")
        game_4.create_player("Xena", "Black")

        game_4.play_game("Xena", (5, 6), (4, 5))
        game_4.play_game("Isidora", (2, 1), (3, 2))
        game_4.play_game("Xena", (5, 2), (4, 3))
        game_4.play_game("Isidora", (3, 2), (4, 1))
        game_4.play_game("Xena", (4, 3), (3, 2))
        game_4.play_game("Isidora", (1, 0), (2, 1))
        game_4.play_game("Xena", (3, 2), (1, 0))
        game_4.play_game("Isidora", (1, 2), (2, 1))
        game_4.play_game("Xena", (5, 0), (3, 2))
        game_4.play_game("Isidora", (2, 3), (4, 1))
        with self.assertRaises(OutofTurn):
            game_4.play_game("Isidora", (4, 1), (5, 0))

    def test_7(self):
        """
        Tests that OutofTurn is raised when the player makes a capturing move but doesn't use the same piece used
        in the previous move.
        """
        game_4 = Checkers()
        game_4.create_player("Isidora", "White")
        game_4.create_player("Xena", "Black")

        game_4.play_game("Xena", (5, 6), (4, 5))
        game_4.play_game("Isidora", (2, 1), (3, 2))
        game_4.play_game("Xena", (5, 2), (4, 3))
        game_4.play_game("Isidora", (3, 2), (4, 1))
        game_4.play_game("Xena", (4, 3), (3, 2))
        game_4.play_game("Isidora", (1, 0), (2, 1))
        game_4.play_game("Xena", (3, 2), (1, 0))
        game_4.play_game("Isidora", (1, 2), (2, 1))
        game_4.play_game("Xena", (5, 0), (3, 2))
        game_4.play_game("Isidora", (2, 3), (4, 1))
        with self.assertRaises(OutofTurn):
            game_4.play_game("Isidora", (2, 5), (3, 6))

    def test_8(self):
        """
        Tests that if a king is made on a capture move OutofTurn will be raised if player tries to move again and make
        another capturing move.
        """
        game_4 = Checkers()
        game_4.create_player("Isidora", "White")
        game_4.create_player("Xena", "Black")

        game_4.play_game("Xena", (5, 6), (4, 5))
        game_4.play_game("Isidora", (2, 1), (3, 2))
        game_4.play_game("Xena", (5, 2), (4, 3))
        game_4.play_game("Isidora", (3, 2), (4, 1))
        game_4.play_game("Xena", (4, 3), (3, 2))
        game_4.play_game("Isidora", (1, 0), (2, 1))
        game_4.play_game("Xena", (3, 2), (1, 0))
        game_4.play_game("Isidora", (1, 2), (2, 1))
        game_4.play_game("Xena", (5, 0), (3, 2))
        game_4.play_game("Isidora", (2, 3), (4, 1))
        game_4.play_game("Xena", (6, 1), (5, 2))
        game_4.play_game("Isidora", (4, 1), (5, 0))
        game_4.play_game("Xena", (7, 2), (6, 1))
        game_4.play_game("Isidora", (5, 0), (7, 2))
        game_4.play_game("Xena", (4, 5), (3, 6))
        game_4.play_game("Isidora", (2, 7), (4, 5))
        game_4.play_game("Xena", (5, 4), (3, 6))
        game_4.play_game("Isidora", (0, 1), (1, 2))
        game_4.play_game("Xena", (1, 0), (0, 1))
        with self.assertRaises(OutofTurn):
            game_4.play_game("Xena", (0, 1), (2, 3))


class TestPlayerClass(unittest.TestCase):
    """Contains unit tests to test the methods in the Player Class."""
    def test_9(self):
        """Tests get_king_count and append_king_count methods."""
        game_5 = Checkers()
        player1 = game_5.create_player("Reggie", "White")
        player2 = game_5.create_player("Bilal", "Black")

        #Tests get_king_count method right after initialization
        self.assertEqual(player1.get_king_count(), 0)
        self.assertEqual(player2.get_king_count(), 0)
        game_5.play_game("Bilal", (5, 6), (4, 5))
        game_5.play_game("Reggie", (2, 1), (3, 2))
        game_5.play_game("Bilal", (5, 2), (4, 3))
        game_5.play_game("Reggie", (3, 2), (4, 1))
        game_5.play_game("Bilal", (4, 3), (3, 2))
        game_5.play_game("Reggie", (1, 0), (2, 1))
        game_5.play_game("Bilal", (3, 2), (1, 0))
        game_5.play_game("Reggie", (1, 2), (2, 1))
        game_5.play_game("Bilal", (5, 0), (3, 2))
        game_5.play_game("Reggie", (2, 3), (4, 1))
        game_5.play_game("Bilal", (6, 1), (5, 2))
        game_5.play_game("Reggie", (4, 1), (5, 0))
        game_5.play_game("Bilal", (7, 2), (6, 1))
        game_5.play_game("Reggie", (5, 0), (7, 2))

        # tests get_king_count method after first append_king_count method for Player 1
        self.assertEqual(player1.get_king_count(), 1)
        self.assertEqual(player2.get_king_count(), 0)
        game_5.play_game("Bilal", (4, 5), (3, 6))
        game_5.play_game("Reggie", (2, 7), (4, 5))
        game_5.play_game("Bilal", (5, 4), (3, 6))
        game_5.play_game("Reggie", (0, 1), (1, 2))
        game_5.play_game("Bilal", (1, 0), (0, 1))

        # tests get_king_count method after first append_king_count method for Player 2
        self.assertEqual(player1.get_king_count(), 1)
        self.assertEqual(player2.get_king_count(), 1)
        game_5.play_game("Reggie", (7, 2), (4, 5))
        game_5.play_game("Bilal", (0, 1), (3, 4))
        game_5.play_game("Reggie", (4, 5), (0, 1))

        #tests get_king_count method after append_king_count is passed a negative number
        self.assertEqual(player1.get_king_count(), 1)
        self.assertEqual(player2.get_king_count(), 0)

    def test_10(self):
        """Tests get_triple_king_count and append_triple_king_count methods."""
        game_5 = Checkers()
        player1 = game_5.create_player("Reggie", "White")
        player2 = game_5.create_player("Bilal", "Black")

        # Tests get_triple_king_count method right after initialization
        self.assertEqual(player1.get_triple_king_count(), 0)
        self.assertEqual(player2.get_triple_king_count(), 0)
        game_5.play_game("Bilal", (5, 6), (4, 5))
        game_5.play_game("Reggie", (2, 1), (3, 2))
        game_5.play_game("Bilal", (5, 2), (4, 3))
        game_5.play_game("Reggie", (3, 2), (4, 1))
        game_5.play_game("Bilal", (4, 3), (3, 2))
        game_5.play_game("Reggie", (1, 0), (2, 1))
        game_5.play_game("Bilal", (3, 2), (1, 0))
        game_5.play_game("Reggie", (1, 2), (2, 1))
        game_5.play_game("Bilal", (5, 0), (3, 2))
        game_5.play_game("Reggie", (2, 3), (4, 1))
        game_5.play_game("Bilal", (6, 1), (5, 2))
        game_5.play_game("Reggie", (4, 1), (5, 0))
        game_5.play_game("Bilal", (7, 2), (6, 1))
        game_5.play_game("Reggie", (5, 0), (7, 2))
        game_5.play_game("Bilal", (4, 5), (3, 6))
        game_5.play_game("Reggie", (2, 7), (4, 5))
        game_5.play_game("Bilal", (5, 4), (3, 6))
        game_5.play_game("Reggie", (0, 1), (1, 2))
        game_5.play_game("Bilal", (1, 0), (0, 1))
        game_5.play_game("Reggie", (7, 2), (4, 5))
        game_5.play_game("Bilal", (0, 1), (3, 4))
        game_5.play_game("Reggie", (4, 5), (0, 1))

        #Tests get_triple_king_count and append_triple_king_count after player1 gets a triple king.
        self.assertEqual(player1.get_triple_king_count(), 1)
        self.assertEqual(player2.get_triple_king_count(), 0)
        game_5.play_game("Bilal", (3, 6), (2, 7))
        game_5.play_game("Reggie", (2, 5), (3, 4))
        game_5.play_game("Bilal", (6, 5), (5, 4))
        game_5.play_game("Reggie", (1, 4), (2, 3))
        game_5.play_game("Bilal", (7, 4), (6, 3))
        game_5.play_game("Reggie", (0, 5), (1, 4))
        game_5.play_game("Bilal", (2, 7), (0, 5))
        game_5.play_game("Reggie", (0, 1), (1, 0))
        game_5.play_game("Bilal", (6, 7), (5, 6))
        game_5.play_game("Reggie", (0, 7), (1, 6))
        game_5.play_game("Bilal", (0, 5), (2, 7))
        game_5.play_game("Reggie", (1, 0), (4, 3))
        game_5.play_game("Bilal", (5, 2), (4, 1))
        game_5.play_game("Reggie", (2, 1), (3, 2))
        game_5.play_game("Bilal", (7, 6), (6, 5))
        game_5.play_game("Reggie", (4, 3), (7, 6))
        game_5.play_game("Bilal", (2, 7), (3, 6))
        game_5.play_game("Reggie", (7, 6), (6, 7))
        game_5.play_game("Bilal", (7, 0), (6, 1))
        game_5.play_game("Reggie", (6, 7), (4, 5))
        game_5.play_game("Reggie", (4, 5), (2, 7))
        game_5.play_game("Reggie", (2, 7), (7, 2))
        game_5.play_game("Reggie", (7, 2), (5, 0))
        game_5.play_game("Bilal", (4, 1), (3, 0))
        game_5.play_game("Reggie", (5, 0), (4, 1))
        game_5.play_game("Bilal", (3, 0), (2, 1))
        game_5.play_game("Reggie", (4, 1), (3, 0))
        game_5.play_game("Bilal", (2, 1), (1, 0))
        game_5.play_game("Reggie", (3, 0), (2, 1))
        game_5.play_game("Bilal", (1, 0), (0, 1))
        game_5.play_game("Reggie", (2, 1), (3, 0))
        game_5.play_game("Bilal", (0, 1), (1, 0))
        game_5.play_game("Reggie", (3, 0), (4, 1))
        game_5.play_game("Bilal", (1, 0), (7, 6))

        #tests get_triple_king_count and append_triple_king_count methods after Player 2 gets a triple king
        self.assertEqual(player1.get_triple_king_count(), 1)
        self.assertEqual(player2.get_triple_king_count(), 1)
        game_5.play_game("Reggie", (4, 1), (0, 5))
        game_5.play_game("Bilal", (7, 6), (6, 7))
        game_5.play_game("Reggie", (1, 4), (2, 5))
        game_5.play_game("Bilal", (6, 7), (1, 2))
        game_5.play_game("Reggie", (0, 3), (2, 1))

        #tests get_triple_king_count after append_triple_king_count is passed a negative number
        self.assertEqual(player1.get_triple_king_count(), 1)
        self.assertEqual(player2.get_triple_king_count(), 0)

    def test_11(self):
        """Tests get_captured_pieces_count and append_captured_pieces_count methods."""
        game_5 = Checkers()
        player1 = game_5.create_player("Reggie", "White")
        player2 = game_5.create_player("Bilal", "Black")

        # Tests get_captured_pieces_count method right after initialization
        self.assertEqual(player1.get_captured_pieces_count(), 0)
        self.assertEqual(player2.get_captured_pieces_count(), 0)
        game_5.play_game("Bilal", (5, 6), (4, 5))
        game_5.play_game("Reggie", (2, 1), (3, 2))
        game_5.play_game("Bilal", (5, 2), (4, 3))
        game_5.play_game("Reggie", (3, 2), (4, 1))
        game_5.play_game("Bilal", (4, 3), (3, 2))
        game_5.play_game("Reggie", (1, 0), (2, 1))
        game_5.play_game("Bilal", (3, 2), (1, 0))

        #Test after Black's first capture
        self.assertEqual(player1.get_captured_pieces_count(), 0)
        self.assertEqual(player2.get_captured_pieces_count(), 1)
        game_5.play_game("Reggie", (1, 2), (2, 1))
        game_5.play_game("Bilal", (5, 0), (3, 2))
        game_5.play_game("Reggie", (2, 3), (4, 1))

        # Test after Black's second capture and White's first capture
        self.assertEqual(player1.get_captured_pieces_count(), 1)
        self.assertEqual(player2.get_captured_pieces_count(), 2)
        game_5.play_game("Bilal", (6, 1), (5, 2))
        game_5.play_game("Reggie", (4, 1), (5, 0))
        game_5.play_game("Bilal", (7, 2), (6, 1))
        game_5.play_game("Reggie", (5, 0), (7, 2))
        game_5.play_game("Bilal", (4, 5), (3, 6))
        self.assertEqual(player2.get_captured_pieces_count(), 2)
        game_5.play_game("Reggie", (2, 7), (4, 5))
        game_5.play_game("Bilal", (5, 4), (3, 6))
        game_5.play_game("Reggie", (0, 1), (1, 2))
        game_5.play_game("Bilal", (1, 0), (0, 1))
        game_5.play_game("Reggie", (7, 2), (4, 5))
        game_5.play_game("Bilal", (0, 1), (3, 4))
        game_5.play_game("Reggie", (4, 5), (0, 1))
        game_5.play_game("Bilal", (3, 6), (2, 7))
        game_5.play_game("Reggie", (2, 5), (3, 4))
        game_5.play_game("Bilal", (6, 5), (5, 4))
        game_5.play_game("Reggie", (1, 4), (2, 3))
        game_5.play_game("Bilal", (7, 4), (6, 3))
        game_5.play_game("Reggie", (0, 5), (1, 4))
        game_5.play_game("Bilal", (2, 7), (0, 5))
        game_5.play_game("Reggie", (0, 1), (1, 0))
        game_5.play_game("Bilal", (6, 7), (5, 6))
        game_5.play_game("Reggie", (0, 7), (1, 6))
        game_5.play_game("Bilal", (0, 5), (2, 7))
        game_5.play_game("Reggie", (1, 0), (4, 3))
        game_5.play_game("Bilal", (5, 2), (4, 1))
        game_5.play_game("Reggie", (2, 1), (3, 2))
        game_5.play_game("Bilal", (7, 6), (6, 5))
        game_5.play_game("Reggie", (4, 3), (7, 6))

        # Test after White takes 2 pieces in 1 move
        self.assertEqual(player1.get_captured_pieces_count(), 7)
        self.assertEqual(player2.get_captured_pieces_count(), 6)
        game_5.play_game("Bilal", (2, 7), (3, 6))
        game_5.play_game("Reggie", (7, 6), (6, 7))
        game_5.play_game("Bilal", (7, 0), (6, 1))
        game_5.play_game("Reggie", (6, 7), (4, 5))
        game_5.play_game("Reggie", (4, 5), (2, 7))
        game_5.play_game("Reggie", (2, 7), (7, 2))
        game_5.play_game("Reggie", (7, 2), (5, 0))

        # Test after White makes 4 captures in a row
        self.assertEqual(player1.get_captured_pieces_count(), 11)
        self.assertEqual(player2.get_captured_pieces_count(), 6)
        game_5.play_game("Bilal", (4, 1), (3, 0))
        game_5.play_game("Reggie", (5, 0), (4, 1))
        game_5.play_game("Bilal", (3, 0), (2, 1))
        game_5.play_game("Reggie", (4, 1), (3, 0))
        game_5.play_game("Bilal", (2, 1), (1, 0))
        game_5.play_game("Reggie", (3, 0), (2, 1))
        game_5.play_game("Bilal", (1, 0), (0, 1))
        game_5.play_game("Reggie", (2, 1), (3, 0))
        game_5.play_game("Bilal", (0, 1), (1, 0))
        game_5.play_game("Reggie", (3, 0), (4, 1))
        game_5.play_game("Bilal", (1, 0), (7, 6))
        game_5.play_game("Reggie", (4, 1), (0, 5))
        game_5.play_game("Bilal", (7, 6), (6, 7))
        game_5.play_game("Reggie", (1, 4), (2, 5))
        game_5.play_game("Bilal", (6, 7), (1, 2))
        game_5.play_game("Reggie", (0, 3), (2, 1))

        #test at end of game
        self.assertEqual(player1.get_captured_pieces_count(), 12)
        self.assertEqual(player2.get_captured_pieces_count(), 9)


class TestCheckersClass(unittest.TestCase):
    """Contains unit tests for the methods in the Checkers class."""

    def test_12(self):
        """
        Tests the init, create_player, get_player_name, get_player_color, get opponent_color,
        and get_checker_details methods.
        """
        game_6 = Checkers()
        game_6.create_player("Samuel", "White")
        game_6.create_player("Lionel", "Black")
        self.assertEqual(game_6.get_player_name("White"), "Samuel")
        self.assertEqual(game_6.get_player_name("Black"), "Lionel")
        self.assertEqual(game_6.get_player_color("Samuel"), "White")
        self.assertEqual(game_6.get_player_color("Lionel"), "Black")
        self.assertIs(game_6.get_checker_details((0, 0)), None)
        self.assertEqual(game_6.get_checker_details((0, 1)), "White")
        self.assertEqual(game_6.get_checker_details((7, 0)), "Black")

    def test_13(self):
        """
        Tests the play_game methods and get_winner methods. This utilizes all methods except init, create_player,
        and the print_board methods in the Checkers class.
        """
        game_6 = Checkers()
        game_6.create_player("Samuel", "White")
        game_6.create_player("Lionel", "Black")

        #Tests that count of captured pieces returned is 0 for non-capture moves
        self.assertEqual(game_6.play_game("Lionel", (5, 6), (4, 5)), 0)
        self.assertEqual(game_6.play_game("Samuel", (2, 1), (3, 2)), 0)
        game_6.play_game("Lionel", (5, 2), (4, 3))
        game_6.play_game("Samuel", (3, 2), (4, 1))
        game_6.play_game("Lionel", (4, 3), (3, 2))
        game_6.play_game("Samuel", (1, 0), (2, 1))

        #Tests count of captured pieces returned is 1 after first capture
        self.assertEqual(game_6.play_game("Lionel", (3, 2), (1, 0)), 1)
        game_6.play_game("Samuel", (1, 2), (2, 1))
        self.assertEqual(game_6.play_game("Lionel", (5, 0), (3, 2)), 1)
        self.assertEqual(game_6.play_game("Samuel", (2, 3), (4, 1)), 1)
        game_6.play_game("Lionel", (6, 1), (5, 2))
        game_6.play_game("Samuel", (4, 1), (5, 0))
        game_6.play_game("Lionel", (7, 2), (6, 1))
        self.assertEqual(game_6.play_game("Samuel", (5, 0), (7, 2)), 1)
        game_6.play_game("Lionel", (4, 5), (3, 6))
        game_6.play_game("Samuel", (2, 7), (4, 5))
        game_6.play_game("Lionel", (5, 4), (3, 6))
        game_6.play_game("Samuel", (0, 1), (1, 2))
        game_6.play_game("Lionel", (1, 0), (0, 1))

        #Tests captures where a jump is over more than 1 space
        self.assertEqual(game_6.play_game("Samuel", (7, 2), (4, 5)), 1)
        self.assertEqual(game_6.play_game("Lionel", (0, 1), (3, 4)), 1)
        self.assertEqual(game_6.play_game("Samuel", (4, 5), (0, 1)), 1)
        game_6.play_game("Lionel", (3, 6), (2, 7))
        game_6.play_game("Samuel", (2, 5), (3, 4))
        game_6.play_game("Lionel", (6, 5), (5, 4))
        game_6.play_game("Samuel", (1, 4), (2, 3))
        game_6.play_game("Lionel", (7, 4), (6, 3))
        game_6.play_game("Samuel", (0, 5), (1, 4))
        game_6.play_game("Lionel", (2, 7), (0, 5))
        game_6.play_game("Samuel", (0, 1), (1, 0))
        game_6.play_game("Lionel", (6, 7), (5, 6))
        game_6.play_game("Samuel", (0, 7), (1, 6))
        game_6.play_game("Lionel", (0, 5), (2, 7))

        #Tests a jump over friendly pieces
        self.assertEqual(game_6.play_game("Samuel", (1, 0), (4, 3)), 0)
        game_6.play_game("Lionel", (5, 2), (4, 1))
        game_6.play_game("Samuel", (2, 1), (3, 2))
        game_6.play_game("Lionel", (7, 6), (6, 5))

        #Tests a jump that captures 2 pieces at once
        self.assertEqual(game_6.play_game("Samuel", (4, 3), (7, 6)), 2)
        game_6.play_game("Lionel", (2, 7), (3, 6))
        game_6.play_game("Samuel", (7, 6), (6, 7))
        game_6.play_game("Lionel", (7, 0), (6, 1))

        #Tests 4 moves in a row that capture 1 piece each move
        self.assertEqual(game_6.play_game("Samuel", (6, 7), (4, 5)), 1)
        self.assertEqual(game_6.play_game("Samuel", (4, 5), (2, 7)), 1)
        self.assertEqual(game_6.play_game("Samuel", (2, 7), (7, 2)), 1)
        self.assertEqual(game_6.play_game("Samuel", (7, 2), (5, 0)), 1)
        game_6.play_game("Lionel", (4, 1), (3, 0))
        game_6.play_game("Samuel", (5, 0), (4, 1))
        game_6.play_game("Lionel", (3, 0), (2, 1))
        game_6.play_game("Samuel", (4, 1), (3, 0))
        game_6.play_game("Lionel", (2, 1), (1, 0))
        game_6.play_game("Samuel", (3, 0), (2, 1))
        game_6.play_game("Lionel", (1, 0), (0, 1))
        game_6.play_game("Samuel", (2, 1), (3, 0))
        game_6.play_game("Lionel", (0, 1), (1, 0))
        game_6.play_game("Samuel", (3, 0), (4, 1))
        game_6.play_game("Lionel", (1, 0), (7, 6))

        #Tests a friendly jump over two pieces
        self.assertEqual(game_6.play_game("Samuel", (4, 1), (0, 5)), 0)
        game_6.play_game("Lionel", (7, 6), (6, 7))
        game_6.play_game("Samuel", (1, 4), (2, 5))

        #Tests another jump that captures two pieces at once
        self.assertEqual(game_6.play_game("Lionel", (6, 7), (1, 2)), 2)

        #Checks winner before and after game winning move
        self.assertEqual(game_6.game_winner(), "Game has not ended")
        game_6.play_game("Samuel", (0, 3), (2, 1))
        self.assertEqual(game_6.game_winner(), "Samuel")

    def test_14(self):
        """Tests play_game method with different checkers game."""
        game_7 = Checkers()
        player3 = game_7.create_player("Zoe", "White")
        player4 = game_7.create_player("Kira", "Black")

        # Check that self._board is updating with moves
        self.assertEqual(game_7.get_checker_details((5, 0)), "Black")
        game_7.play_game("Kira", (5, 0), (4, 1))
        self.assertIs(game_7.get_checker_details((5, 0)), None)
        self.assertEqual(game_7.get_checker_details((4, 1)), "Black")
        self.assertEqual(game_7.get_checker_details((2, 1)), "White")
        game_7.play_game("Zoe", (2, 1), (3, 0))
        self.assertIs(game_7.get_checker_details((2, 1)), None)
        self.assertEqual(game_7.get_checker_details((3, 0)), "White")
        game_7.play_game("Kira", (6, 1), (5, 0))

        #Tests first capture
        self.assertEqual(game_7.play_game("Zoe", (2, 3), (3, 2)), 0)
        self.assertEqual(player4.get_captured_pieces_count(), 0)
        self.assertEqual(game_7.play_game("Kira", (4, 1), (2, 3)), 1)
        self.assertEqual(player4.get_captured_pieces_count(), 1)
        self.assertEqual(game_7.play_game("Zoe", (1, 4), (3, 2)), 1)
        self.assertEqual(player3.get_captured_pieces_count(), 1)
        game_7.play_game("Kira", (5, 6), (4, 7))
        game_7.play_game("Zoe", (2, 5), (3, 6))
        game_7.play_game("Kira", (4, 7), (2, 5))
        game_7.play_game("Zoe", (1, 6), (3, 4))
        game_7.play_game("Kira", (6, 5), (5, 6))
        game_7.play_game("Zoe", (1, 2), (2, 3))
        game_7.play_game("Kira", (7, 4), (6, 5))
        game_7.play_game("Zoe", (3, 4), (4, 5))

        #Tests a turn with more than 1 move
        self.assertEqual(player4.get_captured_pieces_count(), 2)
        self.assertEqual(game_7.play_game("Kira", (5, 6), (3, 4)), 1)
        self.assertEqual(player4.get_captured_pieces_count(), 3)
        self.assertEqual(game_7.play_game("Kira", (3, 4), (1, 2)), 1)
        self.assertEqual(player4.get_captured_pieces_count(), 4)
        game_7.play_game("Zoe", (0, 1), (2, 3))
        game_7.play_game("Kira", (5, 4), (4, 5))
        game_7.play_game("Zoe", (0, 3), (1, 4))
        game_7.play_game("Kira", (6, 7), (5, 6))
        game_7.play_game("Zoe", (3, 2), (4, 3))
        game_7.play_game("Kira", (5, 2), (3, 4))
        game_7.play_game("Kira", (3, 4), (1, 2))
        game_7.play_game("Zoe", (1, 0), (2, 1))
        game_7.play_game("Kira", (1, 2), (0, 3))

        #Tests that king piece was made and put on board
        self.assertEqual(player4.get_king_count(), 1)
        self.assertEqual(game_7.get_checker_details((0, 3)), "Black_king")
        game_7.play_game("Zoe", (2, 7), (3, 6))
        game_7.play_game("Kira", (0, 3), (2, 5))
        game_7.play_game("Kira", (2, 5), (4, 7))
        game_7.play_game("Zoe", (0, 5), (1, 4))
        game_7.play_game("Kira", (4, 5), (3, 6))
        game_7.play_game("Zoe", (0, 7), (1, 6))
        game_7.play_game("Kira", (5, 6), (4, 5))
        game_7.play_game("Zoe", (2, 1), (3, 2))
        game_7.play_game("Kira", (6, 5), (5, 4))
        game_7.play_game("Zoe", (1, 6), (2, 5))
        game_7.play_game("Kira", (5, 0), (4, 1))
        game_7.play_game("Zoe", (3, 0), (5, 2))

        #Tests capture where king is made
        self.assertEqual(game_7.play_game("Zoe", (5, 2), (7, 4)), 1)
        self.assertEqual(player3.get_king_count(), 1)
        self.assertEqual(game_7.get_checker_details((7, 4)), "White_king")
        game_7.play_game("Kira", (3, 6), (2, 7))
        game_7.play_game("Zoe", (1, 4), (2, 3))
        game_7.play_game("Kira", (4, 7), (5, 6))
        game_7.play_game("Zoe", (7, 4), (6, 5))

        #Tests capture where triple king is made
        self.assertEqual(game_7.play_game("Kira", (5, 6), (7, 4)), 1)
        self.assertEqual(player4.get_triple_king_count(), 1)
        self.assertEqual(game_7.get_checker_details((7, 4)), "Black_Triple_King")
        game_7.play_game("Zoe", (2, 5), (3, 4))
        game_7.play_game("Kira", (4, 5), (3, 6))
        game_7.play_game("Zoe", (3, 4), (4, 3))
        game_7.play_game("Kira", (5, 4), (4, 5))
        game_7.play_game("Zoe", (3, 2), (4, 1))
        game_7.play_game("Kira", (7, 4), (3, 0))
        game_7.play_game("Zoe", (2, 3), (3, 2))
        game_7.play_game("Kira", (3, 6), (2, 5))
        game_7.play_game("Zoe", (4, 3), (5, 4))
        game_7.play_game("Kira", (3, 0), (2, 1))
        game_7.play_game("Zoe", (3, 2), (4, 3))

        #Checks Winner
        self.assertEqual(game_7.game_winner(), "Game has not ended")
        game_7.play_game("Kira", (2, 1), (6, 5))
        self.assertEqual(player4.get_captured_pieces_count(), 12)
        self.assertEqual(game_7.game_winner(), "Kira")
