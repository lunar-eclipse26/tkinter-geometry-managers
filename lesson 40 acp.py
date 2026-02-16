from tkinter import *
from datetime import date
def calculate_age():
    current_year = date.today().year
    birth_year = int(year_entry.get())
    age = current_year - birth_year
    label_2.config(text=f"It has been approximately: {age} years")
window = Tk()
window.title('Calculate ur age!')
window.geometry('300x300')
label_1 = Label(text="What year were u born lil bruh")
label_1.pack()
year_entry = Entry()
year_entry.pack()
button = Button(text="Calculate", command=calculate_age)
button.pack()
label_2 = Label(text="Age will appear here\nmay not be fully accurate")
label_2.pack()
window.mainloop()