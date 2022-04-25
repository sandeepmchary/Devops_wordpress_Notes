sfile=input("Enter the source path: ")
dfile=input("Enter the destination path: ")
sfo=open(sfile)
content=sfo.read()
sfo.close()
#print(content)
dfo=open(dfile,'w')
dfo.write(content)
dfo.close()
#print(dfo.readlines())


