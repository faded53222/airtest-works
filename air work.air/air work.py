# -*- encoding=utf8 -*-
__author__ = "Administrator"
from airtest.core.api import *
auto_setup(__file__)
win = device()
while 1:
    win.key_press('DOWN')
    sleep(5)
    win.key_release('DOWN')
    win.key_press('UP')
    sleep(0.05)
    win.key_release('UP')
    sleep(0.5)
    if exists(Template(r"tpl1576728851808.png", record_pos=(1.159, 0.171), resolution=(848, 1038))):
        win.key_press('A')
        sleep(0.1)
        win.key_release('A')
