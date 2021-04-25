from tkinter import*
import math
root=Tk()
display=StringVar()

operator=''

root.geometry('263x272+3+5')
root.title('Simple Calculator')


#functions of the calculator
def btnclick(num):
    global operator
    operator=operator+str(num)
    display.set(operator)

def btnclear(num):
    global operator
    operator=''
    display.set(operator)

def btnEqu():
    global operator
    calc=str(eval(operator))
    display.set(calc)
    operator=calc 

def btnbksp():
    global operator
    operator=operator[:-1]
    display.set(operator)




#display
screen=Entry(root,textvariable=display,justify='left').grid(columnspan=5,padx=3,pady=6)



#numbers and griding
button1=Button(root,text='7',command=lambda:btnclick(7),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#ffe8d6').grid(row=1,column=0,padx=2,pady=3)
button2=Button(root,text='8',command=lambda:btnclick(8),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#ffe8d6').grid(row=1,column=1,padx=2,pady=3)
button3=Button(root,text='9',command=lambda:btnclick(9),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#ffe8d6').grid(row=1,column=2,padx=2,pady=3)
button4=Button(root,text='4',command=lambda:btnclick(4),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#ffe8d6').grid(row=2,column=0,padx=2,pady=3)
button5=Button(root,text='5',command=lambda:btnclick(5),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#ffe8d6').grid(row=2,column=1,padx=2,pady=3)
button6=Button(root,text='6',command=lambda:btnclick(6),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#ffe8d6').grid(row=2,column=2,padx=2,pady=3)
button7=Button(root,text='1',command=lambda:btnclick(1),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#ffe8d6').grid(row=3,column=0,padx=2,pady=3)
button8=Button(root,text='2',command=lambda:btnclick(2),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#ffe8d6').grid(row=3,column=1,padx=2,pady=3)
button9=Button(root,text='3',command=lambda:btnclick(3),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#ffe8d6').grid(row=3,column=2,padx=2,pady=3)
button0=Button(root,text='0',command=lambda:btnclick(0),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#ffe8d6').grid(row=4,column=1,padx=2,pady=3)



#arithmetic symbols adn griding
buttonA1=Button(root,text='+',command=lambda:btnclick('+'),padx= 15,pady=15,font=('calibri',10,'bold'),activebackground='#4895ef').grid(row=4,column=3,padx=2,pady=3 )
buttonA2=Button(root,text='/',command=lambda:btnclick('/'),padx= 15,pady=15,font=('calibri',10,'bold'),activebackground='#4895ef').grid(row=1,column=3 ,padx=2,pady=3)
buttonA3=Button(root,text='*',command=lambda:btnclick('*'),padx= 15,pady=15,font=('calibri',10,'bold'),activebackground='#4895ef').grid(row=2,column=3 ,padx=2,pady=3)
buttonA4=Button(root,text='-',command=lambda:btnclick('-'),padx= 15,pady=15,font=('calibri',10,'bold'),activebackground='#4895ef').grid(row=3,column=3 ,padx=2,pady=3)
buttonA5=Button(root,text='=',command=lambda:btnEqu(),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#4895ef').grid(row=4,column=4 ,padx=2,pady=3)
buttonA6=Button(root,text='clr',command=lambda:btnclear('clr'),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#4895ef').grid(row=4,column=0,padx=2,pady=3)

#other keys
buttonA7=Button(root,text='.',command=lambda:btnclick('.'),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#4895ef').grid(row=4,column=2,padx=2,pady=3 )
buttonA8=Button(root,text='<[X]',command=lambda:btnbksp(),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#4895ef').grid(row=1,column=4 ,padx=2,pady=3)
buttonA9=Button(root,text='Pwr',command=lambda:btnclick('**'),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#4895ef').grid(row=2,column=4 ,padx=2,pady=3)
buttonA10=Button(root,text='mod',command=lambda:btnclick('%'),padx=15,pady=15,font=('calibri',10,'bold'),activebackground='#4895ef').grid(row=3,column=4,padx=2,pady=3)

root.mainloop()