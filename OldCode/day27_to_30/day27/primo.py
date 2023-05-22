import tkinter

from numpy import MAY_SHARE_BOUNDS

window = tkinter.Tk()
window.title("My first gui program")
window.minsize( width= 500, height= 300)
#LABER Nota per qualuncqu componente devi
#crearlo e poi vedere dove posizionarlo
my_label = tkinter.Label(text = "I m a label", font=("Arial", 24,"bold"))
#creato la label
my_label.pack() # lo posizioni al centro alla prima riga disponibile



window.mainloop() #loop in attesa di eventi