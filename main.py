import sys
from Pyside6.QtWidgets import QApplicatoin
from src.game import GameWindow

app = QApplication(sys.arv)
app.setQuitOnLastWindowClosed(True) 
window = GameWindow()
window.show

sys.exit(app.exec())