#|==============================================================|#
# Made by IntSPstudio
# PTB Database
# Thank you for using this software!
# Version: 0.1.3.20170307
# ID: 980005032
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import mse
#RETURN DEFAULT VSL SETTINGS
def rDefVslSettings():
	mse.clearScreen()
	print(mse.getTimeAndDate(1) +" : "+ mse.returnPageName(mainPage))
	print(vslMainTobBar)
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
			mse.scanMasterDatabase() #SCAN
			mse.viewGlobalInvMom(10)
			#TC
			checka = input(vslStInputAB)
			mainPage = mse.uiusBckMenu
		#MODIFY PRODUCT
		elif mainPage == mse.uiusModifyProduct:
			#TA
			rDefVslSettings()
			#TB
			mse.viewGlobalInvMom(10)
			print(vslMainTobBar)
			mse.basicModifyProductData()
			#TC
			mainPage = mse.uiusBckMenu
		#MODIFY PRODUCT INFO
		elif mainPage == mse.uiusBckEditProductInfo:
			#TA
			rDefVslSettings()
			#TB
			mse.basicWriteProductRefData()
			#TC
			mainPage = mse.uiusBckMenu
		#ADD TO INVETORY
		elif mainPage == mse.uiusBcAddToInvetory:
			#TA
			rDefVslSettings()
			#TB
			userInputArray = mse.basicAddBarcodeToInventary() #MAKE LIST
			rDefVslSettings()
			mse.basicAddBarcodesToMasterDatabase(userInputArray) #IMPORT TO MASTER DATABASE
			checka = input("Write down identifications")
			mse.scanMasterDatabase() #SCAN
			#TC
			mainPage = mse.uiusBckMenu
		#EXIT
		elif mainPage == mse.uiusBckExit:
			#TA
			mse.clearScreen()
			continuity =0
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