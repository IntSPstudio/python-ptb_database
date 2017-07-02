#|==============================================================|#
# Made by IntSPstudio
# PTB Database
# Thank you for using this software!
# ID: 980005032
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import it8c
import os
import platform
import datetime
import time
#VISUAL
vslStLineAA ="]"
vslStLineAB ="=="+ vslStLineAA
vslStTopBarAA = it8c.vslTerminalLine(0,"")
#OPERATING SYSTEM SETTINGS
def clearScreen():
	os.system(osClearCommand)
	#print("clear")
checka = str.lower(platform.system())
if checka == "windows":
	osSystem =1
else:
	osSystem =2
if osSystem == 1:
	osClearCommand ="cls"
elif osSystem == 2:
	osClearCommand ="clear"
else:
	osClearCommand =""
#PRINT 1D ARRAY
def print1dArray(userArrayContent):
	return it8c.dataPrintList(userArrayContent,"\n")
#PRINT 2D ARRAY
def print2dArray(userArrayContent):
	return it8c.dataSmrPrintArray(userArrayContent," | ","",0)
#SAVE 1D ARRAY
def save1dArray(userArrayContent,arrayName):
	it8c.fileWriteTextList(userArrayContent,arrayName)
#READ TEXT FILE
def mainReadTextFile(fileName):
	return it8c.fileRead1LText(fileName)
#WRITE TEXT FILE
def mainWriteListTextFile(content, fileName):
	return it8c.fileWrite1LText(content, fileName)
#LDMOD
def makeLdMod(userInput):
	return it8c.lettersdigits(userInput,"")
#SLEEP
def masterSleep(seconds):
	time.sleep(seconds)
#GENERAL
mainExitCommand ="ext"
#FOLDERS
fldrMasterDatabase ="database"
fldrUrlMasterDatabase = fldrMasterDatabase
fldrShoppingList ="shoplists"
fldrUrlShoppingList = fldrUrlMasterDatabase +"/"+ fldrShoppingList
fldrReference ="reference"
fldrUrlReference = fldrUrlMasterDatabase +"/"+ fldrReference
fldrReferenceTemplates ="inrefpl"
fldrUrlReferenceTemplates = fldrUrlMasterDatabase +"/"+ fldrReferenceTemplates
fldrProductDataTemplates ="prrefpl"
fldrUrlProductDataTemplates = fldrUrlMasterDatabase +"/"+ fldrProductDataTemplates
fldrBackupData ="backup"
fldrUrlBackupData = fldrUrlMasterDatabase +"/"+ fldrBackupData
fldrSystem ="system"
fldrUrlSystem = fldrUrlMasterDatabase +"/"+ fldrSystem
#FILES
fldrFileQuantity ="quantity.txt"
fldrFileProduct ="id.txt"
fldrFileCreationDate ="cd.txt"
fldrFileLogAb ="logab.txt"
fldrFileDataContent ="usdaco.txt"
fldrFileDbProductIdList ="dbprid.txt"
fldrFileDbProductAmounts ="dbpram.txt"
fldrFileDbProductGlobalView ="dpprgv.csv"
"""
fldrFileReference ="reference.csv"
fldrUrlFileReference = fldrUrlMasterDatabase +"/"+ fldrFileReference
fldrFileReferenceExist =1
"""
#PAGES
uiusBcCheckInventory ="1"
uiusModifyProduct ="2"
uiusBcAddToInvetory ="4"
uiusBckEditProductInfo ="3"
uiusBckExit ="5"
uiusBckMenu ="0"
def returnPageName(pageID):
	if pageID == uiusBcCheckInventory:
		return "Inventory"
	elif pageID == uiusBcAddToInvetory:
		return "Add to inventory"
	elif pageID == uiusModifyProduct:
		return "Modify product data"
	elif pageID == uiusBckEditProductInfo:
		return "Modify product info"
	elif pageID == uiusBckExit:
		return "Exit"
	elif pageID == uiusBckMenu:
		return "Main menu"
	else:
		return "Error"
#CHECK ID
def checkProductSpecId():
	result =1
	i =1
	while result == 1:
		url = fldrUrlMasterDatabase +"/"+ str(i)
		if os.path.exists(url):
			i +=1
		else:
			result =0
			return i
