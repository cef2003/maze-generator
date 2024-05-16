from random import *
import turtle


class Maze:
    t = turtle.Turtle()
    a = []

    def __init__(self, m, n):
        self.m = m
        self.n = n
        for i in range(0, m*n):
            self.a.append(-1)

    def find(self, x):
        while self.a[x] > 0:
            x = self.a[x]
        return x

    def union(self, a, b):
        i = self.find(a)
        j = self.find(b)
        if i != j:
            if self.a[i] <= self.a[j]:
                # self.a[j] = i
                self.a[i] = self.a[i] + self.a[j]
                self.a[j] = i
            # elif self.a[j] < self.a[i]:
            #     self.a[i] = j
            else:
                # self.a[j] = i
                # self.a[i] -= 1
                self.a[j] = self.a[j] + self.a[i]
                self.a[i] = j

    # method to draw a line from (x1,y1) to (x2,y2)
    def draw(self, x1, y1, x2, y2):
        self.t.penup()
        self.t.goto((x1, y1))
        self.t.pendown()
        self.t.goto((x2, y2))

    # method to draw the border of the maze
    def draw_maze_border(self):
        self.draw(0, 0, self.n*20, 0)
        self.draw(self.n*20, 20, self.n*20, self.m*20)
        self.draw(self.n*20, self.m*20, 0, self.m*20)
        self.draw(0, (self.m - 1)*20, 0, 0)
        screen = self.t.getscreen()
        screen.mainloop()

    def draw_maze(self, l):
        for i in range(0, len(l)):
            j = l[i]
            if j[1] == j[0] + 1:
                self.draw((j[1] % self.n) * 20, (self.m - (j[1]//self.m)) * 20, (j[1] % self.n) * 20,
                          ((self.m - (j[1]//self.m) - 1) * 20))
            else:
                self.draw((j[0] % self.n) * 20, ((self.m - (j[1] // self.m) - 1) * 20), (j[0] % self.n + 1) * 20,
                          ((self.m - (j[1] // self.m) - 1) * 20))
        self.draw(0, 0, self.n * 20, 0)
        self.draw(self.n * 20, 20, self.n * 20, self.m * 20)
        self.draw(self.n * 20, self.m * 20, 0, self.m * 20)
        self.draw(0, (self.m - 1) * 20, 0, 0)
        screen = self.t.getscreen()
        screen.mainloop()


# method that returns a list of possible unions, for example [[0,1],[0,5],[1,2],...]
# based on this method we will use the returned list in the draw_maze method
def possible_unions(m, n):
    l = []
    for i in range(0, m*n):
        right, bottom = True, True
        # last element in a row
        if (i+1) % n == 0:
            right = False
        # last row
        if i in range(m*n-n, m*n):
            bottom = False
        # if there is a possible union to the right,
        # we append the list with the element with its adjacent element to the right (i+1)
        if right:
            l.append([i, i+1])
        # if there is a possible union to the bottom,
        # we append the list with the element with its adjacent element to the bottom (i+n)
        if bottom:
            l.append([i, i + n])
    return l


# create a maze of size rows * cols
rows = 10
cols = 10
maze = Maze(rows, cols)
# get the list of possible unions
union_options = possible_unions(rows, cols)

# generate random int every time and make a union between
# two pairs from the union_options list
while maze.find(0) != maze.find(rows * cols - 1):
    if len(union_options) == 0:
        break
    rand = randint(0, len(union_options) - 1)
    maze.union(union_options[rand][0], union_options[rand][1])
    # for example the random chosen integer is 0, so it's the pair [0,1],
    # we perform a union between 0 and 1 then we remove the pair from the list using pop method
    union_options.pop(rand)

maze.draw_maze(union_options)

