"""                                                  ╔════════╗
                                                     ║EGYPTIAN║
                                                     ╚║║║║║║║║╝
╔════════════════════╗  //////\
║~  Google Search Py ║ ║/////  \
║~  copyright © 2021 ║//////    \
║~  Auther : XAR     ║║║║║║║ ╔╗ ║              _Version_ 1.0.0
║~  Contact With US  ╚╚╚╚╚╚╚═╝╚═╝═════════════════════════════╗
║~  Discord: https://discord.gg/kz4Y5fa9x9                    ║
║~  https://www.youtube.com/channel/UCwJLxZbiR1tT0OikfAHAk1Q  ║
╚═════════════════════════════════════════════════════════════╝
"""
import urllib.request
import urllib.error
import re
import os
# Project Data
__author__      = "AhmedAbdelaziz.Reda"
__copyright__   = "Copyright 2020-2021"
__version__     = "2.0.0"
# Main Class
class XGS:
	def __init__(XAMFRA):
		XAMFRA.__author__      = "AhmedAbdelaziz.Reda"
		XAMFRA.__copyright__   = "Copyright 2020-2021"
		XAMFRA.__version__     = "2.0.0"
	
	def XXCLS(XAMFRA):     # TO CLEAR THE SCREEN
		os.system('cls' if os.name=='nt' else 'clear')
	
	def XFILT(XAMFRA):
		RERESP = re.findall('<a.href="/url\?q=(.*?)\&amp', str(XAMFRA.GORESP))
		for REO in RERESP:
			if "https://support.google.com" in REO or "https://accounts.google.com/" in REO:
				pass
			elif "onion.to" in REO:
				print("|\n| "+REO[8:].replace(".to",""))
			elif "onion.ly" in REO:
				print("|\n| "+REO[8:].replace(".ly",""))
			elif "onion.cab" in REO:
				print("|\n| "+REO[8:].replace(".cab",""))
			elif "onion.city" in REO:
				print("|\n| "+REO[8:].replace(".city",""))
			elif "onion.to" in REO:
				print("|\n| "+REO[8:].replace(".direct",""))
			else: 
				print("|\n| "+REO)

	def XREQU(XAMFRA):
		REQURL = urllib.request.Request(XAMFRA.GOSURL)
		REQURL.add_header('User-Agent', 'Mozilla/7000.0 XAR')
		REQURL.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
		REQURL.add_header('Accept-Language', 'en-US,en;q=0.8')
		REQTGO = urllib.request.urlopen(REQURL, timeout=10)
		XAMFRA.GORESP = REQTGO.read()
		REQTGO.close()

	def XGSN(XAMFRA): # DOCK GOOGLE SEARCH
		XGSINPUT = input("\n#  SEARCH  : ")
		XGSNUPAGE = input("# PAGE NUM : ")
		XAMFRA.GOINPB = XGSNUPAGE
		XAMFRA.GOINPS = XGSINPUT.replace(" ", "%20")
		XAMFRA.GOSURL = 'https://www.google.com/search?q='+XAMFRA.GOINPS+'&client=firefox-b-d&start='+XAMFRA.GOINPB
		XGSC.XREQU()
		print("""    ╔═══════════════╗\n    ║     RESULT    ║\n    ╚═══════════════╝\n""")
		XGSC.XFILT()
		# xx[:-3]	
	def XGSD(XAMFRA): # DOCK GOOGLE SEARCH FOR DARK
		XGSINPUT = input("\n#  SEARCH  : ")
		XGSNUPAGE = input("# PAGE NUM : ")
		XGSDARKLI = ['%20site:"onion.to"','%20site:"onion.city"','%20site:"onion.cab"','%20site:"onion.direct"','%20site:"onion.ly"']
		print("""    ╔═══════════════╗\n    ║     RESULT    ║\n    ╚═══════════════╝\n""")
		for XFI in XGSDARKLI:
			XAMFRA.GOINPB = XGSNUPAGE
			XAMFRA.GOINPS = XGSINPUT.replace(" ", "%20")+XFI
			XAMFRA.GOSURL = 'https://www.google.com/search?q='+XAMFRA.GOINPS+'&client=firefox-b-d&start='+XAMFRA.GOINPB
			XGSC.XREQU()
			XGSC.XFILT()
	def XGAB(XAMFRA):
		print("""
 ########################### ABOUT US ############################
 #                                                               #
 # [1][WE LOVE TO GO DEEP IN ANY THING ]                         #
 # [2][WE THINK BEFORE HOW TO HACK SOMETHING HOW IT WORKS]       #
 #                                                               #
 # <WE FOCUS TO GET ANY NEW INFORMATION IN CYBER SECURITY FIELD> #
 #<AND MAKE THE COMMUNITY HAVE KNOWLEDGE ABOUT ALL THESE THINGS> #
 #                                                               #
 # Discord: discord.gg/kz4Y5fa9x9                                #
 # https://www.youtube.com/channel/UCwJLxZbiR1tT0OikfAHAk1Q      #
 *****************************************************************
""")
	def XGBA(XAMFRA):
		print("""
 #################################
 #    TOOL FOR GOOGLE DORK       #
 #       --- OPTION ----         #
 #   A   #-----> About Us        #
 #   B   #-----> Show Banner     #
 #   C   #-----> CLEAR SCREEN    #
 #   D   #-----> DEEP WEB DORK   #
 #   N   #-----> NORMAL DORK     #
 #   L   #-----> DORK Techniques #
 #################################
""")
	def XGDT(XAMFRA):
		print("""
 ###################################
 #    Google Hacking Techniques    #
 #         --- OPTION ----         #
 # filetype:                       #
 #   SEARCH ABOUT FILE EXTENSION   # 
 #   EX.  filetype:xls             #
 #                                 #
 # inurl:                          #
 #   SEARCH ABOUT SPECIFIC URL     #
 #   EX.  inurl:php?id=            #
 #                                 #
 # intitle:                        #
 #   SEARCH ABOUT TITLE IN THE     #
 #   WEBPAGE.EX.  filetype:pdf     #
 #                                 #
 # inanchor:                       # 
 #   SEARCH ABOUT FILE EXTENSION   #
 #   EX.  inanchor:pdf             # 
 #                                 #
 # intext:                         #
 #   SEARCH ABOUT TEXT IN THE      #
 #   WEBPAGE.EX. intext:cvv        #
 #                                 #
 # site:                           #
 #   SEARCH ABOUT FILE EXTENSION   #
 #   EX.  site:gov                 #
 #                                 #
 # * :                             #
 #   SEARCH ABOUT ANY WORD BETWEEN #
 #   TWO SENTENCES                 #
 #   EX.  site:*.example.com       #
 #                                 #
 # - :                             #
 #   SEARCH ABOUT WORD YOU DON'T   #
 #   WANT IT EX.                   #
 #  site:msn.com -site:www.msn.com #
 #                                 #
 # + :                             #
 #   SEARCH ABOUT WORD YOU WANT IT #
 #   EX.                           #
 #  site:exa.com +site:www.exa.com #
 #                                 #
 ###################################
""")
#===============================================================================================

