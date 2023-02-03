import pygame
import random
from pygame.locals import *

#DEFINISCO TUTTE LE FUNZIONI CHE MI SERVIRANNO DURANTE IL GIOCO
def initMatrix0 (r , c, valore = 0):    #funzione che mi crea una matrice secondo i valori che inserisco
    m=[ [valore]*c  for i in range(r) ]
    return m # mi restistuisce una matrice r x c con elemento i,j= valore
def gameover():
    #GAME OVER
    superf_gameover= pygame.image.load("game_over.png").convert() # carico l'immagine del gameover dalla cartella in cui contengo anche il file .py
    screen.blit(superf_gameover,(160,392)) #unisco l'immagine alla superfice
    #FARO LO STESSO PROCEDIMENTO PER TUTTE LE ALTRE IMMAGINI
    pygame.display.flip()
def posiziona_quadrato(x0,y0):
    surf = pygame.image.load('quadrato.png').convert()   # immagine dei quadrati coperti
    screen.blit(surf, (x0, y0)) 
    pygame.display.flip()  
def posiziona_0(x0,y0):
    superf_vuoto = pygame.image.load('quadrato_vuoto.png').convert()  # immagine del quadratino vuoto, nel quale è presente uno 0 
    screen.blit(superf_vuoto, (x0, y0)) 
    pygame.display.flip()
def posiziona_bombe(x0,y0):
    superf_bomb = pygame.image.load('bomba.jpeg').convert()   # immagine di una bomba , è presente quindi un -1
    screen.blit(superf_bomb, (x0, y0))
    pygame.display.flip()
def posiziona_1(x0,y0):
    superf_n1 = pygame.image.load('n1.png').convert()  #immagine del numero della casella  
    screen.blit(superf_n1, (x0, y0)) 
    pygame.display.flip()  
def posiziona_2(x0,y0):
    superf_n2 = pygame.image.load('n2.png').convert()   #immagine del numero della casella  
    screen.blit(superf_n2, (x0, y0))      
    pygame.display.flip()   
def posiziona_3(x0,y0):
    superf_n3 = pygame.image.load('n3.png').convert()   #immagine del numero della casella  
    screen.blit(superf_n3, (x0, y0))      
    pygame.display.flip()
def posiziona_4(x0,y0):
    superf_n4 = pygame.image.load('n4.png').convert()   #immagine del numero della casella  
    screen.blit(superf_n4, (x0, y0))      
    pygame.display.flip()
def posiziona_5(x0,y0):
    superf_n5 = pygame.image.load('n5.png').convert()   #immagine del numero della casella  
    screen.blit(superf_n5, (x0, y0))      
    pygame.display.flip()    
def posiziona_6(x0,y0):
    superf_n6 = pygame.image.load('n6.png').convert()   #immagine del numero della casella  
    screen.blit(superf_n6, (x0, y0)) 
    pygame.display.flip()
def posiziona_bandierina(x0,y0):
    superf_bandierina= pygame.image.load('bandiera.png').convert() # immagine della bandierina   
    screen.blit(superf_bandierina, (x0,y0))   
    pygame.display.flip()
def smile():
    superf_smile = pygame.image.load('smile.png').convert()  #carico l'immagine dello smile nella barra in alto al centro
    screen.blit(superf_smile, (339,16))
    pygame.display.flip()
def smile_triste():
    #QUADRATO SMILE TRISTE
    superf_smile_triste = pygame.image.load('smile_triste.png').convert() #carico sulla superfice l'immagine di uno smile triste
    screen.blit(superf_smile_triste, (339,16)) 
    pygame.display.flip()    
def conta_bandierine_iniziale(num):
    fnt= pygame.font.SysFont("Special_Agent",48)# font delle scritte 
    surf_sx= pygame.Surface((55,30))
    screen.blit(surf_sx,(28,18)) # sfondo del contatore di bandierine
    surf_font=  fnt.render(f"{num}",True,(255,0,0)) # Scrivo nel riquadro in alto a sx il numero di mine presenti
    screen.blit(surf_font,(40,22)) # CONTATORE DI BANDIERINE, indica il numero di bandierine presenti sul campo
    pygame.display.flip() 
