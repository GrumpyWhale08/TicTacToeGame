using System;

class TicTacToe {
    static char[,] board = {
        { '1', '2', '3' },
        { '4', '5', '6' },
        { '7', '8', '9' }
    };

    static void Main() {
        int turn = 0;
        char player = 'X';
        while (turn < 9) {
            PrintBoard();
            Console.Write($"Player {player}, enter your move (1-9): ");
            int move = int.Parse(Console.ReadLine()) - 1;
            if (board[move / 3, move % 3] != 'X' && board[move / 3, move % 3] != 'O') {
                board[move / 3, move % 3] = player;
                player = player == 'X' ? 'O' : 'X';
                turn++;
            } else {
                Console.WriteLine("Invalid move. Try again.");
            }
        }
    }

    static void PrintBoard() {
        for (int i = 0; i < 3; i++) {
            Console.WriteLine($"{board[i, 0]} | {board[i, 1]} | {board[i, 2]}");
        }
    }
}
