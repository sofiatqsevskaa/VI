from searching_framework import Problem, astar_search


class Labyrinth(Problem):
    def __init__(self, initial, walls, size):
        super().__init__(initial)
        self.walls = walls
        self.size = size

    def goal_test(self, state):
        return state[0] == state[1]

    def successor(self, state):
        successors = dict()

        actions = ("Desno 2", "Desno 3", "Levo", "Gore", "Dolu")
        directions = ((2, 0), (3, 0), (-1, 0), (0, 1), (0, -1))

        for action, direction in zip(actions, directions):
            rez = self.move(state, direction)
            if rez is not None:
                successors[action] = rez

        return successors

    def move(self, state, direction):
        move_player = list(state[0])
        move_player[1] += direction[1]
        if move_player[1] < 0 or move_player[1] >= self.size:
            return None
        if direction[0] > 0:
            for i in range(direction[0]):
                move_player[0] += 1
                if tuple(move_player) in self.walls:
                    return None

        if direction[0] < 0:
            move_player[0] += direction[0]
        if move_player[0] < 0 or move_player[0] >= self.size:
            return None
        if tuple(move_player) in self.walls:
            return None
        final_player = tuple(move_player)
        final_state = (final_player, state[1])
        return tuple(final_state)

    def h(self, node):
        x1, y1 = node.state[0]
        x2, y2 = node.state[1]
        return (abs(x1 - x2) + abs(y1 - y2)) / 3

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    n = int(input())
    num_walls = int(input())
    walls_ = tuple(tuple(map(int, input().split(","))) for _ in range(num_walls))
    player = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))

    initial_state = (player, house)
    problem = Labyrinth(initial_state, walls_, n)

    game = astar_search(problem)
    if game is not None:
        print(game.solution())
    else:
        print("No solution found")
