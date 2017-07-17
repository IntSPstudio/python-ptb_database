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
	return it8c.dataSmrPrintArray(userArrayContent," : ","",0)
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
mainExitCommandWithoutSaving ="nosave"
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
fldrUrlDataContentParameters ="usdaco"
#COM FILES
fldrFileQuantity ="quantity.txt" #OFFLINE
fldrFileProduct ="id.txt" #BARCODE
fldrFileCreationDate ="cd.txt" #DATE WHEN IMPORTED
fldrFileLogAb ="logab.txt" #IS IT LOGAB
fldrFileDataContent = fldrUrlDataContentParameters +".txt" #USER DATA CONTENT
#SETTINGS FOLDER FILES
fldrFileDbProductIdList ="dbprid.txt" #PRODUCTS LIST BY ID
fldrFileDbProductAmounts ="dbpram.txt" #PRODUCTS LIST BY AMOUNT
fldrFileDbProductGlobalView ="dpprgv.csv" #GLOBAL VIEW OF INVENTORY
fldrFileDbProductLogAbTrue ="dpprlatv.csv" #INVENTORY BY LOGAB TRUE
fldrFileDbProductLogAbFalse ="dpprlafv.csv" #INVENTORY BY LOGAB FALSE
fldrFileDbProductQuantityTrue ="dpprqttv.csv" #INVENTORY QUANTITY BY LOGAB TRUE
fldrFileDbProductQuantityFalse ="dpprqtfv.csv" #INVENTORY QUANTITY BY LOGAB FALSE
fldrFileDbProductDataViewTrue = "dpprcwt.csv" #USER DATA CONTENT VIEW BY LOGAB TRUE
fldrFileDbProductDataViewFalse = "dpprcwf.csv" #USER DATA CONTENT VIEW BY LOGAB FALSE
"""
fldrFileReference ="reference.csv"
fldrUrlFileReference = fldrUrlMasterDatabase +"/"+ fldrFileReference
fldrFileReferenceExist =1
"""
#PAGES
uiusBcCheckInventory ="1"
uiusBcCheckProduct ="2"
uiusModifyProduct ="3"
uiusBcAddToInvetory ="5"
uiusBckEditProductInfo ="4"
uiusBckExit ="6"
uiusBckMenu ="0"
def returnPageName(pageID):
	if pageID == uiusBcCheckInventory:
		return "Inventory"
	elif pageID == uiusBcAddToInvetory:
		return "Add to inventory"
	elif pageID == uiusBcCheckProduct:
		return "Check product data"
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
#CHECK PRODUCT DATA
def basicCheckProductData():
	#SELCT
	for i in range(0,2):
		print("01"+ vslStLineAA +"ID")
		print("02"+ vslStLineAA +"Barcode")
		if i == 0:
			inputSelect = str(input(vslStLineAB))
			clearScreen()
			print(vslStTopBarAA)
			print(vslStLineAB  +" "+ getTimeAndDate(1) +" : "+ returnPageName(uiusBcCheckProduct))
	#INPUT SELECT
	if inputSelect == "1":
		#PRODUCT ID
		checka = vslStLineAB +"ID: "
		productID = str(input(checka))
		if productID !="":
			#SCAN
			productUrl = fldrMasterDatabase +"/"+ productID #FOLDER
			if os.path.exists(productUrl): #FOLDER
				dataUrl = fldrFileProduct, fldrFileCreationDate, fldrFileLogAb
				dataUrlLength = len(dataUrl)
				productComData =  it8c.dataCreateList(dataUrlLength,"")
				for i in range(0,dataUrlLength):
					currentUrl = productUrl +"/"+ dataUrl[i]
					if it8c.fileTextExists(currentUrl) == 1:
						productComData[i] = mainReadTextFile(currentUrl)
				#NAME
				productComData.extend([readProductDataRef(productComData[0])])
				#USER CONTENT
				userContentDataUrl = productUrl +"/"+ fldrFileDataContent
				userContentEz =0
				if it8c.fileTextExists(userContentDataUrl) == 1:
					userContentEz =1
					userContentData = it8c.copaRead(userContentDataUrl,"=")
					userContentDataLength = len(userContentData)
				#PRINT
				clearScreen()
				print(vslStTopBarAA)
				print(vslStLineAB  +" "+ getTimeAndDate(1) +" : "+ returnPageName(uiusBcCheckProduct))
				print("Name: ", productComData[3])
				print("Barcode:", productComData[0])
				print("Creation date: ", productComData[1])
				print("LogAb: ", productComData[2])
				if userContentEz == 1:
					print("")
					for i in range(0, userContentDataLength):
						pointa = userContentData[i][0]
						pointb = userContentData[i][1]
						print(pointa +":", pointb)
				checka = input(vslStLineAB)
	"""
	if inputSelect == "2":
		checka = vslStLineAB +"Barcode: "
		productID = str(input(checka))
	"""
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
				if userInput != mainExitCommandWithoutSaving:
					userInputId +=1
					userArrayContent.extend([userInput])
				else:
					continuity =0
					userArrayContent =""
					return ""
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
		dpScanArray = it8c.dataCreateArray(dpMaxID,6,"0")
		dpScanArray[0][0] ="id" #ID
		dpScanArray[0][1] ="logab"
		dpScanArray[0][2] ="mamount" #MAIN QUANTITY
		dpScanArray[0][3] ="camount" #LOGAB QUANTITY
		dpScanArray[0][4] ="barcodes"
		dpScanArray[0][5] ="info"	
		for i in range(1,dpMaxID):
			productUrl = fldrUrlMasterDatabase +"/"+ str(i) #URL
			productID = productUrl +"/"+ fldrFileProduct
			productLogAb = productUrl +"/"+ fldrFileLogAb
			productCreationDate = productUrl +"/"+ fldrFileCreationDate
			#ID FOLDER
			if os.path.exists(productUrl):	
				#LOG AB
				if it8c.fileTextExists(productLogAb) == 1:
					checka = mainReadTextFile(productLogAb)
					checkb = it8c.checkIfItIsNumber(checka)
					if checkb == 1:
						if checka == "1":
							productLogAbValue ="1"
						else:
							productLogAbValue ="0"
					else:
						productLogAbValue ="0"
				#ID (NAME)
				if it8c.fileTextExists(productID) == 1:
					content = mainReadTextFile(productID)
					if content !="":
						productName = content
				#CREATION DATE
				if it8c.fileTextExists(productCreationDate) == 1:
					content = mainReadTextFile(productCreationDate)
					if content !="":
						productCreationDateValue = content
			#COLLECT
			dpScanArray[i][0] = str(i) #ID
			dpScanArray[i][1] = str(productLogAbValue) #LOGAB
			dpScanArray[i][4] = productName #NAME
			dpScanArray[i][5] = readProductDataRef(productName) #INFO (INFO)
		#MATH
		productNameList = it8c.dataExtractArrayColumn(dpScanArray,4)
		productNameListRefd = it8c.dataCheckListObjects(productNameList)
		productNameListRefdLength = len(productNameListRefd)
		productArrayLength = len(dpScanArray)
		#RESET QUANTITY
		for i in range(0,productNameListRefdLength):
			productNameListRefd[i][0] ="0"
			productNameListRefd[i][1] ="0"
		#SCAN
		dpScanArrayHeight = len(dpScanArray)
		for i in range(1, dpScanArrayHeight):
			pointa = dpScanArray[i][4] #NAME
			#SCAN
			for j in range(0,productNameListRefdLength):
				pointb = productNameListRefd[j][2] #NAME
				if pointa == pointb:
					pointc = int(productNameListRefd[j][0]) +1 #MAIN QUANTITY
					pointd = int(productNameListRefd[j][1]) +1 #LOGAB QUANTITY
					productNameListRefd[j][0] = pointc
					dpScanArray[i][2] = pointc #ADD TO MAIN ARRAY
					#LOGAB
					currentProductIdUrl = fldrUrlMasterDatabase +"/"+ str(dpScanArray[i][0]) +"/"+ fldrFileLogAb #URL
					if it8c.fileTextExists(currentProductIdUrl) == 1:
						currentProductLogAb = str(mainReadTextFile(currentProductIdUrl))
						if currentProductLogAb == "1":
							productNameListRefd[j][1] = pointd
							dpScanArray[i][3] = pointd #ADD TO MAIN ARRAY
		#REMOVE 1ST LINE
		dpScanArrayOld = dpScanArray
		dpScanArrayOldLength = len(dpScanArray)
		dpScanArrayHeight = len(dpScanArrayOld) -1
		dpScanArrayWidth = len(dpScanArrayOld[0])
		dpScanArray = it8c.dataCreateArray(dpScanArrayHeight,dpScanArrayWidth,"")
		for i in range(1,dpScanArrayOldLength):
			dpScanArray[i -1] = dpScanArrayOld[i]
		#SEPERATE LOGABBS
		dpScanArrayHeight = len(dpScanArray)
		dpScanArrayWidth = len(dpScanArray[0])
		dpScanArrayTrueHeight =0
		dpScanArrayTrueStep =0
		dpScanArrayFalseHeight =0
		dpScanArrayFalseStep =0
		for xp in range(0,2):
			if xp == 1:
				dpScanArrayTrue = it8c.dataCreateArray(dpScanArrayTrueHeight,dpScanArrayWidth,"")
				dpScanArrayFalse = it8c.dataCreateArray(dpScanArrayFalseHeight,dpScanArrayWidth,"")
			for yp in range(0, dpScanArrayHeight):
				pointa = str(dpScanArray[yp][1])
				if pointa =="1":
					if xp == 0:
						dpScanArrayTrueHeight +=1
					if xp == 1:
						dpScanArrayTrue[dpScanArrayTrueStep] = dpScanArray[yp]
						dpScanArrayTrueStep +=1
				else:
					if xp == 0:
						dpScanArrayFalseHeight +=1
					if xp == 1:
						dpScanArrayFalse[dpScanArrayFalseStep] = dpScanArray[yp]
						dpScanArrayFalseStep +=1
		#CALCULATE QUANTITY
		dpScanArrayQuantity = it8c.dataCheckListObjects(it8c.dataExtractArrayColumn(dpScanArray,4))
		dpScanArrayQuantityLength = len(dpScanArrayQuantity)
		dpScanLogAbbTrueQuantity = it8c.dataCheckListObjects(it8c.dataExtractArrayColumn(dpScanArrayTrue,4))
		dpScanLogAbbTrueQuantityLength = len(dpScanLogAbbTrueQuantity)
		#RESET QUANTITY
		for i in range(0,dpScanArrayQuantityLength):
			dpScanArrayQuantity[i][0] = dpScanArrayQuantity[i][1]
			dpScanArrayQuantity[i][1] ="0"
		#CALCULATE
		for yp in range(0,dpScanArrayQuantityLength):
			pointa = dpScanArrayQuantity[yp][2]
			for xp in range(0,dpScanLogAbbTrueQuantityLength):
				pointb = dpScanLogAbbTrueQuantity[xp][2]
				if pointa == pointb:
					dpScanArrayQuantity[yp][1] = str(dpScanLogAbbTrueQuantity[xp][1])
		dpScanArrayQuantityWidth = len(dpScanArrayQuantity[0])
		dpScanLogAbbTrueLength =0
		dpScanLogAbbTrueStep =0
		dpScanLogAbbFalseLength =0
		dpScanLogAbbFalseStep =0
		for xp in range(0,2):
			if xp == 1:
				dpScanLogAbbTrueQuantity = it8c.dataCreateArray(dpScanLogAbbTrueLength,dpScanArrayQuantityWidth,"")
				dpScanLogAbbFalseQuantity = it8c.dataCreateArray(dpScanLogAbbFalseLength,dpScanArrayQuantityWidth,"")
			for yp in range(0,dpScanArrayQuantityLength):
				pointa = int(dpScanArrayQuantity[yp][1])
				if pointa == 0:
					if xp == 0:
						dpScanLogAbbFalseLength +=1
					if xp == 1:
						dpScanLogAbbFalseQuantity[dpScanLogAbbFalseStep] = dpScanArrayQuantity[yp]
						dpScanLogAbbFalseStep +=1
				else:
					if xp == 0:
						dpScanLogAbbTrueLength +=1
					if xp == 1:
						dpScanLogAbbTrueQuantity[dpScanLogAbbTrueStep] = dpScanArrayQuantity[yp]
						dpScanLogAbbTrueStep +=1
		#ADD INFO
		dpScanLogAbbTrueQuantityLength = len(dpScanLogAbbTrueQuantity)
		dpScanLogAbbTrueQuantityWidth = len(dpScanLogAbbTrueQuantity[0])
		dpScanLogAbbFalseQuantityLength = len(dpScanLogAbbFalseQuantity)
		dpScanLogAbbFalseQuantityWidth = len(dpScanLogAbbFalseQuantity[0])
		for xp in range(0,2):
			if xp ==0:
				currentLength = dpScanLogAbbTrueQuantityLength
				currentWidth = dpScanLogAbbTrueQuantityWidth
				refdArray = dpScanLogAbbTrueQuantity
			if xp ==1:
				currentLength = dpScanLogAbbFalseQuantityLength
				currentWidth = dpScanLogAbbFalseQuantityWidth
				refdArray = dpScanLogAbbFalseQuantity
			currentArray = it8c.dataCreateArray(currentLength,currentWidth +1,"")
			for yp in range(0,currentLength):
				pointa = refdArray[yp][2]
				pointb = readProductDataRef(pointa)
				for zp in range(0,currentWidth):
					currentArray[yp][zp] = refdArray[yp][zp]
				currentArray[yp][currentWidth] = pointb
			if xp ==0:
				del dpScanLogAbbTrueQuantity
				dpScanLogAbbTrueQuantity = currentArray
			if xp ==1:
				del dpScanLogAbbFalseQuantity
				dpScanLogAbbFalseQuantity = currentArray
		#USER DATA CONTENT
		idLineTrue = it8c.dataExtractArrayColumn(dpScanArrayTrue,0) #LOGAB TRUE PRODUCT ID'S
		idLineFalse = it8c.dataExtractArrayColumn(dpScanArrayFalse,0) #LOGAB FALSE PRODUCT ID'S
		#SCAN EXISTS FILES
		for zp in range(0,2):
			if zp == 1:
				idLineTrueKeys =[]
				idLineFalseKeys =[]
			for xp in range(0,2):
				resultArray =[]
				if xp == 0:
					checkArray = idLineTrue
				if xp == 1:
					checkArray = idLineFalse
				checkArrayLength = len(checkArray)
				for yp in range(0,checkArrayLength):
					pointa = str(checkArray[yp]) #ID
					productUrl = fldrUrlMasterDatabase +"/"+ str(pointa) #URL
					productUserDataContent = productUrl +"/"+ fldrFileDataContent
					if it8c.fileTextExists(productUserDataContent) == 1:
						if zp == 0:
							resultArray.extend([pointa])
						if zp == 1:
							fileContent = it8c.copaRead(productUserDataContent,"=")
							fileContentKeys = it8c.dataExtractArrayColumn(fileContent,0)
							fileContentKeysLength = len(fileContentKeys)
							for i in range(0, fileContentKeysLength):
								pointb = fileContentKeys[i]
								if pointb !="":
									resultArray.extend([pointb])
				if zp == 1:
					checka = it8c.encryptSha256("&%2689")
					resultArray.extend([checka])
					fileContent = it8c.dataExtractArrayColumn(it8c.dataCheckListObjects(resultArray),2)
					fileContentLength = len(fileContent)
					resultArray =[]
					for i in range(0, fileContentLength):
						checkb = fileContent[i]
						if checkb != checka:
							resultArray.extend([checkb])
				if xp == 0:
					if zp == 0:
						idLineTrue = resultArray
					if zp == 1:
						idLineTrueKeys = resultArray
				if xp == 1:
					if zp == 0:
						idLineFalse = resultArray
					if zp == 1:
						idLineFalseKeys = resultArray
		
		#PARAMETER ADDER
		idLineTrueAccess =0
		idLineFalseAccess =0
		if len(idLineTrueKeys) > 1:
			idLineTrueAccess =1
			idLineTrueArray = scanDatabaseExtraParameterAa(idLineTrue, idLineTrueKeys)
		if len(idLineFalseKeys) > 1:
			idLineFalseAccess =1
			idLineFalseArray = scanDatabaseExtraParameterAa(idLineFalse, idLineFalseKeys)
		#SAVE FILES
		url = fldrUrlSystem +"/"+ fldrFileDbProductGlobalView #DB GLOBAL VIEW
		it8c.csvWriteFile(dpScanArray,url,";",0)
		url = fldrUrlSystem +"/"+ fldrFileDbProductLogAbTrue #DB LOGAB TRUE
		it8c.csvWriteFile(dpScanArrayTrue,url,";",0)
		url = fldrUrlSystem +"/"+ fldrFileDbProductLogAbFalse #DB LOGAB FALSE
		it8c.csvWriteFile(dpScanArrayFalse,url,";",0)
		url = fldrUrlSystem +"/"+ fldrFileDbProductQuantityTrue #DB QUANTITY TRUE
		it8c.csvWriteFile(dpScanLogAbbTrueQuantity,url,";",0)
		url = fldrUrlSystem +"/"+ fldrFileDbProductQuantityFalse #DB QUANTITY FALSE
		it8c.csvWriteFile(dpScanLogAbbFalseQuantity,url,";",0)
		if idLineTrueAccess == 1:
			url = fldrUrlSystem +"/"+ fldrFileDbProductDataViewTrue #DB USER CONTENT TRUE
			it8c.csvWriteFile(idLineTrueArray,url,";",0)
		if idLineFalseAccess == 1:
			url = fldrUrlSystem +"/"+ fldrFileDbProductDataViewFalse #DB USER CONTENT FALSE
			it8c.csvWriteFile(idLineFalseArray,url,";",0)
		#RESET
		del dpScanArrayOld
		del dpScanArray
		del dpScanArrayTrue
		del dpScanArrayFalse
		del dpScanArrayQuantity
		del dpScanLogAbbTrueQuantity
		del dpScanLogAbbFalseQuantity
		del dpScanArrayQuantityLength
