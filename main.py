from tkinter import*

func=0
def marks():
    global func
    try:
        if rbn.get()=='Enable' and func==0:
            # print("i")
            cal1=float(tcaentry.get())*float(mcaentry.get())
            cal2=float(ticaentry.get())*float(micaentry.get())
            totalmarks=float(cal1-cal2)
            tmval.set(str(totalmarks))
            tmentry.config(state=DISABLED)
            tmentry.config()
            statusbar.config(text="This app is developed and maintained by codex",font=('Bahnschrift',11),fg='#f7f9f9',bg='#2ecc71')
        elif rbn.get()=='Disable' and func==1:
            # print("j")
            cal1=float(tcaentry.get())*float(mcaentry.get())
            tmval.set(str(cal1))
            statusbar.config(text="This app is developed and maintained by codex",font=('Bahnschrift',11),fg='#f7f9f9',bg='#2ecc71')
        elif rbn.get()=='Enable' and func==1:
            # print("k")
            cal1=float(tcaentry.get())*float(mcaentry.get())
            tmval.set(str(cal1))
            statusbar.config(text="This app is developed and maintained by codex",font=('Bahnschrift',11),fg='#f7f9f9',bg='#2ecc71')
        else:
            # print("l")
            cal1=float(tcaentry.get())*float(mcaentry.get())
            cal2=float(ticaentry.get())*float(micaentry.get())
            totalmarks=float(cal1-cal2)
            tmval.set(str(totalmarks))
            tmentry.config(state=DISABLED)
            tmentry.config()
            statusbar.config(text="This app is developed and maintained by codex",font=('Bahnschrift',11),fg='#f7f9f9',bg='#2ecc71')

    except ValueError:
        statusbar.config(text="Fill the correct Value!",bg='red')

def change():
    global func
    if rbn.get()=='Enable':
        tica.place(x=10,y=130)
        ticaentry.place(x=310,y=130)
        mica.place(x=10,y=160)
        micaentry.place(x=310,y=160)
        func=0
    elif rbn.get()=='Disable':
        tica.place_forget()
        ticaentry.place_forget()
        mica.place_forget()
        micaentry.place_forget()
        func=1
    else:
        pass

    if rld.get()=='Light':
        win.config(bg='#eaeded')
        dataframe.config(fg='#4a235a',bg='#eaeded')
        tca.config(fg='#4a235a',bg='#eaeded')
        mca.config(fg='#4a235a',bg='#eaeded')
        tica.config(fg='#4a235a',bg='#eaeded')
        mica.config(fg='#4a235a',bg='#eaeded')
        calculate.config(bg='#4a235a',fg='#eaeded')
        tm.config(fg='#4a235a',bg='#eaeded')
        settingsframe.config(fg='#4a235a',bg='#eaeded')
        ren.config(fg='#4a235a',bg='#eaeded')
        eden.config(fg='#4a235a',bg='#eaeded')
        nm.config(fg='#4a235a',bg='#eaeded')
        ld.config(fg='#4a235a',bg='#eaeded')
        rlm.config(fg='#4a235a',bg='#eaeded')
        rdm.config(fg='#4a235a',bg='#eaeded')
        sframe1.config(bg='#eaeded')
        sframe2.config(bg='#eaeded')
        apply.config(bg='#4a235a',fg='#eaeded')
    elif rld.get()=='Dark':
        win.config(bg='black')
        dataframe.config(fg='white',bg='black')
        tca.config(fg='white',bg='black')
        mca.config(fg='white',bg='black')
        tica.config(fg='white',bg='black')
        mica.config(fg='white',bg='black')
        calculate.config(bg='white',fg='black')
        tm.config(fg='white',bg='black')
        settingsframe.config(fg='white',bg='black')
        ren.config(fg='#979a9a',bg='black')
        eden.config(fg='#979a9a',bg='black')
        nm.config(fg='white',bg='black')
        ld.config(fg='white',bg='black')
        rlm.config(fg='#979a9a',bg='black')
        rdm.config(fg='#979a9a',bg='black')
        sframe1.config(bg='black')
        sframe2.config(bg='black')
        apply.config(bg='white',fg='black')
    else:
        pass

    

        


