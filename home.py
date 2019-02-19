# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from app_back import backend
import sqlite3
proj = backend()

class Ui_Pass(object):
    def setupUi(self,Pass):
        Pass.resize(357, 166)
        self.pushButton = QtGui.QPushButton(Pass)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 80, 25))
        self.label = QtGui.QLabel(Pass)
        self.label.setGeometry(QtCore.QRect(30, 30, 211, 17))
        self.lineEdit = QtGui.QLineEdit(Pass)
        self.lineEdit.setGeometry(QtCore.QRect(60, 70, 171, 25))
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.pushButton.clicked.connect(self.btn)
        self.retranslateUi(Pass)
        QtCore.QMetaObject.connectSlotsByName(Pass)

    def retranslateUi(self, Pass):
        Pass.setWindowTitle("Password")
        self.pushButton.setText("Save")
        self.label.setText("Enter your Sudo Password")

    def btn(self):
        proj.passwrd = self.lineEdit.text()
        self.close()
        ui.setupUi(MainWindow)
        MainWindow.show()


class Pass(QtGui.QDialog, Ui_Pass):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)
        self.setupUi(self)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(245, 307)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.Installbtn)
        self.pushButton_2.clicked.connect(self.Uninstallbtn)
        self.pushButton_3.clicked.connect(self.Updatebtn)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Installbtn(self):
        self.ui = Ui_Aur_Search_window()
        self.ui.setupUi(MainWindow)
        MainWindow.show()

    def Uninstallbtn(self):
        self.ui = Ui_Uninstall()
        self.ui.setupUi(MainWindow)
        MainWindow.show()

    def Updatebtn(self):
        self.ui = Ui_Update()
        self.ui.setupUi(MainWindow)
        MainWindow.show()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
        self.pushButton.setText("Search and Install")
        self.pushButton_2.setText("View/Uninstall")
        self.pushButton_3.setText("Update")

