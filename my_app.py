from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QRadioButton, QListWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox
from instr import*
from second_win import TestWin
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction  = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment=Qt.AlignLeft )
        self.layout_line.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
    def connects(self):
        self.button.clicked.connect(self.next_click)
        
app = QApplication([])
mw = MainWin()
app.exec_()



