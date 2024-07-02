import tkinter as tk

class Grid:
    def __init__(self, root):
        self.root = root
        self.cells = []
        for i in range(10):
            row = []
            for j in range(7):
                cell = tk.Canvas(root, width=50, height=50, bg='white')
                cell.grid(row=i, column=j)
                cell.bind('<Button-1>', self.on_click)
                row.append(cell)
            self.cells.append(row)

    def on_click(self, event):
        cell = event.widget
        if cell['bg'] == 'white':
            cell['bg'] = 'blue'
        else:
            cell['bg'] = 'white'

root = tk.Tk()
grid = Grid(root)
root.mainloop()