#PARAMETER AA
def scanDatabaseExtraParameterAa(contentArray, keyArray):
	contentArrayLength = len(contentArray)
	keyArrayLength = len(keyArray)
	resultArrayWidth = keyArrayLength +3
	resultArrayHeight = contentArrayLength +1
	resultArray = it8c.dataCreateArray(resultArrayHeight,resultArrayWidth," ")
	#KEY CONTENT
	for i in range(0,keyArrayLength):
		resultArray[0][i] = keyArray[i]
	#PRODUCTS
	productIDpos = keyArrayLength
	productBarcodePos = productIDpos +1
	productInfoPos = productBarcodePos +1
	resultArray[0][productIDpos] ="ID"
	resultArray[0][productBarcodePos] ="Barcode"
	resultArray[0][productInfoPos] ="Info"
	for i in range(0, contentArrayLength):
		#i = contentArrayLength - j -1
		y = i+1
		#PRODUCT INFO
		productID = str(contentArray[i])
		productUrl = fldrUrlMasterDatabase +"/"+ str(productID)
		#PRODUCT BARCODE
		url = productUrl +"/"+ fldrFileProduct
		if it8c.fileTextExists(url) == 1:
			productCode = mainReadTextFile(url)
		#PRODUCT INFO
		productInfo = readProductDataRef(productCode)
		#ARRAY BASIC DATA
		resultArray[y][productIDpos] = productID
		resultArray[y][productBarcodePos] = productCode
		resultArray[y][productInfoPos] = productInfo
		#PRODUCT USER DATA
		url = productUrl +"/"+ fldrFileDataContent
		if it8c.fileTextExists(url) == 1:
			#LIMITS
			productUserData = it8c.copaRead(url,"=")
			productUserDataHeight = len(productUserData)
			productUserDataWidth = len(productUserData[0])
			#CONTENT
			for yp in range(0,productUserDataHeight):
				pointa = productUserData[yp][0]
				for xp in range(0,keyArrayLength):
					checka = resultArray[0][xp]
					if pointa == checka:
						#IMPORT USER DATA VALUE BY KEY
						resultArray[y][xp] = productUserData[yp][1]
	return resultArray
