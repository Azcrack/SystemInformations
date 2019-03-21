def displayOperationAvailable():
	print("\t\t SysInfo Menu")
	print("X-------------------------------------------X")
	print("| [1] Informations about system             |")
	print("| [2] Informations about hard drive         |")
	print("| [3] All informations                      |")
	print("| [4] Exit                                  |")
	print("X-------------------------------------------X")

def getProcess():
	"""Function for list all process id with process name
	"""
	for process in c.Win32_Process():
		print(process.ProcessId, process.Name)


def showComputerIP():
	"""Function for display IP
	"""
	hostname = socket.gethostname()
	try:
		print("PC name: %s" %hostname)
		print("IP address: %s" %socket.gethostbyname(hostname))
	except socket.error as err:
		print("%s: %s" %(hostname, msg))

def writeGeneralData(time, file, host, socket, bios):
	file.write("***************************************************\n" + \
		"-------------------General infos-------------------\n" + \
		" Scan Type:\tGeneral system informations\n" + \
		" Flashed at:\t" + time + "\n" + \
		" PC name:\t[" + host.upper() + "]\n" + \
		" IP address:\t[" + socket.gethostbyname(host) + "]\n" + \
		"---------------------BIOS infos--------------------\n" + \
		" Version:\t" + bios.Caption + "\n")

def writeData(time, file, hostname, socket, diskCaption, diskDescription, diskFileSystem, size, freespace, usingspace, rndPercentageFree, rndPercentageUsing):
	"""Function for write data in a data text file
	
	:param time: 				Current time
	:param file: 				File name and permissions
	:param hostname: 			Hostname
	:param socket: 				Get the hostname
	:param diskCaption: 		Get the OS name
	:param diskDescription: 	Get the type of hard drive
	:param diskFileSystem: 		Get the file system
	:param size: 				Get the total space on hard drive
	:param freespace: 			Get the freespace on hard drive
	:param usingspace: 			Get the usingspace on hard drive
	:param rndPercentageFree: 	Convert in %
	:param rndPercentageUsing: 	Convert in %
	"""
	file.write("***************************************************\n" + \
		"-------------------General infos-------------------\n" + \
		" Flashed at:\t" + time + "\n" + \
		" PC name:\t[" + hostname.upper() + "]\n" + \
		" IP address:\t[" + socket.gethostbyname(hostname) + "]\n" + \
		"---------------------Disk infos--------------------\n" + \
		" Device:\t[" + diskCaption.Caption + "]\n" + \
		" Disk Type:\t[" + diskDescription.Description + "]\n" + \
		" File System:\t[" + diskFileSystem.FileSystem + "]\n" + \
		" Total Size:\t[" + size + "] MB\t- 100 %" + "\n" \
		" Free Space:\t[" + freespace + "] MB\t- " + str(rndPercentageFree) + " %" + "\n" \
		" Using Space:\t[" + str(usingspace) + "] MB\t- " + str(rndPercentageUsing) + " %" + "\n" + \
		"***************************************************\n\n" \
		"===================================================\n\n")