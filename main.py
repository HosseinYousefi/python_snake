from tkinter import *
from shared import *
from snake import *
import time

class SnakeGame(Tk):
    def __init__(self):
        super().__init__()
        self.title('Snake Game')
        self.game_screen = GameScreen(self, Shared.WIDTH, Shared.HEIGHT)
        self.game_screen.grid(row=0, column=0, sticky=(N, S, E, W))
        self.menu_screen = MenuScreen(self, Shared.WIDTH, Shared.HEIGHT)
        self.menu_screen.grid(row=0, column=0, sticky=(N, S, E, W))
        
    def play(self):
        print('play button has been clicked')
        self.game_screen.tkraise()
        self.game_screen.game_loop()
        pass

class MenuScreen(Frame):
    def __init__(self, master, width, height):
        super().__init__(master, bg="#FF0000", width=width, height=height)
        self.pack_propagate(0)
        self.grid_propagate(0)
        self.master = master
        self.play_button = Button(self, text='Play', command=self.master.play)
        self.play_button.pack()
    
class GameScreen(Frame):
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height, bg="#0000FF")
        self.canvas = Canvas(self, bg="#0000FF", width=width, height=height)
        self.canvas.pack()
        self.snake = Snake(3)
        self.snake.draw(self.canvas)
        self.mouse = Mouse()
        self.mouse.draw(self.canvas)
        self.direction = 'Up'
        self.canvas.bind('<a>', lambda e: self.change_direction('Left'))
        self.canvas.bind('<s>', lambda e: self.change_direction('Down'))
        self.canvas.bind('<d>', lambda e: self.change_direction('Right'))
        self.canvas.bind('<w>', lambda e: self.change_direction('Up'))

        self.canvas.bind('<Left>', lambda e: self.change_direction('Left'))
        self.canvas.bind('<Down>', lambda e: self.change_direction('Down'))
        self.canvas.bind('<Right>', lambda e: self.change_direction('Right'))
        self.canvas.bind('<Up>', lambda e: self.change_direction('Up'))

        self.canvas.focus_set()
    
    def change_direction(self, d):
        if self.direction == 'Left' and d != 'Right':
            self.direction = d
        if self.direction == 'Right' and d != 'Left':
            self.direction = d
        if self.direction == 'Up' and d != 'Down':
            self.direction = d
        if self.direction == 'Down' and d != 'Up':
            self.direction = d
        
    def game_loop(self):
        self.snake.move(self.direction)
        self.snake.draw(self.canvas)
        self.snake.check_collision(self.mouse)
        self.mouse.draw(self.canvas)
        self.after(100, func=self.game_loop)



if __name__ == '__main__':
    app = SnakeGame()
    app.mainloop()