win=Tk()
win.geometry("700x300")
win.title("Marks Calculator")
win.config(bg='#eaeded')
win.iconbitmap('marks.ico')


statusbar=Label(win,text="This app is developed and maintained by codex",font=('Bahnschrift',11),fg='#f7f9f9',bg='#2ecc71')
statusbar.pack(side=TOP,fill=X)

dataframe=LabelFrame(win,text="Fill the data below",font=('Bahnschrift',11),fg='#4a235a')
dataframe.place(x=5,y=30,width=500,height=270)

tca=Label(win,text="Total correct answers:",font=('Bahnschrift',11),fg='#4a235a')
tca.place(x=10,y=70)

tcaentry=Entry(win,font=('Calibri (Body)',12))
tcaentry.place(x=310,y=70)


mca=Label(win,text="Marks for each correct answers:",font=('Bahnschrift',11),fg='#4a235a')
mca.place(x=10,y=100)

mcaentry=Entry(win,font=('Calibri (Body)',12))
mcaentry.place(x=310,y=100)


tica=Label(win,text="Total incorrect answers:",font=('Bahnschrift',11),fg='#4a235a')
tica.place(x=10,y=130)

ticaentry=Entry(win,font=('Calibri (Body)',12))
ticaentry.place(x=310,y=130)


mica=Label(win,text="Negative marks for each incorrect answers:",font=('Bahnschrift',11),fg='#4a235a')
mica.place(x=10,y=160)

micaentry=Entry(win,font=('Calibri (Body)',12))
micaentry.place(x=310,y=160)

calculate=Button(win,text="Calculate",command=marks,font=('Bahnschrift',11),fg='#f7f9f9',bg='#4a235a')
calculate.place(x=230,y=200)

tm=Label(win,text="Total Marks Obtained:",font=('Bahnschrift',11),fg='#4a235a')
tm.place(x=10,y=250)
tmval=StringVar()
tmentry=Entry(win,font=('Calibri (Body)',12,'bold'),textvariable=tmval)
tmentry.place(x=310,y=250)

settingsframe=LabelFrame(win,text="Settings",font=('Bahnschrift',11),fg='#4a235a')
settingsframe.place(x=510,y=30,height=270,width=185)

sframe1=Frame(win)
sframe1.place(x=515,y=60,height=80,width=175)

nm=Label(sframe1,text='Negative marking:',font=('Bahnschrift',11),fg='#4a235a')
nm.place(x=1,y=1)

rbn=StringVar(value='Enable')
ren=Radiobutton(sframe1,text="Enable",font=('Bahnschrift',11),fg='#4a235a',value='Enable',variable=rbn)
ren.place(x=1,y=30)
eden=Radiobutton(sframe1,text="Disable",font=('Bahnschrift',11),fg='#4a235a',value='Disable',variable=rbn)
eden.place(x=100,y=30)


sframe2=Frame(win)
sframe2.place(x=515,y=140,height=100,width=175)
ld=Label(sframe2,text='Mode:',font=('Bahnschrift',11),fg='#4a235a')
ld.place(x=1,y=1)
rld=StringVar(value='Light')
rlm=Radiobutton(sframe2,text="Light",font=('Bahnschrift',11),fg='#4a235a',value='Light',variable=rld)
rlm.place(x=1,y=30)
rdm=Radiobutton(sframe2,text="Dark",font=('Bahnschrift',11),fg='#4a235a',value='Dark',variable=rld)
rdm.place(x=100,y=30)

apply=Button(sframe2,text="Apply",font=('Bahnschrift',11),bg='#4a235a',fg="white",height=1,width=10,command=change)
apply.place(x=40,y=70)

win.mainloop()