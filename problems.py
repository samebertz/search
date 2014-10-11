from utils import *
from search import *
import math, random, sys, time, bisect, string

class sudoku(Problem):
    def __init__(self, initial, N):
        self.initial = initial
        print_table(initial)
        self.N = N
    def actions(self, state):
        pos = self.get_empty(state)
        if pos is None:
            return []
        else:
            return [n for n in range(1, self.N + 1) if not self.conflicted(state, pos, n)]
    def result(self, state, n):
        pos = self.get_empty(state)
        new = [row[:] for row in state]
        new[pos[0]][pos[1]] = n
        print_table(state)
        print_table(new)
        return new
    def conflicted(self, state, pos, n):
        return (self.conflict_box(state, pos, n)
                or any(n == state[pos[0]][i] for i in range(self.N))
                or any(n == state[i][pos[1]] for i in range(self.N)))
    def conflict_box(self, state, pos, n):
        box_size = int(math.sqrt(self.N))
        box = [int(pos[0] / box_size), int(pos[1] / box_size)]
        "print 'testing {},{} : {} for box conflicts'.format(pos[0], pos[1], n)"
        for i in range(box_size):
            for j in range(box_size):
                if n == state[box[0] * box_size + i][box[1] * box_size + j]:
                    return True
        return False
        "return any(n == state[box[0] * box_size + i][box[1] * box_size + j] for j in range(box_size) for i in range(box_size))"
    def get_empty(self, state):
        for i in range(self.N):
            for j in range(self.N):
                if state[i][j] is None:
                    return [i, j]
        return None
    def goal_test(self, state):
        for i in range(self.N):
            for j in range(self.N):
                if state[i][j] is None:
                    return False
        return True

