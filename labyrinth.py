import sys


# Knoten im Suchbaum
class Knoten:
    def __init__(self, zustand, parent=None, action=None):
        self.zustand = zustand
        self.parent = parent
        self.action = action


# Stack → Tiefensuche (DFS)
class StackGrenze:
    def __init__(self):
        self.grenze = []

    def add(self, knoten):
        self.grenze.append(knoten)

    def __contains__(self, zustand):
        return any(k.zustand == zustand for k in self.grenze)

    def empty(self):
        return len(self.grenze) == 0

    def remove(self):
        if self.empty():
            raise Exception("Leere Grenze")
        return self.grenze.pop()   # einfacher


# Queue → Breitensuche (BFS)
class QueueGrenze(StackGrenze):
    def remove(self):
        if self.empty():
            raise Exception("Leere Grenze")
        return self.grenze.pop(0)


class Labyrinth:
    def __init__(self, filename):

        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1 or contents.count("B") != 1:
            raise Exception("Labyrinth braucht genau A und B")

        lines = contents.splitlines()
        self.height = len(lines)
        self.width = max(len(line) for line in lines)

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    cell = lines[i][j]
                except IndexError:
                    cell = " "

                if cell == "A":
                    self.start = (i, j)
                    row.append(False)
                elif cell == "B":
                    self.goal = (i, j)
                    row.append(False)
                elif cell == " ":
                    row.append(False)
                else:
                    row.append(True)

            self.walls.append(row)

        self.solution = None


    def print(self):
        path = self.solution[1] if self.solution else []
        for i in range(self.height):
            for j in range(self.width):
                if self.walls[i][j]:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif (i, j) in path:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()


    def nachbarn(self, zustand):
        row, col = zustand
        moves = [
            ("oben", (row - 1, col)),
            ("unten", (row + 1, col)),
            ("links", (row, col - 1)),
            ("rechts", (row, col + 1))
        ]

        result = []
        for action, (r, c) in moves:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result


    def solve(self, bfs=False):

        start = Knoten(self.start)
        grenze = QueueGrenze() if bfs else StackGrenze()
        grenze.add(start)

        explored = set()
        self.num_explored = 0

        while not grenze.empty():

            knoten = grenze.remove()
            self.num_explored += 1

            if knoten.zustand == self.goal:
                self.reconstruct(knoten)
                return

            explored.add(knoten.zustand)

            for action, state in self.nachbarn(knoten.zustand):
                if state not in explored and state not in grenze:
                    grenze.add(Knoten(state, knoten, action))

        raise Exception("Keine Lösung")


    def reconstruct(self, knoten):
        actions, cells = [], []
        while knoten.parent:
            actions.append(knoten.action)
            cells.append(knoten.zustand)
            knoten = knoten.parent

        self.solution = (actions[::-1], cells[::-1])


# -------- Start --------

if len(sys.argv) != 2:
    sys.exit("Usage: python labyrinth.py labyrinth.txt")

l = Labyrinth(sys.argv[1])
print("Labyrinth:")
l.print()

print("Löse...")
l.solve(bfs=True)   # BFS = kürzester Weg

print("Zustände untersucht:", l.num_explored)
print("Lösung:")
l.print()