#PRINT LIMITED
def viewLimitedArray(currentLogFile, customHeight, mode):
	if customHeight !="":
		maxHeight = customHeight
	else:
		maxHeight =10
	currentLogWidth = len(currentLogFile[0])
	currentLogHeight = len(currentLogFile)
	checka = it8c.dataFlipArrayObjects(currentLogFile)
	if currentLogHeight <= maxHeight:
		printArray = checka
	else:
		checkb = it8c.dataCreateArray(maxHeight,currentLogWidth,"")
		for i in range(0, maxHeight):
			checkb[i] = checka[i]
		printArray = checkb
	if mode ==2:
		printArray = it8c.dataFlipArrayObjects(printArray)
		printArrayTitles = printArray[0]
		printArrayLength = len(printArray)
		returnArrayWidth = len(printArray[0])
		returnArray = it8c.dataCreateArray(printArrayLength -1,returnArrayWidth,"")
		for i in range(1,printArrayLength):
			returnArray[i -1] = printArray[i]
		returnArray = it8c.dataAddArrayRow(returnArray,printArrayTitles)
		returnArray = it8c.dataFlipArrayObjects(returnArray)
		return returnArray
	else:
		printArrayB = it8c.dataFlipArrayObjects(printArray)
		if mode ==0:
			invArrayInfo = "ID", "LA", "MQ", "CQ", "Barcode", "Info"
		if mode ==1:
			invArrayInfo = "MQ", "CQ", "Barcode", "Info"
		printArray = it8c.dataAddArrayRow(printArrayB,invArrayInfo)
		printArrayB = it8c.dataFlipArrayObjects(printArray)
		return printArrayB
