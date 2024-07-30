import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Hangman Game')
        
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()
        
        self.word_to_guess = self.choose_word()
        self.guessed_letters = []
        self.tries_left = 6
        
        self.draw_board()
        self.draw_word()
        self.draw_hangman()
        self.draw_keyboard()
    
    def choose_word(self):
        words = ['apple', 'banana', 'orange', 'coconut', 'strawberry', 'lime', 'grapefruit', 'lemon', 'kumquat', 'blueberry', 'melon']
        return random.choice(words)
    
    def draw_board(self):
        self.canvas.create_line(150, 350, 450, 350, width=5)  # base
        self.canvas.create_line(300, 350, 300, 100, width=5)  # vertical pole
        self.canvas.create_line(300, 100, 400, 100, width=5)  # horizontal pole
    
    def draw_word(self):
        display_word = ''.join(letter if letter in self.guessed_letters else '_' for letter in self.word_to_guess)
        self.canvas.create_text(300, 380, text=display_word, font=('Arial', 24))
    
    def draw_hangman(self):
        if self.tries_left < 6:
            parts = ['head', 'body', 'left_arm', 'right_arm', 'left_leg', 'right_leg']
            draw_functions = [self.draw_head, self.draw_body, self.draw_left_arm, self.draw_right_arm, self.draw_left_leg, self.draw_right_leg]
            for i in range(6 - self.tries_left):
                draw_functions[i]()
    
    def draw_head(self):
        self.canvas.create_oval(380, 140, 420, 180, width=3)  # head
    
    def draw_body(self):
        self.canvas.create_line(400, 180, 400, 280, width=3)  # body
    
    def draw_left_arm(self):
        self.canvas.create_line(400, 200, 370, 230, width=3)  # left arm
    
    def draw_right_arm(self):
        self.canvas.create_line(400, 200, 430, 230, width=3)  # right arm
    
    def draw_left_leg(self):
        self.canvas.create_line(400, 280, 370, 310, width=3)  # left leg
    
    def draw_right_leg(self):
        self.canvas.create_line(400, 280, 430, 310, width=3)  # right leg
    
    def draw_keyboard(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for idx, letter in enumerate(alphabet):
            row = idx // 7
            col = idx % 7
            button = tk.Button(self.root, text=letter, width=3, command=lambda l=letter: self.check_letter(l))
            button.place(x=100 + col * 50, y=50 + row * 50)
    
    def check_letter(self, letter):
        self.guessed_letters.append(letter)
        if letter not in self.word_to_guess:
            self.tries_left -= 1
            self.draw_hangman()
        self.draw_word()
        self.check_game_status()
    
    def check_game_status(self):
        if all(letter in self.guessed_letters for letter in self.word_to_guess):
            messagebox.showinfo('Hangman Game', 'Congratulations! You guessed the word!')
            self.root.destroy()
        elif self.tries_left == 0:
            messagebox.showinfo('Hangman Game', f'Game Over! The word was "{self.word_to_guess}".')
            self.root.destroy()

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == '__main__':
    main()

