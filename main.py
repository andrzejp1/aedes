#!/usr/bin/python
import time
import pprint
from sense_hat import SenseHat

import lab
import effects

def StateToAction(state):
    if state.Front.temperature > 85 or state.Back.temperature > 85:
        return ('alarm',[255,128,0])
    if state.Front.temperature < 75 or state.Back.temperature < 75:
        return ('alarm',[0,128,255])
    if state.Front.humidity < 70 or state.Back.humidity > 95:
        return ('alarm',[255,255,255])
    if state.Front.battery< 50 or state.Back.battery < 50:
        return ('alarm',[255,255,0])
    if abs(state.Front.temperature - state.Back.temperature) > 5 or abs(state.Front.humidity - state.Back.humidity) > 10:
        return ('alarm',[255,0,0])
    return ('idle')

def StateChangeToAction(prv,cur):
    if prv.Fogger.state <> cur.Fogger.state:
        return ('change', [0,255,0])
    if prv.Heat.state <> cur.Heat.state:
        return ('change', [255,0,0])
    if prv.Vent.state <> cur.Vent.state:
        return ('change', [0,0,255])
    return ('idle')

previousState =  lab.CurrentStatus()
currentState = previousState
def GetAction():
    global previousState
    global currentState
    previousState = currentState
    currentState = lab.CurrentStatus()
    a = StateChangeToAction(previousState, currentState)
    if a[0] == 'idle':
        a = StateToAction(currentState)
    return a

#sense = SenseHat()
#x=lab.CurrentStatus()
#pp = pprint.PrettyPrinter(depth=6)
#pp.pprint(x)
#sense.show_message("Hello world!")

while True:
    a = GetAction()
    type = a[0]
    if type == 'alarm':
        effects.alarm_flash(a[1],1)
    elif type == 'change':
        effects.alarm_flash(a[1],1)
    else:
        effects.rainbow()