#CHECK FOLDERS
def checkSystemFolders():
	#DATABASE
	if not os.path.exists(fldrUrlMasterDatabase):
		os.makedirs(fldrUrlMasterDatabase)
	#SHOPLIST
	if not os.path.exists(fldrUrlShoppingList):
		os.makedirs(fldrUrlShoppingList)
	#REF
	if not os.path.exists(fldrUrlReference):
		os.makedirs(fldrUrlReference)
	#IMPORT REF TEMPLATES
	if not os.path.exists(fldrUrlReferenceTemplates):
		os.makedirs(fldrUrlReferenceTemplates)
	#PRODUCT REF TEMPLATES
	if not os.path.exists(fldrUrlProductDataTemplates):
		os.makedirs(fldrUrlProductDataTemplates)
	#BACKUP
	if not os.path.exists(fldrUrlBackupData):
		os.makedirs(fldrUrlBackupData)
	#SYSTEM
	if not os.path.exists(fldrUrlSystem):
		os.makedirs(fldrUrlSystem)
#ASK TIME AND DATE
def getTimeAndDate(mode):
	#DATE
	clDateA = datetime.datetime.now()
	clYear = clDateA.year
	clMonth = clDateA.month
	clDay = clDateA.day
	clHour = clDateA.hour
	clMinute = clDateA.minute
	clSecond = clDateA.second
	if mode == 0:
		pointa = "{:04d}{:02d}{:02}{:02}{:02}{:02}".format(clYear,clMonth,clDay,clHour,clMinute,clSecond)
	elif mode == 1:
		pointa = "{:04d}-{:02d}.{:02} {:02}:{:02}:{:02}".format(clYear,clMonth,clDay,clHour,clMinute,clSecond)
	return pointa
#CHECK PRODUCT OF REF
def readProductDataRef(productID):
	productID = makeLdMod(productID) #BARCODE
	refPlateUrl = fldrUrlReference +"/"+ productID +".txt"
	if it8c.fileTextExists(refPlateUrl) == 1:
		pointa = it8c.copaRead(refPlateUrl,"=")
		checka = len(pointa)
		if checka >= 1:
			#pointb = pointa[0][0] #A1
			pointc = pointa[0][1] #A2
			#pointd = pointa[1][0] #B1
			pointe = pointa[1][1] #B2
			#checkb = pointb +": "+ pointc +", "+ pointd +": "+ pointe
			#return checkb
			return pointc +" "+ pointe
	else:
		return "no data"
#ADD TO SHOPPING LIST
def basicAddBarcodeToInventary():
	continuity =1
	userInput =""
	userInputId =0
	userArrayContent =[]
	while continuity == 1:
		userRawInput = input("Product barcode: ")
		userInput = makeLdMod(userRawInput)
		if userInput !="":
			if userInput != mainExitCommand:
				userInputId +=1
				userArrayContent.extend([userInput])
			else:
				continuity =0
				if userInputId > 0:
					return userArrayContent
#ADD TO MASTER DATABASE
def basicAddBarcodesToMasterDatabase(rawListArray):
	rawListArrayType = str(type(rawListArray))
	if rawListArrayType == "<class 'list'>":
		shopListArrayLength = len(rawListArray)
		shopListArray = it8c.dataCreateArray(shopListArrayLength,3,"")
		for i in range(0, shopListArrayLength):
			#BASIC
			pointa = str(rawListArray[i]) #PRODUCT
			checka = str(checkProductSpecId()) #ID
			checkb = fldrUrlMasterDatabase +"/"+ checka #URLS
			if not os.path.exists(checkb): #FOLDER
				os.makedirs(checkb)
			#SHOPLIST
			checkc = readProductDataRef(pointa)
			shopListArray[i][0] = checka
			shopListArray[i][1] = pointa
			shopListArray[i][2] = checkc
			#WRITING
			checkb = fldrUrlMasterDatabase +"/"+ checka +"/"+ fldrFileProduct #ID URLS
			mainWriteListTextFile(pointa,checkb) #ID
			checkb = fldrUrlMasterDatabase +"/"+ checka +"/"+ fldrFileCreationDate #CREATION DATE URLS
			mainWriteListTextFile(getTimeAndDate(1),checkb) #CD
			checkb = fldrUrlMasterDatabase +"/"+ checka +"/"+ fldrFileLogAb #LOGAB URLS
			mainWriteListTextFile("1",checkb) #ID
		#PRINT
		print(print2dArray(shopListArray))
		#SHOPLIST
		checka = len(shopListArray)
		pointa = it8c.dataCreateArray(checka,2,"")
		for i in range(0,checka):
			pointa[i][0] = shopListArray[i][0]
			pointa[i][1] = shopListArray[i][1]
		fileUrl = fldrUrlShoppingList +"/"+ str(getTimeAndDate(0)) +".txt" 
		it8c.copaWrite(fileUrl,pointa,":")
