#import preprocessing

#The directories you want to see files from. Inverted index-ing them. If it is for the same system. Use only one of them. You can also make invert-index files for all the systems by specifing them the DIRn.
DIR1 = "A:/IR1/F5000/New Folder" 
# DIR2 = "A:/IR1/F5000/New Folder2"
# DIR3 = "A:/IR1/F5000/New Folder3"
# DIR4 = "A:/IR1/F5000/New Folder4"

def make_inverted(DIR):
    keywords=[]
    for i in range(1707):
        try:
            searchfile = open(DIR+"/freq-t"+str(i+1)+".txt", "r")
        
            for line in searchfile:
                line=line.split(":")
                if line[0] not in keywords:
                    keywords.append(line[0])
            searchfile.close()
        except Exception: pass
    
    ii=open(DIR+"/invertedindex.txt", "a")
    for word in keywords:
        print(word)
        line=word+ " : "
        for i in range(1707):
            try:
                searchfile = open(DIR+"/freq-t"+str(i+1)+".txt", "r")
                for line1 in searchfile:
                    if word in line1:
                        line=line+" file"+str(i+1)+","
                        break
                searchfile.close()
            except Exception: pass
        
        ii.write(line+"\n")
    ii.close()
    

make_inverted(DIR1)
#make_inverted(DIR2)
#make_inverted(DIR3)
#make_inverted(DIR4)
