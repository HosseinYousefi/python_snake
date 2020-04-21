from shared import Shared
from tkinter import *
import random

class Snake:
    def __init__(self, length):
        self.length = length
        self.body = []
        self.is_increasing = False
        for i in range(self.length): # Head is self.body[0]
            self.body.append(SnakeBody(Shared.N // 2, Shared.M // 2 + i, '#000000' if i != 0 else '#FF0000'))

    def draw(self, canvas):
        for body in self.body:
            body.draw(canvas)
    
    def move(self, direction):
        for i in reversed(range(1, self.length)):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        if direction == 'Up':
            self.body[0].y -= 1
        elif direction == 'Down':
            self.body[0].y += 1
        elif direction == 'Left':
            self.body[0].x -= 1
        elif direction == 'Right':
            self.body[0].x += 1
        if self.is_increasing:
            self.length += 1
        self.is_increasing = False
    
    def eat(self):
        self.body.append(SnakeBody(self.body[-1].x, self.body[-1].y, self.body[-1].color))
        self.is_increasing = True

    def check_collision(self, mouse):
        if mouse.x == self.body[0].x and mouse.y == self.body[0].y:
            self.eat()
            mouse.update()



class Cell:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.oval = None
        self.color = color

    def draw(self, canvas: Canvas):
        if self.oval != None:
            canvas.delete(self.oval)
        self.oval = canvas.create_oval((self.x * Shared.CELL_WIDTH, self.y * Shared.CELL_HEIGHT,
                                        (self.x + 1) * Shared.CELL_WIDTH, (self.y + 1) * Shared.CELL_HEIGHT),
                                       fill=self.color)


class SnakeBody(Cell):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)


class Mouse(Cell):
    def __init__(self):
        x = random.randint(0, Shared.N - 1)
        y = random.randint(0, Shared.M - 1)
        super().__init__(x, y, '#FFFF00')
    
    def update(self):
        self.x = random.randint(0, Shared.N - 1)
        self.y = random.randint(0, Shared.M - 1)
        