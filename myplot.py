#!/usr/bin/env python

###########################################################
# myplot.py		                                          #
# (c) 2008 Stefan Klumpp <stefan.klumpp@gmail.com>		  #				
# Stanford Dynamic Design Lab, Stanford University, CA	  #
# VW ERL, Palo Alto, CA                            		  #
#                                                         #
# Licensed under the GPL                                  #
# FOR INTERNAL USE ONLY!                                  #
###########################################################

# for debugging, requires: python configure.py  --trace ...
if False:
    import sip
    sip.settracemask(0x3f)

import random
import sys

from PyQt4 import Qt
import PyQt4.Qwt5 as Qwt
from PyQt4.Qwt5.anynumpy import *


class DataPlot(Qwt.QwtPlot):

    def __init__(self, *args):
        Qwt.QwtPlot.__init__(self, *args)

        self.setCanvasBackground(Qt.Qt.white)
        self.alignScales()

        # Initialize data
        self.x = arange(0, 501, 1)
        self.y = zeros(len(self.x), Float)
       
        self.setTitle("Plot")
       
        self.curveR = Qwt.QwtPlotCurve()
        self.curveR.attach(self)
                
        self.curveR.setPen(Qt.QPen(Qt.Qt.blue))
       
        self.setAxisTitle(Qwt.QwtPlot.xBottom, "Framecount")
        self.setAxisTitle(Qwt.QwtPlot.yLeft, "Values")
                        
        self.curveR.setData(self.x, self.y)
      
        self.marker = m = Qwt.QwtPlotMarker()
        m.setValue(0, 0)
        m.setLineStyle(Qwt.QwtPlotMarker.VLine)
        m.setLinePen(Qt.QPen(Qt.Qt.green, 2, Qt.Qt.DashDotLine))
        text = Qwt.QwtText('')
        text.setColor(Qt.Qt.green)
        text.setBackgroundBrush(Qt.Qt.gray)
        text.setFont(Qt.QFont(self.fontInfo().family(), 12, Qt.QFont.Bold))
        m.setLabel(text)
        m.attach(self)
        



    def alignScales(self):
        self.canvas().setFrameStyle(Qt.QFrame.Box | Qt.QFrame.Plain)
        self.canvas().setLineWidth(1)
        for i in range(Qwt.QwtPlot.axisCnt):
            scaleWidget = self.axisWidget(i)
            if scaleWidget:
                scaleWidget.setMargin(0)
            scaleDraw = self.axisScaleDraw(i)
            if scaleDraw:
                scaleDraw.enableComponent(
                    Qwt.QwtAbstractScaleDraw.Backbone, False)



