# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\Desktop\test\demo\examples\firewall\view\ui\del_rules.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess
import re


class Ui_DelRule(object):
    def setupUi(self, DelRule):
        DelRule.setObjectName("DelRule")
        DelRule.resize(409, 293)
        self.widget = QtWidgets.QWidget(DelRule)
        self.widget.setGeometry(QtCore.QRect(20, 20, 367, 251))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = StrongBodyLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = LineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText(
            "Please enter the ID number of the rule to be deleted."
        )
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_6 = PushButton(self.widget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        spacerItem = QtWidgets.QSpacerItem(
            30, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton_7 = PrimaryPushButton(self.widget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(DelRule)
        QtCore.QMetaObject.connectSlotsByName(DelRule)

    def retranslateUi(self, DelRule):
        _translate = QtCore.QCoreApplication.translate
        DelRule.setWindowTitle(_translate("DelRule", "Form"))
        self.label.setText(_translate("DelRule", "请输入要删除规则的ID号："))
        self.pushButton_6.setText(_translate("DelRule", "取消"))
        self.pushButton_7.setText(_translate("DelRule", "确定"))
    
    def on_pushButton_7_clicked(self):
        rule_id = self.lineEdit.text()
        command = ['sudo', './firewall_cli', '-d', rule_id]
        result = subprocess.run(command, capture_output=True, text = True, cwd = os.getcwd())
        clean_output = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', result.stdout)
        QtWidgets.QMessageBox.information(self, '结果', clean_output)
    
    def on_pushButton_6_clicked(self):
        self.close()


from qfluentwidgets import LineEdit, PrimaryPushButton, PushButton, StrongBodyLabel
