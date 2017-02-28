#coding: utf-8
import re

def cookiesniffing(html):
	result = 0

	if ( bool(re.search('document\.cookie',html, re.IGNORECASE|re.DOTALL)) == True ):  # 자바스크립트에서는 document.cookie 객체를 통해 쿠키에 접근 가능
		if ( bool(re.search('new\s?XMLHttpRequest',html, re.IGNORECASE|re.DOTALL)) == True ):  # 데이터 전송을 위해 사용되는 메서드와 프로퍼티를 가진 객체
			if (html.find('post') or html.find('get')) != -1:
				result = 1
	return result

def cors(html):
	result = 0
	scriptRegExp = re.compile('<script.*?>.*?</script>', re.DOTALL)
	# <script ~~> ~~ </script> 검색
	scriptList = scriptRegExp.findall(html)
	for script in scriptList:
		# withCredentials 검색
		if(bool(re.search('withCredentials', script)) == True):
			result = 1
	return result

def crossdocumentmessaging(html):
	result = 0
	scriptRegExp = re.compile('<script.*?>.*?</script>', re.DOTALL)
	scriptList = scriptRegExp.findall(html)
	for script in scriptList:
		if (bool(re.search('\.postMessage', script, re.IGNORECASE)) == True ):
			if (bool(re.search('\.origin', script, re.IGNORECASE)) == False):
				result = 1
	return result

def csrf(html):
	result = 0
	iframeRegExp = re.compile('<iframe.*?>.*?</iframe>', re.DOTALL)
	imgRegExp = re.compile('<img src.*?>')
	formRegExp = re.compile('<form.*?>.*?</form>', re.DOTALL)
	# [1] CSRF Attack iframe Tag
	# <iframe ~~> ~~ </iframe> 검색
	iframeList = iframeRegExp.findall(html)
	for iframe in iframeList:
		if(bool(re.search('.*\.php|.*\.asp|.*\.html', iframe)) == True):
			# print 'No safety Zone, iframe Tag Threat!!'
			result = 1
		if(bool(re.search('visibility:\s?hidden', iframe)) == True):
			# print "Display-None >> Threat!!"
			result = 1
	# [2] CSRF Attack Img links
	imgList = imgRegExp.findall(html)
	for img in imgList:
		if (bool(re.search('.*\.gif|.*\.jpg|.*\.bmp', img)) == True):
			# print 'No safety Zone, IMG Tag Threat!!'
			result = 1
	# [3] if you found form, check => {% csrf_token %}
	formList = formRegExp.findall(html)
	for form in formList:
		if ((bool(re.search('post', form, re.IGNORECASE)) == True) and (bool(re.search('csrf\.token|token', form)) == True)):
			# print 'No safety Zone, Form Tag Threat!!'
			result = 1
	return result

def fileapi(html):
	result = 0
	# Warning! opacity = 0
	if(bool(re.search('opacity:0',html)) == True):
		result = 1
	# Warning! Using FileAPI
	if (bool(re.search('FileReader', html)) == True):
		result = 1

	return result

def filedownload(html):
	ahrefRegExp = re.compile('<a href\s?=".*?"><.*?>', re.DOTALL)
	result = 0
	ahrefList = ahrefRegExp.findall(html)
	for ahref in ahrefList:
		if(bool(re.search('(file)(path|down|download)?\s*=', ahref, re.IGNORECASE)) == True):
			result = 1
		if (bool(re.search('(path|download)\s*=', ahref, re.IGNORECASE)) == True):
			result = 1
	return result

def geolocationapi(html):
	result = 0
	if (bool(re.search('(getCurrentPosition\(.*?\))|(watchPosition\(.*?\))|(coords)|(maximumAge\s:\s0)', html, re.IGNORECASE|re.DOTALL)) == True):
		result = 1
	return result



def localdb(html):
	result = 0
	scriptRegExp = re.compile('<script.*?>.*?</script>', re.DOTALL)
	# <script ~~> ~~ </script> 검색
	scriptList = scriptRegExp.findall(html)
	for script in scriptList:
		if ( re.search('openDatabase', script, re.IGNORECASE) and re.search('executeSql', script, re.IGNORECASE) ):
			result = 1
	return result

def newtagabusing(html):
	result = 0
	tagList = ['audio', 'video', 'source', 'canvas', 'embed']
	for i in range(len(tagList)):
		if(bool(re.search('<' + tagList[i] + '.*?>.*?</' + tagList[i] + '>', html, re.IGNORECASE|re.DOTALL)) == True):
			result = 1
	return result

def protocolScheme(html):
	result = 0
	scriptRegExp = re.compile('<script.*?>.*?</script>', re.DOTALL)
	scriptList = scriptRegExp.findall(html)
	for script in scriptList:
		if (bool(re.search('\.registerProtocolHandler\(.*?\)', script, re.IGNORECASE)) == True):
			result = 1
	return result

def scriptddos(html):
	result = 0
	whileRegExp = re.compile('while\(.*?\)\s?\{.*\}', re.DOTALL)
	whileList = whileRegExp.findall(html)
	for while_ in whileList:
		# XMLHttpSendCheck
		if (bool(re.search('\.send\(.*?\)', while_, re.IGNORECASE)) == True):
			result = 1
		# XMLHttpOpen Check
		if (bool(re.search('\.open\(.*?\)', while_, re.IGNORECASE)) == True):
			result = 1
		# XMLHttpRequest Check
		if (bool(re.search('new\s?xdomainrequest\(.*?\)|new\s?xmlhttprequest\(.*?\)', while_, re.IGNORECASE)) == True):
			result = 1
		# Image src check
		if (bool(re.search('\.src\(.*?\)', while_, re.IGNORECASE)) == True):
			result = 1
	return result

def websocket(html):
	result = 0
	if (bool(re.search('\.onopen|\.onmessage', html, re.IGNORECASE|re.DOTALL)) == True):
		result = 1
	return result

def webstorage(html):
	result = 0
	APIList = ['length', 'key', 'getitem', 'setitem', 'removeitem', 'clear']

	for i in range(len(APIList)):
		if (bool(re.search('storage\.'+ APIList[i], html, re.IGNORECASE|re.DOTALL)) == True):
			result = 1
	return result

def webworker(html):
	result = 0
	if (bool(re.search('new\s?Worker\(.*?\)', html, re.IGNORECASE|re.DOTALL)) == True):
		result = 1
	return result

def scan(html):
	functions = [cookiesniffing, cors, crossdocumentmessaging, csrf, fileapi, filedownload, geolocationapi, localdb,
				 newtagabusing, protocolScheme, scriptddos, websocket, webstorage, webworker]
	result = []
	for function in functions:
		result.append(function(html))
	return result


