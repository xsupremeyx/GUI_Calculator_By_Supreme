# Import
from tkinter import *

# Program Structure start
window = Tk()
window.title("Calculator")
color1 = '#%02x%02x%02x' % (217, 228, 241)
window.configure(bg='grey')
'''Structure continued ahead'''

# Program's Variables
op=1
operand1=[]
operator=[]
operand2=[]
sum=0

# Functions
def click(a):
    global operand1
    global operand2
    global operator
    global op
    if op==0:
        global sum
        sum=str(sum)
        digits = [int(x) for x in str(sum)]
        operand1=[]
        operand1.extend(digits)
        operator=[]
        operand2=[]
        op=1
    else:
        pass

    if a=='.':
        print("Coming soon")
    else:
        pass

    numentry.insert(END,a)
    if op==1:
        operand1.append(int(a))
        print(operand1,operator,operand2)
        print(op)
    elif op==2:
        op+=1
        operand2.append(int(a))
        print(operand1,operator,operand2)
        print(op)
    elif op==3:
        operand2.append(int(a))
        print(operand1,operator, operand2)
        print(op)

def click2(a):
    global operand1
    global operand2
    global operator
    global op

    if op==0:
        global sum
        sum = str(sum)
        digits = [int(x) for x in str(sum)]
        operand1 = []
        operand1.extend(digits)
        operator=[]
        operator.append(a)
        operand2 = []
        numentry.insert(END, a)
        op+=2

    else:
        pass
    if op==1:
        numentry.insert(END, a)
        operator.append(a)
        op+=1
    elif op==2:
        print("error")
    print(operand1, operator, operand2)
    print(op)

def delete():
    global operand1
    global operand2
    global op
    if op==0:
        clear()
    else:
        pass
    if op==1:
        lenght = len(operand1)
        if lenght==0:
            print("error")
        else:
            strstr= numentry.get()
            numentry.delete(0,END)
            numentry.insert(0,strstr[0:len(strstr)-1])
            operand1.pop(lenght-1)
            print(operand1,operator,operand2)
            print(op)

    elif op==2:
        op-=1
        strstr = numentry.get()
        numentry.delete(0, END)
        numentry.insert(0, strstr[0:len(strstr) - 1])
        print(operand1,operator, operand2)
        print(op)
    elif op==3:
        lenght = len(operand2)
        if lenght==0:
            lenght = len(operator)
            op-=2
            strstr = numentry.get()
            numentry.delete(0, END)
            numentry.insert(0, strstr[0:len(strstr) - 1])
            operator.pop(lenght-1)
            print(operand1,operator,operand2)
            print(op)
        elif lenght>0:
            strstr = numentry.get()
            numentry.delete(0, END)
            numentry.insert(0, strstr[0:len(strstr) - 1])

            operand2.pop(lenght-1)
            print(operand1, operator,operand2)
            print(op)

def clear():
    numentry.delete(0,END)
    global operand1
    global operand2
    global operator
    global op
    operand1=[]
    operand2=[]
    operator=[]
    op=1

def submit_answer():
    global op
    global sum
    num1=""
    num2=""
    for item in operand1:
        item=str(item)
        num1+=item
    for item in operand2:
        item=str(item)
        num2+=item
    num1=int(num1)
    num2=int(num2)
    op=0
    if '+' in operator:
        sum = num1+num2
        numentry.delete(0, END)
        numentry.insert(END, sum)
    if '-' in operator:
        sum = num1-num2
        numentry.delete(0, END)
        numentry.insert(END, sum)
    if '*' in operator:
        sum = num1*num2
        numentry.delete(0, END)
        numentry.insert(END, sum)
    if '/' in operator:
        sum = num1//num2
        numentry.delete(0, END)
        numentry.insert(END, sum)

# Images:
Num1 = PhotoImage(file="Calculator_Num1.png")
Num2 = PhotoImage(file="Calculator_Num2.png")
Num3 = PhotoImage(file="Calculator_Num3.png")
Num4 = PhotoImage(file="Calculator_Num4.png")
Num5 = PhotoImage(file="Calculator_Num5.png")
Num6 = PhotoImage(file="Calculator_Num6.png")
Num7 = PhotoImage(file="Calculator_Num7.png")
Num8 = PhotoImage(file="Calculator_Num8.png")
Num9 = PhotoImage(file="Calculator_Num9.png")
Num0 = PhotoImage(file="Calculator_Num0.png")

Plus = PhotoImage(file="Calculator_Plus.png")
Minus = PhotoImage(file="Calculator_Minus.png")
Division = PhotoImage(file="Calculator_Div.png")
Multi = PhotoImage(file="Calculator_Mult.png")

Point = PhotoImage(file="Calculator_Point.png")

Backspace = PhotoImage(file="Calculator_Backspace.png")
Equal = PhotoImage(file="Calculator_Submit.png")

# Program GUI Structure

Label(window,text="Entry:",bg="black",fg="yellow").grid(row=0,column=0,sticky='wnse')
numentry=Entry(window,bg="light gray",fg="black")
numentry.grid(row=0,column=1,columnspan=5,sticky='wnse')

Label(window,text="Don't use Decimals,Coming soon.",bg="black",fg="yellow").grid(row=6,column=0,columnspan=5,sticky='wnse')

Button(window,image= Num1,command=lambda: click("1")).grid(row=1,column=0,sticky='w')
Button(window,image= Num2,command=lambda: click("2")).grid(row=1,column=1,sticky='wnse')
Button(window,image= Num3,command=lambda: click("3")).grid(row=1,column=2,sticky='w')
Button(window,image= Plus,command=lambda: click2("+")).grid(row=1,column=3,sticky='w')
Button(window,image= Num4,command=lambda: click("4")).grid(row=2,column=0,sticky='w')
Button(window,image= Num5,command=lambda: click("5")).grid(row=2,column=1,sticky='wnse')
Button(window,image= Num6,command=lambda: click("6")).grid(row=2,column=2,sticky='w')
Button(window,image= Minus,command=lambda: click2("-")).grid(row=2,column=3,sticky='w')
Button(window,image= Num7,command=lambda: click("7")).grid(row=3,column=0,sticky='w')
Button(window,image= Num8,command=lambda: click("8")).grid(row=3,column=1,sticky='wnse')
Button(window,image= Num9,command=lambda: click("9")).grid(row=3,column=2,sticky='w')
Button(window,image= Multi,command=lambda: click2("*")).grid(row=3,column=3,sticky='w')
Button(window,image= Num0,command=lambda: click("0")).grid(row=4,column=0,columnspan=2,sticky='w')
Button(window,image= Point,command=lambda: click(".")).grid(row=4,column=2,sticky='w')
Button(window,image= Division,command=lambda: click2("/")).grid(row=4,column=3,sticky='wnse')

Button(window,image=Backspace,command=lambda: delete()).grid(row=1,rowspan=2,column=4,stick='wnse')
Button(window,image=Equal,command=lambda: submit_answer()).grid(row=3,rowspan=2,column=4,stick='wnse')
Button(window,text="Clear",command=lambda: clear()).grid(row=5,column=0,columnspan=5,stick='wnse')
window.mainloop()