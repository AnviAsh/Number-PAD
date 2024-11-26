from tkinter import *
root = Tk()
root.title('NUMBER PAD')
root.geometry('250x300')

#create frame to organise elements

frame = Frame(master = root, height= 200 , width = 360 , bg = "lightgrey")
nums = [[9,8,7],[6,5,4],[3,2,1], ['#' , 0 , '*']]

for i in range(4):
    #confiure rows and coloumns to resize window
    root.columnconfigure(i,weight = 1 , minsize= 75)
    root.rowconfigure(i,weight = 1 , minsize= 50)
    
    for j in range(0,3):
        frame = Frame(master = root , relief= SUNKEN , borderwidth= 3)
        frame.grid(row = i , column= j)
        label = Label(master = frame , text = nums[i][j] , bg = "lightgrey")
        label.pack(padx= 3 , pady= 3)

root.mainloop()