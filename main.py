from Application import Application
from PyQt6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication([])
    window = Application()
    window.show()
    app.exec()
