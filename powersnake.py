import curses
from copy import copy
from random import randint
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

curses.initscr() #Inizializzazione dello schermo
finestra = curses.newwin(30, 60, 0, 0) #Crea una nuova finestra 30x60
finestra.keypad(True) #Abilita la possibilità di premere tasti con le 4 frecce
finestra.border(0) #Mettiamo un bordino esterno al "campo di gioco"
finestra.timeout(10) #Il serpente si muove nella direzione puntata oppure è "statico"
snake = [[15,13], [15,12], [15,11]] #Creiamo il serpente
cibo = [5,35] #Creiamo il primo cibo alla riga,colonna indicata ma NON lo aggiungiamo ancora
doveGuardo = KEY_DOWN #Il serpentello parte guardando in basso
punti = 0 #Ovviamente con 0 punti
finestra.addch(cibo[0], cibo[1], 'O')#La funzione addch aggiunge "O" riga,colonna

while True:
    #Mostriamo costantemente il punteggio del giocatore al centro
    finestra.addstr(0, 14, 'Punteggio: ' + str(punti) + ' ')
    #Aggiorna lo schermo automaticamente ad ogni frame di gioco e ottiene il tasto preso dall'utente
    tasto = finestra.getch()
    if tasto != -1:
        doveGuardo = tasto #Salviamo dentro "doveGuardo" il tasto premuto dall'utente
    
    #In base al tasto premuto dall'utente si fanno diverse azioni.
    #Si genera la nuova testa a partire dalla posizione della vecchia
    #e si aggiunge e sottrae 1 in base al tasto premuto dall'utente e la coordinata richiesta
    nuovaTesta = copy(snake[0])
    if doveGuardo == KEY_DOWN:
        nuovaTesta[0] += 1
    elif doveGuardo ==KEY_UP:
        nuovaTesta[0] -= 1
    elif doveGuardo == KEY_RIGHT:
        nuovaTesta[1] += 1
    elif doveGuardo == KEY_LEFT:
        nuovaTesta[1] -= 1
    
    #Si inserisce la nuova testa
    snake.insert(0, nuovaTesta)

    #Se il serpente esce dallo schermo break
    if snake[0][0] == 0 or snake[0][0] == 29 or snake[0][1] == 0 or snake[0][1] == 59:
        break

    #Se il serpente si cammina sopra break
    if snake[0] in snake[1:]:
        break

    # Se finisco sul cibo
    if snake[0] == cibo:
        cibo = []
        punti += 1
        while cibo == []:
            # Generiamo il prossimo cibo
            cibo = [randint(1, 28), randint(1, 58)]
            if cibo in snake:
                cibo = []
        finestra.addch(cibo[0], cibo[1], 'O') #Aggiunge il nuovo cibo alla finestra
    
    #Se il serpente finisce su qualsiasi casella
    else:
        ultimoPezzo = snake.pop() #Estrai l'ultimo pezzo del serpente e metti ' '
        finestra.addch(ultimoPezzo[0], ultimoPezzo[1], ' ')
    
    #Se non ho
    finestra.addch(snake[0][0], snake[0][1], 'x') #Si aggiunge

curses.endwin()#GAME OVER
print("\n GAME OVER! Punteggio finale: " + str(punti))