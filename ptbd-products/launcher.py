#|==============================================================|#
# Made by IntSPstudio
# PTB Database
# Thank you for using this software!
# Version: 0.1.7.20171707
# ID: 980005032
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
			mse.scanMasterDatabase() #SCAN
			mse.viewLogAbSepInvMom(10) #MAIN
			#TC
			checka = input(vslStInputAB)
			mainPage = mse.uiusBckMenu
		#CHECK PRODUCT DATA
		elif mainPage == mse.uiusBcCheckProduct:
			#TA
			rDefVslSettings()
			#TB
			mse.scanMasterDatabase() #SCAN
			mse.basicCheckProductData() #MAIN
			#TC
			mainPage = mse.uiusBckMenu
		#MODIFY PRODUCT
		elif mainPage == mse.uiusModifyProduct:
			#TA
			rDefVslSettings()
			#TB
			mse.scanMasterDatabase() #SCAN
			mse.viewLogAbTrueInvMom(10) #PRINT
			mse.basicModifyProductData() #MAIN
			#TC
			mainPage = mse.uiusBckMenu
		#MODIFY PRODUCT INFO
		elif mainPage == mse.uiusBckEditProductInfo:
			#TA
			rDefVslSettings()
			#TB
			mse.basicWriteProductRefData() #MAIN
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