# ----------------------------------------------- #
# Prerequisites for run this script:
# 1. install wmi
#	 > Type 'pip install wmi' on a command prompt
# 2. install pywin32
#	 > Type also 'pip install pywin32'
# 3. Run the script on a command line
# 	 > Type 'py SystemInformations.py'
# ----------------------------------------------- #

import wmi, socket, os
#from menu import displayMenu
from datetime import datetime
from functions import *


# Variables declarations & initializations
fileToSaveData = open("data.txt", "a")
c 			   = wmi.WMI() # Connecting to local machine
currentTime	   = datetime.now().strftime("%d/%m/%Y @ %H:%M:%S")
# Research infos system
hostname 	   = socket.gethostname()
# Get BIOS class
bios = c.Win32_BIOS()[0]
# Infos about Hard Drive
logicalDisk    = c.Win32_LogicalDisk()[0]
osName 		   = c.Win32_OperatingSystem()[0].Caption # get OS name
ldFreespace    = logicalDisk.Freespace # get main disk freespace 
ldSize 	   	   = logicalDisk.Size # get main disk total size
ldUsingspace   = int(ldSize) - int(ldFreespace) # get main disk using space
percentageFreespace = 100.0 * int(ldFreespace) / int(ldSize)
roundPercentageFreespace = round(percentageFreespace, 2)
roundPercentageUsingSpace = round(100.0 - roundPercentageFreespace, 2)
#print(bios.Manufacturer)
#exit()
# Display menu
#displayMenu()
clear = lambda: os.system("cls")
while True:	
	clear()
	displayOperationAvailable()
	userSelection = 0	
	while not userSelection:
		try:
			userSelection = int(input("Choice operation > "))
			if userSelection not in (1, 2, 3, 4):
				userSelection = 0
				raise ValueError
		except ValueError:
			print("[ERROR] Please enter a valid choice.")
		#except KeyboardInterrupt:
	#	print("Operation interrupted")
	if userSelection == 1:
		print("Collect general system informations...")
		writeGeneralData(currentTime, fileToSaveData, hostname, socket, bios)
	elif userSelection == 2:
		print("Collect hard drive informations...")
	elif userSelection == 3:
		print("Collect all informations...")
	elif userSelection == 4:
		exit()
	else:
		print("[ERROR] ...")

	# Write data
	#writeData(currentTime, fileToSaveData, hostname, socket, logicalDisk, logicalDisk, logicalDisk, ldSize, ldFreespace, ldUsingspace, roundPercentageFreespace, roundPercentageUsingSpace)

	userWantContinue = input("Again ? [Y/n] > ")
	if userWantContinue != "Y" and userWantContinue != "y" and userWantContinue != "":
		exit()
# Close file
fileToSaveData.close()



# #######################################################################
# Write data formated (DEPRECATED)
# #######################################################################
#fileToSaveData.write("*****************************************\n" + \
#					 "--------------General infos--------------\n" + \
#					  " PC name:\t[" + hostname.upper() + "]\n" + \
#					  " IP address:\t[" + socket.gethostbyname(hostname) + "]\n" + \
#					 "-------------Disk infos--------------\n" + \
#					  " Device:\t[" + logicalDisk.Caption + "]\n" + \
#					  " Disk Type:\t[" + logicalDisk.Description + "]\n" + \
#					  " File System:\t[" + logicalDisk.FileSystem + "]\n" + \
#					  " Total Size:\t[" + ldSize + "] MB - 100%" + "\n" \
#					  " Free Space:\t[" + ldFreespace + "] MB - " + str(roundPercentageFreespace) + "%" + "\n" \
#					  " Using Space:\t[" + str(ldUsingspace) + "] MB - " + str(roundPercentageUsingSpace) + "%" + "\n" + \
#					 "*****************************************\n\n" \
#					 "=========================================\n\n")

###############################
# BEGIN DONT WORK
###############################
#DRIVE_TYPES = {
#  0 : "Unknown",
#  1 : "No Root Directory",
#  2 : "Removable Disk",
#  3 : "Local Disk",
#  4 : "Network Drive",
#  5 : "Compact Disc",
#  6 : "RAM Disk"
#}
#driveType = 3
# Display type of Disk
#for drive in c.Win32_LogicalDisk ():
#	driveType = drive.Caption, DRIVE_TYPES[drive.DriveType]
#print(driveType)
################################
# END DONT WORK
################################
