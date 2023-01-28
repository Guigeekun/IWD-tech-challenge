
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QFileDialog, QDialog, QStackedWidget
from PyQt5.uic import loadUi
from crud.storyCrud import handle_stories


class Window(QDialog):
    def __init__(self, url: str, global_headers: dict, workflow_name: str, default_path: str):
        self.url = url
        self.global_headers = global_headers
        self.workflow_name = workflow_name
        super(Window, self).__init__()
        # Loading ui from ui.xml
        loadUi("ui/ui.xml", self)
        self.filename.setText(default_path)
        # Assigning function to "browse" button
        self.browse.clicked.connect(self.browsefiles)
        # Assigning function to "process" button
        self.process.clicked.connect(self.processFile)

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', '/', 'CSV (*.csv)')
        self.filename.setText(fname[0])

    def processFile(self):
        handle_stories(self.url, self.global_headers, self.workflow_name, self.filename.text())
        self.processingLabel.setText('Done !')


def init_ui(url: str, global_headers: dict, workflow_name: str, default_path: str):
    # Creating app
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    widget.addWidget(Window(url, global_headers, workflow_name, default_path))
    widget.setFixedWidth(400)
    widget.setFixedHeight(100)
    widget.show()
    sys.exit(app.exec_())
