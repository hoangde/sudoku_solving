# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 16:09:41 2021

@author: Hoang De
"""

import os, time

class Sudoku:
    def __init__(self, board):
        self._board = board
        self._display_progress = True
        
    def displayBoard(self):
        for i in range(len(self._board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")
    
            for j in range(len(self._board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
    
                if j == 8:
                    print(self._board[i][j])
                else:
                    print(str(self._board[i][j]) + " ", end="")
            
    def isCellValid(self, value, position):
        #Check row valid
        for col in range(0, len(self._board[0])):
            if self._board[position[0]][col] == value and position[1] != col:
                return False
            
        #Check column valid
        for row in range(0, len(self._board[0])):
            if self._board[row][position[1]] == value and position[0] != row:
                return False
            
        #Check box valid
        cur_box_row = position[1] // 3
        cur_box_col = position[0] // 3
        
        for row in range(cur_box_col*3, cur_box_col*3 + 3):
            for col in range(cur_box_row*3, cur_box_row*3 + 3):
                if self._board[row][col] == value and (row, col) != position:
                    return False
        
        return True
        
         
    def findEmptyCell(self):
        for row in range(0, len(self._board)):
            for col in range(0, len(self._board[row])):
                if self._board[row][col] == 0:
                    return row, col
                
        return None
        
    
    def solveSudoku(self):
        cur_cell = self.findEmptyCell()
        if cur_cell == None:
            return True
        else:
            row, col = cur_cell
            
        if self._display_progress:
            time.sleep(0.1)
            os.system('cls')
            print("--------------------------------")
            print("          SOLVING SUDOKU")
            print("--------------------------------")
            self.displayBoard()
        
        for value in range(1,10):
            if self.isCellValid(value, (row, col)):
                self._board[row][col] = value
                               
                if self.solveSudoku():
                    return True
        
                self._board[row][col] = 0

        return False
        
                    
        
        