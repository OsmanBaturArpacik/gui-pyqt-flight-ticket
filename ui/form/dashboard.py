# -*- coding: utf-8 -*-
import os

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate


class Ui_dashboard_window(object):
    def setupUi(self, dashboard_window):
        dashboard_window.setObjectName("dashboard_window")
        dashboard_window.resize(1200, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dashboard_window.sizePolicy().hasHeightForWidth())
        dashboard_window.setSizePolicy(sizePolicy)
        dashboard_window.setMinimumSize(QtCore.QSize(1200, 600))
        dashboard_window.setMaximumSize(QtCore.QSize(1200, 600))
        self.centralwidget = QtWidgets.QWidget(dashboard_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_bar = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_bar.sizePolicy().hasHeightForWidth())
        self.left_bar.setSizePolicy(sizePolicy)
        self.left_bar.setMinimumSize(QtCore.QSize(200, 600))
        self.left_bar.setObjectName("left_bar")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.left_bar)
        self.verticalLayout_18.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_18 = QtWidgets.QLabel(self.left_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QtCore.QSize(300, 200))
        self.label_18.setMaximumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_18.setFont(font)
        self.label_18.setText("")
        image_path = os.path.join(os.getcwd(), 'images', 'login-user.png')
        self.label_18.setPixmap(QtGui.QPixmap(image_path))
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_18.addWidget(self.label_18)
        spacerItem = QtWidgets.QSpacerItem(10, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_18.addItem(spacerItem)
        self.nickname_label = QtWidgets.QLabel(self.left_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nickname_label.sizePolicy().hasHeightForWidth())
        self.nickname_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nickname_label.setFont(font)
        self.nickname_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nickname_label.setObjectName("nickname_label")
        self.verticalLayout_18.addWidget(self.nickname_label)
        self.label_19 = QtWidgets.QLabel(self.left_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_18.addWidget(self.label_19)
        spacerItem1 = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_18.addItem(spacerItem1)
        self.my_tickets_btn = QtWidgets.QPushButton(self.left_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.my_tickets_btn.sizePolicy().hasHeightForWidth())
        self.my_tickets_btn.setSizePolicy(sizePolicy)
        self.my_tickets_btn.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.my_tickets_btn.setFont(font)
        self.my_tickets_btn.setObjectName("my_tickets_btn")
        self.verticalLayout_18.addWidget(self.my_tickets_btn)
        self.my_history_btn = QtWidgets.QPushButton(self.left_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.my_history_btn.sizePolicy().hasHeightForWidth())
        self.my_history_btn.setSizePolicy(sizePolicy)
        self.my_history_btn.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.my_history_btn.setFont(font)
        self.my_history_btn.setObjectName("my_history_btn")
        self.verticalLayout_18.addWidget(self.my_history_btn)
        self.my_acc_about_btn = QtWidgets.QPushButton(self.left_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.my_acc_about_btn.sizePolicy().hasHeightForWidth())
        self.my_acc_about_btn.setSizePolicy(sizePolicy)
        self.my_acc_about_btn.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.my_acc_about_btn.setFont(font)
        self.my_acc_about_btn.setObjectName("my_acc_about_btn")
        self.verticalLayout_18.addWidget(self.my_acc_about_btn)
        spacerItem2 = QtWidgets.QSpacerItem(0, 170, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_18.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.left_bar)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(15, 0, 5, 50)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(450, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(-1, 5, -1, -1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMinimumSize(QtCore.QSize(100, 20))
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout_11.addWidget(self.login_btn)
        self.logout_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout_btn.sizePolicy().hasHeightForWidth())
        self.logout_btn.setSizePolicy(sizePolicy)
        self.logout_btn.setMinimumSize(QtCore.QSize(100, 20))
        self.logout_btn.setObjectName("logout_btn")
        self.verticalLayout_11.addWidget(self.logout_btn)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_11.addWidget(self.label_8)
        self.horizontalLayout_7.addLayout(self.verticalLayout_11)
        self.horizontalLayout_7.setStretch(0, 100)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_8.setSpacing(40)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.from_cmbx = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.from_cmbx.sizePolicy().hasHeightForWidth())
        self.from_cmbx.setSizePolicy(sizePolicy)
        self.from_cmbx.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.from_cmbx.setFont(font)
        self.from_cmbx.setObjectName("from_cmbx")
        self.from_cmbx.addItem("")
        self.from_cmbx.addItem("")
        self.from_cmbx.addItem("")
        self.from_cmbx.addItem("")
        self.from_cmbx.addItem("")
        self.verticalLayout_6.addWidget(self.from_cmbx)
        self.horizontalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.to_cmbx = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_cmbx.sizePolicy().hasHeightForWidth())
        self.to_cmbx.setSizePolicy(sizePolicy)
        self.to_cmbx.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.to_cmbx.setFont(font)
        self.to_cmbx.setObjectName("to_cmbx")
        self.to_cmbx.addItem("")
        self.to_cmbx.addItem("")
        self.to_cmbx.addItem("")
        self.to_cmbx.addItem("")
        self.to_cmbx.addItem("")
        self.verticalLayout_5.addWidget(self.to_cmbx)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.go_date = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_date.sizePolicy().hasHeightForWidth())
        self.go_date.setSizePolicy(sizePolicy)
        self.go_date.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.go_date.setFont(font)
        self.go_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 1, 1), QtCore.QTime(0, 0, 0)))
        self.go_date.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2023, 12, 31), QtCore.QTime(0, 0, 0)))
        self.go_date.setObjectName("go_date")
        self.verticalLayout_8.addWidget(self.go_date)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.return_date = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_date.sizePolicy().hasHeightForWidth())
        self.return_date.setSizePolicy(sizePolicy)
        self.return_date.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.return_date.setFont(font)
        self.return_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 1, 1), QtCore.QTime(0, 0, 0)))
        self.return_date.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2023, 12, 31), QtCore.QTime(0, 0, 0)))
        self.return_date.setObjectName("return_date")
        self.verticalLayout_7.addWidget(self.return_date)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.search_ticket_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_ticket_btn.sizePolicy().hasHeightForWidth())
        self.search_ticket_btn.setSizePolicy(sizePolicy)
        self.search_ticket_btn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_ticket_btn.setFont(font)
        self.search_ticket_btn.setObjectName("search_ticket_btn")
        self.verticalLayout_10.addWidget(self.search_ticket_btn)
        self.horizontalLayout_8.addLayout(self.verticalLayout_10)
        self.horizontalLayout_8.setStretch(0, 20)
        self.horizontalLayout_8.setStretch(1, 20)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(100, 10, 10, 10)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 22))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_13.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(100, 0, 100, 0)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pnr_ln = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pnr_ln.sizePolicy().hasHeightForWidth())
        self.pnr_ln.setSizePolicy(sizePolicy)
        self.pnr_ln.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pnr_ln.setFont(font)
        self.pnr_ln.setObjectName("pnr_ln")
        self.horizontalLayout_11.addWidget(self.pnr_ln)
        self.search_pnr_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_pnr_btn.sizePolicy().hasHeightForWidth())
        self.search_pnr_btn.setSizePolicy(sizePolicy)
        self.search_pnr_btn.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.search_pnr_btn.setFont(font)
        self.search_pnr_btn.setObjectName("search_pnr_btn")
        self.horizontalLayout_11.addWidget(self.search_pnr_btn)
        self.horizontalLayout_11.setStretch(0, 2)
        self.horizontalLayout_11.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        spacerItem4 = QtWidgets.QSpacerItem(20, 160, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(4, 10)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(1, 4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        dashboard_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dashboard_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        dashboard_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dashboard_window)
        self.statusbar.setObjectName("statusbar")
        dashboard_window.setStatusBar(self.statusbar)

        self.retranslateUi(dashboard_window)
        QtCore.QMetaObject.connectSlotsByName(dashboard_window)

    def retranslateUi(self, dashboard_window):
        _translate = QtCore.QCoreApplication.translate
        dashboard_window.setWindowTitle(_translate("dashboard_window", "Uçak Bileti Rezervasyon"))
        self.nickname_label.setText(_translate("dashboard_window", "Nickname"))
        self.label_19.setText(_translate("dashboard_window", "___________________________________________________"))
        self.my_tickets_btn.setText(_translate("dashboard_window", "Biletlerim"))
        self.my_history_btn.setText(_translate("dashboard_window", "Geçmiş Seyahatlerim"))
        self.my_acc_about_btn.setText(_translate("dashboard_window", "Hesap Bilgileri"))
        self.label.setText(_translate("dashboard_window", "Uçak Bileti Rezarvasyonu"))
        self.login_btn.setText(_translate("dashboard_window", "Giriş Yap"))
        self.logout_btn.setText(_translate("dashboard_window", "Çıkış Yap"))
        self.label_3.setText(_translate("dashboard_window", "Nereden?"))
        self.from_cmbx.setCurrentText(_translate("dashboard_window", "İstanbul (Avrupa)"))
        self.from_cmbx.setItemText(0, _translate("dashboard_window", "İstanbul (Avrupa)"))
        self.from_cmbx.setItemText(1, _translate("dashboard_window", "İstanbul (Anadolu)"))
        self.from_cmbx.setItemText(2, _translate("dashboard_window", "Ankara"))
        self.from_cmbx.setItemText(3, _translate("dashboard_window", "İzmir"))
        self.from_cmbx.setItemText(4, _translate("dashboard_window", "Kütahya"))
        self.label_6.setText(_translate("dashboard_window", "Nereye?"))
        self.to_cmbx.setItemText(0, _translate("dashboard_window", "İstanbul (Avrupa)"))
        self.to_cmbx.setItemText(1, _translate("dashboard_window", "İstanbul (Anadolu)"))
        self.to_cmbx.setItemText(2, _translate("dashboard_window", "Ankara"))
        self.to_cmbx.setItemText(3, _translate("dashboard_window", "İzmir"))
        self.to_cmbx.setItemText(4, _translate("dashboard_window", "Kütahya"))
        self.label_4.setText(_translate("dashboard_window", "Gidiş Tarihi"))
        self.go_date.setDisplayFormat(_translate("dashboard_window", "d/M/yyyy"))
        self.label_5.setText(_translate("dashboard_window", "Dönüş Tarihi"))
        self.return_date.setDisplayFormat(_translate("dashboard_window", "d/M/yyyy"))
        self.search_ticket_btn.setText(_translate("dashboard_window", "Sorgula"))
        self.label_2.setText(_translate("dashboard_window", "PNR Numarası Giriniz:"))
        self.pnr_ln.setPlaceholderText(_translate("dashboard_window", "PNR GİRİNİZ: PC4175"))
        self.search_pnr_btn.setText(_translate("dashboard_window", "Sorgula"))

    def get_date(self, date_obj):
        date = date_obj.text()
        date = QDate.fromString(date, "d/M/yyyy")
        date = date.toString("dd/MM/yyyy")
        return date


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dashboard_window = QtWidgets.QMainWindow()
    ui = Ui_dashboard_window()
    ui.setupUi(dashboard_window)
    dashboard_window.show()
    sys.exit(app.exec_())
