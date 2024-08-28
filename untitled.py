# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
import sqlite3
import utils
import crud
import time
from datetime import datetime
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(497, 361)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hours = QtWidgets.QComboBox(self.centralwidget)
        self.hours.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        self.hours.setFont(font)
        self.hours.setObjectName("hours")
        self.verticalLayout_2.addWidget(self.hours, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.minutes = QtWidgets.QComboBox(self.centralwidget)
        self.minutes.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        self.minutes.setFont(font)
        self.minutes.setObjectName("minutes")
        self.horizontalLayout_7.addWidget(self.minutes, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.add_new_time())
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        self.add_button.setFont(font)
        self.add_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_3.addWidget(self.add_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.show_times = QtWidgets.QComboBox(self.centralwidget)
        self.show_times.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        self.show_times.setFont(font)
        self.show_times.setObjectName("show_times")
        self.horizontalLayout_9.addWidget(self.show_times, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.delete_time())
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        self.delete_button.setFont(font)
        self.delete_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_8.addWidget(self.delete_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # additionals
        self.__on_start()
        t = threading.Thread(target=self.check_time_against_database)
        t.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sleep Schedular - www.fiverr.com/code_of_duty"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))

    def __on_start(self):
        hours = ['','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
        minutes = ['','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']
        self.hours.addItems(hours)
        self.minutes.addItems(minutes)

        # create database for storing time
        db_path = utils.get_database_path()
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sleep_schedular (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                hours TEXT NOT NULL,
                minutes TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()

        self.show_times.addItem('')
        list_of_times = crud.get_formatted_times()
        if list_of_times:
            self.show_times.addItems(list_of_times)

    def add_new_time(self):
        if self.hours.currentText() and self.minutes.currentText():
            try:
                crud.insert_sleep_schedule(self.hours.currentText(),self.minutes.currentText())
            except:
                QMessageBox.critical(None,'ERROR','Failed to insert new time')
            else:
                self.show_times.addItem(f'{self.hours.currentText()}:{self.minutes.currentText()}')
                self.hours.setCurrentIndex(0)
                self.minutes.setCurrentIndex(0)
                QMessageBox.information(None,'INFO','New time added')
        else:
            QMessageBox.critical(None,'ERROR','Please select the desired time')

    def delete_time(self):
        if self.show_times.currentText():
            try:
                hour,min = self.show_times.currentText().split(':')
                crud.delete_sleep_schedule_by_time(hour,min)
            except:
                QMessageBox.critical(None,'ERROR','Failed to delete selected time')
            else:
                current_index = self.show_times.currentIndex()
                if current_index != -1:  # Ensure there is a valid selected item
                    self.show_times.removeItem(current_index)
                self.show_times.setCurrentIndex(0)
                QMessageBox.information(None,'INFO','Removed selected time')
        else:
            QMessageBox.critical(None,'ERROR','Please select the desired time')

    def check_time_against_database(self):
        
        while True:
            formatted_times = crud.get_formatted_times()
            current_time = datetime.now().strftime('%H:%M')
            # Compare the current time with times in the database
            if current_time in formatted_times:
                os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")
            time.sleep(50)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
