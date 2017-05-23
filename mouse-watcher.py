#!/usr/bin/env python

import os
from AppKit import NSObject, NSApplication, NSEvent, NSLeftMouseUpMask, NSOtherMouseDownMask
from PyObjCTools import AppHelper
import subprocess

# display dialog
print "hello world"
#import ctypes  
#ctypes.windll.user32.MessageBoxA(0, "hello world", "mouse-watcher.py", 1)
#from Tkinter import *
#import tkMessageBox
#tkMessageBox.showinfo('mouse-watcher.py','hello world') 
 
class AppDelegate(NSObject):
	def applicationDidFinishLaunching_(self, aNotification):
		AppDelegate.myMonitor=NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(NSLeftMouseUpMask, self.leftMouseClick)
		AppDelegate.myMonitor=NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(NSOtherMouseDownMask, self.middleMouseClick)

	def applicationWillTerminate_(self, notification):
		NSEvent.removeMonitor_(AppDelegate.myMonitor)
		AppHelper.stopEventLoop()

	def leftMouseClick(event):
		#os.system(\"osascript  " & myAppleScriptPath & "\")
		#ctypes.windll.user32.MessageBoxW(0, "left click", "Your title", 1)
		print "left click"
		
	def middleMouseClick(event):
		#os.system(\"osascript  " & myAppleScriptPath & "\")
		#ctypes.windll.user32.MessageBoxW(0, "middle click", "Your title", 1)
		print "middle click"
		# paste
		cmd = """
		osascript -e 'tell application "System Events" to keystroke "v" using {command down}' 
		"""
		os.system(cmd)
		#ctrl+click (for click on finder sidebar)
		subprocess.call(['/usr/local/Cellar/cliclick/3.3/bin/cliclick kd:cmd c:.'])

tDeleg=AppDelegate.new()
NSApplication.sharedApplication().setDelegate_(tDeleg)
AppHelper.runEventLoop()