def conta_bandierine(x):
    fnt= pygame.font.SysFont("Special_Agent",48)# font delle scritte 
    surf_sx= pygame.Surface((55,40))
    surf_font=  fnt.render(f"{x}",True,(255,0,0)) # Scrivo nel riquadro in alto a sx il numero ottenuto da numMine-bandierine posizionate, se ne togliamo una esso giustamente aumenta di 1
    screen.blit(surf_sx,(28,18)) 
    screen.blit(surf_font,(40,22))
    pygame.display.flip()
def timer():
    fnt= pygame.font.SysFont("Special_Agent",43) # font delle scritte 
    surf_timer= pygame.Surface((55,40))
    screen.blit(surf_timer,(637,18)) # sfondo del timer
    surf_font=  fnt.render("000",True,(255,0,0)) # Timer inizializzato a 0 ed aumenta ogni secondo
    screen.blit(surf_font,(638,22))
    pygame.display.flip()
def quadrato_difficolta(difficolta):
    '''Ho preso tutte le variabili che servono per il gioco affinché esse cambiano al cambio di difficoltà.
    Faccio variare la difficoltà cliccando sul riquadro in alto a sx
        STAR =               FACILE                   matrice(7x7) con 5 mine
        COSTRUTTORE = MEDIO                   matrice(12x12) con 13 mine
        SUPERMAN =       DIFFICILE              matrice(15x15) con 28 mine
        ALIEN =              MOLTO DIFFICILE    matrice(18x18) con 55 mine '''
    global righe 
    global numMine
    global colonne
    global coordinate
    
    if difficolta==1:
        star= pygame.image.load('star.png').convert()
        screen.blit(star, (83, 17)) 
        pygame.display.flip()
        #DIFFICOLTA FACILE
        righe=7
        colonne=7
        numMine=5 
        coordinate={}                 
        pygame.display.flip()        
    if difficolta==2:
        costruttore= pygame.image.load('costruttore.png').convert()
        screen.blit(costruttore, (83, 17))
        pygame.display.flip()
        #DIFFICOLTA MEDIA
        righe=12
        colonne=12
        numMine= 13
        coordinate={}                 
        pygame.display.flip()    
    if difficolta==3:  
        superman= pygame.image.load('superman.png').convert()
        screen.blit(superman, (83, 17))    
        pygame.display.flip()
        #DIFFICOLTA DIFFICILE
        righe=15
        colonne=15
        numMine=28  
        coordinate={}                 
        pygame.display.flip()        
    if difficolta==4:    
        alien= pygame.image.load('alien.png').convert()
        screen.blit(alien, (83, 17)) 
        pygame.display.flip()
        #DIFFICOLTA MOLTO DIFFICILE
        righe=18
        colonne=18
        numMine=55
        coordinate={}                 
        pygame.display.flip()    
def quadrato_emoji(x): 
    '''funzione che serve per estetica infatti essa cambia l'emoji vicino al timer per indicare un'espressione simpatic, prendo x come paramentro che mi indica i decimi di tempo trascorso'''
    if x <2: # cambia a 30 secondi ecc
        emoji1=pygame.image.load("curioso.png").convert()
        screen.blit(emoji1,(595,17))
    elif x>2 and x<6:
        emoji2=pygame.image.load("curioso2.png") .convert()
        screen.blit(emoji2,(595,17))
    elif x>6 and x<9:
        emoji3=pygame.image.load("timer4.png").convert()
        screen.blit(emoji3,(595,17))
    elif x>9:
        emoji4=pygame.image.load("timer3.png").convert()
        screen.blit(emoji4,(595,17))    
def vittoria(celle):
    ''' Questa è la funzione che mi dice se ho vinto o meno, essa viene invocata ogni volta che scopro una nuova casella.
    Controlla per ogni quadrato posizionato, nella matrice di gioco, se esso è scoperto allora il contatore aumenta. Se il valore delle casella è un numero positivo o 0 ed essa è scoperta aumenta il contentatore. Se il numero di celle scoperte è uguale al numero di celle meno quello delle mine, abbiamo vinto'''
    global coordinate
    celle_scoperte=0
    victory=False
    for k,v in coordinate.items():
        (i,j)=k
        if v["scoperta"]== True and celle[i][j] in [1,2,3,4,5,6,0]:
            celle_scoperte+=1
    
    if celle_scoperte==((righe*colonne)-numMine):
        victory=True
    return victory    
