#!/usr/bin/env python

###########################################################
# myread.py		                                          #
# (c) 2008 Stefan Klumpp <stefan.klumpp@gmail.com>		  #				
# Stanford Dynamic Design Lab, Stanford University, CA	  #
# VW ERL, Palo Alto, CA                            		  #
#                                                         #
# Licensed under the GPL                                  #
# FOR INTERNAL USE ONLY!                                  #
###########################################################

import struct

def process(file, frame):
  print "*** process()"
  file.seek(frame*128)
  for i in range(10):
    tmp = struct.unpack("6i12d1Q",file.read(128))
    print tmp
  
  
  
    

if __name__ == "__main__":
  try:
    fh = open("storage.dat", "rb")
    process(fh, 0)
  except IOError, e:
    print "I/O error: %s" % e
  finally:
    if fh:
      fh.close()