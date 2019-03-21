import os
from functions import displayOperationAvailable


# ####################
#		Menu
# ###################
def displayMenu():
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
			print("System informations...")
		elif userSelection == 2:
			print("Hard drive informations...")
		elif userSelection == 3:
			print("All informations...")
		elif userSelection == 4:
			exit()
		else:
			print("[ERROR] ...")

		userWantContinue = input("Again ? [Y/n] > ")
		if userWantContinue != "Y" and userWantContinue != "y" and userWantContinue != "":
			exit()

