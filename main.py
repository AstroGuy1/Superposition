# main.py
import sys
from PyQt5.QtWidgets import QApplication
from gui import QuantumApp

def main():
    app = QApplication(sys.argv)
    quantum_app = QuantumApp()
    quantum_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
