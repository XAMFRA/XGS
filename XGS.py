"""
                                                     ╔════════╗
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

class XGS:
	def __init__(MAINXAR,INP,INPB):
		MAINXAR.GOINPS = INP
		MAINXAR.GOINPB = INPB
		MAINXAR.GOSURL = 'https://www.google.com/search?q='+MAINXAR.GOINPS+'&client=firefox-b-d&start='+MAINXAR.GOINPB
		MAINXAR.GORESP = ''

	def GWSR(XAR):
		CRESP = re.findall('<a.href="/url\?q=(.*?)\&amp', str(XAR.GORESP))
		os.system("cls") if os.name == "nt" else os.system("clear")
		print("""
   ╔═══════════════╗
   ║ GOOGLE RESULT ║
   ╚═══════════════╝
""")
		for SRN in CRESP:
			if "https://support.google.com" in SRN or "https://accounts.google.com/" in SRN:
				pass
			else:
				print("══════════════════════════\n"+SRN)

	def REQW(XAR):
		REQURL = urllib.request.Request(XAR.GOSURL)
		REQURL.add_header('User-Agent', 'Mozilla/7000.0 XAR')
		REQURL.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
		REQURL.add_header('Accept-Language', 'en-US,en;q=0.8')
		REQTGO = urllib.request.urlopen(REQURL, timeout=10)
		XAR.GORESP = REQTGO.read()
		REQTGO.close()

	def XGSM(XAR):
		print(XAR.GOINPS)
		print(XAR.GOINPB)
		print(XAR.GOSURL)


def main():
	while True:
		XGSUSERR = input("\n|SEARCH|  : ")
		XGSUSERW = XGSUSERR.replace(" ", "%20")
		XGSUSERP = input("|PAGE NUM|: ")
		XGSCLASS = XGS(XGSUSERW,XGSUSERP)
		#XGSCLASS.XGSM()
		XGSCLASS.REQW()
		XGSCLASS.GWSR()


if __name__ == '__main__':
	main()