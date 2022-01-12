from tkinter import*
from tkinter.messagebox import*
import random
import time
Jeu = True
def fichierLire():
    """ int --> list
    Max de T """
    try :
    
        with open ("option.txt", "r",encoding="utf-8") as f:
            caracteres = f.read()
            return caracteres
    except AssertionError :
        print("Erreur d'assertion dans fichier")
        return False
def fichierO(option):
    x = fichierLire()
    a = ""
    b=0
    T=[]
    T1=[]
    for i in x :
        if i == ":":
            T.append(a)
            a = ""
        elif i == "\n" :
            if a != "" and a != " ":
                T.append(a)
                T1.append(T)
                T=[]
                a = ""
        else : 
            a += str(i)
    for i in range(len(T1)):
        if str(T1[i][0]) == str(option):
            return T1[i][1]
def fichierLire2():
    """ int --> list
    Max de T """
    try :
    
        with open ("result.txt", "r",encoding="utf-8") as f:
            caracteres = f.read()
            #print (caracteres)
            return caracteres
    except AssertionError :
        print("Erreur d'assertion dans fichier")
        return False
def fichier(option):
    x = fichierLire2()
    a = ""
    b=0
    T=[]
    T1=[]
    for i in x :
        if i == ":":
            T.append(a)
            a = ""
        elif i == "\n" :
            if a != "" and a != " ":
                T.append(a)
                T1.append(T)
                T=[]
                a = ""
        else : 
            a += str(i)
    f = 0
    for i in range(len(T1)):
        if str(T1[i][0]) == str(option):
            return T1[i][1]
        else :
            f += 1
    if f == len(T1):
        return False
def fichierEcrireS(n):
  """ int --> list
  Max de T """
  try :
    with open ("option.txt", "w",encoding="utf-8") as f:
      f.write(str(n)+"\n")
  except AssertionError :
    print("Erreur d'assertion dans fichier")
    return False
def fichierEcrireS2(n):
  """ int --> list
  Max de T """
  try :
    with open ("result.txt", "w",encoding="utf-8") as f:
      f.write(str(n)+"\n")
  except AssertionError :
    print("Erreur d'assertion dans fichier")
    return False

def disparition():
  """ int --> list
  Max de T """
  try :
    a2 = ""
    a = fichierLire()
    T=[]
    for i in a:
      T.append(i)
    for i in T :
      if i != " ":
        a2= a2+i
    fichierEcrireS(str(a2))
  except AssertionError :
    print("Erreur d'assertion dans fichier")
    return False
disparition()
def fichierEcrire3(n):
  """ int --> list
  Max de T """
  try :
    with open ("result.txt", "a",encoding="utf-8") as f:
      f.write(str(n)+"\n")
  except AssertionError :
    print("Erreur d'assertion dans fichier")
    return False

def fichierEcrire(x,y):
  """ int --> list
  Max de T """
  try :
    with open ("result.txt", "a",encoding="utf-8") as f:
        if fichier(x)== False:
            f.write(str(x)+":"+str(y)+"\n")
            print("autre")
        else :
            if float(fichier(x))<y:
                print("+")
                enlever(str(x))
                f.write(str(x)+":"+str(y)+"\n")
                
                
  except AssertionError :
    print("Erreur d'assertion dans fichier")
    return False
def tableauToTxt(T):
  """ int --> list
  Max de T """
  try :
    for i in range(len(T)):
        
      if i == 0 :
        fichierEcrireS2(str(T[i][0])+":"+str(T[i][1]))
      else :
        fichierEcrire3(str(T[i][0])+":"+str(T[i][1]))
  except AssertionError :
    print("Erreur d'assertion dans fichier")
    return False

def enlever(option):
    x = fichierLire2()
    a = ""
    b=0
    T=[]
    T1=[]
    T2=[]
    for i in x :
        if i == ":":
            T.append(a)
            a = ""
        elif i == "\n" :
            if a != "" and a != " ":
                T.append(a)
                T1.append(T)
                T=[]
                a = ""
        else : 
            a += str(i)
    print(T,T1)
    #print(T1[i][0], option)
    for i in range(len(T1)):
        if str(T1[i][0]) != str(option):
            T2.append(T1[i][:])
            tableauToTxt(T2)
            
