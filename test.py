import tkinter
import re
import nltk

file=open("data.text","r+")
STOPP=[]
text=str(file.read())
text= re.split("Art [0-9]+\n",text)

result={}
im=0
for items in text:


    result[im]=items[3:]
    im+=1

ia=0
b=[]





class word (object):

    name=""

    def __init__(self,name):

        self.name=name
        self.i=1

    def __repr__(self):

        return self.name + " kommt "+ str(self.i)+"mal vor"

    def addaword(self):

        self.i+=1




def showSTOPPword ():
    stemming=[]
    for keys in result:
        list=result[keys].split(" ")
        stemming.append(list)

    stem=[]
    for items in stemming:
        for ite in items:
            stem.append(ite.lower())
    classes=[]
    print (stem)
    for itemss in stem:
        notthere=True
        for item in classes:
            if item.name==itemss:
                notthere=False
                item.addaword()
        if notthere:

            classes.append(word(itemss))
    for il in range(1,10000):
        for it in classes:
            if it.i==il:
                print (it)
                if (it.i)>15:
                    STOPP.append(it.name)

showSTOPPword()
inp= input ("Geben Sie eine Suchanfrage an")
wordlist=[]
result1={}
integer=-1
for keyss in result:
    for word in result[keyss]:
        integer+=1
        if word not in STOPP:
            wordlist.append(word)
            result1[integer]= " ".join(wordlist)




