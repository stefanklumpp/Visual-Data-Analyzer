Visual Data Analyzer
---------------------
When I was at the Stanford's Dynamic Design Lab in 2008 I worked on a project about estimating side slip by using computer vision. I developed a framework in C/C++ to record and synchronize camera and vehicle data. Unfortunately I can't publish the source code of that project, because it contains confidential data about the CAN-bus specifications from Volkswagen.

But to analyze and visualize the recorded data I developed an additional tool in Python/PyQt4. That was actually something I started just for fun and to learn Python, but was really useful and in the end and replaced some of the old crappy tools that have been used until then.

To make it run it requires some external libraries and other software (see below).

I also put a screenshot in the root folder, so you get the idea, without having to install these dependencies.


Installation:
--------------
1) Install from the "Dependencies" folder the following programs and libraries
	a) python-2.5.1.msi (or newer)
	b) PyQt-Py2.5-gpl-4.3.3-2.exe (or newer)
	c) python-2.5.1.msi (or newer)
	d) You maybe have to reboot Windows

2) Run DataAnalyzer.pyw


License:
--------
This program is released under the GPLv3

Dependencies:
-------------
Qt (Trolltech) [License: GPL]
PyQt (Riverbank Computing) [License: GPL]
ffmpeg [License: LGPL]
NumPy [All rights reserved.]



--
(c) 2008 Stefan Klumpp <stefan.klumpp@gmail.com>
02/15/2008, Palo Alto, CA
