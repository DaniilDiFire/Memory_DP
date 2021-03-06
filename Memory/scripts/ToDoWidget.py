import os
from scripts import path
from scripts.Dialog import Dialog

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap


class ToDoWidget(QWidget):
    def __init__(self, task, MainWindow, parent=None):
        super(QWidget, self).__init__(parent)
        self.MainWindow = MainWindow
        self.is_created = False
        self.status_changed = False
        self.pics = {
            0: QPixmap(os.path.join(path, "image", "progress.png")),
            1: QPixmap(os.path.join(path, "image", "yes.png")),
            2: QPixmap(os.path.join(path, "image", "runTime.png")),
        }
        self.task = task
        self.HBoxLayout = QHBoxLayout()

        self.status_icon = QLabel()
        self.status_icon.setMinimumSize(50, 50)
        self.status_icon.setMaximumSize(50, 50)
        self.HBoxLayout.addWidget(self.status_icon, 0)

        self.name = QLabel(self)
        self.HBoxLayout.addWidget(self.name, 1)

        self.is_imp = QLabel(self)
        self.HBoxLayout.addWidget(self.is_imp, 2)

        self.display()

        self.edit_btn = QPushButton(self, text="Изменить")
        self.edit_btn.setMaximumSize(70, 20)
        self.HBoxLayout.addWidget(self.edit_btn, 3)
        self.edit_btn.clicked.connect(self.new_dialog)

        self.setLayout(self.HBoxLayout)
    
    def new_dialog(self):
        new_message = Dialog(self)
        new_message.exec_()

    def display(self):
        self.status_icon.setPixmap(self.pics[self.task.status_id])
        if len(self.task.name) > 30:
            self.name.setText(self.task.name[:27] + "...")
        else:
            self.name.setText(self.task.name)
        self.is_imp.setText("Важное" if self.task.is_imp == 1 else "")
        if self.status_changed:
            print(self.MainWindow)
            self.MainWindow.customize_table()