#VIEW GLOBAL INVENTORY MOMENT
def viewGlobalInvMom(customHeight):
	currentLogUrl = fldrUrlSystem +"/"+ fldrFileDbProductGlobalView
	if it8c.fileTextExists(currentLogUrl) == 1:
		currentLogFile = it8c.csvReadFile(currentLogUrl,";")
		print(print2dArray(viewLimitedArray(currentLogFile,customHeight,0)))
#VIEW LOGAB TRUE INVENTORY MOMENT
def viewLogAbTrueInvMom(customHeight):
	currentLogUrl = fldrUrlSystem +"/"+ fldrFileDbProductLogAbTrue
	if it8c.fileTextExists(currentLogUrl) == 1:
		currentLogFile = it8c.csvReadFile(currentLogUrl,";")
		print(print2dArray(viewLimitedArray(currentLogFile,customHeight,0)))
#VIEW LOGAB SEP INVENTORY MOMENT
def viewLogAbSepInvMom(customHeight):
	#SELCT
	print("01"+ vslStLineAA +"Log")
	print("02"+ vslStLineAA +"Quantity")
	print("03"+ vslStLineAA +"Parameters")
	inputSelect = str(input(vslStLineAB))
	if inputSelect !="":
		clearScreen()
		print(vslStTopBarAA)
		print(vslStLineAB  +" "+ getTimeAndDate(1) +" : "+ returnPageName(uiusBcCheckInventory))	
		access =0
		if inputSelect == "1":
			#URL
			dpScanArrayFalseUrl = fldrUrlSystem +"/"+ fldrFileDbProductLogAbFalse
			dpScanArrayTrueUrl = fldrUrlSystem +"/"+ fldrFileDbProductLogAbTrue
			access =1
			printMode =0
		if inputSelect == "2":
			#URL
			dpScanArrayFalseUrl = fldrUrlSystem +"/"+ fldrFileDbProductQuantityFalse
			dpScanArrayTrueUrl = fldrUrlSystem +"/"+ fldrFileDbProductQuantityTrue
			access =1
			printMode =1
		if inputSelect == "3":
			#URL
			dpScanArrayFalseUrl = fldrUrlSystem +"/"+ fldrFileDbProductDataViewFalse
			dpScanArrayTrueUrl = fldrUrlSystem +"/"+ fldrFileDbProductDataViewTrue
			access =1
			printMode =2
		if access == 1:
			#LOAD FILES
			if it8c.fileTextExists(dpScanArrayTrueUrl) == 1:
				if it8c.fileTextExists(dpScanArrayFalseUrl) == 1:
					#ARRAYS
					dpScanArrayTrue = it8c.csvReadFile(dpScanArrayTrueUrl,";")
					dpScanArrayFalse = it8c.csvReadFile(dpScanArrayFalseUrl,";")
					#PRINT
					print("Current")
					print(print2dArray(viewLimitedArray(dpScanArrayTrue,customHeight,printMode)))
					print()
					print("History")
					print(print2dArray(viewLimitedArray(dpScanArrayFalse,customHeight,printMode)))
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
	if productID !="":
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
								#PAR HISTORY FOLDER
								fldrUrl = productUrl +"/"+ fldrUrlDataContentParameters
								if not os.path.exists(fldrUrl):
									os.makedirs(fldrUrl)
								#PAR HISTORY NAME
								fileName = str.lower(it8c.lettersdigits(pointa,""))
								fileUrl = fldrUrl +"/"+ fileName +".txt"
								it8c.copaMod(fileUrl,getTimeAndDate(0),pointb,0,"")
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
#EXIT
def exitLogo():
	a = "#########################"
	b = "##      ##########      ##"
	c = "##      ##      ##      ##"
	d = "##########      ########"
	e = "##      ##      ########"
	f = "##      ##      ##      ##"
	g = "##      ##      ##      ##"
	h = "##      ##      ########"
	return "\n"+ a +"\n"+ b +"\n"+ c +"\n"+ d +"\n"+ e +"\n"+ f +"\n"+ g +"\n"+ h