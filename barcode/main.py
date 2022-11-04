from barcode_module import *
from drawing_barcode import drawing_barcode
import sys
from PyQt5 import QtWidgets
from main_window import Ui_main_window as win


def main():
    
    # input_code = input("enter 12 number decimal code:\n")
    #
    # dec_barcode = calculate_last_number(input_code)
    #
    # write_encoding_data()
    # bin_barcode = encoding_barecode(dec_barcode)
    #
    # print(dec_barcode)
    # print(bin_barcode)
    # print(len(bin_barcode))
    #
    # drawing_barcode(bin_barcode)


    #tu jest kod odpowiedzialny za wywolanie okna aplikacji

    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    #app.lastWindowClosed.connect(end_application)
    MainWindow = QtWidgets.QMainWindow()
    ui = win()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if(__name__ == '__main__'):
    main()
