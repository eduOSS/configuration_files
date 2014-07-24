#cut the first two characters in the file BaseHTTPServer.py
fileHandle = open('BaseHTTPServer.py','r+') 
fileList = fileHandle.readlines() 
newList = [] 
for i in fileList: 
    newList.append(i[3:]) 
fileHandle.seek(0,0)
fileHandle.truncate()
fileHandle.writelines(newList) 
fileHandle.close()

