import tkinter as tk

import source.gui.game_window as gui


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Крестики-нолики")
    game_window = gui.GameWindow(root, 3)

    root.mainloop()
