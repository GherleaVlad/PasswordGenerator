

import random
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
symbols = '!@#$%^&*()'
numbers = '123456789'
all = lower+upper+symbols+numbers

# ZONA DE FUNCTII

def generare_parola_simpla(lungime):
    if combox_lungime_parola.get() == "":
        lungime = 5
        parola_generata = ''.join(random.sample(all, lungime))
        parola = entry_continut_parola_simpla.get() + parola_generata

        entry_parola.config(state='normal')

        entry_parola.delete(0, END)
        entry_parola.insert(0, parola)

        entry_parola.config(state='readonly')


    else:
        lungime = int(combox_lungime_parola.get())
        simple_all = numbers + symbols
        parola_generata = ''.join(random.sample(simple_all, lungime))
        parola = entry_continut_parola_simpla.get() + parola_generata
        
        entry_parola.config(state='normal')
        
        entry_parola.delete(0, END)
        entry_parola.insert(0, parola)

        entry_parola.config(state='readonly')

def generare_parola_complexa(lungime):
    if combox_lungime_parola.get() == "":
        lungime = 10
        parola = ''.join(random.sample(all, lungime))

        entry_parola.config(state='normal')

        entry_parola.delete(0, END)
        entry_parola.insert(0, parola)

        entry_parola.config(state='readonly')

    else:
        lungime = int(combox_lungime_parola.get())
        parola = ''.join(random.sample(all, lungime))

        entry_parola.config(state='normal')

        entry_parola.delete(0, END)
        entry_parola.insert(0, parola)

        entry_parola.config(state='readonly')

def salvare_parola():
    parola = entry_parola.get()
    scop = entry_scop.get()

    if parola != '':
        locatie = filedialog.asksaveasfilename(title="Salveaza parolele",
                                    defaultextension=".txt",
                                    filetypes=[("Fisiere text", "*.txt")])


        if locatie: 
            with open(locatie, "a", encoding="utf-8") as fisier:
                fisier.write(f"Scop: {scop} | Parola: {parola}\n")
            messagebox.showinfo('SUCCES', f'Parola a fost salvata cu succes! Locatia fisierului: {locatie}.')

        else:
            messagebox.showerror('EROARE', 'Eroare la salvarea fisierului!')
    else:
        messagebox.showerror('EROARE', 'Nu exista nicio parola generata pentru a fi salvata!')



def stergere_parola():

    entry_parola.config(state='normal')
    entry_parola.delete(0, END)
    entry_parola.config(state='readonly')


# ZONA DE INTERFATA


root = Tk()

root.title('GENERATOR DE PAROLE')


screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

window_height = 620
window_width = 600

pozitionare_height = (screen_height // 2) - (window_height // 2)
pozitionare_width = (screen_width // 2) - (window_width // 2)


root.geometry(f'{window_width}x{window_height}+{pozitionare_width}+{pozitionare_height}')

root.resizable(False, False)

# PALETA DE CULORI
BG_MAIN = "#0F172A"
BG_BUTTON = "#1E293B"
BLUE = "#2563EB"
TURQUOISE = "#2DD4BF"
TEXT_WHITE = "#F8FAFC"
TEXT_MUTED = "#94A3B8"
VIOLET = "#A625EB"

root.config(bg=BG_MAIN)

titlu = Label(
    root,
    text="GENERATOR DE PAROLE",
    font=("Segoe UI", 20, "bold"),
    bg=BG_MAIN,
    fg=TEXT_WHITE
)

titlu.pack(pady=25)

frame_butoane = Frame (root, width=450,height=150, bg=BG_MAIN)
frame_butoane.pack()

buton_generare_simpla = Button(frame_butoane, 
                               text='PAROLA SIMPLA',
                               font=("Segoe UI", 13, "bold"),
                               width=25,
                               fg=TURQUOISE,
                               bg=BG_BUTTON, 
                               relief='raised',
                               command=lambda: generare_parola_simpla(combox_lungime_parola.get()))


buton_generare_complexa = Button(frame_butoane, 
                                 text='PAROLA COMPLEXA', 
                                 font=("Segoe UI", 13, "bold"),
                                 width=25, 
                                 fg=TURQUOISE, 
                                 bg=BG_BUTTON, 
                                 relief='raised',
                                 command=lambda: generare_parola_complexa(combox_lungime_parola.get()))

buton_generare_simpla.grid(row=0, column=0, padx=15, pady=15)
buton_generare_complexa.grid(row=0, column=1, padx=15, pady=15)

frame_user_input = Frame(root, width=450, height=100, bg=BG_MAIN)
frame_user_input.pack()

label_lungime = Label(frame_user_input,
                      text="LUNGIME PAROLA:",
                      bg=BG_MAIN,
                      fg=TURQUOISE,
                      font=("Segoe UI", 15, "bold"))                     

# entry_lungime = Entry(frame_user_input,
#                       font=("Segoe UI", 10, "bold"),
#                       width=10)

combox_lungime_parola = ttk.Combobox(frame_user_input,
                      font=("Segoe UI", 15, "bold"),
                      width=10,
                      height=7,
                      state="readonly",
                      values=[5, 7, 9, 10, 12, 14, 15, 18])
root.option_add("*TCombobox*Listbox.font", ("Segoe UI", 20, "bold"))


label_continut_parola_simpla = Label(frame_user_input,
                      text="CONTINUT PAROLA SIMPLA:",
                      bg=BG_MAIN,
                      fg=TURQUOISE,
                      font=("Segoe UI", 15, "bold"))                     

entry_continut_parola_simpla = Entry(frame_user_input,
                      font=("Segoe UI", 20, "bold"),
                      width=15)


label_lungime.grid(row=0, column=0, padx=15, pady=10)
# entry_lungime.grid(row=1, column=0, padx=15, pady=10)
combox_lungime_parola.grid(row=1, column=0, padx=15, pady=10)

label_continut_parola_simpla.grid(row=0, column=1, padx=15, pady=10)
entry_continut_parola_simpla.grid(row=1, column=1, padx=15, pady=10)

label_parola_generata = Label(root,
                            text="PAROLA GENERATA:",
                            bg=BG_MAIN,
                            fg=TURQUOISE,
                            font=("Segoe UI", 20, "bold"))

label_parola_generata.pack(pady=5)


entry_parola = Entry(root,
                    font=("Segoe UI", 20, "bold"),
                    width=30,
                    state="readonly")
entry_parola.pack(pady=(5,10))

label_scop = Label(root,
                    text="SCOP:",
                    bg=BG_MAIN,
                    fg=TURQUOISE,
                    font=("Segoe UI", 20, "bold"))

label_scop.pack(pady=5)


entry_scop = Entry(root,
                font=("Segoe UI", 20, "bold"),
                width=30)
entry_scop.pack(pady=(5,30))

frame_butoane= Frame (root, width=450,height=150, bg=BG_MAIN)
frame_butoane.pack()

buton_salvare = Button(frame_butoane,
                        text='SALVARE PAROLA',
                        font=("Segoe UI", 13, "bold"),
                        width=25, 
                        fg=TURQUOISE, 
                        bg=BG_BUTTON, 
                        relief='raised',
                        command=lambda: salvare_parola())

buton_stergere = Button(frame_butoane,
                        text='STERGERE PAROLA',
                        font=("Segoe UI", 13, "bold"),
                        width=25, 
                        fg=TURQUOISE, 
                        bg=BG_BUTTON, 
                        relief='raised',
                        command=lambda: stergere_parola())
buton_salvare.grid(row=0, column=0, padx=15, pady=10)
buton_stergere.grid(row=0, column=1, padx=15, pady=10)

root.mainloop()








        





    