#SCAN DATABASE
def scanMasterDatabase():
	#SCAN
	dpMaxID = checkProductSpecId()
	if dpMaxID > 1:
		dpScanArray = it8c.dataCreateArray(dpMaxID,3,"")
		dpScanArray[0][0] ="id"
		dpScanArray[0][1] ="logab"
		dpScanArray[0][2] ="barcode"
		for i in range(1,dpMaxID):
			pointa = fldrUrlMasterDatabase +"/"+ str(i)
			productQuant = pointa +"/"+ fldrFileQuantity
			productID = pointa +"/"+ fldrFileProduct
			productLogAb = pointa +"/"+ fldrFileLogAb
			#ID FOLDER
			if os.path.exists(pointa):	
				#LOG AB
				if it8c.fileTextExists(productLogAb) == 1:
					checka = mainReadTextFile(productLogAb)
					checkb = it8c.checkIfItIsNumber(checka)
					if checkb == 1:
						if checka == "1":
							checkc ="1"
						else:
							checkc ="0"
					else:
						checkc ="0"
				#ID
				if it8c.fileTextExists(productID) == 1:
					content = mainReadTextFile(productID)
					if content !="":
						dpScanArray[i][0] = str(i)
						dpScanArray[i][1] = checkc
						dpScanArray[i][2] = content
		#LOGAB -
		dpScanArrayHeight = len(dpScanArray)
		dpRefdArrayHeight =0
		z =0
		for x in range(0,2):
			if x == 1:
				dpRefdArrayContent = it8c.dataCreateArray(dpRefdArrayHeight,2,"")
			for y in range(0,dpScanArrayHeight):
				checka = dpScanArray[y][1]
				if checka == "1":
					if x == 0:
						dpRefdArrayHeight +=1
					if x == 1:
						dpRefdArrayContent[z][1] = dpScanArray[y][0]
						dpRefdArrayContent[z][0] = dpScanArray[y][2]
						z +=1
		#CHECK OBJECTS
		pointa = it8c.dataExtractArrayColumn(dpRefdArrayContent,0)
		pointb = it8c.dataCheckListObjects(pointa)
		pointc = len(pointb)
		pointa = it8c.dataCreateArray(pointc,2,"")
		for i in range(0,pointc):
			pointa[i][0] = pointb[i][2]
			pointa[i][1] = pointb[i][1]
		#INVENTORY SHEET
		inventoryHeight = len(dpRefdArrayContent)
		inventoryWidth =5
		inventoryArray = it8c.dataCreateArray(inventoryHeight,inventoryWidth,"")
		for i in range(0,inventoryHeight):
			#COM
			productID = str(dpRefdArrayContent[i][1]) #ID
			#AMOUNT
			checka = str(dpRefdArrayContent[i][0])
			checkb =1
			for y in range(0,i):
				checkc = str(dpRefdArrayContent[y][0])
				if checka == checkc:
					checkb +=1
			#DATE
			productDateUrl = fldrUrlMasterDatabase +"/"+ productID +"/"+ fldrFileCreationDate
			if it8c.fileTextExists(productDateUrl) == 1:
				productDate = mainReadTextFile(productDateUrl)
			#COLLECT
			inventoryArray[i][0] = productDate #DATE
			inventoryArray[i][1] = productID #ID
			inventoryArray[i][2] = checkb #AMOUNT
			inventoryArray[i][3] = checka #BARCODE
			inventoryArray[i][4] = readProductDataRef(checka) #INFO FROM REF
		#SAVE FILES
		url = fldrUrlSystem +"/"+ fldrFileDbProductIdList #DB PRODUCT ID's
		it8c.copaWrite(url,dpRefdArrayContent,"=")
		url = fldrUrlSystem +"/"+ fldrFileDbProductAmounts #DB PRODUCT AMOUNTS
		it8c.copaWrite(url,pointa,"=")
		url = fldrUrlSystem +"/"+ fldrFileDbProductGlobalView #DB INVENTORY VIS
		it8c.csvWriteFile(inventoryArray,url,";",0)
		dpRefdArrayContent =""
		pointa =""
		inventoryArray =""
#VIEW GLOBAL INVENTORY MOMENT
def viewGlobalInvMom(customHeight):
	currentLogUrl = fldrUrlSystem +"/"+ fldrFileDbProductGlobalView
	if it8c.fileTextExists(currentLogUrl) == 1:
		currentLogFile = it8c.csvReadFile(currentLogUrl,";")
		currentLogWidth = len(currentLogFile[0])
		currentLogHeight = len(currentLogFile)
		if customHeight !="":
			maxHeight = customHeight
		else:
			maxHeight =10
		checkb = it8c.dataFlipArrayObjects(currentLogFile)
		if currentLogHeight <= maxHeight:
			print(print2dArray(checkb))
		else:
			checkc = it8c.dataCreateArray(maxHeight,currentLogWidth,"")
			for i in range(0, maxHeight):
				checkc[i] = checkb[i]
			print(print2dArray(checkc))
