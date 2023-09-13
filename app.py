from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QLineEdit, QPushButton, QWidget, QVBoxLayout, QDialog, QWidgetAction
from PyQt6.QtGui import QIcon, QKeySequence, QAction

from PyQt6.QtCore import Qt
import webbrowser
import sys

def go_to_job():
    job_id = text_field.text()
    url = f"https://waterlooworks.uwaterloo.ca/myAccount/co-op/coop-postings.htm?ck_jobid={job_id}"
    webbrowser.open_new_tab(url)

class MyLineEdit(QLineEdit):
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:
            go_to_job()
        else:
            super().keyPressEvent(event)

def show_dialog():
    dialog = QDialog()
    layout = QVBoxLayout()
    
    global text_field
    text_field = MyLineEdit()
    text_field.setPlaceholderText("Enter Job ID")
    
    button = QPushButton("Go")
    button.clicked.connect(go_to_job)
    
    layout.addWidget(text_field)
    layout.addWidget(button)
    
    dialog.setLayout(layout)
    dialog.exec()

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("icon.png")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

# Add action to show dialog
show_action = QAction("Show")
show_action.triggered.connect(show_dialog)
menu.addAction(show_action)

# Add a Quit option to the menu, also set the shortcut
quit_action = QAction("Quit", menu, shortcut=QKeySequence.StandardKey.Quit)
quit_action.triggered.connect(app.quit)
menu.addAction(quit_action)

# Add the menu to the tray
tray.setContextMenu(menu)

app.exec()
