# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejemplo_tarea2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import pyqtgraph as pg
import numpy as np
from db.model import Protocol0, Protocol1, Protocol2, Protocol3, Protocol4, Protocol5
from qt_utils.connection import searchConnectionBT, connectBT
from qt_utils.configs import saveConfiguration
from qt_utils.plots import updatePlots

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(816, 684)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 781, 621))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_searchBT = QtWidgets.QLabel(self.tab)
        self.label_searchBT.setGeometry(QtCore.QRect(20, 30, 191, 21))
        self.label_searchBT.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_searchBT.setObjectName("label_searchBT")
        self.label_statusESP = QtWidgets.QLabel(self.tab)
        self.label_statusESP.setGeometry(QtCore.QRect(500, 30, 191, 21))
        self.label_statusESP.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_statusESP.setObjectName("label_statusESP")
        self.label_statusESP.setFont(QtGui.QFont("Arial", 13))
        self.searchBTButton = QtWidgets.QPushButton(self.tab)
        self.searchBTButton.setGeometry(QtCore.QRect(200, 20, 101, 41))
        self.searchBTButton.setMinimumSize(QtCore.QSize(101, 41))
        self.searchBTButton.setStyleSheet("color: rgb(213, 213, 213);\n"
"background-color: rgb(11, 0, 172);\n"
"")
        self.searchBTButton.setObjectName("searchBTButton")
        self.selectBTComboBox = QtWidgets.QComboBox(self.tab)
        self.selectBTComboBox.setGeometry(QtCore.QRect(10, 70, 291, 31))
        self.selectBTComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selectBTComboBox.setObjectName("selectBTComboBox")
        self.selectBTComboBox.addItem("")
        self.selectBTComboBox.setItemText(0, "")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(30, 440, 141, 20))
        self.label_21.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_21.setObjectName("label_21")
        self.consoleTextBox = QtWidgets.QTextEdit(self.tab)
        self.consoleTextBox.setGeometry(QtCore.QRect(20, 460, 751, 121))
        self.consoleTextBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.consoleTextBox.setObjectName("consoleTextBox")
        self.batteryProgressBar = QtWidgets.QProgressBar(self.tab)
        self.batteryProgressBar.setGeometry(QtCore.QRect(660, 550, 111, 16))
        self.batteryProgressBar.setProperty("value", 0)
        self.batteryProgressBar.setObjectName("batteryProgressBar")
        self.selectBTButton = QtWidgets.QPushButton(self.tab)
        self.selectBTButton.setGeometry(QtCore.QRect(310, 20, 101, 41))
        self.selectBTButton.setMinimumSize(QtCore.QSize(101, 41))
        self.selectBTButton.setMaximumSize(QtCore.QSize(16777215, 41))
        self.selectBTButton.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.selectBTButton.setObjectName("selectBTButton")
        self.label_29 = QtWidgets.QLabel(self.tab)
        self.label_29.setGeometry(QtCore.QRect(370, 120, 81, 16))
        self.label_29.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_29.setObjectName("label_29")
        self.AccSamplingBox = QtWidgets.QTextEdit(self.tab)
        self.AccSamplingBox.setGeometry(QtCore.QRect(100, 150, 71, 31))
        self.AccSamplingBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AccSamplingBox.setObjectName("AccSamplingBox")
        self.label_30 = QtWidgets.QLabel(self.tab)
        self.label_30.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_30.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(10, 210, 91, 16))
        self.label_31.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_31.setObjectName("label_31")
        self.AccSensibilityBox = QtWidgets.QTextEdit(self.tab)
        self.AccSensibilityBox.setGeometry(QtCore.QRect(100, 200, 71, 31))
        self.AccSensibilityBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AccSensibilityBox.setObjectName("AccSensibilityBox")
        self.GyroSensibilityBox = QtWidgets.QTextEdit(self.tab)
        self.GyroSensibilityBox.setGeometry(QtCore.QRect(100, 250, 71, 31))
        self.GyroSensibilityBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GyroSensibilityBox.setObjectName("GyroSensibilityBox")
        self.label_39 = QtWidgets.QLabel(self.tab)
        self.label_39.setGeometry(QtCore.QRect(10, 260, 91, 16))
        self.label_39.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_39.setObjectName("label_39")
        self.label_41 = QtWidgets.QLabel(self.tab)
        self.label_41.setGeometry(QtCore.QRect(200, 160, 111, 16))
        self.label_41.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_41.setObjectName("label_41")
        self.BME688SamplingBox = QtWidgets.QTextEdit(self.tab)
        self.BME688SamplingBox.setGeometry(QtCore.QRect(310, 150, 71, 31))
        self.BME688SamplingBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BME688SamplingBox.setObjectName("BME688SamplingBox")
        self.label_42 = QtWidgets.QLabel(self.tab)
        self.label_42.setGeometry(QtCore.QRect(200, 210, 111, 16))
        self.label_42.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_42.setObjectName("label_42")
        self.discontinuosTimeBox = QtWidgets.QTextEdit(self.tab)
        self.discontinuosTimeBox.setGeometry(QtCore.QRect(310, 200, 71, 31))
        self.discontinuosTimeBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.discontinuosTimeBox.setObjectName("discontinuosTimeBox")
        self.portTCPBox = QtWidgets.QTextEdit(self.tab)
        self.portTCPBox.setGeometry(QtCore.QRect(310, 250, 71, 31))
        self.portTCPBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.portTCPBox.setObjectName("portTCPBox")
        self.label_54 = QtWidgets.QLabel(self.tab)
        self.label_54.setGeometry(QtCore.QRect(240, 260, 61, 16))
        self.label_54.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.tab)
        self.label_55.setGeometry(QtCore.QRect(430, 160, 51, 16))
        self.label_55.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_55.setObjectName("label_55")
        self.portUDPBox = QtWidgets.QTextEdit(self.tab)
        self.portUDPBox.setGeometry(QtCore.QRect(500, 150, 71, 31))
        self.portUDPBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.portUDPBox.setObjectName("portUDPBox")
        self.hostIPAddrBox = QtWidgets.QTextEdit(self.tab)
        self.hostIPAddrBox.setGeometry(QtCore.QRect(500, 200, 71, 31))
        self.hostIPAddrBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hostIPAddrBox.setObjectName("hostIPAddrBox")
        self.label_70 = QtWidgets.QLabel(self.tab)
        self.label_70.setGeometry(QtCore.QRect(410, 210, 81, 16))
        self.label_70.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_70.setObjectName("label_70")
        self.ssidBox = QtWidgets.QTextEdit(self.tab)
        self.ssidBox.setGeometry(QtCore.QRect(630, 150, 131, 31))
        self.ssidBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ssidBox.setObjectName("ssidBox")
        self.label_86 = QtWidgets.QLabel(self.tab)
        self.label_86.setGeometry(QtCore.QRect(590, 160, 31, 16))
        self.label_86.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_86.setObjectName("label_86")
        self.label_87 = QtWidgets.QLabel(self.tab)
        self.label_87.setGeometry(QtCore.QRect(590, 210, 31, 16))
        self.label_87.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_87.setObjectName("label_87")
        self.passBox = QtWidgets.QTextEdit(self.tab)
        self.passBox.setGeometry(QtCore.QRect(630, 200, 131, 31))
        self.passBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passBox.setObjectName("passBox")
        self.saveConfButton = QtWidgets.QPushButton(self.tab)
        self.saveConfButton.setGeometry(QtCore.QRect(540, 300, 161, 41))
        self.saveConfButton.setMinimumSize(QtCore.QSize(101, 41))
        self.saveConfButton.setStyleSheet("color: rgb(213, 213, 213);\n"
"background-color: rgb(0, 115, 0);\n"
"")
        self.saveConfButton.setObjectName("saveConfButton")
        self.label_28 = QtWidgets.QLabel(self.tab)
        self.label_28.setGeometry(QtCore.QRect(310, 310, 121, 16))
        self.label_28.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_28.setObjectName("label_28")
        self.protocolIDBox = QtWidgets.QComboBox(self.tab)
        self.protocolIDBox.setGeometry(QtCore.QRect(310, 340, 71, 31))
        self.protocolIDBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.protocolIDBox.setObjectName("protocolIDBox")
        self.protocolIDBox.addItem("")
        self.startMonitoringButton = QtWidgets.QPushButton(self.tab)
        self.startMonitoringButton.setGeometry(QtCore.QRect(180, 400, 161, 41))
        self.startMonitoringButton.setMinimumSize(QtCore.QSize(101, 41))
        self.startMonitoringButton.setStyleSheet("color: rgb(213, 213, 213);\n"
"background-color: rgb(0, 115, 0);\n"
"")
        self.startMonitoringButton.setObjectName("startMonitoringButton")
        self.stopMonitoringButton = QtWidgets.QPushButton(self.tab)
        self.stopMonitoringButton.setGeometry(QtCore.QRect(380, 400, 151, 41))
        self.stopMonitoringButton.setMinimumSize(QtCore.QSize(101, 41))
        self.stopMonitoringButton.setStyleSheet("color: rgb(213, 213, 213);\n"
"background-color: rgb(108, 5, 5);\n"
"")
        self.stopMonitoringButton.setObjectName("stopMonitoringButton")
        self.operationModeBox = QtWidgets.QComboBox(self.tab)
        self.operationModeBox.setGeometry(QtCore.QRect(35, 340, 200, 31))
        self.operationModeBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.operationModeBox.setObjectName("operationModeBox_1")
        self.operationModeBox.addItem("")
        self.operationModeBox.addItem("")
        self.operationModeBox.addItem("")
        self.operationModeBox.addItem("")
        self.operationModeBox.addItem("")
        self.operationModeBox.addItem("")
        self.operationModeBox.addItem("")
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setGeometry(QtCore.QRect(70, 310, 121, 16))
        self.label_26.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_26.setObjectName("label_26")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.plot1 = pg.GraphicsLayoutWidget(self.tab_2)
        self.plot1.setGeometry(QtCore.QRect(-10, 30, 501, 141))
        self.plot1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plot1.setObjectName("plot1")
        self.plot2 = pg.GraphicsLayoutWidget(self.tab_2)
        self.plot2.setGeometry(QtCore.QRect(-10, 180, 501, 141))
        self.plot2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plot2.setObjectName("plot2")
        self.plot3 = pg.GraphicsLayoutWidget(self.tab_2)
        self.plot3.setGeometry(QtCore.QRect(0, 330, 491, 141))
        self.plot3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plot3.setObjectName("plot3")
        self.startPlotButton = QtWidgets.QPushButton(self.tab_2)
        self.startPlotButton.setGeometry(QtCore.QRect(540, 100, 101, 41))
        self.startPlotButton.setMinimumSize(QtCore.QSize(101, 41))
        self.startPlotButton.setStyleSheet("color: rgb(213, 213, 213);\n"
"background-color: rgb(0, 115, 0);\n"
"")
        self.startPlotButton.setObjectName("startPlotButton")
        self.stopPlotButton = QtWidgets.QPushButton(self.tab_2)
        self.stopPlotButton.setGeometry(QtCore.QRect(650, 100, 101, 41))
        self.stopPlotButton.setMinimumSize(QtCore.QSize(101, 41))
        self.stopPlotButton.setStyleSheet("color: rgb(213, 213, 213);\n"
"background-color: rgb(108, 5, 5);\n"
"")
        self.stopPlotButton.setObjectName("stopPlotButton")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(500, 60, 71, 20))
        self.label_23.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_23.setObjectName("label_23")
        self.selectVariableBox = QtWidgets.QComboBox(self.tab_2)
        self.selectVariableBox.setGeometry(QtCore.QRect(560, 60, 61, 21))
        self.selectVariableBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selectVariableBox.setObjectName("selectVariableBox")
        self.selectVariableBox.addItem("")
        self.selectVariableBox.addItem("")
        self.selectVariableBox.addItem("")
        self.selectVariableBox.addItem("")
        self.selectVariableBox.addItem("")
        self.selectVariableBox.addItem("")
        self.selectVariableBox.addItem("")
        self.selectVariableBox.addItem("")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(640, 60, 71, 20))
        self.label_25.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_25.setObjectName("label_25")
        self.selectPlotBox = QtWidgets.QComboBox(self.tab_2)
        self.selectPlotBox.setGeometry(QtCore.QRect(720, 60, 61, 21))
        self.selectPlotBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selectPlotBox.setObjectName("selectPlotBox")
        self.selectPlotBox.addItem("")
        self.selectPlotBox.addItem("")
        self.selectPlotBox.addItem("")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #### IMPLEMENTACION PROPIA

        self.protocol_list = [Protocol0, Protocol1, Protocol2, Protocol3, Protocol4, Protocol5]
        self.protocol = None  # Protocolo al monitorear - Guardado al conectar
        self.started_monitoring = False  # Al pulsar iniciar monitoreo
        self.device = None
        self.deviceUUID = "0000ff01-0000-1000-8000-00805F9B34FB"
        self.mac = None

        self.STATUS_DICT = {
            "Configuracion por Bluetooth": 0,
            "Configuracion via TCP en BD": 20,
            "Conexion TCP continua": 21,
            "Conexion TCP discontinua": 22,
            "Conexion UDP": 23,
            "BLE continua": 30,
            "BLE discontinua": 31
        }
        
        self.time_data = np.zeros(20)  # Eje X
        self.battery_data = np.zeros(20)
        self.temp_data = np.zeros(20)
        self.press_data = np.zeros(20)
        self.hum_data = np.zeros(20)
        self.co_data = np.zeros(20)
        self.RMS_data = np.zeros(20)
        self.Amp_x_data = np.zeros(20)
        self.Frec_x_data = np.zeros(20)
        self.Amp_y_data = np.zeros(20)
        self.Frec_y_data = np.zeros(20)
        self.Amp_z_data = np.zeros(20)
        self.Frec_z_data = np.zeros(20)
        self.Acc_x_data = np.zeros(20)
        self.Acc_y_data = np.zeros(20)
        self.Acc_z_data = np.zeros(20)

        self.searchBTButton.clicked.connect(lambda  x: searchConnectionBT(self))
        self.selectBTButton.clicked.connect(lambda  x: connectBT(self))
        self.saveConfButton.clicked.connect(lambda  x: saveConfiguration(self))
        self.startPlotButton.clicked.connect(self.startPlot)
        self.stopPlotButton.clicked.connect(self.stopPlot)
        self.startMonitoringButton.clicked.connect(self.startMonitoring)
        self.stopMonitoringButton.clicked.connect(self.stopMonitoring)


        ### PLOT
        # Aca guardaremos el array que corresponde a cada grafico
        self.plots_data = np.array(["", "", ""], dtype=object)
        self.plots_started = [False, False, False]

        self.timer = QTimer()
        self.timer.timeout.connect(self.updatePlots)
        self.timer.start(500)

        self.graph_item_1 = pg.PlotItem()
        self.plot1.addItem(self.graph_item_1)
        
        self.graph_item_2 = pg.PlotItem()
        self.plot2.addItem(self.graph_item_2)
    
        self.graph_item_3 = pg.PlotItem()
        self.plot3.addItem(self.graph_item_3)
        
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_searchBT.setText(_translate("Dialog", "Buscar dispositivos Bluetooth"))
        self.label_statusESP.setText(_translate("Dialog", "Desconectado"))
        self.searchBTButton.setText(_translate("Dialog", "Buscar BLE"))
        self.label_21.setText(_translate("Dialog", "Consola"))
        self.selectBTButton.setText(_translate("Dialog", "Conectar"))
        self.label_29.setText(_translate("Dialog", "Parametros "))
        self.label_30.setText(_translate("Dialog", "Acc Sampling"))
        self.label_31.setText(_translate("Dialog", "Acc Sensibility"))
        self.label_39.setText(_translate("Dialog", "Gyro Sensibility"))
        self.label_41.setText(_translate("Dialog", "BME688 Sampling"))
        self.label_42.setText(_translate("Dialog", "Discontinuos time"))
        self.label_54.setText(_translate("Dialog", "Port TCP"))
        self.label_55.setText(_translate("Dialog", "Port UDP"))
        self.label_70.setText(_translate("Dialog", "Host_ip_addr"))
        self.label_86.setText(_translate("Dialog", "Ssid"))
        self.label_87.setText(_translate("Dialog", "Pass"))
        self.saveConfButton.setText(_translate("Dialog", "Guardar Conf"))
        self.label_28.setText(_translate("Dialog", "ID Protocolo"))
        self.protocolIDBox.setItemText(0, _translate("Dialog", "0"))
        self.startMonitoringButton.setText(_translate("Dialog", "Iniciar Monitoreo"))
        self.stopMonitoringButton.setText(_translate("Dialog", "Detener Monitoreo"))
        self.operationModeBox.setItemText(0, _translate("Dialog", "Configuracion por Bluetooth"))
        self.operationModeBox.setItemText(1, _translate("Dialog", "Configuracion via TCP en BD"))
        self.operationModeBox.setItemText(2, _translate("Dialog", "Conexion TCP continua"))
        self.operationModeBox.setItemText(3, _translate("Dialog", "Conexion TCP discontinua"))
        self.operationModeBox.setItemText(4, _translate("Dialog", "Conexion UDP"))
        self.operationModeBox.setItemText(5, _translate("Dialog", "BLE continua"))
        self.operationModeBox.setItemText(6, _translate("Dialog", "BLE discontinua"))
        self.label_26.setText(_translate("Dialog", "Modo de operacion"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Configuracion"))
        self.startPlotButton.setText(_translate("Dialog", "Inicio"))
        self.stopPlotButton.setText(_translate("Dialog", "Detener"))
        self.label_23.setText(_translate("Dialog", "Variable"))
        self.selectVariableBox.setItemText(0, _translate("Dialog", "Temperatura"))
        self.selectVariableBox.setItemText(1, _translate("Dialog", "Humedad"))
        self.selectVariableBox.setItemText(2, _translate("Dialog", "Co"))
        self.selectVariableBox.setItemText(3, _translate("Dialog", "Presion"))
        self.selectVariableBox.setItemText(4, _translate("Dialog", "Aceleracion Eje X"))
        self.selectVariableBox.setItemText(5, _translate("Dialog", "Aceleracion Eje Y"))
        self.selectVariableBox.setItemText(6, _translate("Dialog", "Aceleracion Eje Z"))
        self.selectVariableBox.setItemText(7, _translate("Dialog", "RMS"))
        self.label_25.setText(_translate("Dialog", "Selecion plot"))
        self.selectPlotBox.setItemText(0, _translate("Dialog", "1"))
        self.selectPlotBox.setItemText(1, _translate("Dialog", "2"))
        self.selectPlotBox.setItemText(2, _translate("Dialog", "3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Visualizacion"))

    def consoleLog(self, line):
        self.consoleTextBox.setPlainText(self.consoleTextBox.toPlainText() + line + "\n")

    def updateBTList(self, devices):
        _translate = QtCore.QCoreApplication.translate
        for device in devices:
                self.selectBTComboBox.addItem(
                f"{device['name']} - {device['address']}")
        self.consoleLog(f"{len(devices)} BLE devices found")
        self.searchBTButton.setText(_translate("Dialog", "Buscar BLE"))

    def operationModeSelected(self):
        operation = self.operationModeBox.currentIndex()
        self.protocolIDBox.clear()
        if operation in [0, 1]:
            self.protocolIDBox.addItems(["0"])
        elif operation in [2, 3, 4]:
            self.protocolIDBox.addItems(["1", "2", "3", "4", "5"])
        elif operation in [5, 6]:
            self.protocolIDBox.addItems(["1", "2", "3", "4"])

    def updatePlots(self):
        updatePlots(self)

    def startPlot(self):
        plot_index = self.selectPlotBox.currentIndex()
        variable_index = self.selectVariableBox.currentIndex()
        self.consoleLog(f"Start plot {plot_index} with variable {variable_index}")

        #TODO: Que en vez de battery_data, sea segun variable_index
        self.plots_data[plot_index] = "Batt_level"
        self.plots_started[plot_index] = True

    def stopPlot(self):
        plot_index = self.selectPlotBox.currentIndex()
        self.plots_started[plot_index] = False
    
    def setProtocol(self, protocol):
        self.protocol = self.protocol_list[protocol]
        self.selectVariableBox.clear()
        if protocol == 1:
            self.selectVariableBox.addItems(["Batt_level"])
        if protocol == 2:
            self.selectVariableBox.addItems(["Batt_level", "Temp", "Press", "Hum", "Co"])
        if protocol == 3:
            self.selectVariableBox.addItems(["Batt_level", "Temp", "Press", "Hum", "Co", "RMS"])
        if protocol == 4:
            self.selectVariableBox.addItems(["Batt_level", "Temp", "Press", "Hum", "Co", "RMS",
                                                "Amp_x", "Frec_x", "Amp_y", "Frec_y", "Amp_z", "Frec_z"])
        if protocol == 5:
            self.selectVariableBox.addItems(["Batt_level", "Temp", "Press", "Hum", "Co",
                                                "Acc_x", "Acc_y", "Acc_z"])

    #TODO: Hacer que estos comiencen y finalicen el monitoreo
    # Recordar que con protocolo 0 no se puede monitorear
    def startMonitoring(self):
        if self.protocol != self.protocol_list[0]:
            self.started_monitoring = True
    def stopMonitoring(self):
        self.started_monitoring = False

    def getPlotData(self, var):
        if var == "Batt_level": return self.battery_data
        elif var == "Temp": return self.temp_data
        elif var == "Press": return self.press_data
        elif var == "Hum": return self.hum_data
        elif var == "Co": return self.co_data
        elif var == "RMS": return self.RMS_data
        elif var == "Amp_x": return self.Amp_x_data
        elif var == "Frec_x": return self.Frec_x_data
        elif var == "Amp_y": return self.Amp_y_data
        elif var == "Frec_y": return self.Frec_y_data
        elif var == "Amp_z": return self.Amp_z_data
        elif var == "Frec_z": return self.Frec_z_data
        elif var == "Acc_x": return self.Acc_x_data
        elif var == "Acc_y": return self.Acc_y_data
        elif var == "Acc_z": return self.Acc_z_data
        else: return np.zeros(20)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
