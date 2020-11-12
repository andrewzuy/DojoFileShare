from PyQt5 import QtWidgets, QtCore
from window import Ui_MainWindow
from NetworkUtil import get_interfaces_addresses
from server import flask_app
import sys
from threading import Thread



class DojoShare(QtWidgets.QMainWindow):
    def __init__(self):
        super(DojoShare, self).__init__()
        netList = get_interfaces_addresses()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(netList)
        self.ui.pushButton.clicked.connect(self.buttonClicked)
        self.server_thread = Thread(target=self.start_server)

    def start_server(self):
        flask_app.run(debug=False, port=80, host=self.ui.comboBox.currentText())
        
    def buttonClicked(self):
        self.server_thread.start()
        self.ui.pushButton.setText("Sarvar started")
        self.ui.pushButton.setEnabled(False)
        self.ui.comboBox.setEnabled(False)
        self.ui.label_2.setText("<a href='http://"+self.ui.comboBox.currentText()+"'>http://"+self.ui.comboBox.currentText()+"</a>")
        self.ui.label_2.setOpenExternalLinks(True)
        
    def closeEvent(self, closedEvent):
        self.server_thread._stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = DojoShare()
    application.show()
    sys.exit(app.exec())
