
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMRK = "✓"
from tkinter import *
import math
from numpy import size
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer ():  
    global reps #accessibile
    reps +=1


    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    
    #IF IT IS 1RD/3RD/5TH/7TH 
    
        
    #IF IT IS 8TH  REPEAT
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config (text= "Break", fg = RED )

    #IF IT IS 2nD/4TH/6TH  rep
    if reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config (text= "Break", fg = PINK )
    else:
        count_down(work_sec)
        title_label.config (text= "Work", fg = GREEN )



    
    
    count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# DA QUI INIZIA LE FUNZIONALITA. principio base è che programma segue costantemente eventi
#e reagisce di conseguenza. Per seguire quello che avviene e reagire a un evento usa
#window.after() che va nella sezxione di window
def count_down(count):
    count_min = math.floor (count / 60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}" #dynamic typing
    canvas.itemconfig(timer_text, text= F"{count_min}:{count_sec}")
    print(count)
    if count > 0:
        window.after(1000, count_down, count-1 ) #richiama se stessa con count sceso di 1 
    else :
        start_timer()
# import time
# count = 5
# while True:
#     time.sleep(1)
#     count -=1  
#quanto sopra è quello che per principio dovrebbe avvenire


# ---------------------------- UI SETUP  prima fase da fare------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady= 50, bg= YELLOW) #terza fase di padding E 5 DI BACKGROUND


def say_something(thing):
    print(thing)
#window.after(1000, say_something, "hello") #ma si deve ripetere quindi va in un loop (vedi countdown mechanism)
#FASE 6 INSERISCI LABEL TIMER
title_label = Label(text = "Timer", fg= GREEN, bg= YELLOW, font= (FONT_NAME, 50) )
title_label.grid(column=1, row=0)

#per inserire immagine usa canvas 
canvas = Canvas(width= 204, height=224, bg = YELLOW, highlightthickness=0)    #guardando grandezza dell'imagine
tomato_img = PhotoImage (file ="./day28/tomato.png" )  #necessario a creare un argomento valido per il metodo create_image sotto 
canvas.create_image(103, 112, image = tomato_img )  #messo a meta e nota che non accetta il file immagine 
                                        #ma una elaborzione dell'immagine
#4 fase inserisci testo 
timer_text = canvas.create_text(103, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
#usa color hunt per palette of color
#count_down(5)
start_button = Button(text="Start", command=start_timer )
start_button.grid(column=0, row=2)

reset_button = Button(text= "Reset")
reset_button.grid(column= 2, row= 2)

check_marks = Label(text=CHECKMRK, fg= GREEN, bg = YELLOW, font = (FONT_NAME,  40 ))
check_marks.grid(column= 1, row= 3)


canvas.grid(column=1, row=1) #per visualizzare

window.mainloop()



