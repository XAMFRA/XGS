# XGS
Python Code To Search On Google And Use It To Search By Dorks In Same Time
<img src = 'https://github.com/XZRFMA/XDGe/blob/XAR/images/text.png' width=500 alt = 'Awesome Tool LOL' align='left'/>
 

<img src = 'https://github.com/XZRFMA/XDGe/blob/XAR/images/logo.png' width=255 alt = 'Awesome Tool LOL' align='right'/><br>


-
-
-



## What Does The Tool Support?
- [X] http proxy
- [X] http authentication
- [X] User-Agent List
- [X] Multi Process in Same Time
- [X] Using Google Dork To Get More Data


## Programming Languages
<img src = 'https://github.com/MarikIshtar007/MarikIshtar007/blob/master/images/python2.png' height='30'/>

### IF You Want GoogleDork Function?
```python
def GOscan(URLTARGET,DORKUSERFILE):
	DOKERLIST = []
	GODOKERFILE = open(DORKUSERFILE,"r")
	for CONGODOKER in GODOKERFILE:
		DOKERLIST.append(CONGODOKER)
	for CONDOKERLIST in range(len(DOKERLIST)):
			DORKTARGET = DOKERLIST[CONDOKERLIST].replace(" ","+").replace("\n","")
			SETGODORK  = "site:{URLTARGET}+{DORKTARGET}".format(URLTARGET=URLTARGET, DORKTARGET=DORKTARGET)
			SETGOWEBS  = 'https://www.google.com/search?q='+SETGODORK+'&client=firefox-b-d&start=0'
			REQGODORK  = urllib.request.Request(SETGOWEBS)
			REQGODORK.add_header('User-Agent', 'Mozilla/7000.0 XAR')
			REQGODORK.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
			REQGODORK.add_header('Accept-Language', 'en-US,en;q=0.8')
			#---------------------------------------------
			REQGOOGLE  = urllib.request.urlopen(REQGODORK, timeout=10)
			RESGODORK  = REQGOOGLE.read()
			REQGOOGLE.close()
			CLEARREQD  = re.findall('<a.href="/url\?q=(.*?)\&amp', str(RESGODORK))
			for DO in CLEARREQD:
				if "https://support.google.com" in DO or "https://accounts.google.com/" in DO:
					pass
				else:
					print(DO)
			time.sleep(1)
```
 

<img src="images/XDGLOGO.png" width=47% align='right'>
<img src="images/XDG-TEM.png" width=47% align='left'>

![XAR's github stats](https://github-readme-stats.vercel.app/api?username=XZRFMA&show_icons=true&hide=[%22issues%22])

 
 