def posizionaMine(celle, x):
    '''Funzione che serve a posizionare all'interno della matrice di gioco il numero di mine prestabilito in maniera casuale'''
    while x>0 :
        i= random.randint(0,len(celle)-1)
        j= random.randint(0,len(celle[0])-1)
        if celle[i][j] !=-1:
            celle[i][j]=-1
            x -=1
def vicini(m , xy):
    '''Funzione di supporto che serve per restituirmi gli indici degli elementi vicini ad xy che sarebbe una tuple'''
    ris=[]
    x= xy[0]
    y= xy[1]
    for i in range (x-1,x+2):
        for j in range(y-1,y+2):
            if 0<=i<len(m) and 0<=j<len(m[0])  and (i != x or j!=y):
                ris.append((i,j))                  
    return ris
def vicini_0(m , xy):
    '''Funzione simile a vicini ma in questo caso questa mi controlla se l'elemento con indice x,y ha dei vicini che hanno valore 0, se è così mi inserisce i loro indici in una lista e me la restituisce'''
    ris=[]
    x= xy[0]
    y= xy[1]
    for i in range (x-1,x+2):
        for j in range(y-1,y+2):
            if 0<=i<len(m) and 0<=j<len(m[0])  and (i != x or j!=y) and m[i][j]==0:
                ris.append((i,j))                  
    return ris
def vicini_m(m , xy):
    ris=[]
    x= xy[0]
    y= xy[1]
    for i in range (x-1,x+2):
        for j in range(y-1,y+2):
            if 0<=i<len(m) and 0<=j<len(m[0])  and (i != x or j!=y) and m[i][j]>0:
                ris.append((i,j))                  
    return ris
def numBandierina(coordinate):
    '''Funzione che mi restituisce il numero di bandierine che ho inserito nella matrice di gioco'''
    ris=0
    for k,v in coordinate.items(): # controllo per ogni quadratino della matrice se su di esso è presente una bandierina, se lo è aumento il contatore
            if v["bandierina"]== True:
                ris+=1
    return ris
def rettangoli(righe,colonne):
    ''' costruisco una matrice di rettangoli'''
    rl=40 
    rh= 40
    global coordinate  # prendo dall'esterno un dizionario nel quale salverò le coordinate, se il quadrato è scoperto e se è presente una bandierina su di esso
    # disegno i rettangoli nella finestra
    for i in range(colonne):
        for j in range(righe):
            surf = pygame.image.load('quadrato.png').convert()   # immagine dei rettangoli 
            screen.blit(surf,(0+ i*rl, 72+rh*j)) 
            pygame.display.flip()  
            #salvo le coordinate del rettangolo 
            x1= 0 +i*40
            x2= 0 +i*40 +40
            y1=72 +j*40
            y2= 72+j*40 +40
            coordinate[(i,j)] = {"x1": x1, "x2":x2 , "y1": y1, "y2":y2, "scoperta": False, "bandierina": False}    
def inizializza(righe,colonne,numMine):
    '''Questa è la funzione che mi va a cambiare il valore di tutti gli elementi in base a quante mine hanno vicino. Per ogni mina vicina, il valore dell'elemento i,j aumenta di 1'''
    celle_iniziale= initMatrix0(righe,colonne) # crea una matrice di 0
    posizionaMine(celle_iniziale, numMine) # posiziona le mine  e poi mi controllerà ogni elemento 
    for i in range(righe):
        for j in range (0, colonne):
            if celle_iniziale[i][j] != -1:
                t= (i,j)
                celleVicine= vicini(celle_iniziale,t)
                num=0
                for a,b in celleVicine:
                    if celle_iniziale[a][b]== -1:
                        num +=1
                celle_iniziale[i][j]= num
    return celle_iniziale
