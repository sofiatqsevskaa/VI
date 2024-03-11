from searching_framework import Problem, breadth_first_graph_search


class Explorer(Problem):
    def __init__(self, person, house):
        super().__init__((person, (2, 5, -1), (5, 0, +1)))
        self.house = house
        self.rows = 6
        self.cols = 8

    def goal_test(self, state):
        person = state[0]
        return person == house

    def successor(self, state):
        neighbors = dict()

        actions = ("Right", "Left", "Up", "Down")
        directions = ((+1, 0), (-1, 0), (0, +1), (0, -1))
        for action, direction in zip(actions, directions):
            rez = self.move(state, direction)
            if rez is not None:
                neighbors[action] = rez

        return neighbors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def move(self, state, direction):
        person = self.move_person_dir(state[0], direction)
        block1 = self.move_block(state[1])
        block2 = self.move_block(state[2])

        new_state = (person, block1, block2)

        if self.is_valid_state(new_state):
            return new_state
        else:
            return None

    def move_person_dir(self, person, direction):
        "direction is tuple: (amount_move_x, amount_move_y)"
        person = list(person)
        person[0] += direction[0]
        person[1] += direction[1]
        return tuple(person)

    def move_block(self, block):
        x, y, n = block
        y += n
        if y < 0 or y >= self.rows:
            n *= -1
            y += 2 * n
        return (x, y, n)

    def is_valid_state(self, state):
        person, block1, block2 = state
        px, py = person
        return 0 <= px < self.cols and \
            0 <= py < self.rows and \
            person != block1[:2] and person != block2[:2]


""" example:
0 2
7 4
"""
if __name__ == '__main__':

    person = tuple(map(int, input().split()))
    house = tuple(map(int, input().split()))
    problem = Explorer(person, house)
    node = breadth_first_graph_search(problem)
    if node is not None:
        print(node.solution())
        print(node.solve())
        print(node.path())
    else:
        print("Nema Resenie")