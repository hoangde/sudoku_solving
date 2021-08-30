# -*- coding: utf-8 -*-
"""
Spyder Editor

This is an auto solve sudoku game with backtracking algorithm 

"""

from sudoku_class import Sudoku
import os, time

#Initialize Sudoku board
board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
                                        ]

if __name__ == "__main__":
    #Create instance
    sudoku = Sudoku(board) 
    #Display board
    sudoku.displayBoard()
    
    input("Press Enter to start solving...")
    
    #Get start time
    start_time = time.time()
    
    #Start solving
    sudoku.solveSudoku()
    
    #Calculate total solving time
    solving_time = time.time() - start_time
        
    os.system('cls')
    
    print("--------------------------------")
    print("          SOLVED SUDOKU")
    print("--------------------------------")
       
    sudoku.displayBoard()
    
    print("\nSolving time: " + str(round(solving_time, 2)) + "s")


















