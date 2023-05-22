import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Modern Calculator")
        self.setMinimumSize(600, 800)
        self.setMaximumSize(600, 800)
        self.setStyleSheet("""
            QWidget {
                background-color: #333;
            }
            QPushButton {
                border: 2px solid #555;
                border-radius: 10px;
                color: #FFF;
                font-size: 35px;
                height: 100px;
                width: 100px;
                margin: 5px;
            }
            QPushButton:pressed {
                background-color: #555;
            }
            QLineEdit {
                border: 2px solid #555;
                border-radius: 10px;
                color: #333;
                font-size: 50px;
                padding: 5px;
                background-color: #CCCCCC;
                height: 100px;
            }
        """)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.grid = QGridLayout()
        
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.grid.addWidget(self.display, 0, 0, 1, 4)

        self.clear_button = QPushButton('Clear')
        self.clear_button.setStyleSheet("background-color: #FF6347")
        self.grid.addWidget(self.clear_button, 1, 0, 1, 3)  
        self.clear_button.clicked.connect(self.clear_display)

        self.backspace_button = QPushButton('<-')
        self.backspace_button.setStyleSheet("background-color: #FF6347")
        self.grid.addWidget(self.backspace_button, 1, 3)  
        self.backspace_button.clicked.connect(self.backspace)

        self.buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-')
        ]

        for i, button_row in enumerate(self.buttons):
            for j, text in enumerate(button_row):
                button = QPushButton(text)
                if text in ['/', '*', '-', '+']:
                    button.setStyleSheet("background-color: #808080")
                self.grid.addWidget(button, i + 2, j)
                button.clicked.connect(self.button_clicked)

        dot_button = QPushButton('.')
        dot_button.setStyleSheet("background-color: #CCCCCC; color: #333")
        self.grid.addWidget(dot_button, 5, 0)
        dot_button.clicked.connect(self.button_clicked)

        zero_button = QPushButton('0')
        self.grid.addWidget(zero_button, 5, 1)
        zero_button.clicked.connect(self.button_clicked)

        plus_button = QPushButton('+')
        plus_button.setStyleSheet("background-color: #808080")
        self.grid.addWidget(plus_button, 5, 3)
        plus_button.clicked.connect(self.button_clicked)

        equal_button = QPushButton('=')
        equal_button.setStyleSheet("background-color: #32CD32")
        self.grid.addWidget(equal_button, 5, 2)
        equal_button.clicked.connect(self.calculate_result)

        self.main_widget.setLayout(self.grid)

    def button_clicked(self):
        sender = self.sender()
        new_text = self.display.text() + sender.text()
        self.display.setText(new_text)

    def calculate_result(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except Exception:
            self.display.setText("Error")

    def clear_display(self):
        self.display.clear()

    def backspace(self):
        text = self.display.text()[:-1]
        self.display.setText(text)

def main():
    app = QApplication(sys.argv)
    win = CalculatorApp()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