def scopri_zeri(i,j,celle):
    '''La funzione in questione mi consente di scoprire tutti gli zeri e le caselle con numero maggiori di zero vicini. Se è stato clicclato un quadrato in cui è presente uno 0, questa funziona controllerà tutti i vicini di quell'elemento e se sono zeri li scoprirà e faà la stessa cosa per i vicini del'elemento. Funzione ricorsiva'''
    global coordinate
    indici = (i,j)
    celle_vicine0= vicini_0(celle,indici)
    for a,b in celle_vicine0 :
        ab= (a,b)
        ris=vicini_0(celle,ab)        
        for (r,c) in ris:
            if (r,c) not in celle_vicine0:
                celle_vicine0.append((r,c))
    for (x,y) in celle_vicine0:
        xy=(x,y)
        vic= vicini_m(celle,xy)
        for (l,p) in vic:    #per ogni vicino >0 cerca le coordinate nel dizionario e stamperà l'immagine adatta.
            for q,w in coordinate.items():
                (i,j)=q
                if (i,j) == (l,p) :
                    x0= w["x1"]
                    y0= w["y1"]
                    w["scoperta"]=True
                    w["bandierina"]=False
                    if celle[i][j]==1:
                        posiziona_1(x0,y0) 
                    elif celle[i][j]==6:
                        posiziona_6(x0,y0) 
                    elif celle[i][j]==5:
                        posiziona_5(x0,y0) 
                    elif celle[i][j]==4:
                        posiziona_4(x0,y0)
                    elif celle[i][j]==3:
                        posiziona_3(x0,y0)     
                    elif celle[i][j]==2:
                        posiziona_2(x0,y0) 
            
    #trova gli indici nel dizionario e ottenendo le coordinate stamperò gli 0 nelle posizioni giuste
    for (a,b) in celle_vicine0:
        for k,v in coordinate.items():
            (i,j)=k
            if (i,j) == (a,b) :
                x0= v["x1"]
                y0= v["y1"]
                v["scoperta"]=True
                v["bandierina"]=False
                posiziona_0(x0,y0)     
def scopri_campo(celle):
    '''Mi scoprirà tutto il campo, essa viene eseguita in caso di vittoria o di game over'''
    global coordinate #PRENDO LE COORDINATE DAL DIZIONARIO    
    for k,v in coordinate.items(): # controllo tutto il dizionario e stampo tutti i quadrati presenti in base al loro contenuto
                        x0 =int( v["x1"])
                        y0=int(v["y1"])
                        (i,j)=k
                        if celle[i][j] == 0:
                            posiziona_0(x0,y0)
                        elif celle[i][j] ==-1:   
                            posiziona_bombe(x0,y0)                        
                        elif celle[i][j]== 1:
                            posiziona_1(x0,y0)                            
                        elif celle[i][j]== 2:
                            posiziona_2(x0,y0)
                        elif celle[i][j]== 3:
                            posiziona_3(x0,y0)
                        elif celle[i][j]== 4:
                            posiziona_4(x0,y0)
                        elif celle[i][j]== 5:
                            posiziona_5(x0,y0)                            
                        elif celle[i][j] == 6:
                            posiziona_6(x0,y0)
    pygame.display.flip() 
 
#DOPO AVER DEFINITO LE FUNZIONI UTILI ALLO SVOLGIMENTO DEL GIOCO
#DEFINISCO LO SCHERMO E ALTRO PRIMA DI FAR PARTIRE IL GIOCO

#CHIAMO LA FUNZIONE CLOCK, utile per il timer
clk = pygame.time.Clock()

pygame.init()
'''Variabili della matrice di gioco'''
righe=0 
colonne=0
numMine=0
difficolta=1 
coordinate={}

#SCHERMO
size=(720,792) # dimensioni finestra di gioco
screen= pygame.display.set_mode(size) # creo una finestra dalle dimensioni gia stabilite 
pygame.display.set_caption("CAMPO MINATO by Mattia Corigliano") #titolo della finestra
def schermo(volta,x,r,c):
    ''' Funzione che serve a ricreare, ogni volta che cambia la modalità, la matrice di gioco e le varie interfacce interattive.'''
    screen.fill((144,144,144)) #sfondo grigio
    parte_alta=pygame.image.load("up.png").convert()
    screen.blit(parte_alta,(0,0))
    smile()
    quadrato_emoji(0)
    quadrato_difficolta(volta)
    timer()
    conta_bandierine_iniziale(x)
    rettangoli(r,c)
    pygame.display.flip()
