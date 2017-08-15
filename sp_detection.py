from nltk.corpus import stopwords 
import csv
import numpy as np
from future import *
from decimal import *


#def cont_bag_of_word(h):
 #   if h[0]=='spam':
       # for t in range len(h[1]):
       #     print h[1][t]
      #  print h[1][1]
  #    
        #    
            #arrp[p][0].append(h[]
        
#def cont_bag_of_wordnspam(h)


csv_path="spam.csv"
#print arrp[0][0]
#print arrp[0][1]
msg=raw_input("Enter the message ")
print msg
#msg="Free trip to kerala"
lmsg=len(msg.split())
print lmsg
#arrp=[2*[ u] for u in (msg.split())]
arrp=[[u,0]  for u in (msg.split())]
arrnsp=[[u,0]  for u in (msg.split())]
#print (arrt[2][0])
#print arrt
cachedStopWords = stopwords.words("english")
sp=0
with open(csv_path,"rb") as cfobj:
    read=csv.reader(cfobj)
    nonspam=0
    for h in read:
        r=tuple(h[1])
        h[1]=[wor for wor in (h[1]).split() if wor not in cachedStopWords]
        if h[0]=='spam':
            sp+=1
            for g in range(lmsg):
                f=0
                for y in range(len(h[1])):
                    if arrp[g][0]==h[1][y]:
                        f+=1
                        arrp[g][1]=(arrp[g][1])+f
  #                      print h[1]
        else:
            nonspam+=1
            
            for g in range(lmsg):
                f=0
                for y in range(len(h[1])):
                    if arrnsp[g][0]==h[1][y]:
                        f+=1
                        arrnsp[g][1]=(arrnsp[g][1])+f
  #                      print h[1]
                     
        #print res
      #  cont_bag_of_word(h)
print "Array For spam"      
print arrp
print "Array For nonspam"
print arrnsp
print "Spam Count"
print sp
print "Non Spam Count"
print nonspam
#print
con=1
for k in range(len(arrp)):
    psp= Decimal(arrp[0][1])/Decimal(sp) #probality that the text is spam with the spam text p(x/c)
#psp= np.divide()
    prt=Decimal(sp)/Decimal(sp+nonspam)#probality that the text
    ptw=Decimal(arrnsp[0][1]+arrp[0][1])/Decimal(sp+nonspam)
    tpor=Decimal(psp*prt)/Decimal(ptw)
    con=con*tpor
    print tpor#(str.format('{0:.6f}',psp))
print con
    
