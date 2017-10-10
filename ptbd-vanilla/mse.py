#|==============================================================|#
# Made by IntSPstudio
# PTB Database
# Thank you for using this software!
# ID: 980005031
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
#FOLDERS
fldrMasterDatabase ="database"
fldrUrlMasterDatabase = fldrMasterDatabase
fldrFileModifyAdder ="macon"
fldrFileUrlModifyAdder = fldrUrlMasterDatabase +"/"+ fldrFileModifyAdder +".txt"
fldrFileMasterContentFile ="mstfle"
fldrFileUrlMasterContentFile = fldrUrlMasterDatabase +"/"+ fldrFileMasterContentFile +".csv"
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
#READ LIST FILE
def mainReadTextListFile(fileName):
	return it8c.fileReadText(fileName)
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
#PAGES
uiusBcCheckInventory ="1"
uiusBcAddToInvetory ="2"
uiusBcModifyAdder ="3"
uiusBckExit ="4"
uiusBckMenu ="0"
def returnPageName(pageID):
	if pageID == uiusBcCheckInventory:
		return "Inventory"
	elif pageID == uiusBcAddToInvetory:
		return "Add to inventory"
	elif pageID == uiusBcModifyAdder:
		return "Modify input"
	elif pageID == uiusBckExit:
		return "Exit"
	elif pageID == uiusBckMenu:
		return "Main menu"
	else:
		return "Error"
#CLEAR SCREEN START
def clsScreenStart():
	clearScreen()
	print(vslStTopBarAA)
	print(vslStLineAB  +" "+ getTimeAndDate(1))
#READ USER CONTENT
def readUserContentFromDatabase():
	maxHeight =15
	if it8c.fileTextExists(fldrFileUrlMasterContentFile) == 1:
		if it8c.fileTextExists(fldrFileUrlModifyAdder) == 1:
			#TITLE
			userInSkelTxt = mainReadTextListFile(fldrFileUrlModifyAdder)
			userInSkelTxtHeight = len(userInSkelTxt)
			userInSkelTxtTitles = it8c.dataCreateList(userInSkelTxtHeight +1,"")
			userInSkelTxtTitles[0] ="DATE"
			for i in range(0, userInSkelTxtHeight):
				userInSkelTxtTitles[i +1] = str.upper(userInSkelTxt[i])
			#MASTER DATA
			pointe = it8c.csvReadFile(fldrFileUrlMasterContentFile,";")
			pointa = it8c.dataFlipArrayObjects(pointe)
			pointb = len(pointa)
			pointd = len(pointa[0])
			#LIMITED HEIGHT CHECK
			if pointb <= maxHeight:
				pointc = it8c.dataFlipArrayObjects(it8c.dataAddArrayRow(pointa,userInSkelTxtTitles))
				return print2dArray(pointc)
			else:
				pointc = it8c.dataCreateArray(maxHeight,pointd," ")
				for i in range(0, maxHeight):
					pointc[i] = pointa[i]
				pointa = it8c.dataFlipArrayObjects(it8c.dataAddArrayRow(pointc,userInSkelTxtTitles))
				return print2dArray(pointa)
#INPUT CONTENT
def addUserContentToDatabase():
	if it8c.fileTextExists(fldrFileUrlModifyAdder) == 1:
		#LOAD IN SKEL TXT
		userInSkelTxt = mainReadTextListFile(fldrFileUrlModifyAdder)
		userInSkelTxtHeight = len(userInSkelTxt)
		#ADD RESULTS
		resultArrayHeight = userInSkelTxtHeight +1
		resultArray = it8c.dataCreateList(resultArrayHeight,"")
		resultArray[0] = getTimeAndDate(1)
		for i in range(0, userInSkelTxtHeight):
			pointa = userInSkelTxt[i]
			pointb = vslStLineAB +" "+ pointa +": "
			pointc = input(pointb)
			if pointc =="":
				pointc =" "
			resultArray[i +1] = pointc
		#PRINT RESULTS
		clsScreenStart()
		print(print1dArray(resultArray))
		#SAVE RESULTS
		if it8c.fileTextExists(fldrFileUrlMasterContentFile) == 1:
			pointa = it8c.csvReadFile(fldrFileUrlMasterContentFile,";")
			pointb = it8c.dataAddArrayRow(pointa,resultArray)
			it8c.csvWriteFile(pointb,fldrFileUrlMasterContentFile,";",0)
		else:
			pointa =""
			for i in range(0, resultArrayHeight):
				pointb = resultArray[i]
				if pointa !="":
					pointa = pointa +";"+ pointb
				else:
					pointa = pointb
			mainWriteListTextFile(pointa, fldrFileUrlMasterContentFile)
	else:
		print("File doesent exists")
	pointc = input(vslStLineAB)
#INPUT MODIFY
def getInputSkelTexts():
	userInput =""
	userInpCounter =0
	userInputList =[]
	while userInput != mainExitCommand:
		pointa = str(userInpCounter) +": "
		pointb = input(pointa)
		pointc = makeLdMod(pointb)
		if pointc !="":
			if pointc != mainExitCommand:
				if pointc == mainExitCommandWithoutSaving:
					return ""
				else:
					userInput = pointc
					userInputList.extend([userInput])
					userInpCounter +=1
			else:
				userInput = mainExitCommand
	#CLEAR
	clsScreenStart()
	#PRINT LIST
	print(print1dArray(userInputList))
	pointa = input(vslStLineAB)
	#SAVE
	if os.path.exists(fldrUrlMasterDatabase):
		save1dArray(userInputList, fldrFileUrlModifyAdder)
#CHECK FOLDERS
def checkSystemFolders():
	#DATABASE
	if not os.path.exists(fldrUrlMasterDatabase):
		os.makedirs(fldrUrlMasterDatabase)
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