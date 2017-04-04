#|==============================================================|#
# Made by IntSPstudio
# PTB Database
# Thank you for using this software!
# Version: 0.0.1.20170404
# ID: 980005032
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import it8c  #Data handling
import os #OS commands
import mse #Main settings
import datetime #Timing
#SETTINGS
uiusOS = mse.osSystem
mainClearCommand = mse.osClearCommand
#dataFolderName = use.folderDataName
continuity =1
mainPage =""
clcnPages =""

currentProject =""
currentLogUrl =""
currentLogFile =""
currentLogID =0
currentLog =""
#PAGES
uiusBckAddEvent = mse.pagesAddEvent
uiusBckShowEvents = mse.pagesShowEvents
uiusBckShowInfo = mse.pagesShowInfo
uiusBckOpenLog = mse.pagesOpenLog
uiusBckOpenProject = mse.pagesOpenProject
uiusBckMainMenu = mse.pagesMainMenu
uiusBckExit = mse.pagesExit
#VISUAL
bgdLine = it8c.vslTerminalLine(0,"")
dcnyStInputLine = mse.vslStLineAB
#BASIC OS COMMANDS
def exCommand(command):
	if command == "clear":
		os.system(mainClearCommand)
#BASIC PRINT
def vslBasicTopPrint():
	print(bgdLine)
	if currentProject !="":
		if currentLog !="":
			#print(dcnyStInputLine +" "+ mse.checkCurrentPage(mainPage) +" - Project: "+ currentProject +" - Log: "+ currentLog)
			print(dcnyStInputLine +" "+ "Project:"+ currentProject +" - Log:"+ currentLog)
		else:
			#print(dcnyStInputLine +" "+ mse.checkCurrentPage(mainPage) +" - Project: "+ currentProject)
			print(dcnyStInputLine +" "+ "Project:"+ currentProject)
	else:
		#print(dcnyStInputLine +" "+ mse.checkCurrentPage(mainPage))
		print(dcnyStInputLine)
#CHANGE LOG FILE
def changeLogFile():
	result =""
	if currentProject !="":
		checka = str(input("Log name: "))
		checkb = str.lower(it8c.lettersdigits(checka,""))
		if checkb !="":
			result = checkb
		else:
			checka = input("Incorrect name")
	else:
		checka = input("No open project")
	return result
#ADD EVENT TO PROJECT
def addEventToProject():
	currentLogUrl = currentProject +"/"+ currentLog +".csv"
	if it8c.fileTextExists(currentLogUrl) == 1:
		currentLogFile = it8c.csvReadFile(currentLogUrl,";")
		currentLogID = len(currentLogFile)
	else:
		if not os.path.exists(currentProject):
			os.makedirs(currentProject)
		currentLogID =0
	checka = datetime.datetime.now()
	pointa = it8c.dataCreateList(2,"")
	pointb = mse.updateDateTime(checka)
	pointa[0] = str(currentLogID)
	pointa[1] = pointb[0] +" "+ pointb[1]
	pointc =""
	exitCode = "ext"
	while pointc != exitCode:
		pointc = input("Event: ")
		if pointc !="":
			if pointc != exitCode:
				pointa.extend([pointc])
			
	if currentLogID > 0:
		currentLogFile = it8c.dataAddArrayRow(currentLogFile,pointa)
	else:
		
		currentLogFile = it8c.dataCreateArray(1,1,"")
		currentLogFile[0] = pointa
	it8c.csvWriteFile(currentLogFile,currentLogUrl,";",0)
#START
if __name__ == "__main__":
	while continuity == 1:
		#ADD EVENT
		if mainPage == uiusBckAddEvent:
			#TA
			exCommand("clear")
			vslBasicTopPrint()
			#TB
			if currentProject !="":
				if currentLog !="":
					addEventToProject()
				else:
					checka = input("Open log first")
			else:
				checka = input("No open project")
			#TC
			mainPage = uiusBckMainMenu
		#SHOW EVENTS
		if mainPage == uiusBckShowEvents:
			#TA
			exCommand("clear")
			vslBasicTopPrint()
			#TB
			if currentProject !="":
				if currentLog !="":
					currentLogUrl = currentProject +"/"+ currentLog +".csv"
					if it8c.fileTextExists(currentLogUrl) == 1:
						currentLogFile = it8c.csvReadFile(currentLogUrl,";")
						currentLogWidth = len(currentLogFile[0])
						currentLogHeight = len(currentLogFile)
						maxHeight =10
						checkb = it8c.dataFlipArrayObjects(currentLogFile)
						if currentLogHeight <= maxHeight:
							print(it8c.dataSmrPrintArray(checkb," : "," ",0))
						else:
							checkc = it8c.dataCreateArray(maxHeight,currentLogWidth,"")
							for i in range(0, maxHeight):
								checkc[i] = checkb[i]
							print(it8c.dataSmrPrintArray(checkc," : "," ",0))
			#TC
			checka = input(dcnyStInputLine)
			mainPage = uiusBckMainMenu
		#INFO
		if mainPage == uiusBckShowInfo:
			#TA
			exCommand("clear")
			vslBasicTopPrint()
			#TC
			checka = input(dcnyStInputLine)
			mainPage = uiusBckMainMenu
		#LOG
		if mainPage == uiusBckOpenLog:
			#TA
			exCommand("clear")
			vslBasicTopPrint()
			#TB
			checka = changeLogFile()
			if checka !="":
				currentLog = checka
			#TC
			mainPage = uiusBckMainMenu
		#PROJECT
		if mainPage == uiusBckOpenProject:
			#TA
			exCommand("clear")
			vslBasicTopPrint()
			#TB
			checka = str(input("Project name: "))
			checkb = str.lower(it8c.lettersdigits(checka,""))
			if checkb !="":
				currentProject = checkb
			#TC
			mainPage = uiusBckMainMenu
		#EXIT
		if mainPage == uiusBckExit:
			#TA
			exCommand("clear")
			continuity =0
		#MENU
		else:
			#TA
			exCommand("clear")
			vslBasicTopPrint()
			print(mse.printAllPages())
			#TC
			checka = input(dcnyStInputLine)
			mainPage = str(checka)