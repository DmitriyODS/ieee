# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ieee.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IEEE(object):
    def setupUi(self, IEEE):
        IEEE.setObjectName("IEEE")
        IEEE.resize(1043, 657)
        IEEE.setStyleSheet("#content {\n"
"    background-color: rgb(58, 67, 81);\n"
"    color: rgb(231, 231, 231);\n"
"}\n"
"\n"
"#btn_load {\n"
"    background-color: rgb(85, 170, 127);\n"
"    color: rgb(34, 68, 50);\n"
"    border: none;\n"
"}\n"
"\n"
"#btn_load:hover {\n"
"    background-color: rgb(104, 209, 155);\n"
"}\n"
"\n"
"#btn_load:pressed {\n"
"    background-color: rgb(42, 85, 63);\n"
"    color: rgb(85, 170, 127);\n"
"}\n"
"\n"
"#btn_run {\n"
"    background-color: rgb(85, 170, 255);\n"
"    color: rgb(24, 49, 74);\n"
"    border: none;\n"
"}\n"
"\n"
"#btn_run:hover {\n"
"    background-color: rgb(142, 201, 255);\n"
"}\n"
"\n"
"#btn_run:pressed {\n"
"    background-color: rgb(24, 49, 74);\n"
"    color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"#btn_reset {\n"
"    background-color: rgb(255, 0, 127);\n"
"    color: rgb(81, 0, 40);\n"
"    border: 2none;\n"
"}\n"
"\n"
"#btn_reset:hover {\n"
"    background-color: rgb(255, 89, 169);\n"
"}\n"
"\n"
"#btn_reset:pressed {\n"
"    background-color: rgb(94, 0, 47);\n"
"    color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(35, 40, 49);\n"
"    border-radius: 16px;\n"
"    border: 2px solid rgb(97, 179, 255);\n"
"}\n"
"\n"
"QPushButton[numpad=true] {\n"
"    background-color: rgb(35, 40, 49);\n"
"    color: rgb(97, 179, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 67, 81);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(97, 179, 255);\n"
"    color: rgb(35, 40, 49);\n"
"}\n"
"\n"
"#label_input {\n"
"    border: 2px solid rgb(97, 179, 255);\n"
"    border-radius: 16px;\n"
"    color: rgb(124, 174, 255);\n"
"}\n"
"\n"
"#part_symbol {\n"
"    background-color: rgb(170, 170, 255);\n"
"    border-top-left-radius: 16px;\n"
"    border-bottom-left-radius: 16px;\n"
"}\n"
"\n"
"#label_output_symbol {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#label_output_order {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#part_order {\n"
"    background-color: rgb(85, 0, 127);\n"
"}\n"
"\n"
"#label_output_exp {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#part_exp {\n"
"    background-color: rgb(85, 170, 127);\n"
"    border-top-right-radius: 16px;\n"
"    border-bottom-right-radius: 16px;\n"
"}\n"
"\n"
"#part_symbol_res {\n"
"    background-color: rgb(170, 170, 255);\n"
"    border-top-left-radius: 16px;\n"
"    border-bottom-left-radius: 16px;\n"
"}\n"
"\n"
"#label_output_symbol_res {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#label_output_order_res {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#part_order_res {\n"
"    background-color: rgb(85, 0, 127);\n"
"}\n"
"\n"
"#label_output_exp_res {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#part_exp_res {\n"
"    background-color: rgb(85, 170, 127);\n"
"    border-top-right-radius: 16px;\n"
"    border-bottom-right-radius: 16px;\n"
"}")
        self.content = QtWidgets.QWidget(IEEE)
        self.content.setObjectName("content")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.content)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.content)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.putput = QtWidgets.QHBoxLayout()
        self.putput.setSpacing(0)
        self.putput.setObjectName("putput")
        self.part_symbol = QtWidgets.QFrame(self.content)
        self.part_symbol.setMaximumSize(QtCore.QSize(98, 16777215))
        self.part_symbol.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.part_symbol.setFrameShadow(QtWidgets.QFrame.Raised)
        self.part_symbol.setObjectName("part_symbol")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.part_symbol)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.part_symbol)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_output_symbol = QtWidgets.QLabel(self.part_symbol)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_output_symbol.setFont(font)
        self.label_output_symbol.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output_symbol.setObjectName("label_output_symbol")
        self.verticalLayout_2.addWidget(self.label_output_symbol)
        self.putput.addWidget(self.part_symbol)
        self.part_order = QtWidgets.QFrame(self.content)
        self.part_order.setMaximumSize(QtCore.QSize(256, 16777215))
        self.part_order.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.part_order.setFrameShadow(QtWidgets.QFrame.Raised)
        self.part_order.setObjectName("part_order")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.part_order)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.part_order)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_output_order = QtWidgets.QLabel(self.part_order)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_output_order.setFont(font)
        self.label_output_order.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_output_order.setObjectName("label_output_order")
        self.verticalLayout_4.addWidget(self.label_output_order)
        self.putput.addWidget(self.part_order)
        self.part_exp = QtWidgets.QFrame(self.content)
        self.part_exp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.part_exp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.part_exp.setObjectName("part_exp")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.part_exp)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.part_exp)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.label_output_exp = QtWidgets.QLabel(self.part_exp)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_output_exp.setFont(font)
        self.label_output_exp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_output_exp.setObjectName("label_output_exp")
        self.verticalLayout_5.addWidget(self.label_output_exp)
        self.putput.addWidget(self.part_exp)
        self.verticalLayout_12.addLayout(self.putput)
        spacerItem = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem)
        self.label_13 = QtWidgets.QLabel(self.content)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_12.addWidget(self.label_13)
        self.putput_3 = QtWidgets.QHBoxLayout()
        self.putput_3.setSpacing(0)
        self.putput_3.setObjectName("putput_3")
        self.part_symbol_res = QtWidgets.QFrame(self.content)
        self.part_symbol_res.setMaximumSize(QtCore.QSize(98, 16777215))
        self.part_symbol_res.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.part_symbol_res.setFrameShadow(QtWidgets.QFrame.Raised)
        self.part_symbol_res.setObjectName("part_symbol_res")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.part_symbol_res)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.part_symbol_res)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.label_output_symbol_res = QtWidgets.QLabel(self.part_symbol_res)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_output_symbol_res.setFont(font)
        self.label_output_symbol_res.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output_symbol_res.setObjectName("label_output_symbol_res")
        self.verticalLayout_9.addWidget(self.label_output_symbol_res)
        self.putput_3.addWidget(self.part_symbol_res)
        self.part_order_res = QtWidgets.QFrame(self.content)
        self.part_order_res.setMaximumSize(QtCore.QSize(256, 16777215))
        self.part_order_res.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.part_order_res.setFrameShadow(QtWidgets.QFrame.Raised)
        self.part_order_res.setObjectName("part_order_res")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.part_order_res)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.part_order_res)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.label_output_order_res = QtWidgets.QLabel(self.part_order_res)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_output_order_res.setFont(font)
        self.label_output_order_res.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_output_order_res.setObjectName("label_output_order_res")
        self.verticalLayout_10.addWidget(self.label_output_order_res)
        self.putput_3.addWidget(self.part_order_res)
        self.part_exp_res = QtWidgets.QFrame(self.content)
        self.part_exp_res.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.part_exp_res.setFrameShadow(QtWidgets.QFrame.Raised)
        self.part_exp_res.setObjectName("part_exp_res")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.part_exp_res)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.part_exp_res)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_11.addWidget(self.label_12)
        self.label_output_exp_res = QtWidgets.QLabel(self.part_exp_res)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_output_exp_res.setFont(font)
        self.label_output_exp_res.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_output_exp_res.setObjectName("label_output_exp_res")
        self.verticalLayout_11.addWidget(self.label_output_exp_res)
        self.putput_3.addWidget(self.part_exp_res)
        self.verticalLayout_12.addLayout(self.putput_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_input = QtWidgets.QLabel(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_input.sizePolicy().hasHeightForWidth())
        self.label_input.setSizePolicy(sizePolicy)
        self.label_input.setMinimumSize(QtCore.QSize(0, 64))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_input.setFont(font)
        self.label_input.setObjectName("label_input")
        self.verticalLayout.addWidget(self.label_input)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_reset = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_reset.sizePolicy().hasHeightForWidth())
        self.btn_reset.setSizePolicy(sizePolicy)
        self.btn_reset.setMinimumSize(QtCore.QSize(0, 64))
        self.btn_reset.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reset.setFont(font)
        self.btn_reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout.addWidget(self.btn_reset)
        self.btn_load = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_load.sizePolicy().hasHeightForWidth())
        self.btn_load.setSizePolicy(sizePolicy)
        self.btn_load.setMinimumSize(QtCore.QSize(0, 64))
        self.btn_load.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load.setFont(font)
        self.btn_load.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_load.setStyleSheet("")
        self.btn_load.setObjectName("btn_load")
        self.horizontalLayout.addWidget(self.btn_load)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btn_run = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_run.sizePolicy().hasHeightForWidth())
        self.btn_run.setSizePolicy(sizePolicy)
        self.btn_run.setMinimumSize(QtCore.QSize(0, 64))
        self.btn_run.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_run.setFont(font)
        self.btn_run.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_run.setStyleSheet("")
        self.btn_run.setObjectName("btn_run")
        self.verticalLayout.addWidget(self.btn_run)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_7 = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_7.setProperty("numpad", True)
        self.btn_7.setObjectName("btn_7")
        self.btn_group_digits = QtWidgets.QButtonGroup(IEEE)
        self.btn_group_digits.setObjectName("btn_group_digits")
        self.btn_group_digits.addButton(self.btn_7)
        self.gridLayout.addWidget(self.btn_7, 0, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_8.setProperty("numpad", True)
        self.btn_8.setObjectName("btn_8")
        self.btn_group_digits.addButton(self.btn_8)
        self.gridLayout.addWidget(self.btn_8, 0, 1, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_4.setProperty("numpad", True)
        self.btn_4.setObjectName("btn_4")
        self.btn_group_digits.addButton(self.btn_4)
        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_5.setProperty("numpad", True)
        self.btn_5.setObjectName("btn_5")
        self.btn_group_digits.addButton(self.btn_5)
        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dot.setFont(font)
        self.btn_dot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_dot.setProperty("numpad", True)
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout.addWidget(self.btn_dot, 3, 0, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_6.setProperty("numpad", True)
        self.btn_6.setObjectName("btn_6")
        self.btn_group_digits.addButton(self.btn_6)
        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_0.setProperty("numpad", True)
        self.btn_0.setObjectName("btn_0")
        self.btn_group_digits.addButton(self.btn_0)
        self.gridLayout.addWidget(self.btn_0, 3, 1, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1.setProperty("numpad", True)
        self.btn_1.setObjectName("btn_1")
        self.btn_group_digits.addButton(self.btn_1)
        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2.setProperty("numpad", True)
        self.btn_2.setObjectName("btn_2")
        self.btn_group_digits.addButton(self.btn_2)
        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_9.setProperty("numpad", True)
        self.btn_9.setObjectName("btn_9")
        self.btn_group_digits.addButton(self.btn_9)
        self.gridLayout.addWidget(self.btn_9, 0, 2, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_3.setProperty("numpad", True)
        self.btn_3.setObjectName("btn_3")
        self.btn_group_digits.addButton(self.btn_3)
        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)
        self.btn_symbol = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_symbol.sizePolicy().hasHeightForWidth())
        self.btn_symbol.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_symbol.setFont(font)
        self.btn_symbol.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_symbol.setProperty("numpad", True)
        self.btn_symbol.setObjectName("btn_symbol")
        self.gridLayout.addWidget(self.btn_symbol, 3, 2, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_12.addLayout(self.horizontalLayout_3)
        IEEE.setCentralWidget(self.content)

        self.retranslateUi(IEEE)
        QtCore.QMetaObject.connectSlotsByName(IEEE)

    def retranslateUi(self, IEEE):
        _translate = QtCore.QCoreApplication.translate
        IEEE.setWindowTitle(_translate("IEEE", "IEEE-754"))
        self.label.setText(_translate("IEEE", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Изначальное число</span></p></body></html>"))
        self.label_3.setText(_translate("IEEE", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Знак</span></p></body></html>"))
        self.label_output_symbol.setText(_translate("IEEE", "0"))
        self.label_5.setText(_translate("IEEE", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Порядок</span></p></body></html>"))
        self.label_output_order.setText(_translate("IEEE", "0"))
        self.label_6.setText(_translate("IEEE", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Мантисса</span></p></body></html>"))
        self.label_output_exp.setText(_translate("IEEE", "0"))
        self.label_13.setText(_translate("IEEE", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Результат</span></p></body></html>"))
        self.label_10.setText(_translate("IEEE", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Знак</span></p></body></html>"))
        self.label_output_symbol_res.setText(_translate("IEEE", "0"))
        self.label_11.setText(_translate("IEEE", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Порядок</span></p></body></html>"))
        self.label_output_order_res.setText(_translate("IEEE", "0"))
        self.label_12.setText(_translate("IEEE", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Мантисса</span></p></body></html>"))
        self.label_output_exp_res.setText(_translate("IEEE", "0"))
        self.label_input.setText(_translate("IEEE", "0"))
        self.btn_reset.setText(_translate("IEEE", "Сбросить"))
        self.btn_load.setText(_translate("IEEE", "Загрузить"))
        self.btn_run.setText(_translate("IEEE", "Вычислить"))
        self.btn_7.setText(_translate("IEEE", "7"))
        self.btn_8.setText(_translate("IEEE", "8"))
        self.btn_4.setText(_translate("IEEE", "4"))
        self.btn_5.setText(_translate("IEEE", "5"))
        self.btn_dot.setText(_translate("IEEE", "."))
        self.btn_6.setText(_translate("IEEE", "6"))
        self.btn_0.setText(_translate("IEEE", "0"))
        self.btn_1.setText(_translate("IEEE", "1"))
        self.btn_2.setText(_translate("IEEE", "2"))
        self.btn_9.setText(_translate("IEEE", "9"))
        self.btn_3.setText(_translate("IEEE", "3"))
        self.btn_symbol.setText(_translate("IEEE", "+/-"))