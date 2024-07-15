# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\Desktop\test\demo\examples\firewall\view\ui\set_rules.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setRules(object):
    def setupUi(self, setRules):
        setRules.setObjectName("setRules")
        setRules.resize(900, 700)
        self.frame = CardWidget(setRules)
        self.frame.setGeometry(
            QtCore.QRect(30, 50, 531, 70)
        )  # 参数分别为x,y,width,height
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        # self.frame.setFrameShape(QtCore.Qt.QFrame::Shape::NoFrame)
        # self.frame.setFrameShadow(QtCore.Qt.QFrame::Shadow::Plain)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 5, 511, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = PushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = PushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = PushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = PrimaryPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = PrimaryPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.frame_2 = CardWidget(setRules)
        self.frame_2.setGeometry(QtCore.QRect(30, 130, 821, 511))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        # self.frame_2.setFrameShape(QtCore.Qt.QFrame::Shape::NoFrame)
        # self.frame_2.setFrameShadow(QtCore.Qt.QFrame::Shadow::Plain)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = TableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 781, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.frame_2.raise_()
        self.frame.raise_()

        # self.switchButton = SwitchButton(parent=self)
        # self.switchButton.move(700, 70)
        # self.switchButton.setOnText("Dark")
        # self.switchButton.setOffText("Light")
        # self.switchButton.resize(200, 60)

        self.retranslateUi(setRules)
        QtCore.QMetaObject.connectSlotsByName(setRules)

    def retranslateUi(self, setRules):
        _translate = QtCore.QCoreApplication.translate
        setRules.setWindowTitle(_translate("setRules", "Form"))
        self.pushButton.setText(_translate("setRules", "添加"))
        self.pushButton_2.setText(_translate("setRules", "删除"))
        self.pushButton_3.setText(_translate("setRules", "修改"))
        self.pushButton_4.setText(_translate("setRules", "导入"))
        self.pushButton_5.setText(_translate("setRules", "导出"))

        self.pushButton.setIcon(FluentIcon.ADD)
        self.pushButton_2.setIcon(FluentIcon.DELETE)
        self.pushButton_3.setIcon(FluentIcon.UPDATE)
        self.pushButton_4.setIcon(FluentIcon.DOWN)
        self.pushButton_5.setIcon(FluentIcon.UP)

        item = self.tableWidget.horizontalHeaderItem(0)
        self.tableWidget.setColumnWidth(0, 50)
        item.setText(_translate("setRules", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        self.tableWidget.setColumnWidth(1, 70)
        item.setText(_translate("setRules", "协议类型"))
        item = self.tableWidget.horizontalHeaderItem(2)
        self.tableWidget.setColumnWidth(2, 90)
        item.setText(_translate("setRules", "网络接口"))
        item = self.tableWidget.horizontalHeaderItem(3)
        #设置宽度
        self.tableWidget.setColumnWidth(3, 150)
        item.setText(_translate("setRules", "源IP地址:端口"))
        item = self.tableWidget.horizontalHeaderItem(4)
        self.tableWidget.setColumnWidth(4, 150)
        item.setText(_translate("setRules", "目标IP地址:端口"))
        item = self.tableWidget.horizontalHeaderItem(5)
        self.tableWidget.setColumnWidth(5, 200)
        item.setText(_translate("setRules", "开始时间"))
        item = self.tableWidget.horizontalHeaderItem(6)
        self.tableWidget.setColumnWidth(6, 200)
        item.setText(_translate("setRules", "结束时间"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("setRules", "执行动作"))
        # 隐藏最左边的行号
        self.tableWidget.verticalHeader().setVisible(False)


from qfluentwidgets import (
    CardWidget,
    PrimaryPushButton,
    PushButton,
    TableWidget,
    FluentIcon,
    SwitchButton,
)
