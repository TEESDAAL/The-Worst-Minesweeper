##
# minesweeper.py

import itertools
from grid import Grid
from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QMainWindow,
    QApplication,
    QLabel,
    QPushButton,
    QStackedWidget,
)
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("MineSweeper :)")
        self.layout: QGridLayout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)

        self.main_widget: QWidget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
        self.grid = Grid(10, 10)
        size: int = self.grid.grid_size
        for row in range(size):
            widgets_grid.append([])
            for col in range(size):
                cell = Cell(row, col, self.grid.grid)

                widgets_grid[row].append(cell)
                self.layout.addWidget(cell.stacked_cell, row, col)

        self.setFixedSize(20 * (size) + 18, 20 * (size) + 18)


class Cell:
    def __init__(self, row, col, grid):
        self.row: int = row
        self.col: int = col
        self.stacked_cell: QStackedWidget = QStackedWidget()
        self.cell: QPushButton = QPushButton(" ")
        self.cell.setFixedSize(20, 20)
        self.value = grid[row][col]
        self.stacked_cell.addWidget(self.cell)
        self.stacked_cell.addWidget(QLabel(f" {str(self.value)} "))
        self.cell.clicked.connect(lambda: self.show_value())
        self.value_shown: bool = False

    def show_value(self):
        if self.value_shown:
            return
        if self.cell.text() == "🚩":
            self.value_shown = True
            self.stacked_cell.setCurrentIndex(1)
            if self.value == 0:
                self.check_neighbors()
        else:
            self.cell.setText("🚩")

    def check_neighbors(self):
        for row in (-1, 0, 1):
            for col in (-1, 0, 1):
                if (row, col) == (0, 0):
                    continue
                if (
                    max(self.row + row, self.col + col)
                    > window.grid.grid_size - 1
                    or min(self.row + row, self.col + col) < 0
                ):
                    continue
                if widgets_grid[self.row + row][self.col + col].value_shown:
                    continue
                widgets_grid[self.row + row][self.col + col].show_value()
                widgets_grid[self.row + row][self.col + col].show_value()
                widgets_grid[self.row + row][self.col + col].value_shown = True


grid: Grid = Grid(10, 10)
widgets_grid: list[Cell] = []


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)

    window: MainWindow = MainWindow()
    window.show()
    window.resize(640, 480)
    app.exec()
