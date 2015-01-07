#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

#PyQt
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

#時計本体部
from Model.TinyClockModel import TinyClockModel

#時計表示部
from View.mainwindow import Ui_MainWindow
from View.TinyClockViewGUI import TinyDigitalClockView
from View.TinyClockViewGUI import TinyAnalogClockView

class ClockViewWidget(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kw):
        QtGui.QMainWindow.__init__(self, *args, **kw)
        self.setupUi(self)

        #時計本体部を生成.
        self.ClockModel = TinyClockModel()

        #デジタル時計表示部を生成.
        self.DigitalClock = TinyDigitalClockView()
        self.DigitalClock.setup_ui(self.dateTimeEdit)

        #アナログ時計表示部を生成.
        self.AnalogClock = TinyAnalogClockView(self.widget)
        self.AnalogClock.setup_ui(self.dateEdit)

        #時計 本体部 と 表示部 を接続
        self.ClockModel.attach(self.DigitalClock)
        self.ClockModel.attach(self.AnalogClock)

        #タイマーを設定（時計本体部と接続. 1000mse毎に時刻を設定）
        self.timer = QtCore.QTimer(parent=self)
        self.timer.timeout.connect(self.ClockModel.set_time)
        self.timer.setInterval(1*1000)
        self.timer.start()


def main():
	app = QtGui.QApplication(sys.argv)

        panel = ClockViewWidget()

	main_window = QtGui.QMainWindow()
        main_window.setGeometry(0, 0, panel.width(), panel.height())
        main_window.setWindowTitle("TinyClock")
        main_window.setCentralWidget(panel)
	main_window.show()

	app.exec_()

if __name__=='__main__':
	main()

