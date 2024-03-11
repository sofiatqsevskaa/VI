import random
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
random.seed(0)


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, position):
        self.x, self.y = position


class Game:
    def __init__(self, width, height, state):
        self.width = width
        self.height = height
        self.state = state

    def has_remaining_dots(self):
        return any('.' in row for row in self.state)

    def eat(self, position):
        x, y = position
        if self.state[x][y] != "#":
            self.state[x][y] = "#"

    def successor(self, x, y):
        moves = []
        if x > 0 and self.state[x-1][y] == '.':
            moves.append((x-1, y))
        if x < self.width - 1 and self.state[x+1][y] == '.':
            moves.append((x+1, y))
        if y > 0 and self.state[x][y-1] == '.':
            moves.append((x, y-1))
        if y < self.height - 1 and self.state[x][y+1] == '.':
            moves.append((x, y+1))

        if not moves:
            if x > 0:
                moves.append((x-1, y))
            if x < self.height-1:
                moves.append((x+1, y))
            if y > 0:
                moves.append((x, y-1))
            if y < self.width-1:
                moves.append((x, y+1))
        return moves


class Pacman:
    def __init__(self, width, height, state):
        self.player = Player()
        self.game = Game(width, height, state)

    def play_game(self):
        while self.game.has_remaining_dots():
            moves = self.game.successor(self.player.x, self.player.y)
            next_move = random.choice(moves)
            self.player.move(next_move)
            self.game.eat(next_move)
            print(f"[{self.player.x}, {self.player.y}]")


if __name__ == "__main__":
    width = int(input())
    height = int(input())
    state = []
    for i in range(0, height):
        line = input()
        row = [cell for cell in line]
        state.append(row)

    if state:
        pacman = Pacman(width, height, state)
        pacman.play_game()