tailleJx = int(fichierO("tailleJx"))
tailleJy = int(fichierO("tailleJy"))
tailleO = int(fichierO("tailleJy"))
sPV = int(fichierO("sPV"))
M = int(fichierO("multiplicateur"))
tailleJoueur=tailleJy//10
tailleE=tailleJy//20
coords=[0,tailleJx-tailleJoueur]
score = 1
niveau = 0
scoreT = 0
t=0
t1=0
res = 0
temp = 100000
x = 0
y = random.randint(0,(tailleJy-tailleE)//10)
coords2=[y*10,x]
best = 0
fenetre = Tk()
fenetre.title('Ma première application tkinter')
canvas = Canvas(fenetre, width=tailleJy, height=tailleJx, bg="white")
rectangle = canvas.create_rectangle(0,0,tailleJoueur,tailleJoueur,fill="green")
canvas.coords(rectangle, coords[0], coords[1], coords[0]+tailleJoueur, coords[1]+tailleJoueur)
rectangle2 = canvas.create_rectangle(x,y,tailleE,tailleE,fill="red")
canvas.coords(rectangle2, coords2[0], coords2[1], coords2[0]+tailleE, coords2[1]+tailleE)
text = canvas.create_text((50, 25), text="score : "+str(scoreT)+"\nniveau : "+str(niveau)+"\nbest : "+str(best))
text2 = canvas.create_text((tailleJx//2, tailleJy//2-4), text="")
canvas.pack()

fenetre.bind("<Right>", lambda event: mouvement("R"))
fenetre.bind("<Left>", lambda event: mouvement("L"))
fenetre.bind("<d>", lambda event: mouvement("R"))
fenetre.bind("<q>", lambda event: mouvement("L"))



def getEntry():
    global temp,pseudo,best
    res = myEntry.get()
    pseudo = myEntry2.get()
    if int(res) <=1000 and int(res) > 0 and type(pseudo)==str:
        temp = (1000-int(res))/100
        btn.destroy()
        myEntry.destroy()
        myEntry2.destroy()
        canvas.itemconfig(text2, text="")
        best = float(fichier(pseudo))
        canvas.itemconfig(text, text="score : "+str(scoreT)+"\nniveau : "+str(niveau)+"\nbest : "+str(best))
        
    
myEntry = Entry(fenetre, width=10,justify='center')
myEntry.pack(pady=5)
myEntry2 = Entry(fenetre, width=20,justify='center')
myEntry2.pack(pady=5)
btn = Button(fenetre, height=1, width=10, text="Validé", command=getEntry)
btn.pack(pady=5)
canvas.itemconfig(text2, text="1 line : dificult (0/1000)"+"\n2 ligne : pseudo")

def update():
    global fenetre
    fenetre.update_idletasks()
    fenetre.update()

def dead():
    global Jeu,pseudo
    Jeu = False
    canvas.itemconfig(text2, text="dead")
    update()
    showwarning('Mort', 'score : '+str(scoreT)+"\net \nniveau : "+ str(niveau))
    fichierEcrire(pseudo,scoreT)

def mouvement(a):
    global coords, canvas, rectangle
    if a == "R":
        if (coords[0]+tailleJy//15)<=tailleJy-tailleJoueur:
            coords[0]+=tailleJy//15
    elif a == "L":
        if (coords[0]-tailleJy//15)>=0:
            coords[0]-=tailleJy//15
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+tailleJoueur, coords[1]+tailleJoueur)

def jeu():
    global Jeu, tailleJx,coords2,score,canvas,tailleJy,niveau,tailleE,scoreT,sPV,M,t,t1,best
    while Jeu:
        if t >= temp :
            t = 0
            if coords2[1]+tailleE>tailleJx-tailleJoueur:
                if coords[0]+tailleJoueur>=coords2[0]>=coords[0]:
                    dead()
                elif coords[0]+tailleJoueur>=coords2[0]+tailleE>=coords[0]:
                    dead()
            if coords2[1]+tailleE <= tailleJx-tailleE//2:
                coords2[1]+=tailleE//2
                canvas.coords(rectangle2, coords2[0], coords2[1], coords2[0]+tailleE, coords2[1]+tailleE)
            elif coords2[1]+tailleE//2 > tailleJx-tailleE:
                x = 0
                y = random.randint(0,(tailleJy-tailleE)//10)
                coords2=[y*10,x]
                
                if score >= sPV :
                    tailleE += tailleO//200
                    niveau += 1
                    M +=1
                    score = 0
                    update()
                score +=1
                scoreT+= 10+M-temp
                scoreT = round(scoreT,1)
                canvas.itemconfig(text, text="score : "+str(scoreT)+"\nniveau : "+str(niveau)+"\nbest : "+str(best))
                x = 0
                y = random.randint(0,(tailleJy-tailleE)//10)
                coords2=[y*10,x]
                
            else :
                Jeu = False
                print("false")
        update()
        time.sleep(0.01)
        t +=1
        t1 +=1
jeu()
        

