from PyQt5 import QtCore, QtGui, QtWidgets
from barcode_module import *
from drawing_barcode import drawing_barcode

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(300, 200)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.bar_code_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar_code_label.sizePolicy().hasHeightForWidth())
        self.bar_code_label.setSizePolicy(sizePolicy)
        self.bar_code_label.setAutoFillBackground(False)
        self.bar_code_label.setText("")

        self.bar_code_label.setPixmap(QtGui.QPixmap("example_bar_code.png"))
        self.bar_code_label.setObjectName("bar_code_label")
        self.verticalLayout.addWidget(self.bar_code_label)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.number_QtextEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_QtextEdit.sizePolicy().hasHeightForWidth())
        self.number_QtextEdit.setSizePolicy(sizePolicy)
        self.number_QtextEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.number_QtextEdit.setObjectName("number_QtextEdit")
        self.gridLayout_2.addWidget(self.number_QtextEdit, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)

        #apply button
        self.apply_button = QtWidgets.QPushButton(self.centralwidget)
        self.apply_button.setObjectName("apply_button")
        self.gridLayout_2.addWidget(self.apply_button, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        self.apply_button.clicked.connect(self.apply)

    def apply(self):
        input_code = self.number_QtextEdit.toPlainText()
        dec_barcode = calculate_last_number(str(input_code))
        write_encoding_data()
        bin_barcode = encoding_barecode(dec_barcode)
        drawing_barcode(bin_barcode)
        self.bar_code_label.setPixmap(QtGui.QPixmap("barcode.png"))

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Generate Bar Code"))
        self.apply_button.setText(_translate("main_window", "Apply"))