schermo(difficolta,numMine,righe,colonne)

def main():  # definisco una funzione all'interno del quale vado a scrivere le funzioni del gioco
    #INZIA IL GIOCO
    global difficolta # mi vado a prendere la variabile che mi indica la difficoltà
    global righe 
    global numMine
    global colonne
    global coordinate
    schermo(difficolta,numMine,righe,colonne)    
    
    #CONTATORI UTILI :
    bandierine=0 # inizializzo una variabile che mi indica il numero di bandierine che abbiamo inserito nella matrice
    tick=0 #numero di tick che aumenta una volta ogni 1/120 secondi
    #CONTATORI DEL TIMER:
    c=0 # contatore delle centinaia
    d=0 #contatore delle decine
    u=0 #contatore delle unità
    a=0 # contatore delle decine del timer che mi serve per la funzione dell'emoji
    
    celle= inizializza(righe,colonne,numMine) # MATRICE CON I NUMERI DI GIOCO [ 0: quadrato vuoto ,  1: 1 mina vicina, 2: 2 mine vicine ecc.., -1: bomba]
    
    # CONDIZIONE DEI WHILE
    done = False # booleano che mi inizializza il primo while che contiene il gioco
    done1= False # booleano che mi inizializza il secondo while, dopo aver perso o vinto con delle scelte all'interno
    
    #BOOLEANO DELLA VITTORIA
    victory=False

    #PARTE IL GIOCO
    while not done:
        eventlists= pygame.event.get() #PRENDO IN UNA LISTA TUTTI GLI EVENTI CHE ACCADONO NELLA FINESTRA DI GIOCO
        contatore_bandierine=numMine-bandierine
        for ev in eventlists:  # INIZIO A CONTROLLARE OGNI EVENTO NELLA LISTA DI EVENTI               
            if ev.type == MOUSEBUTTONDOWN: # controllo se è stato cliccato un tasto del mouse 
                #prendo le posizioni del puntatore del mouse 
                x= ev.pos[0]
                y=ev.pos[1]
                if ev.button == 1 : # Se il tasto cliccato del mouse è il sx, voglio quindi scoprire la casella su cui ho cliccato oppure sto interaggendo con le 2 emoji 
                    if x in range (339,381) and y in range (18,60):# se è in questo range di coordinate significa che l'utente sta cliccando sullo smile e voglio che ricrei la matrice di gioco                          
                            main() # faccio ripartire il gioco
                            done = True
                    elif x in range(83,125) and y in range(17,59): # se le coordinate sono in questo range allora il giocatore vuole cambiare modalità, controllo in quale modalità è adesso e la cambierò
                        if difficolta<=3:
                            difficolta+=1
                        else:   
                            difficolta=1
                        quadrato_difficolta(difficolta) # cambio la difficoltà
                        main()
                    for k,v in coordinate.items(): #ANALIZZO IL DIZIONARIO, cioè trovo le coordinate del quadrato su cui ho cliccato
                        x0 =v["x1"] # valore x nell'angolo in alto a sx del quadrato
                        x1 =v["x2"]  # valore x nell'angolo in alto a dx del quadrato
                        y0=v["y1"] # valore y nell'angolo in alto a sx del quadrato
                        y1=v["y2"] # valore x nell'angolo in basso a dx del quadrato
                        if x in range (x0,x1) and y in range(y0,y1):  # controllo se le coordinate sono nella chiave del dizionario 
                            (i,j)=k   # definisco gli indici che sono la chiave del dizionario
                            if celle[i][j]== 0:  #HO TROVATO UNA CELLA VUOTA
                                posiziona_0(x0,y0) #posiziono il quadrato vuoto                                
                                scopri_zeri(i,j,celle) #scopro tutti gli zeri adiacenti  e i numeri adiacenti                              
                                pygame.display.flip()
                                v["scoperta"]=True # aggiungo nel dizionario il fatto che il quadrato è stato scoperto
                                victory= vittoria(celle) #controllo se ho vinto
                            if celle[i][j] ==-1:   #HAI BECCATO UNA BOMBA
                                posiziona_bombe(x0,y0) #posiziono l'immagine della bomba 
                                # finisce il gioco e hai perso 
                                done = True
                                scopri_campo(celle) #scopro tutto il campo
                                gameover() #mi appare l'immagine del game over
                                smile_triste() # immagine della faccina triste
                            elif celle[i][j]== 1: # HAI BECCATO UN QUADRATO CON 1 BOMBA ADIACENTE
                                posiziona_1(x0,y0)
                                v["scoperta"]=True
                                v["bandierina"]=False
                                victory= vittoria(celle)                                
                            elif celle[i][j]== 2: # HAI BECCATO UN QUADRATO CON 2 BOMBA ADIACENTE
                                posiziona_2(x0,y0)
                                v["scoperta"]=True
                                v["bandierina"]=False
                                victory= vittoria(celle)                                
                            elif celle[i][j]== 3: # HAI BECCATO UN QUADRATO CON 3 BOMBA ADIACENTE
                                posiziona_3(x0,y0)
                                v["scoperta"]=True
                                v["bandierina"]=False
                                victory= vittoria(celle)                                
                            elif celle[i][j]== 4: # HAI BECCATO UN QUADRATO CON 4 BOMBA ADIACENTE
                                posiziona_4(x0,y0)
                                v["scoperta"]=True
                                v["bandierina"]=False
                                victory= vittoria(celle)                                
                            elif celle[i][j]== 5: # HAI BECCATO UN QUADRATO CON 5 BOMBA ADIACENTE
                                posiziona_5(x0,y0)
                                v["scoperta"]=True
                                v["bandierina"]=False
                                victory= vittoria(celle)                                
                            elif celle[i][j]== 6: # HAI BECCATO UN QUADRATO CON 6 BOMBA ADIACENTE
                                posiziona_6(x0,y0)
                                v["scoperta"]=True
                                v["bandierina"]=False
                                victory= vittoria(celle)
                if ev.button ==3 :  # Se il tasto cliccato del mouse è il dx, voglio quindi piazzare una bandierina                    
                    for k,v in coordinate.items():
                        x0 =int( v["x1"])
                        x1 =int(v["x2"])
                        y0=int(v["y1"])
                        y1=int(v["y2"])
                        (i,j)=k
                        scoperta = v["scoperta"] # Controllo dal dizionario se la casella che ho cliccato è scoperta o meno
                        if x in range (x0,x1) and y in range(y0,y1) and not scoperta and v["bandierina"]==True : # Se clicco la casella ed essa non è scoperta ma contiene già una bandierina vado a rimpizzarla con un quadrato ed elimino la bandierina
                            posiziona_quadrato(x0,y0)
                            v["bandierina"]=False # scriverò nel dizionario che in quella casella non c'è più la bandierina
                            pygame.display.flip()
                        elif x in range (x0,x1) and y in range(y0,y1) and not scoperta and contatore_bandierine>0: #Se la casella cliccata non è scoperta e il numero delle bandierine nella matrice è minore del numero di mine metto una bandierina nella casella 
                            posiziona_bandierina(x0,y0)
                            v["bandierina"]=True # scriverò nel dizionario che in quella casella c'è una bandierina
            if ev.type == QUIT: #Se l'evento all'interno della finestra è  il clicco sulla croce che chiude la finestra 
                # Rendo vere le condizioni dei While e chiudo la finestra di gioco
                done=True 
                done1=True
                pygame.quit()
            if ev.type== KEYDOWN: #Se l'evento all'interno del gioco  riguarda la pressione di un tasto della tastiera
                if ev.key == K_ESCAPE:    # Se il tasto premuto sulla tastiera è il tasto ESC chiuderò il gioco come con QUIT
                    done=True
                    done1= True
                    pygame.quit()                       
        if victory:# SE ABBIAMO VINTO, cioè nel caso in cui abbiamo scoperto tutte le caselle tranne quelle delle bombe, FACCIO APPARIRE LA SCRITTA DI VITTORIA
            scopri_campo(celle) #scopro tutto il campo
            surf_victory = pygame.image.load('vittoria.png').convert()  # FACCIO APPARIRE L'IMMAGINE DI HAI VINTO
            screen.blit(surf_victory, (160,473)) 
            smilevittoria = pygame.image.load('smile_vittoria.png').convert() #CARICO L'IMMAGINE DELLO SMILE DI VITTORIA
            screen.blit(smilevittoria, (339,16))     
            #RENDO VERA LA CONDIZIONE DEL PRIMO WHILE
            done=True
            done1=True
            contatore_bandierine=0
        conta_bandierine(contatore_bandierine) #vado a scrivere nel contatore quante bandierine sono state piazzate all'interno della matrice di gioco
        bandierine= numBandierina(coordinate) # ricevo il numero di bandierine piazzate
        clk.tick(120) #definisco gli fps a cui deve andare il clock. #rappresenta un "battito" dell'orologio. Esso avviene ogni 1/120 secondi. Python aspetterà il tempo appropriato prima di ricominciare il ciclo
        tick+=1    # ogni 1/120 secondi aumenta di uno poiché all'interno del while
        if tick==120: # Se il valore di tick arriva a 120 significa che è passato esattamente un secondo 
            fnt= pygame.font.SysFont("Special_Agent",43)
            surf_timer= pygame.Surface((55,40))
            screen.blit(surf_timer,(637,18))
            surf_font=  fnt.render(f"{c}{d}{u}",True,(255,0,0)) #scrivero i secondi passati sotto forma di centinaia, decine e unità
            screen.blit(surf_font,(638,22))
            quadrato_emoji(a)
            tick=0 # definisco il tick di nuovo uguale a 0 così mi ricalcola il secondo che passerà
            u+=1
            if u ==10: # se arrivo a 10 unità 
                a+=1 # aumenta di 1 il numero di decine totali, contatore utile per la funzione quadrato_emoji
                d+=1 # aumento di 1 il numero delle decine
                u=0
            if d==10:  # se arrivo a 10 decine            
                c+=1  # aumento di 1 il numero delle centinaia
                d=0
    while not done1:    #WHILE CHE INIZIA IN CASO DI GAME OVER O VITTORIA, mi serve per capire le intenzioni del giocatore se esso vuole rigiocare oppure uscire dal gioco
        eventlists2= pygame.event.get()
        for ev in eventlists2: 
            if ev.type == MOUSEBUTTONDOWN:
                    x= ev.pos[0]
                    y=ev.pos[1]
                    if ev.button == 1:   # SE FA CLICK CON IL TASTO SX DEL MOUSE SULLA FACCINA VUOLE RIGIOCARE
                        if x in range (339,381) and y in range (18,60):# se è in questo range di coordinate significa che l'utente sta cliccando sullo smile e voglio che ricrei la matrice di gioco                          
                            main() # faccio ripartire il gioco
                            done = True
                        elif x in range(83,125) and y in range(17,59): # se le coordinate sono in questo range allora il giocatore vuole cambiare modalità, controllo in quale modalità è adesso e la cambierò
                            if difficolta<=3:
                                difficolta+=1
                            else:   
                                difficolta=1
                            quadrato_difficolta(difficolta) # cambio la difficoltà
                            main()
            if ev.type== KEYDOWN:
                if ev.key == K_RETURN:  #Se il tasto della tastiera premuto è l'ENTER(invio) il giocatore vuole rigiocare                    
                    pygame.display.flip()
                    main() # faccio riniziare la funzione di gioco   
            if ev.type == QUIT:
                done= True
                done1=True
                pygame.quit() 
                break            
            if ev.type== KEYDOWN:
                if ev.key == K_ESCAPE:   
                    done=True 
                    done1=True
                    pygame.quit() 
                    break               
main()                        
            
'''Scritto e analizzato unicamente da Mattia Corigliano'''        
