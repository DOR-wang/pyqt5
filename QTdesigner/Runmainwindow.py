import sys
import mainwindow
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindowl = QMainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(mainwindowl)
    mainwindowl.show()
    sys.exit(app.exec_())
