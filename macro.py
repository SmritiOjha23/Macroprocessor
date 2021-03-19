#  SMRITI OJHA
#  1913130
handle=open('input.txt',"r")
lines=(handle.read()).split("\n")
mdt=open('mdt.txt',"w")
mnt=open('mnt.txt',"w")
pass1=open('pass1.txt',"w")
mdtc=0
mntc=0
i=0
while i<len(lines):
    if lines[i].startswith('MACRO'):
        while lines[i].startswith('MEND')==False:
            if lines[i].startswith('MACRO'):
                mnt.write(lines[i+1]+" "+str(mdtc)+"\n")
                mntc=mntc+1
            else:
                mdtc=mdtc+1
                mdt.write(lines[i]+"\n")
            i=i+1
        mdt.write(lines[i]+"\n")
        mdtc=mdtc+1
        i=i+1
    else:
        pass1.write(lines[i]+"\n")
        i=i+1
mdt.close()
mdt=open('MDT.txt',"r")
mdtlist=list()
for line in mdt:
    line=line.strip()
    mdtlist.append(line)
mdt.close()
mnt.close()
pass1.close()
mdt=open('mdt.txt',"w")
mdt.truncate(0)
j=0
while j<len(mdtlist):
    if mdtlist[j].startswith('MEND')==False:
        linea=(mdtlist[j]).split(" ")
        ala=(linea[1]).split(",")
        mdt.write(mdtlist[j]+"\n")
        j=j+1
        while mdtlist[j].startswith('MEND')==False:
            lineaa=mdtlist[j].split(" ")
            lineb=lineaa[1].split(",")
            for ele in lineb:
                if ele in ala:
                    lineb[lineb.index(ele)]='#'+str(ala.index(ele))
            mdt.write(lineaa[0]+" "+lineb[0]+","+lineb[1]+"\n")
            j=j+1
    mdt.write("MEND\n")
    j=j+1
mdt.close()
pass1=open('pass1.txt',"r")
pass2=open('pass2.txt',"w")
mnt=open('MNT.txt',"r")
mdt=open('MDT.txt',"r")
mntlist=(mnt.read()).split("\n")
mdtlist=(mdt.read()).split("\n")
pass1list=(pass1.read()).split("\n")
i=0
while i<len(pass1list):
    flag=0
    j=0
    while j<len(mntlist)-1:
        if ((pass1list[i]).split(" "))[0]==((mntlist[j]).split(" "))[0]:
            pos=((mntlist[j]).split(" "))[2]
            index=int(pos)
            index=index+1
            linea=(pass1list[i]).split(" ")
            ala=(linea[1]).split(",")
            while mdtlist[index]!="MEND":
                lineb=(mdtlist[index]).split(" ")
                alb=(lineb[1]).split(",")
                pass2.write(lineb[0]+" ")
                k=0
                while k<len(alb):
                    if alb[k].startswith("#"):
                        pass2.write(ala[int((alb[k])[1:])])
                    else:
                        pass2.write(alb[k])
                        pass2.write(",")
                    k=k+1
                pass2.write("\n")
                index=index+1
            flag=1
            break
        j=j+1
    if flag==0:
        pass2.write(pass1list[i]+"\n")
    i=i+1
pass2.close()
mnt.close()
mdt.close()
pass1.close()