#WRITE PRODUCT REF DATA
def basicWriteProductRefData():
	productID = makeLdMod(input("Product barcode: "))
	refPlateName = input("Ref file: ")
	refPlateUrl = fldrUrlReferenceTemplates +"/"+ refPlateName +".txt"
	if it8c.fileTextExists(refPlateUrl) == 1:
		refPlateList = it8c.fileReadText(refPlateUrl)
		refPlateListLength = len(refPlateList)
		productDataList = it8c.dataCreateArray(refPlateListLength,2,"")
		for i in range(0, refPlateListLength):
			pointa = refPlateList[i] #PARAMETER
			checka = pointa +": "
			pointb = input(checka) #DATA INPUT
			productDataList[i][0] = makeLdMod(pointa) #PARAMETER
			productDataList[i][1] = pointb #DATA
		#FILE CHECK
		productDataUrl = fldrUrlReference +"/"+ str(productID) +".txt"
		if it8c.fileTextExists(productDataUrl) == 1:
			backupData = it8c.fileReadText(productDataUrl)
			backupDataUrl = fldrUrlBackupData +"/"+ str(getTimeAndDate(0)) +".txt"
			it8c.fileWriteTextList(backupData,backupDataUrl)
		#WRITE FILE
		it8c.copaWrite(productDataUrl,productDataList,"=")
	else:
		print("Ref file doesent exists")
#MODIFY PRODUCT DATA
def basicModifyProductData():
	productID = makeLdMod(str(input("Product id: ")))
	if productID != mainExitCommand:
		productUrl = fldrUrlMasterDatabase +"/"+ productID
		if os.path.exists(productUrl):
			#PRODUCT CHECK
			prCheckUrl = fldrUrlMasterDatabase +"/"+ productID +"/"+ fldrFileProduct
			if it8c.fileTextExists(prCheckUrl) == 1:
				checka = it8c.fileRead1LText(prCheckUrl)
				checkb = readProductDataRef(checka)
			print(checkb)
			#MAIN
			refPlateName = input("Ref file: ")
			refPlateUrl = fldrUrlProductDataTemplates +"/"+ refPlateName +".txt"
			if it8c.fileTextExists(refPlateUrl) == 1:
				refPlateList = it8c.fileReadText(refPlateUrl)
				refPlateListLength = len(refPlateList)
				pageLogAb = refPlateListLength #LOGAB MODE
				#PRINT
				clearScreen()
				for i in range(0,refPlateListLength):
					checka ="{:02}".format(i)
					print(checka + vslStLineAA + refPlateList[i])
				checka ="{:02}".format(pageLogAb)
				print(checka + vslStLineAA +"Logab")
				#INPUT
				checka = str(input("Option: "))
				if checka != mainExitCommand:
					checkb = it8c.checkIfItIsNumber(checka)
					clearScreen()
					if checkb == 1:
						checka = int(checka)
						if checka < pageLogAb:
							pointa = refPlateList[checka] #CONTENT TITLE
							checkc = pointa +": "
							pointb = input(checkc) #CONTENT INPUT
							checkd = fldrUrlMasterDatabase +"/"+ productID +"/"+ fldrFileDataContent #DATA FILE
							if it8c.fileTextExists(checkd) == 1:
								pointc = it8c.copaRead(checkd,"=") #CONTENT FILE
								pointaLength = len(pointc)
								success =0
								for i in range(0,pointaLength):
									pointd = pointc[i][0] #TITLE
									print("dif", pointd, pointa)
									if pointd == pointa:
										success =1
										pointc[i][1] = pointb #CONTENT
								if success == 0:
									pointd = it8c.dataCreateList(2,"")
									pointd[0] = pointa #TITLE
									pointd[1] = pointb #CONTENT
									pointe = it8c.dataAddArrayRow(pointc,pointd)
									pointc = pointe
								it8c.copaWrite(checkd,pointc,"=")
							else:
								pointc = it8c.dataCreateArray(1,2,"")
								pointc[0][0] = pointa #TITLE
								pointc[0][1] = pointb #CONTENT
								it8c.copaWrite(checkd,pointc,"=")
						else:
							if checka == pageLogAb:
								pageLogAbUrl = fldrUrlMasterDatabase +"/"+ productID +"/"+ fldrFileLogAb #URL
								if it8c.fileTextExists(pageLogAbUrl) == 1:
									pageLogAbContent = str(mainReadTextFile(pageLogAbUrl)) #READ
									if pageLogAbContent != "0":
										result ="0"
									else:
										result ="1"
									mainWriteListTextFile(result,pageLogAbUrl) #SAVE
			else:
				print("Ref file doesent exists")
		else:
			print("Product id could not found")