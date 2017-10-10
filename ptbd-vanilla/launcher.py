#|==============================================================|#
# Made by IntSPstudio
# PTB Database
# Thank you for using this software!
# Version: 0.1.2.20171010
# ID: 980005031
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import mse
#RETURN DEFAULT VSL SETTINGS
def rDefVslSettings():
	mse.clearScreen()
	print(vslMainTobBar)
	print(mse.vslStLineAB  +" "+ mse.getTimeAndDate(1) +" : "+ mse.returnPageName(mainPage))
#START
if __name__ == "__main__":
	#SETTINGS
	continuity =1
	#VISUAL
	vslMainTobBar = mse.vslStTopBarAA
	vslStInputAB = mse.vslStLineAB
	#PAGES
	mainPage = mse.uiusBckMenu
	#FOLDERS
	mse.checkSystemFolders()
	#LOOP
	while continuity == 1:
		#CHECK INVETORY
		if mainPage == mse.uiusBcCheckInventory:
			#TA
			rDefVslSettings()
			#TB
			print(mse.readUserContentFromDatabase())
			pointa = input(vslStInputAB)
			#TC
			mainPage = mse.uiusBckMenu
		#ADD TO INVETORY
		elif mainPage == mse.uiusBcAddToInvetory:
			#TA
			rDefVslSettings()
			#TB
			mse.addUserContentToDatabase()
			#TC
			mainPage = mse.uiusBckMenu
		#MODIFY ADDER
		elif mainPage == mse.uiusBcModifyAdder:
			#TA
			rDefVslSettings()
			#TB
			mse.getInputSkelTexts()
			#TC
			mainPage = mse.uiusBckMenu
		#EXIT
		elif mainPage == mse.uiusBckExit:
			#TA
			mse.clearScreen()
			continuity =0
			print(mse.exitLogo())
		#MENU
		else:
			#TA
			mainPage = mse.uiusBckMenu
			rDefVslSettings()
			#TB
			for i in range(1,int(mse.uiusBckExit) +1):
				checka = str(i)
				checkb = mse.returnPageName(checka)
				print("0"+ checka +"]"+ checkb)
			#TC
			checka = input(vslStInputAB)
			mainPage = str(checka)