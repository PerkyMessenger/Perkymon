import cv
import Quartz
import time
import os
import sys

with open('raw_keys_125.txt') as f:
	lines=[L[:-1] for L in f.readlines()]

vidFile = (cv.CaptureFromFile('perkymon_125.avi'))

nFrames = int(cv.GetCaptureProperty( vidFile, cv.CV_CAP_PROP_FRAME_COUNT))

fps = cv.GetCaptureProperty(vidFile, cv.CV_CAP_PROP_FPS)

event_U_Down = Quartz.CGEventCreateKeyboardEvent(None, 32, True)
event_U_Up = Quartz.CGEventCreateKeyboardEvent(None, 32, False)

event_D_Down = Quartz.CGEventCreateKeyboardEvent(None, 2, True)
event_D_Up = Quartz.CGEventCreateKeyboardEvent(None, 2, False)

event_L_Down = Quartz.CGEventCreateKeyboardEvent(None, 37, True)
event_L_Up = Quartz.CGEventCreateKeyboardEvent(None, 37, False)

event_R_Down = Quartz.CGEventCreateKeyboardEvent(None, 15, True)
event_R_Up = Quartz.CGEventCreateKeyboardEvent(None, 15, False)

event_A_Down = Quartz.CGEventCreateKeyboardEvent(None, 0, True)
event_A_Up = Quartz.CGEventCreateKeyboardEvent(None, 0, False)

event_B_Down = Quartz.CGEventCreateKeyboardEvent(None, 11, True)
event_B_Up = Quartz.CGEventCreateKeyboardEvent(None, 11, False)

event_E_Down = Quartz.CGEventCreateKeyboardEvent(None, 14, True)
event_E_Up = Quartz.CGEventCreateKeyboardEvent(None, 14, False)

event_T_Down = Quartz.CGEventCreateKeyboardEvent(None, 17, True)
event_T_Up = Quartz.CGEventCreateKeyboardEvent(None, 17, False)

if fps != 4:
	print 'FPS ERROR!'

if nFrames != 125000:
	print 'FRAME NUMBER ERROR!'

waitPerFrameInMillisec = 150

print 'Num. Frames = ', nFrames

print 'Frame Rate = ', fps, 'frames per second'

for f in xrange(nFrames):
	frameImg = cv.QueryFrame(vidFile)
	cv.ShowImage("Perkymon", frameImg)
	print lines[f]
	if f==0:
		time.sleep(120)
	if lines[f] == 'U':
		Quartz.CGEventPost(0, event_U_Down)
		time.sleep(0.1)
		Quartz.CGEventPost(0, event_U_Up)
	elif lines[f] == 'D':
		Quartz.CGEventPost(0, event_D_Down)
		time.sleep(0.1)
		Quartz.CGEventPost(0, event_D_Up)
	elif lines[f] == 'L':
		Quartz.CGEventPost(0, event_L_Down)
		time.sleep(0.1)
		Quartz.CGEventPost(0, event_L_Up)
	elif lines[f] == 'R':
		Quartz.CGEventPost(0, event_R_Down)
		time.sleep(0.1)
		Quartz.CGEventPost(0, event_R_Up)
	elif lines[f] == 'A':
		Quartz.CGEventPost(0, event_A_Down)
		time.sleep(0.1)
		Quartz.CGEventPost(0, event_A_Up)
	elif lines[f] == 'B':
		Quartz.CGEventPost(0, event_B_Down)
		time.sleep(0.1)
		Quartz.CGEventPost(0, event_B_Up)
	elif lines[f] == 'E':
		Quartz.CGEventPost(0, event_E_Down)
		time.sleep(0.1)
		Quartz.CGEventPost(0, event_E_Up)
	elif lines[f] == 'T':
		Quartz.CGEventPost(0, event_T_Down)
		time.sleep(0.1)
		Quartz.CGEventPost(0, event_T_Up)
	cv.WaitKey (waitPerFrameInMillisec)

cv.DestroyWindow("Perkymon")


