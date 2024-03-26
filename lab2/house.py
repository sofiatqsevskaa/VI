from searching_framework import Problem, astar_search


class House(Problem):
    def __init__(self, initial, allowed):
        super().__init__(initial)
        self.allowed = allowed

    def goal_test(self, state):
        return state[0] == state[1]

    def successor(self, state):
        successors = dict()

        actions = ("Stoj", "Gore 1", "Gore 2", "Gore-desno 1", "Gore-desno 2", "Gore-levo 1", "Gore-levo 2")
        directions = ((0, 0), (0, 1), (0, 2), (1, 1), (2, 2), (-1, 1), (-2, 2))
        for action, direction in zip(actions, directions):
            rez = self.move(state, direction)
            if rez is not None:
                successors[action] = rez

        return successors

    def move(self, state, direction):
        player_move = list(state[0])
        house_move = list(state[1])
        house_direction = int(state[2])
        if house_move[0] == 0 or house_move[0] == 4:
            house_direction *= -1
        house_move[0] += house_direction
        player_move[0] += direction[0]
        player_move[1] += direction[1]
        if player_move[0] < 0 or player_move[0] > 4 or player_move[1] < 0 or player_move[1] > 8:
            return None
        if tuple(player_move) not in self.allowed :
            if player_move != house_move:
                return None
        final_player = tuple(player_move)
        final_house = tuple(house_move)
        final_state = (final_player, final_house, house_direction)
        return final_state

    def h(self, node):
        return ((8-node.state[0][1])/2)-1

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    player = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))
    direction_input = input()
    dir = 1
    if direction_input == "levo":
        dir = -1
    initial = (player,house,dir)
    game = House(initial, allowed)
    result = astar_search(game)
    if result is not None:
        print(result.solution())
    else:
        print("No solution found")