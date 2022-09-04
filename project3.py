import math
import tkinter
root=tkinter.Tk()
root.title("Calculator")
def buttonc1(number):
    current=e.get()
    e.delete(0,tkinter.END)
    e.insert(0,str(current)+str(number))
def buttonclear():
    e.delete(0,tkinter.END)
def buttoncadd():
    global maths
    maths="addition"
    global f_num
    f_num=float(e.get())
    e.delete(0,tkinter.END)
    e.insert(0,e.get())
def buttoncequal():
    if maths=="addition":
        second=e.get()
        e.delete(0,tkinter.END)
        e.insert(0,f_num+float(second))
    elif maths=="multiply":
        second=e.get()
        e.delete(0,tkinter.END)
        e.insert(0,m*float(second))
    elif maths=="subtraction":
        second=e.get()
        e.delete(0,tkinter.END)
        e.insert(0,s-float(second))
    elif maths=="division":
        second=e.get()
        e.delete(0,tkinter.END)
        e.insert(0,d/float(second))
    elif maths=="remainder":
        second=e.get()
        e.delete(0,tkinter.END)
        e.insert(0,float(r)%float(second))
    elif maths=="power":
        second=e.get()
        e.delete(0,tkinter.END)
        e.insert(0,math.pow(p,float(second)))
    elif maths=="fact":
        e.delete(0,tkinter.END)
        ans=1
        for a in range(1,f+1):
            ans=ans*a
        e.insert(0,ans)
    else:
        e.delete(0,tkinter.END)
        e.insert(0,math.sqrt(ro))
        
    
def buttonmult():
    global maths
    maths="multiply"
    global m
    m=float(e.get())
    e.delete(0,tkinter.END)
    e.insert(0,e.get())
    
def buttonsub():
    global maths
    maths="subtraction"
    global s
    s=float(e.get())
    e.delete(0,tkinter.END)
    e.insert(0,e.get())
    
def buttondiv():
    global maths
    maths="division"
    global d
    d=float(e.get())
    e.delete(0,tkinter.END)
    e.insert(0,e.get())
def buttonroot():
    global maths
    maths="root"
    global ro
    ro=float(e.get())
    e.delete(0,tkinter.END)
    e.insert(0,e.get())
def buttonpower():
    global maths
    maths="power"
    global p
    p=float(e.get())
    e.delete(0,tkinter.END)
    e.insert(0,e.get())   
def buttonrem():
    global maths
    maths="remainder"
    global r
    r=float(e.get())
    e.delete(0,tkinter.END)
    e.insert(0,e.get())
def remove():
    current=e.get()
    e.delete(0,tkinter.END)
    a=e.get()
    b=""
    for c in a:
        b=b+c
    e.insert(0,b)
def fact():
    global maths
    maths="fact"
    global f
    f=int(e.get())
    e.delete(0,tkinter.END)
    e.insert(0,str(f)+"!")
e=tkinter.Entry(root,bg='white',fg='green',font=('Cambria',16),width=30,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
tkinter.Button(root,text="1",padx=51,pady=20,fg='blue',font=('Cambria',14),command=lambda:buttonc1(1)).grid(row=3,column=0)
tkinter.Button(root,text="2",padx=51,pady=20,fg='blue',font=('Cambria',14),command=lambda:buttonc1(2)).grid(row=3,column=1)
tkinter.Button(root,text="3",padx=51,pady=20,fg='blue',font=('Cambria',14),command=lambda:buttonc1(3)).grid(row=3,column=2)
tkinter.Button(root,text="4",padx=51,pady=20,fg='blue',font=('Cambria',14),command=lambda:buttonc1(4)).grid(row=2,column=0)
tkinter.Button(root,text="5",padx=51,pady=20,fg='blue',font=('Cambria',14),command=lambda:buttonc1(5)).grid(row=2,column=1)
tkinter.Button(root,text="6",padx=51,pady=20,fg='blue',font=('Cambria',14),command=lambda:buttonc1(6)).grid(row=2,column=2)
tkinter.Button(root,text="7",padx=51,pady=20,fg='blue',font=('Cambria',14),command=lambda:buttonc1(7)).grid(row=1,column=0)
tkinter.Button(root,text="8",padx=51,pady=20,fg='blue',font=('Cambria',14),command=lambda:buttonc1(8)).grid(row=1,column=1)
tkinter.Button(root,text="9",padx=51,pady=20,fg='blue',font=('Cambria',14),command=lambda:buttonc1(9)).grid(row=1,column=2)
tkinter.Button(root,text="0",padx=51,pady=20,fg='blue',font=('Cambria',14),command=lambda:buttonc1(0)).grid(row=4,column=0)
tkinter.Button(root,text="+",padx=51,pady=20,fg='blue',font=('Cambria',14),command=buttoncadd).grid(row=5,column=0)
tkinter.Button(root,text="=",padx=116,pady=20,fg='blue',font=('Cambria',14),command=buttoncequal).grid(row=6,column=1,columnspan=2)
tkinter.Button(root,text="Clear",padx=36,pady=20,fg='blue',font=('Cambria',14),command=buttonclear).grid(row=8,column=0)
tkinter.Button(root,text="*",padx=51,pady=20,fg='blue',font=('Cambria',14),command=buttonmult).grid(row=4,column=1)
tkinter.Button(root,text="-",padx=48,pady=10,fg='blue',font=('Cambria',20),command=buttonsub).grid(row=4,column=2)
tkinter.Button(root,text="/",padx=51,pady=20,fg='blue',font=('Cambria',14),command=buttondiv).grid(row=6,column=0)
tkinter.Button(root,text="Rem",padx=36,pady=20,fg='blue',font=('Cambria',14),command=buttonrem).grid(row=7,column=0)
tkinter.Button(root,text="Power",padx=32,pady=20,fg='blue',font=('Cambria',14),command=buttonpower).grid(row=7,column=1)
tkinter.Button(root,text="Root",padx=36,pady=20,fg='blue',font=('Cambria',14),command=buttonroot).grid(row=7,column=2)
tkinter.Button(root,text=".",padx=48,pady=10,fg='blue',font=('Cambria',20),command=lambda:buttonc1(".")).grid(row=5,column=2)
tkinter.Button(root,text="Remove",padx=92,pady=20,fg='blue',font=('Cambria',14),command=remove).grid(row=8,column=1,columnspan=2)
tkinter.Button(root,text="Factorial",padx=20,pady=20,fg='blue',font=('Cambria',14),command=fact).grid(row=5,column=1)
root.mainloop()