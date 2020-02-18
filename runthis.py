import mainsw
print("Enter input file name:")
filename=input()
file1 = open(filename,"r")
og=file1.read()
file1.close()
print("Choose mode compress/decompress (c/d)")
mode=input()
newtext=""

if mode=='c':
    newtext=mainsw.compress(og)
    file2 = open("compresstext.txt","w")
    file2.write(newtext)
    file2.close()
elif mode=='d':
    newtext=mainsw.decompress(og)
    file2 = open("decompresstext.txt","w")
    file2.write(newtext)
    file2.close()
else:
    print ("Choose c or d")
