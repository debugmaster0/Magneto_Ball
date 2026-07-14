import sys
from PySide6.QtWidgets import QApplication
from src.game import GameWindow

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(True) 
window = GameWindow()
window.show()

sys.exit(app.exec())