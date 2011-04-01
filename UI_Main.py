# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Main.ui'
#
# Created: Mon Jun 02 10:40:57 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,1265,947).size()).expandedTo(MainWindow.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowIcon(QtGui.QIcon("images/icon.png"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frameData = QtGui.QFrame(self.centralwidget)
        self.frameData.setEnabled(False)
        self.frameData.setGeometry(QtCore.QRect(0,340,590,570))
        self.frameData.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameData.setFrameShadow(QtGui.QFrame.Raised)
        self.frameData.setObjectName("frameData")

        self.groupBoxBremse3 = QtGui.QGroupBox(self.frameData)
        self.groupBoxBremse3.setGeometry(QtCore.QRect(10,10,141,140))
        self.groupBoxBremse3.setObjectName("groupBoxBremse3")

        self.speed_FL = QtGui.QLineEdit(self.groupBoxBremse3)
        self.speed_FL.setGeometry(QtCore.QRect(40,50,61,20))
        self.speed_FL.setReadOnly(True)
        self.speed_FL.setObjectName("speed_FL")

        self.speed_FR = QtGui.QLineEdit(self.groupBoxBremse3)
        self.speed_FR.setGeometry(QtCore.QRect(40,70,61,20))
        self.speed_FR.setReadOnly(True)
        self.speed_FR.setObjectName("speed_FR")

        self.speed_RL = QtGui.QLineEdit(self.groupBoxBremse3)
        self.speed_RL.setGeometry(QtCore.QRect(40,90,61,20))
        self.speed_RL.setReadOnly(True)
        self.speed_RL.setObjectName("speed_RL")

        self.speed_RR = QtGui.QLineEdit(self.groupBoxBremse3)
        self.speed_RR.setGeometry(QtCore.QRect(40,110,61,20))
        self.speed_RR.setReadOnly(True)
        self.speed_RR.setObjectName("speed_RR")

        self.label_2 = QtGui.QLabel(self.groupBoxBremse3)
        self.label_2.setGeometry(QtCore.QRect(10,70,16,16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtGui.QLabel(self.groupBoxBremse3)
        self.label_3.setGeometry(QtCore.QRect(10,50,16,16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtGui.QLabel(self.groupBoxBremse3)
        self.label_4.setGeometry(QtCore.QRect(10,90,20,20))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtGui.QLabel(self.groupBoxBremse3)
        self.label_5.setGeometry(QtCore.QRect(10,110,16,16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtGui.QLabel(self.groupBoxBremse3)
        self.label_6.setGeometry(QtCore.QRect(110,50,23,16))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtGui.QLabel(self.groupBoxBremse3)
        self.label_7.setGeometry(QtCore.QRect(110,70,23,16))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtGui.QLabel(self.groupBoxBremse3)
        self.label_8.setGeometry(QtCore.QRect(110,90,23,16))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtGui.QLabel(self.groupBoxBremse3)
        self.label_9.setGeometry(QtCore.QRect(110,110,23,16))
        self.label_9.setObjectName("label_9")

        self.label_28 = QtGui.QLabel(self.groupBoxBremse3)
        self.label_28.setGeometry(QtCore.QRect(10,20,16,16))
        self.label_28.setObjectName("label_28")

        self.speed_car = QtGui.QLineEdit(self.groupBoxBremse3)
        self.speed_car.setGeometry(QtCore.QRect(40,20,61,20))
        self.speed_car.setReadOnly(True)
        self.speed_car.setObjectName("speed_car")

        self.label_29 = QtGui.QLabel(self.groupBoxBremse3)
        self.label_29.setGeometry(QtCore.QRect(110,20,23,16))
        self.label_29.setObjectName("label_29")

        self.groupBoxBrake = QtGui.QGroupBox(self.frameData)
        self.groupBoxBrake.setGeometry(QtCore.QRect(160,10,250,140))
        self.groupBoxBrake.setObjectName("groupBoxBrake")

        self.label_14 = QtGui.QLabel(self.groupBoxBrake)
        self.label_14.setGeometry(QtCore.QRect(10,50,50,16))
        self.label_14.setObjectName("label_14")

        self.yaw = QtGui.QLineEdit(self.groupBoxBrake)
        self.yaw.setGeometry(QtCore.QRect(110,50,61,20))
        self.yaw.setReadOnly(True)
        self.yaw.setObjectName("yaw")

        self.label_15 = QtGui.QLabel(self.groupBoxBrake)
        self.label_15.setGeometry(QtCore.QRect(180,50,60,16))
        self.label_15.setObjectName("label_15")

        self.label_16 = QtGui.QLabel(self.groupBoxBrake)
        self.label_16.setGeometry(QtCore.QRect(10,80,80,16))
        self.label_16.setObjectName("label_16")

        self.brake = QtGui.QLineEdit(self.groupBoxBrake)
        self.brake.setGeometry(QtCore.QRect(110,80,61,20))
        self.brake.setReadOnly(True)
        self.brake.setObjectName("brake")

        self.label_17 = QtGui.QLabel(self.groupBoxBrake)
        self.label_17.setGeometry(QtCore.QRect(180,80,23,16))
        self.label_17.setObjectName("label_17")

        self.checkBoxESP = QtGui.QCheckBox(self.groupBoxBrake)
        self.checkBoxESP.setGeometry(QtCore.QRect(10,110,81,19))
        self.checkBoxESP.setCheckable(True)
        self.checkBoxESP.setObjectName("checkBoxESP")

        self.label_11 = QtGui.QLabel(self.groupBoxBrake)
        self.label_11.setGeometry(QtCore.QRect(180,20,23,16))
        self.label_11.setObjectName("label_11")

        self.lateral = QtGui.QLineEdit(self.groupBoxBrake)
        self.lateral.setGeometry(QtCore.QRect(110,20,61,20))
        self.lateral.setReadOnly(True)
        self.lateral.setObjectName("lateral")

        self.label_10 = QtGui.QLabel(self.groupBoxBrake)
        self.label_10.setGeometry(QtCore.QRect(10,20,100,16))
        self.label_10.setObjectName("label_10")

        self.MotorCurrent = QtGui.QLineEdit(self.groupBoxBrake)
        self.MotorCurrent.setGeometry(QtCore.QRect(180,110,61,20))
        self.MotorCurrent.setReadOnly(True)
        self.MotorCurrent.setObjectName("MotorCurrent")

        self.label_32 = QtGui.QLabel(self.groupBoxBrake)
        self.label_32.setGeometry(QtCore.QRect(100,110,71,21))
        self.label_32.setObjectName("label_32")

        self.groupBoxSuspension = QtGui.QGroupBox(self.frameData)
        self.groupBoxSuspension.setGeometry(QtCore.QRect(420,90,140,80))
        self.groupBoxSuspension.setObjectName("groupBoxSuspension")

        self.Front = QtGui.QLineEdit(self.groupBoxSuspension)
        self.Front.setGeometry(QtCore.QRect(40,20,61,20))
        self.Front.setReadOnly(True)
        self.Front.setObjectName("Front")

        self.Rear = QtGui.QLineEdit(self.groupBoxSuspension)
        self.Rear.setGeometry(QtCore.QRect(40,50,61,20))
        self.Rear.setReadOnly(True)
        self.Rear.setObjectName("Rear")

        self.label_26 = QtGui.QLabel(self.groupBoxSuspension)
        self.label_26.setGeometry(QtCore.QRect(10,50,40,16))
        self.label_26.setObjectName("label_26")

        self.label_27 = QtGui.QLabel(self.groupBoxSuspension)
        self.label_27.setGeometry(QtCore.QRect(10,20,40,16))
        self.label_27.setObjectName("label_27")

        self.label_30 = QtGui.QLabel(self.groupBoxSuspension)
        self.label_30.setGeometry(QtCore.QRect(110,20,23,16))
        self.label_30.setObjectName("label_30")

        self.label_31 = QtGui.QLabel(self.groupBoxSuspension)
        self.label_31.setGeometry(QtCore.QRect(110,50,23,16))
        self.label_31.setObjectName("label_31")

        self.groupBoxMisc = QtGui.QGroupBox(self.frameData)
        self.groupBoxMisc.setGeometry(QtCore.QRect(10,150,350,110))
        self.groupBoxMisc.setObjectName("groupBoxMisc")

        self.ClutchStiffness = QtGui.QLineEdit(self.groupBoxMisc)
        self.ClutchStiffness.setGeometry(QtCore.QRect(240,20,61,20))
        self.ClutchStiffness.setReadOnly(True)
        self.ClutchStiffness.setObjectName("ClutchStiffness")

        self.label_38 = QtGui.QLabel(self.groupBoxMisc)
        self.label_38.setGeometry(QtCore.QRect(20,20,210,20))
        self.label_38.setObjectName("label_38")

        self.label_39 = QtGui.QLabel(self.groupBoxMisc)
        self.label_39.setGeometry(QtCore.QRect(310,50,60,16))
        self.label_39.setObjectName("label_39")

        self.label_40 = QtGui.QLabel(self.groupBoxMisc)
        self.label_40.setGeometry(QtCore.QRect(310,80,23,16))
        self.label_40.setObjectName("label_40")

        self.label_41 = QtGui.QLabel(self.groupBoxMisc)
        self.label_41.setGeometry(QtCore.QRect(310,20,23,16))
        self.label_41.setObjectName("label_41")

        self.label_42 = QtGui.QLabel(self.groupBoxMisc)
        self.label_42.setGeometry(QtCore.QRect(20,80,180,16))
        self.label_42.setObjectName("label_42")

        self.ClutchValue = QtGui.QLineEdit(self.groupBoxMisc)
        self.ClutchValue.setGeometry(QtCore.QRect(240,80,61,20))
        self.ClutchValue.setReadOnly(True)
        self.ClutchValue.setObjectName("ClutchValue")

        self.label_43 = QtGui.QLabel(self.groupBoxMisc)
        self.label_43.setGeometry(QtCore.QRect(20,50,190,16))
        self.label_43.setObjectName("label_43")

        self.SteeringTorque = QtGui.QLineEdit(self.groupBoxMisc)
        self.SteeringTorque.setGeometry(QtCore.QRect(240,50,61,20))
        self.SteeringTorque.setReadOnly(True)
        self.SteeringTorque.setObjectName("SteeringTorque")

        self.groupBoxSteering = QtGui.QGroupBox(self.frameData)
        self.groupBoxSteering.setGeometry(QtCore.QRect(420,10,161,80))
        self.groupBoxSteering.setObjectName("groupBoxSteering")

        self.label_34 = QtGui.QLabel(self.groupBoxSteering)
        self.label_34.setGeometry(QtCore.QRect(10,20,50,16))
        self.label_34.setObjectName("label_34")

        self.Torque = QtGui.QLineEdit(self.groupBoxSteering)
        self.Torque.setGeometry(QtCore.QRect(50,20,61,20))
        self.Torque.setReadOnly(True)
        self.Torque.setObjectName("Torque")

        self.label_35 = QtGui.QLabel(self.groupBoxSteering)
        self.label_35.setGeometry(QtCore.QRect(120,20,30,16))
        self.label_35.setObjectName("label_35")

        self.label_36 = QtGui.QLabel(self.groupBoxSteering)
        self.label_36.setGeometry(QtCore.QRect(10,50,40,16))
        self.label_36.setObjectName("label_36")

        self.Angle = QtGui.QLineEdit(self.groupBoxSteering)
        self.Angle.setGeometry(QtCore.QRect(50,50,61,20))
        self.Angle.setReadOnly(True)
        self.Angle.setObjectName("Angle")

        self.label_37 = QtGui.QLabel(self.groupBoxSteering)
        self.label_37.setGeometry(QtCore.QRect(120,50,40,16))
        self.label_37.setObjectName("label_37")

        self.groupBoxEngine = QtGui.QGroupBox(self.frameData)
        self.groupBoxEngine.setGeometry(QtCore.QRect(370,180,210,80))
        self.groupBoxEngine.setObjectName("groupBoxEngine")

        self.label_44 = QtGui.QLabel(self.groupBoxEngine)
        self.label_44.setGeometry(QtCore.QRect(10,20,90,16))
        self.label_44.setObjectName("label_44")

        self.IntTorque = QtGui.QLineEdit(self.groupBoxEngine)
        self.IntTorque.setGeometry(QtCore.QRect(90,20,60,20))
        self.IntTorque.setReadOnly(True)
        self.IntTorque.setObjectName("IntTorque")

        self.label_45 = QtGui.QLabel(self.groupBoxEngine)
        self.label_45.setGeometry(QtCore.QRect(160,20,40,16))
        self.label_45.setObjectName("label_45")

        self.label_46 = QtGui.QLabel(self.groupBoxEngine)
        self.label_46.setGeometry(QtCore.QRect(10,50,80,16))
        self.label_46.setObjectName("label_46")

        self.TorqueLoss = QtGui.QLineEdit(self.groupBoxEngine)
        self.TorqueLoss.setGeometry(QtCore.QRect(90,50,60,20))
        self.TorqueLoss.setReadOnly(True)
        self.TorqueLoss.setObjectName("TorqueLoss")

        self.label_47 = QtGui.QLabel(self.groupBoxEngine)
        self.label_47.setGeometry(QtCore.QRect(160,50,40,16))
        self.label_47.setObjectName("label_47")

        self.groupBox501 = QtGui.QGroupBox(self.frameData)
        self.groupBox501.setGeometry(QtCore.QRect(10,270,371,80))
        self.groupBox501.setObjectName("groupBox501")

        self.ddl_timestamp = QtGui.QLineEdit(self.groupBox501)
        self.ddl_timestamp.setGeometry(QtCore.QRect(70,20,70,20))
        self.ddl_timestamp.setReadOnly(True)
        self.ddl_timestamp.setObjectName("ddl_timestamp")

        self.label_21 = QtGui.QLabel(self.groupBox501)
        self.label_21.setGeometry(QtCore.QRect(150,20,23,16))
        self.label_21.setObjectName("label_21")

        self.label_22 = QtGui.QLabel(self.groupBox501)
        self.label_22.setGeometry(QtCore.QRect(10,20,70,16))
        self.label_22.setObjectName("label_22")

        self.led_status = QtGui.QLineEdit(self.groupBox501)
        self.led_status.setGeometry(QtCore.QRect(70,50,20,20))
        self.led_status.setReadOnly(True)
        self.led_status.setObjectName("led_status")

        self.label_23 = QtGui.QLabel(self.groupBox501)
        self.label_23.setGeometry(QtCore.QRect(10,50,70,16))
        self.label_23.setObjectName("label_23")

        self.label_24 = QtGui.QLabel(self.groupBox501)
        self.label_24.setGeometry(QtCore.QRect(180,50,120,16))
        self.label_24.setObjectName("label_24")

        self.model_version = QtGui.QLineEdit(self.groupBox501)
        self.model_version.setGeometry(QtCore.QRect(300,50,60,20))
        self.model_version.setReadOnly(True)
        self.model_version.setObjectName("model_version")

        self.label_25 = QtGui.QLabel(self.groupBox501)
        self.label_25.setGeometry(QtCore.QRect(180,20,60,16))
        self.label_25.setObjectName("label_25")

        self.save_date = QtGui.QLineEdit(self.groupBox501)
        self.save_date.setGeometry(QtCore.QRect(240,20,120,20))
        self.save_date.setReadOnly(True)
        self.save_date.setObjectName("save_date")

        self.groupBox502 = QtGui.QGroupBox(self.frameData)
        self.groupBox502.setGeometry(QtCore.QRect(10,360,260,80))
        self.groupBox502.setObjectName("groupBox502")

        self.yawAngle = QtGui.QLineEdit(self.groupBox502)
        self.yawAngle.setGeometry(QtCore.QRect(70,20,60,20))
        self.yawAngle.setReadOnly(True)
        self.yawAngle.setObjectName("yawAngle")

        self.label_50 = QtGui.QLabel(self.groupBox502)
        self.label_50.setGeometry(QtCore.QRect(10,20,70,16))
        self.label_50.setObjectName("label_50")

        self.rollAngle = QtGui.QLineEdit(self.groupBox502)
        self.rollAngle.setGeometry(QtCore.QRect(190,20,60,20))
        self.rollAngle.setReadOnly(True)
        self.rollAngle.setObjectName("rollAngle")

        self.label_51 = QtGui.QLabel(self.groupBox502)
        self.label_51.setGeometry(QtCore.QRect(140,20,50,16))
        self.label_51.setObjectName("label_51")

        self.label_52 = QtGui.QLabel(self.groupBox502)
        self.label_52.setGeometry(QtCore.QRect(10,50,50,16))
        self.label_52.setObjectName("label_52")

        self.yawRate = QtGui.QLineEdit(self.groupBox502)
        self.yawRate.setGeometry(QtCore.QRect(70,50,60,20))
        self.yawRate.setReadOnly(True)
        self.yawRate.setObjectName("yawRate")

        self.label_53 = QtGui.QLabel(self.groupBox502)
        self.label_53.setGeometry(QtCore.QRect(140,50,50,16))
        self.label_53.setObjectName("label_53")

        self.rollRate = QtGui.QLineEdit(self.groupBox502)
        self.rollRate.setGeometry(QtCore.QRect(190,50,60,20))
        self.rollRate.setReadOnly(True)
        self.rollRate.setObjectName("rollRate")

        self.groupBox503 = QtGui.QGroupBox(self.frameData)
        self.groupBox503.setGeometry(QtCore.QRect(280,360,230,80))
        self.groupBox503.setObjectName("groupBox503")

        self.vx = QtGui.QLineEdit(self.groupBox503)
        self.vx.setGeometry(QtCore.QRect(50,20,60,20))
        self.vx.setReadOnly(True)
        self.vx.setObjectName("vx")

        self.label_54 = QtGui.QLabel(self.groupBox503)
        self.label_54.setGeometry(QtCore.QRect(10,20,50,16))
        self.label_54.setObjectName("label_54")

        self.vyCG = QtGui.QLineEdit(self.groupBox503)
        self.vyCG.setGeometry(QtCore.QRect(160,20,60,20))
        self.vyCG.setReadOnly(True)
        self.vyCG.setObjectName("vyCG")

        self.label_55 = QtGui.QLabel(self.groupBox503)
        self.label_55.setGeometry(QtCore.QRect(120,20,30,16))
        self.label_55.setObjectName("label_55")

        self.label_56 = QtGui.QLabel(self.groupBox503)
        self.label_56.setGeometry(QtCore.QRect(10,50,30,16))
        self.label_56.setObjectName("label_56")

        self.axCG = QtGui.QLineEdit(self.groupBox503)
        self.axCG.setGeometry(QtCore.QRect(50,50,60,20))
        self.axCG.setReadOnly(True)
        self.axCG.setObjectName("axCG")

        self.label_57 = QtGui.QLabel(self.groupBox503)
        self.label_57.setGeometry(QtCore.QRect(120,50,30,16))
        self.label_57.setObjectName("label_57")

        self.ayCG = QtGui.QLineEdit(self.groupBox503)
        self.ayCG.setGeometry(QtCore.QRect(160,50,60,20))
        self.ayCG.setReadOnly(True)
        self.ayCG.setObjectName("ayCG")

        self.groupBox504 = QtGui.QGroupBox(self.frameData)
        self.groupBox504.setGeometry(QtCore.QRect(390,270,120,80))
        self.groupBox504.setObjectName("groupBox504")

        self.PosE = QtGui.QLineEdit(self.groupBox504)
        self.PosE.setGeometry(QtCore.QRect(50,20,60,20))
        self.PosE.setReadOnly(True)
        self.PosE.setObjectName("PosE")

        self.label_58 = QtGui.QLabel(self.groupBox504)
        self.label_58.setGeometry(QtCore.QRect(10,20,50,16))
        self.label_58.setObjectName("label_58")

        self.label_60 = QtGui.QLabel(self.groupBox504)
        self.label_60.setGeometry(QtCore.QRect(10,50,30,16))
        self.label_60.setObjectName("label_60")

        self.PosN = QtGui.QLineEdit(self.groupBox504)
        self.PosN.setGeometry(QtCore.QRect(50,50,60,20))
        self.PosN.setReadOnly(True)
        self.PosN.setObjectName("PosN")

        self.groupBox505 = QtGui.QGroupBox(self.frameData)
        self.groupBox505.setGeometry(QtCore.QRect(10,450,150,110))
        self.groupBox505.setObjectName("groupBox505")

        self.sideslip = QtGui.QLineEdit(self.groupBox505)
        self.sideslip.setGeometry(QtCore.QRect(70,20,60,20))
        self.sideslip.setReadOnly(True)
        self.sideslip.setObjectName("sideslip")

        self.label_64 = QtGui.QLabel(self.groupBox505)
        self.label_64.setGeometry(QtCore.QRect(10,20,70,16))
        self.label_64.setObjectName("label_64")

        self.label_66 = QtGui.QLabel(self.groupBox505)
        self.label_66.setGeometry(QtCore.QRect(10,50,50,16))
        self.label_66.setObjectName("label_66")

        self.rawIpitch = QtGui.QLineEdit(self.groupBox505)
        self.rawIpitch.setGeometry(QtCore.QRect(70,50,60,20))
        self.rawIpitch.setReadOnly(True)
        self.rawIpitch.setObjectName("rawIpitch")

        self.label_67 = QtGui.QLabel(self.groupBox505)
        self.label_67.setGeometry(QtCore.QRect(10,80,50,16))
        self.label_67.setObjectName("label_67")

        self.rawIaz = QtGui.QLineEdit(self.groupBox505)
        self.rawIaz.setGeometry(QtCore.QRect(70,80,60,20))
        self.rawIaz.setReadOnly(True)
        self.rawIaz.setObjectName("rawIaz")

        self.groupBox506 = QtGui.QGroupBox(self.frameData)
        self.groupBox506.setGeometry(QtCore.QRect(170,450,340,110))
        self.groupBox506.setObjectName("groupBox506")

        self.LFDuration = QtGui.QLineEdit(self.groupBox506)
        self.LFDuration.setGeometry(QtCore.QRect(90,20,60,20))
        self.LFDuration.setReadOnly(True)
        self.LFDuration.setObjectName("LFDuration")

        self.label_65 = QtGui.QLabel(self.groupBox506)
        self.label_65.setGeometry(QtCore.QRect(10,20,80,16))
        self.label_65.setObjectName("label_65")

        self.label_68 = QtGui.QLabel(self.groupBox506)
        self.label_68.setGeometry(QtCore.QRect(10,50,70,16))
        self.label_68.setObjectName("label_68")

        self.LRDuration = QtGui.QLineEdit(self.groupBox506)
        self.LRDuration.setGeometry(QtCore.QRect(90,50,60,20))
        self.LRDuration.setReadOnly(True)
        self.LRDuration.setObjectName("LRDuration")

        self.label_69 = QtGui.QLabel(self.groupBox506)
        self.label_69.setGeometry(QtCore.QRect(10,80,70,16))
        self.label_69.setObjectName("label_69")

        self.LeftTieRod = QtGui.QLineEdit(self.groupBox506)
        self.LeftTieRod.setGeometry(QtCore.QRect(90,80,60,20))
        self.LeftTieRod.setReadOnly(True)
        self.LeftTieRod.setObjectName("LeftTieRod")

        self.label_70 = QtGui.QLabel(self.groupBox506)
        self.label_70.setGeometry(QtCore.QRect(190,20,80,16))
        self.label_70.setObjectName("label_70")

        self.RRDuration = QtGui.QLineEdit(self.groupBox506)
        self.RRDuration.setGeometry(QtCore.QRect(260,50,60,20))
        self.RRDuration.setReadOnly(True)
        self.RRDuration.setObjectName("RRDuration")

        self.RightTieRod = QtGui.QLineEdit(self.groupBox506)
        self.RightTieRod.setGeometry(QtCore.QRect(260,80,60,20))
        self.RightTieRod.setReadOnly(True)
        self.RightTieRod.setObjectName("RightTieRod")

        self.label_71 = QtGui.QLabel(self.groupBox506)
        self.label_71.setGeometry(QtCore.QRect(190,50,70,16))
        self.label_71.setObjectName("label_71")

        self.RFDuration = QtGui.QLineEdit(self.groupBox506)
        self.RFDuration.setGeometry(QtCore.QRect(260,20,60,20))
        self.RFDuration.setReadOnly(True)
        self.RFDuration.setObjectName("RFDuration")

        self.label_72 = QtGui.QLabel(self.groupBox506)
        self.label_72.setGeometry(QtCore.QRect(190,80,70,16))
        self.label_72.setObjectName("label_72")

        self.framePlot = QtGui.QFrame(self.centralwidget)
        self.framePlot.setEnabled(False)
        self.framePlot.setGeometry(QtCore.QRect(600,10,660,391))
        self.framePlot.setFrameShape(QtGui.QFrame.StyledPanel)
        self.framePlot.setFrameShadow(QtGui.QFrame.Raised)
        self.framePlot.setObjectName("framePlot")

        self.comboSelectData = QtGui.QComboBox(self.framePlot)
        self.comboSelectData.setGeometry(QtCore.QRect(10,360,231,22))
        self.comboSelectData.setObjectName("comboSelectData")

        self.frameImage = QtGui.QFrame(self.centralwidget)
        self.frameImage.setEnabled(True)
        self.frameImage.setGeometry(QtCore.QRect(600,410,660,500))
        self.frameImage.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameImage.setFrameShadow(QtGui.QFrame.Raised)
        self.frameImage.setObjectName("frameImage")

        self.labelFrame = QtGui.QLabel(self.frameImage)
        self.labelFrame.setEnabled(True)
        self.labelFrame.setGeometry(QtCore.QRect(10,10,640,480))
        self.labelFrame.setObjectName("labelFrame")

        self.frameControl = QtGui.QFrame(self.centralwidget)
        self.frameControl.setGeometry(QtCore.QRect(0,10,590,230))
        self.frameControl.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameControl.setFrameShadow(QtGui.QFrame.Raised)
        self.frameControl.setObjectName("frameControl")

        self.ButtonQuit = QtGui.QPushButton(self.frameControl)
        self.ButtonQuit.setGeometry(QtCore.QRect(500,190,75,24))
        self.ButtonQuit.setObjectName("ButtonQuit")

        self.groupBoxDataFile = QtGui.QGroupBox(self.frameControl)
        self.groupBoxDataFile.setGeometry(QtCore.QRect(10,10,570,80))
        self.groupBoxDataFile.setObjectName("groupBoxDataFile")

        self.lineEditFile = QtGui.QLineEdit(self.groupBoxDataFile)
        self.lineEditFile.setGeometry(QtCore.QRect(10,20,550,20))
        self.lineEditFile.setReadOnly(True)
        self.lineEditFile.setObjectName("lineEditFile")

        self.ButtonLoadFile = QtGui.QToolButton(self.groupBoxDataFile)
        self.ButtonLoadFile.setGeometry(QtCore.QRect(10,50,100,24))
        self.ButtonLoadFile.setObjectName("ButtonLoadFile")

        self.groupBoxVideo = QtGui.QGroupBox(self.frameControl)
        self.groupBoxVideo.setEnabled(False)
        self.groupBoxVideo.setGeometry(QtCore.QRect(10,100,570,80))
        self.groupBoxVideo.setObjectName("groupBoxVideo")

        self.lineEditVideo = QtGui.QLineEdit(self.groupBoxVideo)
        self.lineEditVideo.setGeometry(QtCore.QRect(10,20,550,20))
        self.lineEditVideo.setReadOnly(True)
        self.lineEditVideo.setObjectName("lineEditVideo")

        self.ButtonEnableVideo = QtGui.QToolButton(self.groupBoxVideo)
        self.ButtonEnableVideo.setEnabled(False)
        self.ButtonEnableVideo.setGeometry(QtCore.QRect(120,50,100,24))
        self.ButtonEnableVideo.setObjectName("ButtonEnableVideo")

        self.ButtonDisableVideo = QtGui.QToolButton(self.groupBoxVideo)
        self.ButtonDisableVideo.setEnabled(False)
        self.ButtonDisableVideo.setGeometry(QtCore.QRect(230,50,100,24))
        self.ButtonDisableVideo.setObjectName("ButtonDisableVideo")

        self.ButtonLoadVideo = QtGui.QToolButton(self.groupBoxVideo)
        self.ButtonLoadVideo.setEnabled(False)
        self.ButtonLoadVideo.setGeometry(QtCore.QRect(10,50,100,24))
        self.ButtonLoadVideo.setObjectName("ButtonLoadVideo")

        self.ButtonPause = QtGui.QPushButton(self.groupBoxVideo)
        self.ButtonPause.setEnabled(False)
        self.ButtonPause.setGeometry(QtCore.QRect(440,50,75,24))
        self.ButtonPause.setObjectName("ButtonPause")

        self.ButtonPlay = QtGui.QPushButton(self.groupBoxVideo)
        self.ButtonPlay.setEnabled(False)
        self.ButtonPlay.setGeometry(QtCore.QRect(360,50,75,24))
        self.ButtonPlay.setObjectName("ButtonPlay")

        self.InfoButton = QtGui.QPushButton(self.frameControl)
        self.InfoButton.setGeometry(QtCore.QRect(420,190,75,24))
        self.InfoButton.setObjectName("InfoButton")

        self.frameSelect = QtGui.QFrame(self.centralwidget)
        self.frameSelect.setEnabled(True)
        self.frameSelect.setGeometry(QtCore.QRect(0,250,590,80))
        self.frameSelect.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameSelect.setFrameShadow(QtGui.QFrame.Raised)
        self.frameSelect.setObjectName("frameSelect")

        self.label = QtGui.QLabel(self.frameSelect)
        self.label.setGeometry(QtCore.QRect(10,20,46,20))
        self.label.setObjectName("label")

        self.timestampBox = QtGui.QLineEdit(self.frameSelect)
        self.timestampBox.setGeometry(QtCore.QRect(350,20,80,20))
        self.timestampBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timestampBox.setReadOnly(True)
        self.timestampBox.setObjectName("timestampBox")

        self.label_12 = QtGui.QLabel(self.frameSelect)
        self.label_12.setGeometry(QtCore.QRect(150,20,46,20))
        self.label_12.setObjectName("label_12")

        self.timeBox = QtGui.QLineEdit(self.frameSelect)
        self.timeBox.setGeometry(QtCore.QRect(190,20,80,20))
        self.timeBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeBox.setReadOnly(True)
        self.timeBox.setObjectName("timeBox")

        self.spinBoxFrame = QtGui.QSpinBox(self.frameSelect)
        self.spinBoxFrame.setGeometry(QtCore.QRect(60,20,80,22))
        self.spinBoxFrame.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxFrame.setAccelerated(True)
        self.spinBoxFrame.setObjectName("spinBoxFrame")

        self.horizontalSlider = QtGui.QSlider(self.frameSelect)
        self.horizontalSlider.setGeometry(QtCore.QRect(10,50,570,20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.label_18 = QtGui.QLabel(self.frameSelect)
        self.label_18.setGeometry(QtCore.QRect(440,20,20,20))
        self.label_18.setObjectName("label_18")

        self.label_13 = QtGui.QLabel(self.frameSelect)
        self.label_13.setGeometry(QtCore.QRect(280,20,70,20))
        self.label_13.setObjectName("label_13")

        self.diffBox = QtGui.QLineEdit(self.frameSelect)
        self.diffBox.setGeometry(QtCore.QRect(500,20,60,20))
        self.diffBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.diffBox.setReadOnly(True)
        self.diffBox.setObjectName("diffBox")

        self.label_20 = QtGui.QLabel(self.frameSelect)
        self.label_20.setGeometry(QtCore.QRect(470,20,30,20))
        self.label_20.setObjectName("label_20")

        self.label_19 = QtGui.QLabel(self.frameSelect)
        self.label_19.setGeometry(QtCore.QRect(570,20,20,20))
        self.label_19.setObjectName("label_19")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,1265,21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.ButtonQuit,QtCore.SIGNAL("clicked()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "VW ERL :: Data Analyzer", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxBremse3.setTitle(QtGui.QApplication.translate("MainWindow", "Wheelspeed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "FR", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "FL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "RL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "RR", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "km/h", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "km/h", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "km/h", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "km/h", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("MainWindow", "Car", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("MainWindow", "km/h", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxBrake.setTitle(QtGui.QApplication.translate("MainWindow", "Brake and ESP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Yaw rate:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "degree/sec", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Brake pressure:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "bar", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxESP.setText(QtGui.QApplication.translate("MainWindow", "ESP status ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Lateral acceleration:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("MainWindow", "Motor Current", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxSuspension.setTitle(QtGui.QApplication.translate("MainWindow", "Suspension deflection", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("MainWindow", "Rear", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("MainWindow", "Front", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("MainWindow", "mm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("MainWindow", "mm", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxMisc.setTitle(QtGui.QApplication.translate("MainWindow", "Misc", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(QtGui.QApplication.translate("MainWindow", "Desired center differential clutch stiffness", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setText(QtGui.QApplication.translate("MainWindow", "Nm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setText(QtGui.QApplication.translate("MainWindow", "Nm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_41.setText(QtGui.QApplication.translate("MainWindow", "Nm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("MainWindow", "Actual center differential clutch value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("MainWindow", "Demanded steering torque from ESP", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxSteering.setTitle(QtGui.QApplication.translate("MainWindow", "Steering", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("MainWindow", "Torque", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("MainWindow", "Nm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("MainWindow", "Angle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("MainWindow", "degree", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxEngine.setTitle(QtGui.QApplication.translate("MainWindow", "Engine", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate("MainWindow", "Internal torque", None, QtGui.QApplication.UnicodeUTF8))
        self.label_45.setText(QtGui.QApplication.translate("MainWindow", "% MDI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_46.setText(QtGui.QApplication.translate("MainWindow", "Torque loss", None, QtGui.QApplication.UnicodeUTF8))
        self.label_47.setText(QtGui.QApplication.translate("MainWindow", "% MDI", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox501.setTitle(QtGui.QApplication.translate("MainWindow", "0x501", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "sec", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Timestamp:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "LED status:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("MainWindow", "Simulink model version:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("MainWindow", "Save date:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox502.setTitle(QtGui.QApplication.translate("MainWindow", "0x502", None, QtGui.QApplication.UnicodeUTF8))
        self.label_50.setText(QtGui.QApplication.translate("MainWindow", "yawAngle:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_51.setText(QtGui.QApplication.translate("MainWindow", "rollAngle:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_52.setText(QtGui.QApplication.translate("MainWindow", "yawRate:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_53.setText(QtGui.QApplication.translate("MainWindow", "rollRate:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox503.setTitle(QtGui.QApplication.translate("MainWindow", "0x503", None, QtGui.QApplication.UnicodeUTF8))
        self.label_54.setText(QtGui.QApplication.translate("MainWindow", "vx:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_55.setText(QtGui.QApplication.translate("MainWindow", "vyCG:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_56.setText(QtGui.QApplication.translate("MainWindow", "axCG:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_57.setText(QtGui.QApplication.translate("MainWindow", "ayCG:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox504.setTitle(QtGui.QApplication.translate("MainWindow", "0x504", None, QtGui.QApplication.UnicodeUTF8))
        self.label_58.setText(QtGui.QApplication.translate("MainWindow", "PosE:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_60.setText(QtGui.QApplication.translate("MainWindow", "PosN:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox505.setTitle(QtGui.QApplication.translate("MainWindow", "0x505", None, QtGui.QApplication.UnicodeUTF8))
        self.label_64.setText(QtGui.QApplication.translate("MainWindow", "sideslip:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_66.setText(QtGui.QApplication.translate("MainWindow", "rawIpitch:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_67.setText(QtGui.QApplication.translate("MainWindow", "rawIaz:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox506.setTitle(QtGui.QApplication.translate("MainWindow", "0x506", None, QtGui.QApplication.UnicodeUTF8))
        self.label_65.setText(QtGui.QApplication.translate("MainWindow", "LFDuration:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_68.setText(QtGui.QApplication.translate("MainWindow", "LRDuration:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_69.setText(QtGui.QApplication.translate("MainWindow", "LeftTieRod:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_70.setText(QtGui.QApplication.translate("MainWindow", "RFDuration:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_71.setText(QtGui.QApplication.translate("MainWindow", "RRDuration:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_72.setText(QtGui.QApplication.translate("MainWindow", "RightTieRod:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "ESP status (active)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Suspension deflection (front)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Suspension deflection (rear)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Desired center differential clutch stiffness", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Actual center differential clutch value", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "MotorCurrent", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Car speed", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Wheelspeed FL", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Wheelspeed FR", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Wheelspeed RL", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Wheelspeed RR", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Lateral acceleration", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Brake pressure", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Yaw rate", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Steering torque", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Steering angle", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Demanded steering torque from ESP", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Internal torque (engine)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "Torque loss (engine)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: yawAngle", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: yawRate", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: rollAngle", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: rollRate", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: vx", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: axCG", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: vyCG", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: ayCG", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: posE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: posN", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: sideslip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: rawIpitch", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: rawIaz", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: LRDuration", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: RRDuration", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: LFDuration", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: RFDuration", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: LeftTieRod", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSelectData.addItem(QtGui.QApplication.translate("MainWindow", "DDL: RightTieRod", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxDataFile.setTitle(QtGui.QApplication.translate("MainWindow", "CAN Data File", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditFile.setText(QtGui.QApplication.translate("MainWindow", "(No file selected)", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonLoadFile.setText(QtGui.QApplication.translate("MainWindow", "Load Data File", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxVideo.setTitle(QtGui.QApplication.translate("MainWindow", "Video File", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditVideo.setText(QtGui.QApplication.translate("MainWindow", "(No file selected)", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonEnableVideo.setText(QtGui.QApplication.translate("MainWindow", "Enable Video", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonDisableVideo.setText(QtGui.QApplication.translate("MainWindow", "Disable Video", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonLoadVideo.setText(QtGui.QApplication.translate("MainWindow", "Load Video File", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonPause.setText(QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonPlay.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.InfoButton.setText(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Frame:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.timestampBox.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Time:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.timeBox.setText(QtGui.QApplication.translate("MainWindow", "00:00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><span style=\" font-weight:600;\">Timestamp:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.diffBox.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><span style=\" font-weight:600;\">Diff:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "ms", None, QtGui.QApplication.UnicodeUTF8))

