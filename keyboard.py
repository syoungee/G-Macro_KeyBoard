import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QDialog
from PyQt5 import uic, QtCore, QtGui
from collections import defaultdict

macro_list = defaultdict(list)

class ShowDialog(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi('keyboard.ui', self)
        self.btnComplete.clicked.connect(self.btnComplete_onClick)

    def btnComplete_onClick(self, v):
        data = self.plainTextEdit.toPlainText()
        print(data)

        if(self.btnAppend.isChecked()):
            flag = 1 # 한번 누름
        elif (self.btnInsert.isChecked()):
            flag = 2 # 누른 상태
        else:
            print("error!")

        print(flag)
        macro_list[data].append(flag)
        print(macro_list) # dic에 받은 것들 저장
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowDialog()
    window.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

    sys.exit(app.exec_())
