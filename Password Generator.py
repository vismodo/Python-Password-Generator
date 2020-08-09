import tkinter as tk
from tkinter.messagebox import showinfo
import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
more = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '&', '*', '/', '?', '.']
start = tk.Tk()
start.title('Python Password Generator')
start.geometry('500x100')
opt = tk.IntVar()
nums = tk.Checkbutton(start, text='Include Numbers and Special Characters', variable = opt)
length = tk.Spinbox(start, from_= 4, to=14)
label = tk.Label(start, text = 'Length of your password:')
label.pack()
length.pack()
nums.pack()
def gen_password():
    try:
        pass_len = int(length.get())
        result = []
        if (opt.get() == 1):
            while (not any(item in more for item in result)) or (not any(item in letters for item in result)):
                result = []
                for x in range(pass_len):
                    result.append(r.choice(letters+more))
        else:
            result = []
            for x in range(pass_len):
                result.append(r.choice(letters))
        result = str(result)
        pass_result = result.replace(',', '')
        pass_result = pass_result.replace('[', '')
        pass_result = pass_result.replace(']', '')
        pass_result = pass_result.replace("'", "")
        pass_result = pass_result.replace(" ", "")

        showinfo('Your Password', str(pass_result))
    except Exception as error:
        showinfo('Error', error)

generate = tk.Button(start, text = 'Generate Password', command = gen_password, font = ('Aerial', 16))
generate.pack(side = 'bottom')
start.mainloop()
