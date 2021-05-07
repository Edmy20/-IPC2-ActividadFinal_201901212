from tkinter import *
from tkinter.ttk import *
#El tablero de 3x3 se llena con -'s
tablero = list('-' for i in range(0, 9))

def crear_tablero(tablero):
    #Aqui se va a Actualizar el tablero
    #El tablero se representa como una string para usarlo en la caja de texto
    tic_tac = ""
    n = 0
    for i in range(3):
        
        tic_tac += '\n'#Cada 3 casilklas se realiza un salto de linea
        for j in range(3):
            tic_tac+=' |'+str(tablero[n])#Se actualiza el contenido del tablero
            n+=1

    return tic_tac

def ganador(letter):
    # El tablero es de 3x3 Asi que tiene 3 columnas y 3 filas
    # Si todos las casillas ue forman una columan o fila son iguales, el jugador ha ganado
    # Si todos las casillas ue forman una diagonal, el jugador ha ganado
    winner = False
    if tablero[0] == letter and tablero[1] == letter and tablero[2]==letter:#Todas las casillas en la 1ra.Fila son iguales
        winner = True
    elif tablero[3] == letter and tablero[4] == letter and tablero[5]==letter:#Todas las casillas en la 2da.Fila son iguales
        winner = True
    elif tablero[6] == letter and tablero[7] == letter and tablero[8]==letter:#Todas las casillas en la 3ra.Fila son iguales
        winner = True
    elif tablero[0] == letter and tablero[3] == letter and tablero[6]==letter:#Todas las casillas en la 1ra.Columna son iguales
        winner = True
    elif tablero[1] == letter and tablero[4] == letter and tablero[7]==letter:##Todas las casillas en la 2da.Columna son iguales
        winner = True
    elif tablero[2] == letter and tablero[5] == letter and tablero[8]==letter:#Todas las casillas en la 3ra.Columna son iguales
        winner = True
    elif tablero[0] == letter and tablero[4] == letter and tablero[8]==letter:#Todas las casillas de la diagonal (\), son iguales
        winner = True
    elif tablero[2] == letter and tablero[4] == letter and tablero[6]==letter:#Todas las casillas de la diagonal (/), son iguales
        winner = True

    return winner

def limpiar():
    #Limpia el tablero
    global tablero
    tablero = list(0 for i in range(0, 9))#Se vuelve a llenar de -'s el tablero
    text.delete('1.0',END)#Se borra el contenido de la caja de texto
    tic_tac = crear_tablero(tablero)#Se actualiza el tablero
    text.insert(END, tic_tac)#Se muestra el tablero en la caja de texo

def jugador1():
    op = selected.get()#Se optiene la posicion que eligio el jugador
    tablero[op]='X'#Se rellena esa posicion con el simbolo del jugador
    text.delete('1.0',END)
    tic_tac = crear_tablero(tablero)#Se manda a actualizar el tablero
    text.insert(END, tic_tac)

    winner = ganador('X')#Se verfica si se a formado 3 en raya

    if winner == True:#De ser asi se envia el mensaje de que el jugador a ganado
        text.insert(END,'\n\n______________________\nEl jugador 1 ha ganado')
    else: #Por el contrario, se envia el mensaje de que es el turno del otro jugador
        text.insert(END,'\n\n_____________________\nLe toca elegir al:\nJugador 2')

#Esta funcion realiza lo mismo que jugador1, solo que con el simbolo del jugador2
def jugador2():
    op = selected.get()
    tablero[op]='O'
    text.delete('1.0',END)
    tic_tac = crear_tablero(tablero)
    text.insert(END, tic_tac)

    winner = ganador('O')

    if winner == True:
        text.insert(END,'\n\n______________________\nEl jugador 2 ha ganado')
    else: 
        text.insert(END,'\n\n_____________________\nLe toca elegir al:\nJugador 1')

#Se crea la ventana Principal
root = Tk()
root.geometry('600x400')
root['background']='LightPink3'
root.title("VENTANA PRINCIPAL")
#Selected se usa para obtener la posicion que el jugador eligio
selected = IntVar()
#Se crea la caja de texto donde se mostrara el tablero
text = Text(root, wrap=NONE,font=("Consolas",15))
tic_tac = crear_tablero(tablero)
text.insert(END, tic_tac)
text.place(x=10,y=100,width=260,height=285)


#----------El jugador elegira la posicion donde desea colocar su simbolo, estas iran del 1-9
rad1 = Radiobutton(root,text='1', value=0, variable=selected)

rad2 = Radiobutton(root,text='2', value=1, variable=selected)

rad3 = Radiobutton(root,text='3', value=2, variable=selected)

rad4 = Radiobutton(root,text='4', value=3, variable=selected)

rad5 = Radiobutton(root,text='5', value=4, variable=selected)

rad6 = Radiobutton(root,text='6', value=5, variable=selected)

rad7 = Radiobutton(root,text='7', value=6, variable=selected)

rad8 = Radiobutton(root,text='8', value=7, variable=selected)

rad9 = Radiobutton(root,text='9', value=8, variable=selected)

rad1.place(x=280, y=100, width=50, height=30)
rad2.place(x=330, y=100, width=50, height=30)
rad3.place(x=380, y=100, width=50, height=30)
rad4.place(x=280, y=135, width=50, height=30)

rad5.place(x=330, y=135, width=50, height=30)
rad6.place(x=380, y=135, width=50, height=30)
rad7.place(x=280, y=170, width=50, height=30)
rad8.place(x=330, y=170, width=50, height=30)

rad9.place(x=380, y=170, width=50, height=30)

#Una vez el jugador haya elegido la posicion, debe de presionar el boton que le corresponde
btn1 = Button(root, text="Jugar: Player 1", command=jugador1)
btn2 = Button(root, text="Jugar: Player 2", command=jugador2)

#Boton para limpiar
btn3 = Button(root, text="RESET", command=limpiar)

btn1.place(x=30, y=30, width=200, height=30)
btn2.place(x=300, y=30, width=200, height=30)
btn3.place(x=300, y=220, width=200, height=30)


root.mainloop()