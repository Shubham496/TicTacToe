# Import libraries
import tkinter as tk

# root window
root = tk.Tk()
root.title("TicTacToe")
root.iconbitmap('tic-tac-toe.ico')
root.geometry("400x400")
root.resizable(False, False)    

# create items 
header = "Hello everyone lets start the game"
firstLable = tk.Label(text=header)
firstLable.place(x=(400/2)-len(header)*4//2, y=10)

# place items

root.mainloop()