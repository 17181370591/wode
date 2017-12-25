import sys
from PyQt5.QtWidgets import qApp,QAction,QWidget,QApplication,QMessageBox,QPushButton,QMainWindow
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
class ee(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initui()
        
    def initui(self):
        self.setGeometry(111,222,333,444)
        self.setWindowTitle('外窗口')
        p=self.statusBar()
        p.showMessage('ready')
        p.setToolTip('aaa')

        eac=QAction(QIcon(r'C:\Python34\1.jpg'),'&关闭',self)
        eac.setShortcut('ctrl+q')
        eac.setStatusTip('????')
        eac.triggered.connect(qApp.quit)
        ead=QAction('&7',self)
        ead.setShortcut('ctrl+6')
        
        tb=self.addToolBar()

        
        self.setWindowTitle('menub')
        self.setWindowIcon(QIcon(r'c:\python34\1.jpg'))
        self.show()
    def closeEvent(self,event):
        
        reply=QMessageBox.question(self,'Message',
             "Are you sure to quit?",QMessageBox.Yes |
            QMessageBox.No,QMessageBox.No)

        if reply==QMessageBox.Yes:
            #event.accept()
            event.accept()
        else:
            event.ignore()
        
        



app=QApplication(sys.argv)
e=ee()
#w=QWidget()
#w.resize(600,300)
#w.move(600,600)
#w.setWindowTitle('蛋')
#w.show()
sys.exit(app.exec_())