if __name__ == '__main__':
	XGSC = XGS()
	XGSC.XXCLS()
	print("""
 #################################
 #    TOOL FOR GOOGLE DORK       #
 #       --- OPTION ----         #
 #   A   #-----> About Us        #
 #   B   #-----> Show Banner     #
 #   C   #-----> CLEAR SCREEN    #
 #   D   #-----> DEEP WEB DORK   #
 #   N   #-----> NORMAL DORK     #
 #   L   #-----> DORK Techniques #
 #################################
""")
	while True:
		XCOMMANDER = input("\n XGS #>")
		if XCOMMANDER == "A" or XCOMMANDER == "a":
			XGSC.XGAB()
		elif XCOMMANDER == "B" or XCOMMANDER == "b":
			XGSC.XGBA()
		elif XCOMMANDER == "C" or XCOMMANDER == "c":
			XGSC.XXCLS()
		elif XCOMMANDER == "D" or XCOMMANDER == "d":
			XGSC.XGSD()
		elif XCOMMANDER == "N" or XCOMMANDER == "n":
			XGSC.XGSN()
		elif XCOMMANDER == "L" or XCOMMANDER == "l":
			XGSC.XGDT()
		else:
			print("\n# can't To Understand This command .\n# IF you Can to contact with us and\n# tell us about this error.\n#\n# Discord: discord.gg/kz4Y5fa9x9\n")