class Ui_Aur_Search_window(object):
    def setupUi(self, Aur_Search_window):
        Aur_Search_window.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Aur_Search_window)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.Search_button = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.Search_button, 0, 2, 1, 1)
        self.Cancel_button = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.Cancel_button, 1, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        Aur_Search_window.setCentralWidget(self.centralwidget)
        self.Search_button.clicked.connect(self.Installbtn)
        self.Cancel_button.clicked.connect(self.Cancelbtn)
        self.retranslateUi(Aur_Search_window)
        QtCore.QMetaObject.connectSlotsByName(Aur_Search_window)

    def retranslateUi(self, Aur_Search_window):
        Aur_Search_window.setWindowTitle("MainWindow")
        self.Search_button.setText("Search")
        self.Cancel_button.setText("Back")
        self.label.setText("Enter Package Name :")
    
    def Installbtn(self):
        aurlist = proj.aur_search(self.lineEdit.text())
        paclist = proj.pacsearch(self.lineEdit.text())
        self.ui = Ui_Install()
        self.ui.setupUi(MainWindow)
        MainWindow.show()

    def Cancelbtn(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()

class Ui_Install(object):
    def setupUi(self, Install):
        Install.resize(848, 618)
        self.centralwidget = QtGui.QWidget(Install)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(4)

        conn = sqlite3.connect('aur_search.db')
        c = conn.cursor()
        c.execute("SELECT Name, Description,Version FROM searchdata")
        data=c.fetchall()
        c.execute("SELECT count(*) FROM searchdata")
        r = c.fetchone()[0]

        conn1 = sqlite3.connect('pac_search.db')
        c1 = conn1.cursor()
        c1.execute("SELECT * FROM searchdata")
        data1=c1.fetchall()
        c1.execute("SELECT count(*) FROM searchdata")
        r1 = c1.fetchone()[0]
        
        self.tableWidget.setRowCount(r+r1)


        for i in range(0,r):
            item = QtGui.QTableWidgetItem()
            item.setText("AUR")
            self.tableWidget.setItem(i, 0, item)
            item = QtGui.QTableWidgetItem()
            item.setText(unicode(data[i][0]))
            self.tableWidget.setItem(i, 1, item)
            item = QtGui.QTableWidgetItem()
            item.setText(unicode(data[i][2]))
            self.tableWidget.setItem(i, 2, item)
            item = QtGui.QTableWidgetItem()
            item.setText(unicode(data[i][1]))
            self.tableWidget.setItem(i, 3, item)
            if r==i:
                break
            else:
                i+=1
        for i in range(0,r1):
            item = QtGui.QTableWidgetItem()
            item.setText(unicode(data1[i][0]))
            self.tableWidget.setItem(r, 0, item)
            item = QtGui.QTableWidgetItem()
            item.setText(unicode(data1[i][1]))
            self.tableWidget.setItem(r, 1, item)
            item = QtGui.QTableWidgetItem()
            item.setText(unicode(data1[i][2]))
            self.tableWidget.setItem(r, 2, item)
            item = QtGui.QTableWidgetItem()
            item.setText(unicode(data1[i][3]))
            self.tableWidget.setItem(r, 3, item)
            if r==r+r1:
                break
            else:
                r+=1
        header = self.tableWidget.horizontalHeader()
        header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)

        conn.close()
        conn1.close()

        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(607, 22, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        Install.setCentralWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.pushButton.clicked.connect(self.install)
        self.pushButton_2.clicked.connect(self.Cancel)

        self.retranslateUi(Install)
        QtCore.QMetaObject.connectSlotsByName(Install)

    def install(self):
        p=self.tableWidget.currentRow()
        repo = self.tableWidget.item(p,0).text()
        name= self.tableWidget.item(p,1).text()
        if repo=="AUR" :
            proj.makepkg(name)
        else :
            proj.pacinstall(name)
           
        self.dui=Dialog("Installed")
        self.dui.show()

    def Cancel(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()




    def retranslateUi(self, Install):
        Install.setWindowTitle("Install")
        self.pushButton.setText("Install")
        self.pushButton_2.setText("Back")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Repo")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Name")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Version")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("Description")
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


class Ui_Uninstall(object):
    def setupUi(self, Uninstall):
        proj.installed_db()
        Uninstall.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Uninstall)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(3)

        conn = sqlite3.connect('installed_db.db')
        c = conn.cursor()
        c.execute("SELECT * FROM installed")
        data1=c.fetchall()
        c.execute("SELECT count(*) FROM installed")
        r = c.fetchone()[0]
        self.tableWidget.setRowCount(r)
        for i in range(0,r):
            item = QtGui.QTableWidgetItem()
            item.setText(unicode(data1[i][0]))
            self.tableWidget.setItem(i, 0, item)
            item = QtGui.QTableWidgetItem()
            item.setText(unicode(data1[i][1]))
            self.tableWidget.setItem(i, 1, item)
            item = QtGui.QTableWidgetItem()
            item.setText(unicode(data1[i][2]))
            self.tableWidget.setItem(i, 2, item)
            if r==i:
                break

        header = self.tableWidget.horizontalHeader()
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        header = self.tableWidget.horizontalHeader()
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        header = self.tableWidget.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)

        conn.close()

        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)
        Uninstall.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.Cancel)
        self.pushButton_2.clicked.connect(self.uninstall)



        self.retranslateUi(Uninstall)
        QtCore.QMetaObject.connectSlotsByName(Uninstall)

    def Cancel(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()

    def uninstall(self):
        p=self.tableWidget.currentRow()
        name = self.tableWidget.item(p,0).text()
        proj.uninstall(name)
        self.dui=Dialog("Uninstalled")
        self.dui.show()
        self.ui = Ui_Uninstall()
        self.ui.setupUi(MainWindow)
        MainWindow.show()


    def retranslateUi(self, Uninstall):
        Uninstall.setWindowTitle("Uninstall")
        self.pushButton.setText("Back")
        self.pushButton_2.setText("Uninstall")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Name")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Installed Version")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Aur Package")
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

class Ui_Dialog(object):
    def setupUi(self, Dialog,text):
        Dialog.resize(331, 155)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 60, 241, 17))

        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 110, 80, 25))

        self.pushButton.clicked.connect(self.Cancel)


        self.retranslateUi(Dialog,text)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog,text):
        Dialog.setWindowTitle("Popup")
        self.label.setText(text)
        self.pushButton.setText("Ok")

    def Cancel(self):
        self.close()

class Dialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, text, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)

        self.setupUi(self,text)



class Ui_Update(object):
    def setupUi(self, Update):
        Update.resize(245, 188)
        self.centralwidget = QtGui.QWidget(Update)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        Update.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.aur)
        self.pushButton_2.clicked.connect(self.Update)
        self.pushButton_3.clicked.connect(self.Cancel)


        self.retranslateUi(Update)
        QtCore.QMetaObject.connectSlotsByName(Update)


    def retranslateUi(self, Update):
        Update.setWindowTitle("Update")
        self.pushButton.setText("Aur Update")
        self.pushButton_2.setText("System Update")
        self.pushButton_3.setText("Back")

    def Cancel(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()

    def aur(self):
        proj.installed_db()
        proj.aur_update()
        self.dui = Dialog("All AUR updates installed")
        self.dui.show()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
    
    def Update(self):
        proj.pac_update()
        self.dui = Dialog("Update Complete")
        self.dui.show()
       
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()



if __name__  ==  "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    dui = Pass()
    dui.show()
    ui = Ui_MainWindow()
    sys.exit(app.exec_())

