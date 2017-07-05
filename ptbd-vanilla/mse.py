#|==============================================================|#
# Made by IntSPstudio
# PTB Database
# Thank you for using this software!
# ID: 980005032
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import platform
import datetime
#OPERATING SYSTEM SETTINGS
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
#PAGES
pagesMainMenuTitle ="Menu"
pagesMainMenu ="0"
pagesAddEventTitle ="Add event"
pagesAddEvent ="1"
pagesInventoryTitle ="Inventory"
pagesInventory ="Inventory"
pagesShowEventsTitle ="Events"
pagesShowEvents ="2"
pagesFeaturesTitle ="Features"
pagesFeatures ="3"
pagesShowInfoTitle ="Info"
pagesShowInfo ="4"
pagesOpenLogTitle ="Select Log"
pagesOpenLog ="5"
pagesOpenProjectTitle ="Select Project"
pagesOpenProject ="6"
pagesExitTitle ="Exit"
pagesExit ="7"
#VISUAL
vslStLineAA ="]"
vslStLineAB ="=="+ vslStLineAA
#TIME
clDate =""
clYear =""
clMonth =""
clDay =""
clHour =""
clMinute =""
clSecond =""
def updateDateTime(checka):
	pointa = str(checka.year) +"-"+ str(checka.month) +"."+ str(checka.day)
	pointb = str(checka.hour) +":"+ str(checka.minute) +":"+ str(checka.second)
	pointc = pointa, pointb
	return pointc
#CHECK PAGE
def checkCurrentPage(pid):
	if pid == pagesAddEvent:
		result = pagesAddEventTitle
	elif pid == pagesShowEvents:
		result = pagesShowEventsTitle
	elif pid == pagesFeatures:
		result = pagesFeaturesTitle
	elif pid == pagesShowInfo:
		result = pagesShowInfoTitle
	elif pid == pagesOpenLog:
		result = pagesOpenLogTitle
	elif pid == pagesOpenLog:
		result = pagesOpenLogTitle
	elif pid == pagesOpenProject:
		result = pagesOpenProjectTitle
	elif pid == pagesExit:
		result = pagesExitTitle
	else:
		result = pagesMainMenuTitle
	return result
#PRINT PAGES
def printAllPages():
	list =""
	imax = int(pagesExit) +1
	for i in range(1, imax):
		checka = str(i)
		pointa = checkCurrentPage(checka)
		if i < imax -1:
			list = list +"0"+ checka + vslStLineAA + pointa +"\n"
		else:
			list = list +"0"+ checka + vslStLineAA + pointa
	return list
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