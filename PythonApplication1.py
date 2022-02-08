#перевод чисел между системами счисления
from tkinter import *

def calculate():
    entry3.delete(0, END)
    NumBefore = entry1.get()                            
    NumSys = entry2.get()
    try:
        NumBefore = float(NumBefore)
        NumSys = int(NumSys)
        if NumBefore >= 0 and int(NumSys)<=9 and int(NumSys)>=2:               
            NumAfter = 0.0
            count = 0
            frc = NumBefore - int(NumBefore)            #отделение целой части от дробной
            NumBefore = int(NumBefore)                  #


            while NumBefore >= NumSys:
                rem = NumBefore % NumSys
                rem = rem * (10 ** count)
                NumAfter = NumAfter + rem                           #перевод целой части
                NumBefore = int(NumBefore / NumSys)
                count = count + 1
            NumAfter = NumAfter + (NumBefore * (10**count))


            for countpos in range(1, 4, 1):
                countneg = countpos * (-1)
                rem = frc // (NumSys ** countneg)
                rem = rem * (10 ** countneg)                        #перевод дробной части
                NumAfter = NumAfter + rem
                frc = frc - rem * (10 ** countpos) * (NumSys ** countneg)
            entry3.insert(0, NumAfter)
        else:
            entry3.insert(0, 'Проверьте ввод')
    except:
        entry3.insert(0, 'Проверьте ввод')

    

root = Tk()
root.geometry('200x100')
entry1 = Entry(root, width = 20)
entry1.insert(0, 'Введите сюда число')
entry2 = Entry(root, width = 20)
entry2.insert(0, 'Введите сюда систему счисления')
button = Button(root, text = 'Перевести', command = calculate)
entry3 = Entry(root, width = 20)


entry1.pack()
entry2.pack()
button.pack()
entry3.pack()
root.mainloop()