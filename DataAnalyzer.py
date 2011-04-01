#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################
# DataAnalyzer.py										  #				
# (c) 2008 Stefan Klumpp <stefan.klumpp@gmail.com>		  #				
# Stanford Dynamic Design Lab, Stanford University, CA    #
# VW ERL, Palo Alto, CA									  #				
#														  #				
# Licensed under the GPL								  #				
###########################################################

#CHANGE_IF_NEW_CAN_MESSAGE_ADDED
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore

from UI_Main import Ui_MainWindow 
from myplot import DataPlot
import struct

# Settings
containerFormat = "9i13f1Q7I20f1i"  #CHANGE_IF_NEW_CAN_MESSAGE_ADDED
DATASET = struct.calcsize(containerFormat)  # size in bytes of a single dataset in the .dat file
FPS = 30  # frames per second
FFMPEG = ".\\ffmpeg.exe"  # location of the ffmpeg utility to process the video file
DAT_FILE_VERSION = 2  # version number to compare for the correct order of data inside the .dat-file, CHANGE_IF_NEW_CAN_MESSAGE_ADDED

class MainWindow(QMainWindow, Ui_MainWindow):
  
  
  
  def __init__(self, parent = None):
    """ Initializes the main window, the plot, signals & slots and class global variables """
    QMainWindow.__init__(self, parent)
    self.setupUi(self)
    self.plot = DataPlot(self.framePlot)  
    self.plot.resize(640, 350)
              
    # Signals & Slots
    # ----------------
    # Buttons:
    self.connect(self.ButtonLoadFile, SIGNAL("clicked()"),self.selectFile)
    self.connect(self.ButtonLoadVideo, SIGNAL("clicked()"),self.selectVideo)
    self.connect(self.ButtonQuit, SIGNAL("clicked()"), self.closeFile)
    self.connect(self.InfoButton, SIGNAL("clicked()"), self.infoPopup)
    self.connect(self.ButtonDisableVideo, SIGNAL("clicked()"), self.disableVideo)
    self.connect(self.ButtonEnableVideo, SIGNAL("clicked()"), self.enableVideo)
    self.connect(self.ButtonPlay, SIGNAL("clicked()"), self.playVideo)
    self.connect(self.ButtonPause, SIGNAL("clicked()"), self.pauseVideo)
    
    # SpinBox & Slider:
    self.connect(self.horizontalSlider, SIGNAL("valueChanged(int)"), self.spinBoxFrame.setValue)
    self.connect(self.spinBoxFrame, SIGNAL("valueChanged(int)"), self.horizontalSlider.setValue)
    self.connect(self.spinBoxFrame, SIGNAL("valueChanged(int)"), self.readFramesForPlot)
    self.connect(self.spinBoxFrame, SIGNAL("valueChanged(int)"), self.getTime)
    self.connect(self.spinBoxFrame, SIGNAL("valueChanged(int)"), self.readFrame)
    self.connect(self.spinBoxFrame, SIGNAL("valueChanged(int)"), self.showVideoFrame)
    
    # ComboBox:
    self.connect(self.comboSelectData, SIGNAL("currentIndexChanged(const QString&)"), self.plot.setTitle)
    self.connect(self.comboSelectData, SIGNAL("currentIndexChanged(int)"), self.selectionChanged)
   
    
    #DEBUG
    #self.connect(self.TestButton, SIGNAL("clicked()"), self.debugFunction)

    # Variables
    self.fh=0    # file handler
    self.offset=0 
    self.selectedFrame=0
    self.selectedSlot=0
    self.lastFrame=-1
    self.elapsedTime=0
    self.toggle="A"
    self.videoMode=0
    

  def debugFunction(self):
    print "Start Timer"
    self.startTimer(80)  
  
  def playVideo(self):
    """ Starts the video player and initializes the first two sets of frames
        The following frames are pre processed by the timerEvent """
    import os,time
    self.toggle = "A"
    self.ButtonPlay.setEnabled(0)
    self.ButtonLoadVideo.setEnabled(0)
    self.ButtonPause.setEnabled(1)
    self.ButtonDisableVideo.setEnabled(0)
    self.spinBoxFrame.setEnabled(0)
    self.horizontalSlider.setEnabled(0)
    
    # Process message 
    self.labelFrame.setPixmap(QPixmap())
    self.labelFrame.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><span style=\" font-size:29pt; font-weight:600; color:#ffa500;\">       Please wait ... processing.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    self.repaint()
    
    # Processing (1st set)    
    argList = ["-an","-i","\"".join(("",self.videofile,"")),"-ss",self.elapsedTime,"-t","00:00:01","-r","30","-y","-s","640x480","frameshots/videoA%d.jpg"]
    os.waitpid(os.spawnv(os.P_NOWAIT,FFMPEG, argList), 0)
    # Processing (2nd set)
    seektime=time.strftime("%H:%M:%S",time.gmtime((self.selectedFrame+30) / FPS))
    argList = ["-an","-i","\"".join(("",self.videofile,"")),"-ss",seektime,"-t","00:00:01","-r","30","-y","-s","640x480","frameshots/videoB%d.jpg"]
    os.spawnv(os.P_NOWAIT,FFMPEG, argList)
    
    #Start timer  
    self.timerID = self.startTimer(80)  # Timer for the video player; time in ms; 80 is the current maxiumum due to the time ffmpeg needs for processing
    print "Start Timer: %i" % self.timerID
    
  
  def pauseVideo(self):
    print "Kill Timer: %i" % self.timerID
    self.killTimer(self.timerID)
    self.ButtonPlay.setEnabled(1)
    self.ButtonPause.setEnabled(0)
    self.ButtonLoadVideo.setEnabled(1)
    self.ButtonDisableVideo.setEnabled(1)
    self.spinBoxFrame.setEnabled(1)
    self.horizontalSlider.setEnabled(1)
    
  def timerEvent(self, e): 
    """ Timer for the video player
        Current max. speed is 80ms; ffmpeg isn't fast enough for processing """
    if self.labelFrame.isEnabled() and self.selectedFrame <= self.maxFrames-1:
      # Pre processing:
      if self.selectedFrame%FPS == 1:
        import os,time
        seektime=time.strftime("%H:%M:%S",time.gmtime((self.selectedFrame+30) / FPS))  
        if self.toggle=="A":
          argList = ["-an","-i","\"".join(("",self.videofile,"")),"-ss",seektime,"-t","00:00:01","-r","30","-y","-s","640x480","frameshots/videoB%d.jpg"]
        else: # self.toggle="B"
          argList = ["-an","-i","\"".join(("",self.videofile,"")),"-ss",seektime,"-t","00:00:01","-r","30","-y","-s","640x480","frameshots/videoA%d.jpg"]
        os.spawnv(os.P_NOWAIT,FFMPEG, argList)
        
      # Show image:
      image = (self.selectedFrame % FPS) + 1
      if self.toggle=="A":
        pixmap = QPixmap("frameshots/videoA%i.jpg" % image)
      else: # self.toggle="B"
        pixmap = QPixmap("frameshots/videoB%i.jpg" % image)
      self.labelFrame.setPixmap(pixmap)
      
      self.spinBoxFrame.setValue(self.selectedFrame)
      self.readFramesForPlot(self.selectedFrame)
      if self.selectedFrame%30==29:
        if self.toggle=="A":
          self.toggle="B"
        else:
          self.toggle="A"
      self.selectedFrame=self.selectedFrame+1
    
    else:
      self.pauseVideo()
      pixmap = QPixmap("images/logo_chrome.png")
      self.labelFrame.setPixmap(pixmap)
      
  def disableVideo(self):
    self.frameImage.setEnabled(0)
    self.labelFrame.setEnabled(0)
    self.ButtonDisableVideo.setEnabled(0)
    self.ButtonEnableVideo.setEnabled(1)
    self.ButtonPlay.setEnabled(0)
    self.horizontalSlider.setTracking(1)
    pixmap = QPixmap("images/logo_chrome.png")
    self.labelFrame.setPixmap(pixmap)
      
  def enableVideo(self):
    if QFile.exists(self.videofile):
      self.lineEditVideo.setText(self.videofile)
      self.ButtonEnableVideo.setEnabled(0)
      self.ButtonDisableVideo.setEnabled(1)
      self.ButtonPlay.setEnabled(1)
      self.frameImage.setEnabled(1)
      self.labelFrame.setEnabled(1)
      self.showVideoFrame(self.selectedFrame)
      self.horizontalSlider.setTracking(0)
    
  
  
  
  def showVideoFrame(self,frame):
    """ Shows the corresponding video frame to the selected frame number
        Needs some time for processing after each new second """
    if self.labelFrame.isEnabled() and self.ButtonPlay.isEnabled():
      diff = (self.selectedFrame%FPS - self.lastFrame%FPS) * self.sign(self.selectedFrame - self.lastFrame)  # Are we moving upwards or downwards?
      if diff < 0 or abs(self.selectedFrame-self.lastFrame)>FPS-1:
        import os
        # Show "processing..." message
        self.labelFrame.setPixmap(QPixmap())
        self.labelFrame.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><span style=\" font-size:29pt; font-weight:600; color:#ffa500;\">       Please wait ... processing.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.repaint()
        
        # Process video with ffmpeg
        argList = ["-an","-i","\"".join(("",self.videofile,"")),"-ss",self.elapsedTime,"-t","00:00:01","-r","30","-y","-s","640x480","frameshots/video%d.jpg"]
        os.waitpid(os.spawnv(os.P_NOWAIT,FFMPEG, argList), 0)

      # Display image (frame)
      image = (self.selectedFrame % FPS) + 1
      pixmap = QPixmap("frameshots/video%i.jpg" % image)
      self.labelFrame.setPixmap(pixmap)
      self.lastFrame=self.selectedFrame
      
  
  def readFrame(self,frame):
    """ Reads a single dataset out of the .dat file and displays it on the form """

    self.selectedFrame=frame
    self.fh.seek(frame*DATASET)
    tmp = struct.unpack(containerFormat,self.fh.read(DATASET))  # See http://docs.python.org/lib/module-struct.html

    #CHANGE_IF_NEW_CAN_MESSAGE_ADDED, below
    # ESP
    if tmp[3]:
      self.checkBoxESP.setCheckState(Qt.Checked)
    else:
      self.checkBoxESP.setCheckState(Qt.Unchecked)
    # Suspension deflection
    self.Front.setText(str(tmp[4]))
    self.Rear.setText(str(tmp[5]))  
    # Clutch
    self.ClutchStiffness.setText(str(tmp[6]))
    self.ClutchValue.setText(str(tmp[7]))
    # Motor Current
    self.MotorCurrent.setText(str(tmp[8]))
    # Wheelspeed
    self.speed_car.setText(str(round(tmp[9],3)))
    self.speed_FL.setText(str(round(tmp[10],3)))
    self.speed_FR.setText(str(round(tmp[11],3)))
    self.speed_RL.setText(str(round(tmp[12],3)))
    self.speed_RR.setText(str(round(tmp[13],3)))
    # Brake and ESP
    self.lateral.setText(str(round(tmp[14],3)))
    self.brake.setText(str(round(tmp[15],3)))
    self.yaw.setText(str(round(tmp[16],3)))
    # Steering
    self.Torque.setText(str(round(tmp[17],3)))  
    self.Angle.setText(str(round(tmp[18],3)))
    # Demanded steering torque
    self.SteeringTorque.setText(str(round(tmp[19],3)))
    # Engine
    self.IntTorque.setText(str(round(tmp[20],3)))
    self.TorqueLoss.setText(str(round(tmp[21],3)))
    # Timestamp
    self.diffBox.setText(str(abs(tmp[22]-int(self.timestampBox.displayText()))))
    self.timestampBox.setText(str(tmp[22]))
    
    # Stanford 0x501
    self.model_version.setText(str(tmp[23]))
    tmp_str = '_'.join([str(tmp[24]),str(tmp[25]),str(tmp[26]),str(tmp[27])])
    tmp_str = ':'.join([tmp_str,str(tmp[28]),str(tmp[29])])
    self.save_date.setText(tmp_str)
    self.ddl_timestamp.setText(str(round(tmp[30],3)))
    
    # Stanford 0x502
    self.yawAngle.setText(str(round(tmp[31],3)))
    self.yawRate.setText(str(round(tmp[32],3)))
    self.rollAngle.setText(str(round(tmp[33],3)))
    self.rollRate.setText(str(round(tmp[34],3)))
    
    # Stanford 0x503
    self.vx.setText(str(round(tmp[35],3)))
    self.axCG.setText(str(round(tmp[36],3)))
    self.vyCG.setText(str(round(tmp[37],3)))
    self.ayCG.setText(str(round(tmp[38],3)))
    
    # Stanford 0x504
    self.PosE.setText(str(round(tmp[39],3)))
    self.PosN.setText(str(round(tmp[40],3)))
    
    # Stanford 0x505
    self.sideslip.setText(str(round(tmp[41],3)))
    self.rawIpitch.setText(str(round(tmp[42],3)))
    self.rawIaz.setText(str(round(tmp[43],3)))
    
    # Stanford 0x506
    self.LRDuration.setText(str(round(tmp[44],3)))
    self.RRDuration.setText(str(round(tmp[45],3)))
    self.LFDuration.setText(str(round(tmp[46],3)))
    self.RFDuration.setText(str(round(tmp[47],3)))
    self.LeftTieRod.setText(str(round(tmp[48],3)))
    self.RightTieRod.setText(str(round(tmp[49],3)))
    
    # Stanford 0x507
    self.led_status.setText(str(tmp[50]))
    
      
  def readFramesForPlot(self, startFrame):
    """ Reading data out of the .dat file and painting it to the plot """
    import struct

    # Special cases for the beginning and the end of the plot (dataset)
    centerFrame=startFrame
    if startFrame < 250:
      centerFrame = 250
    elif startFrame >= (self.maxFrames-250):
      centerFrame = self.maxFrames-251
        
    # Read data (-250..startFrame..+250 = 501 values)
    for i in range(501):
      self.fh.seek((i+centerFrame-250)*DATASET+2*4)  #this is to find the frame count, currently offseting dummy + version variables, 2*4 bytes (frameCount is 3rd variable), CHANGE_IF_NEW_CAN_MESSAGE_ADDED
      tmp = struct.unpack("i",self.fh.read(4))
      self.plot.x[i] = float(tmp[0])
      
      self.fh.seek((i+centerFrame-250)*DATASET + self.offset)
      if self.selectedSlot <= 5:    #first 6 variables are integers, all others are floats, CHANGE_IF_NEW_CAN_MESSAGE_ADDED
        tmp = struct.unpack("i",self.fh.read(4))
      else:
        tmp = struct.unpack("f",self.fh.read(4))
      self.plot.y[i] = tmp[0]
      
    # Set the label showing the data value
    # -> special cases for the beginning and the end of the dataset
    label = self.plot.marker.label()
    if startFrame < 250:
      label.setText('%.3f' % self.plot.y[startFrame])
      print self.plot.x[startFrame]
    elif startFrame >= (self.maxFrames-250):
      label.setText('%.3f' % self.plot.y[501-self.maxFrames+startFrame])
      print self.plot.x[501-self.maxFrames+startFrame]
    else:
      label.setText('%.3f' % self.plot.y[250])
      print self.plot.x[250]
    self.plot.marker.setLabel(label)
    
    # Prepare and plot the curve
    self.plot.curveR.setData(self.plot.x, self.plot.y)
    self.plot.marker.setValue(self.selectedFrame, 0)
    self.plot.replot()
   
  
  def selectionChanged(self, slot):
    """ SLOT for changes in the combo box """

    #print "Selected slot: %i" % slot  # debug
    self.selectedSlot=slot  #slot, refers to the drop down menu for the plot starting from zero, see UI_Main.ui for organization
                            #drop down list does not contain dummy, version, frameCount, xPC "model" info, timestamp...basically anythign that isn't to be plotted.
    
    # Set the offset for reading the dataset
    # Exlcuding the timestamps, version number and other meta data
    
    # Basic powertrain CAN signals
    if slot in range(0,19): #range is the number of basic powertrain CAN signals, increment appropriately if you add a signal, CHANGE_IF_NEW_CAN_MESSAGE_ADDED
      self.offset=(slot+3)*4 #ignore the first three variables (dummy, version, and frameCount), used for plotting y-axis, CHANGE_IF_NEW_CAN_MESSAGE_ADDED
    # Stanford DDL signals
    elif slot in range(19,38): #range of Stanford DDL signals, increment appropriately if you add a signal, CHANGE_IF_NEW_CAN_MESSAGE_ADDED
      self.offset=(slot+13)*4 #CHANGE_IF_NEW_CAN_MESSAGE_ADDED
      
    self.readFramesForPlot(self.selectedFrame)
   
    
  def selectFile(self):
    """ Opens a file select dialog and some basic setup """
    if self.fh:
      self.fh.close()
    filename=unicode(QFileDialog.getOpenFileName(self, "Select File", ".", "CAN data file (*.dat)"))  # opens file select dialog
    self.lineEditFile.setText(filename)
    self.openFile(filename)
    import os
    self.maxFrames = os.stat(filename)[6]/DATASET  # get the maximum amount of frames; lastframe = maxFrames - 1
    self.spinBoxFrame.setMaximum(self.maxFrames-1)
    self.horizontalSlider.setMaximum(self.maxFrames-1)
    self.getTime(0)  
    self.readFrame(0)
    self.selectionChanged(0)
    self.frameData.setEnabled(1)
    self.frameSelect.setEnabled(1)
    self.framePlot.setEnabled(1)
    self.groupBoxVideo.setEnabled(1)
    self.ButtonLoadVideo.setEnabled(1)
    
  def openFile(self, filename):
    """ Opens the file and creates a file handler """
    import struct,sys
    try:
      self.fh = open(filename, "rb")
    except IOError, e:
      print "I/O error: %s" % e
    else:
      tmp = struct.unpack("i",self.fh.read(4))
      if tmp[0] != DAT_FILE_VERSION:
        QMessageBox.critical(self, " I/O ERROR", "ERROR: .dat-file does not match requirements. Was it recorded with an older/newer release of the VW ERL CAN-Camera-Framework?\n\nData Analyzer: %i\nData File: %i" % (DAT_FILE_VERSION,tmp[0]))
        sys.exit("\n*** ERROR: .dat-file does not match requirements. Was it recorded with an older/newer release of the VW ERL CAN-Camera-Framework?")
        
                    
  def closeFile(self):
    if self.fh:
      self.fh.close()
      
  def selectVideo(self):
    """ Select a video file; the video is not really opened, but parsed to ffmpeg for further processing """
    self.videofile=unicode(QFileDialog.getOpenFileName(self, "Select File", ".", "Video file (*.avi)"))
    self.enableVideo()
    
  def infoPopup(self):
    """ Information and license popup message """
    QMessageBox.information(self, "Info", "VW ERL :: Data Analyzer\n\n(c) 2008 Stefan Klumpp <stefan.klumpp@vw.com>\nVW ERL, Palo Alto, CA\n\nLicensed under the GPL\n\nFOR INTERNAL USE ONLY!")
    
    
    
  def getTime(self, frame):
    """  Calculates the relative time out of the current frame number and FPS; format is hh:mm:ss """
    import time
    self.elapsedTime = time.strftime("%H:%M:%S",time.gmtime(frame / FPS))
    self.timeBox.setText(self.elapsedTime)
    
  def sign(self,x):
    if x < 0: return -1
    elif x > 0: return 1
    else: return 0
    
if __name__ == "__main__":
  import sys
  app = QtGui.QApplication(sys.argv)
  Main = MainWindow()
  Main.show()
  
  sys.exit(app.exec_())

