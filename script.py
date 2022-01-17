#We want to know the serial number of the computer motherboard.

import os, sys
from tkinter import *

root = Tk()
root.title("Serial Number")
root.geometry("800x200")


def getMachineAdrr():
#We open the cmd and type the following command.
	os_type = sys.platform.lower()
	if 'win' in os_type:
			command = 'wmic bios get serialnumber'
	return os.popen(command).read().replace("\n","").replace("	","").replace(" ","")



label = Label(root, text = 'Your serial number is ' + str(getMachineAdrr())).pack()

root.mainloop()
