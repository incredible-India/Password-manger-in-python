"""Trust me is a project which keeps all the password  of some basic apps like flipkart ,amazone,netflix,gmail,facebook,
 mobile Unlock in Database (Mongodb) . With the help of this we can easily access our password .
 Project Admin : - Himanshu Sharma B.E Third sem , Date of starting this project 04/11/2020"""
"""//////////////////////////////////////////////////////////////////////////////////"""

# importing all modules which will be used in this project
from tkinter import *    #for gui
#import pymongo #for mongodb database
from tkinter import  colorchooser  #changing the color of background
import os   #operating system module help for making and cheking directories
import  datetime #for the current date and time
from PIL import Image,ImageTk  #for supporting the png or jpg formate type images
import tkinter.messagebox as msg  #this will show the message as dialougebox






"""All the functions ,used in this project"""

"""for changing the background Color"""
def changingColor():
    mychoice=colorchooser.askcolor(title="Select the theme")
    root.config(bg=mychoice[1])
    trust.config(bg=mychoice[1])
    pic.config(bg=mychoice[1])
    f1.config(bg=mychoice[1])
    if mychoice=="#000000" or "#000040" or "#004040" or "400040" or "#0000a0" or "#000080":
        trust.config(fg="red")
  
    """////////////////////////////////////////////////////////"""
"""for feedback"""
def feedback():
    
     def submit(feedbackdata):
          if os.path.exists("Feedback")==False:
             os.mkdir("Feedback")


          with open("Feedback\\feedbaks.txt","a") as inserdata:
                inserdata.write(f" On {datetime.datetime.now()} \n {feedbackdata} --------\n")
                feed.destroy()




     feed=Toplevel()
     feed.title("Trust Me :- Feedback")
     feed.iconbitmap('icons\\paste.ico')
     feed.resizable(False,False)
     Label(feed,text="Give Your Valuable Feedback",font="elephant 15 underline").pack(pady=6)

     myscroll=Scrollbar(feed)
     myscroll.pack(fill=Y,side=RIGHT,anchor=E)
     text=Text(feed,yscrollcommand=myscroll.set,selectbackground="#000040",font="times 15 ")
     text.pack(expand=True,fill=BOTH)
     myscroll.config(command=text.yview)

     Button(feed,text="Submit",width=20,font="arial 12",bg="green",fg="white",command=lambda : submit(text.get(1.0,END))).pack(side=LEFT,pady=5)
     Button(feed,text="Cancel",width=20,font="arial 12",command=feed.destroy,bg="red",fg="white").pack(side=LEFT,pady=5)

     feed.mainloop()
"""//////////////////"""
"""Help page"""
def help():
    help=Toplevel()
    help.resizable(False,False)
    help.title("Trust Me :- Help Desk")
    help.config(bg="#000040")
    help.iconbitmap('icons\\ask.ico')
    Label(help,text="Help Desk",fg="red",font="arial 15 underline").pack(pady=10)
    textFrame=Frame(help,bd=3,relief=GROOVE)
    textFrame.pack(padx=10,pady=10)
    with open("about\\help.txt") as readData:
        text=Label(textFrame,text=readData.read(),bd=2,relief=SUNKEN,font="times 15",fg="#004040")
        text.pack()
    Button(help,text="Got It",width=20,bg="red",fg="white",font="arial 12 ",command=help.destroy).pack(pady=5)
    help.mainloop()

"""/////////////////////////////////////////////////////////////"""

"""about page"""
def about():
    about=Toplevel()
    about.config(bg="#004040")
    about.resizable(False,False)
    about.iconbitmap('icons\\admin.ico')
    Label(about,text="Project Admin",font="elephant 16",bd=2,relief=GROOVE
          ,).pack(pady=10)

    maiLabel=Frame(about,bd=2 ,relief=SUNKEN,width=50,padx=10,pady=10)
    maiLabel.pack(padx=2,pady=10)

    adminpic=Image.open('images\\hj.jpg')
    imgadmin=ImageTk.PhotoImage(adminpic)
    piclabale=Label(maiLabel,image=imgadmin,bd=2,relief=SUNKEN)
    piclabale.pack(side=TOP)
    Label(maiLabel,text="Himanshu Sharma \n B.E 3rd Sem",font="times 16").pack(side=TOP)


    ab=Frame(about)
    ab.pack()
    with open("about\\about.txt") as data:

        statement=Label(ab,text=data.read(),bd=2,relief=GROOVE,font="arail 12",fg="#004040")
        statement.pack()
    bfram=Frame(about)
    bfram.pack()
    Button(bfram,text="Got it",bg="#400040",fg="white",width=25,command=about.destroy).pack(side=LEFT,padx=5,pady=5)
    Button(bfram,text="Feedback",bg="green",fg="white",width=25,command=feedback).pack(side=LEFT,padx=5,pady=5)


    about.mainloop()
    """//////////////////////////////////////////////////////"""


"""for the new user registration form"""
def NewRegistration():
    def quitit():
        form.destroy()
        pass
    def Confirmation(name,password,CNFpassword,email,app1,app1p,app2,app2p,app3,app3p,app4,app4p,app5,app5p,app6,app6p,app7,app7p,app8,app8p
                     ,app9,app9p,app10,app10p,app11,app11p,app12,app12p,textdata):
        # print(len(name),print(email),len(password))
        if len(name) == 0 or len(password)==0 or len(password)==0 or len(CNFpassword)==0 or len(email)==0:

            msg.showerror("Input Error","Name,Email,Password and Confirm password can not be blank,please check and fill this. ")
            return
        elif password != CNFpassword:

            msg.showerror("Password Error","Password did not matche with confirm password..")
            return
        elif len(password)<=3:

            msg.showerror("Samll password","Password is too small,it should be greater than 3")
            return
        elif "@gmail.com" not in email and len(email) <=10:

            msg.showerror("Email Error","Incorrect Email id")
        else:
            confirm=Tk()
            confirm.resizable(False,False)
            k = 0
            toSaveData = {}

            Label(confirm,text="Do not forgate your Email Name and Password",fg="red",bd=2,relief=SUNKEN,font="times 16").pack(pady=10)
            l1=Label(confirm,text=f'Name is {name.capitalize()} and Password is {password}\nemail is {email}',font="arial 16",bg="black",fg="white")
            l1.pack(pady=10)
            allpassword=[app1,app1p,app2,app2p,app3,app3p,app4,app4p,app5,app5p,app6,app6p,app7,app7p
                ,app8,app8p,app9,app9p,app10,app10p,app11,app11p,app12,app12p]


            for lists in allpassword:
                if lists=="":
                      k +=1

            if k==24:
                msg.showerror("Entry Error","Please Enter at least one app`s name and its password")
                confirm.destroy()
                return

            """now we will show to the user to save the data or not"""

            if (len(app1)!=0 and len(app1p)!=0):
                toSaveData[app1]=app1p

            if (len(app2)!=0 and len(app2p)!=0):
                toSaveData[app2] = app2p

            if (len(app3)!=0 and len(app3p)!=0):
                toSaveData[app3] = app3p

            if (len(app4)!=0 and len(app4p)!=0):
                toSaveData[app4] = app4p

            if (len(app5)!=0 and len(app5p)!=0) :
                toSaveData[app5] = app5p

            if (len(app6)!=0 and len(app6p)!=0):
                toSaveData[app6] = app6p

            if (len(app7)!=0 and len(app7p)!=0):
                toSaveData[app7] = app7p

            if (len(app8)!=0 and len(app8p)!=0) :
                toSaveData[app8] = app8p

            if (len(app9) != 0 and len(app9p) != 0) :
                toSaveData[app9] = app9p

            if (len(app10) != 0 and len(app10p) != 0):
                toSaveData[app10] = app10p

            if (len(app11) != 0 and len(app11p) != 0):
                toSaveData[app11] = app11p

            if (len(app12) != 0 and len(app12p) != 0):
                toSaveData[app12] = app12p

            """for notes textdata"""
            if (len(textdata)) > 1:
                toSaveData["Notes"] = textdata



            for app  in toSaveData:
                Label(confirm,text=f' {app} --> {toSaveData[app]}',font="arial 13").pack(side=TOP,pady=1)

            fbutton=Frame(confirm) #for buttond
            
            fbutton.pack()

            Button(fbutton, text="Confirm" ,width=12 ,bg="#400040",fg="white" ,font="arial 12").pack(side=LEFT,padx=5)

            Button(fbutton, text="Edit",width=12, command=confirm.destroy,bg="red" ,font="arial 12").pack(side=LEFT,padx=5)

            Label(confirm,text="Name ,Email and password are required for Log in",font="arial 16",bd=2,fg="green",relief=SUNKEN).pack(padx=5,pady=6)







            confirm.mainloop()
            """////////////////////////////////////////////////////////////////////////////////////////////////////////"""





    """making the variable for the Entry Widget"""
    name=StringVar()
    password=StringVar()
    CNFpassword=StringVar()
    email=StringVar()

    app1=StringVar()
    app1pass=StringVar()

    app2 = StringVar()
    app2pass = StringVar()

    app3 = StringVar()
    app3pass = StringVar()

    app4 = StringVar()
    app4pass = StringVar()
    app5 = StringVar()
    app5pass = StringVar()
    app6 = StringVar()
    app6pass = StringVar()
    app7 = StringVar()
    app7pass = StringVar()
    app8 = StringVar()
    app8pass = StringVar()
    app9 = StringVar()
    app9pass = StringVar()
    app10 = StringVar()
    app10pass = StringVar()
    app11 = StringVar()
    app11pass = StringVar()
    app12 = StringVar()
    app12pass = StringVar()

    """////////////////////////////////"""
    form=Toplevel()
    form.geometry("1170x800")
    form.config(bg="#000040")

    Label(form, text="Registration", font="arial 15 ", fg="red").pack(side=TOP,pady=4)
    mainFrame=Frame(form,bd=2,relief=SUNKEN,bg="#000040")
    mainFrame.pack(padx=5,pady=15)

    qFrame1=Frame(mainFrame,bd=2,relief=SUNKEN,bg="#000040")
    qFrame1.pack(side=TOP,pady=9,padx=3)

    qlab1=Label(qFrame1,text="Name :",font="arial 15" ,bg="red")
    qlab1.pack(side=LEFT ,padx=10)
    qentry1=Entry(qFrame1,textvariable=name,justify=CENTER ,font="imapact 15",selectbackground="green")
    qentry1.pack(side=LEFT)

    qlab2 = Label(qFrame1, text="Create Password :" ,font="arial 15" ,bg="green")
    qlab2.pack(side=LEFT,padx=7)
    qentry2 = Entry(qFrame1,textvariable=password, justify=CENTER,font="imapact 15",show='*',selectbackground="green")
    qentry2.pack(side=LEFT)

    qlab3 = Label(qFrame1, text="Confirm Password :",font="arial 15", bg="blue",fg="white")
    qlab3.pack(side=LEFT, padx=7)
    qentry3 = Entry(qFrame1, textvariable=CNFpassword, justify=CENTER,font="imapact 15" ,selectbackground="green",show='*',)
    qentry3.pack(side=LEFT)
    """"""
    qFrame2 = Frame(mainFrame, bd=2, relief=SUNKEN,bg="#000040")
    qFrame2.pack(side=TOP, pady=9, padx=5)
    applab1=Label(qFrame2,text="App 1 :",font="arial 12",bg="yellow")
    applab1.pack(side=LEFT,padx=5)
    appEntry1=Entry(qFrame2,textvariable=app1, justify=CENTER,font="impact 12",selectbackground="green")
    appEntry1.pack(side=LEFT)

    apppass1 = Label(qFrame2, text="App1`password:", font="arial 12", bg="yellow")
    apppass1.pack(side=LEFT, padx=5)
    appEntry2 = Entry(qFrame2,textvariable=app1pass, justify=CENTER, font="impact 12", selectbackground="green", show='*')
    appEntry2.pack(side=LEFT)

    """"""
    qFrame3 = Frame(qFrame2, bd=2, relief=SUNKEN,pady=5,bg="#000040")
    qFrame3.pack(side=TOP, pady=9, padx=5)
    applab2 = Label(qFrame2, text="App 2 :", font="arial 12", bg="orange")
    applab2.pack(side=LEFT, padx=5)
    appEntry3 = Entry(qFrame2,textvariable=app2, justify=CENTER, font="impact 12", selectbackground="green")
    appEntry3.pack(side=LEFT)

    apppass2 = Label(qFrame2, text="App2`password:", font="arial 12", bg="orange")
    apppass2.pack(side=LEFT, padx=5)
    appEntry4 = Entry(qFrame2,textvariable=app2pass, justify=CENTER, font="impact 12", selectbackground="green", show='*')
    appEntry4.pack(side=LEFT)
    """new frame"""
    qFrame3 = Frame(mainFrame, bd=2, relief=SUNKEN,bg="#000040")
    qFrame3.pack(side=TOP, pady=9, padx=5)
    applab3 = Label(qFrame3, text="App 3 :", font="arial 12", bg="yellow")
    applab3.pack(side=LEFT, padx=5)
    appEntry5 = Entry(qFrame3,textvariable=app3, justify=CENTER, font="impact 12", selectbackground="green")
    appEntry5.pack(side=LEFT)

    apppass4 = Label(qFrame3, text="App3`password:", font="arial 12", bg="yellow")
    apppass4.pack(side=LEFT, padx=5)
    appEntry6 = Entry(qFrame3,textvariable=app3pass, justify=CENTER, font="impact 12", selectbackground="green", show='*')
    appEntry6.pack(side=LEFT)

    """"""
    qFrame4 = Frame(qFrame3, bd=2, relief=SUNKEN, pady=5)
    qFrame4.pack(side=TOP, pady=9, padx=5)
    applab5 = Label(qFrame3, text="App 4 :", font="arial 12", bg="orange")
    applab5.pack(side=LEFT, padx=5)
    appEntry7 = Entry(qFrame3,textvariable=app4, justify=CENTER, font="impact 12", selectbackground="green")
    appEntry7.pack(side=LEFT)

    apppass6 = Label(qFrame3, text="App4`password:", font="arial 12", bg="orange")
    apppass6.pack(side=LEFT, padx=5)
    appEntry8 = Entry(qFrame3,textvariable=app4pass, justify=CENTER, font="impact 12", selectbackground="green", show='*')
    appEntry8.pack(side=LEFT)

    qFrame3 = Frame(mainFrame, bd=2, relief=SUNKEN,bg="#000040")
    qFrame3.pack(side=TOP, pady=9, padx=5)
    applab3 = Label(qFrame3, text="App 5 :", font="arial 12", bg="yellow")
    applab3.pack(side=LEFT, padx=5)
    appEntry5 = Entry(qFrame3,textvariable=app5, justify=CENTER, font="impact 12", selectbackground="green")
    appEntry5.pack(side=LEFT)

    apppass4 = Label(qFrame3, text="App5`password:", font="arial 12", bg="yellow")
    apppass4.pack(side=LEFT, padx=5)
    appEntry6 = Entry(qFrame3,textvariable=app5pass, justify=CENTER, font="impact 12", selectbackground="green", show='*')
    appEntry6.pack(side=LEFT)

    """"""
    qFrame4 = Frame(qFrame3, bd=2, relief=SUNKEN, pady=5)
    qFrame4.pack(side=TOP, pady=9, padx=5)
    applab5 = Label(qFrame3, text="App 6 :", font="arial 12", bg="orange")
    applab5.pack(side=LEFT, padx=5)
    appEntry7 = Entry(qFrame3,textvariable=app6, justify=CENTER, font="impact 12", selectbackground="green")
    appEntry7.pack(side=LEFT)

    apppass6 = Label(qFrame3, text="App6`password:", font="arial 12", bg="orange")
    apppass6.pack(side=LEFT, padx=5)
    appEntry8 = Entry(qFrame3,textvariable=app6pass, justify=CENTER, font="impact 12", selectbackground="green", show='*')
    appEntry8.pack(side=LEFT)



    """"make"""

    qFrame2 = Frame(mainFrame, bd=2, relief=SUNKEN,bg="#000040")
    qFrame2.pack(side=TOP, pady=9, padx=5)
    applab1 = Label(qFrame2, text="App 7 :", font="arial 12", bg="yellow")
    applab1.pack(side=LEFT, padx=5)
    appEntry1 = Entry(qFrame2,textvariable=app7, justify=CENTER, font="impact 12", selectbackground="green")
    appEntry1.pack(side=LEFT)

    apppass1 = Label(qFrame2, text="App7`password:", font="arial 12", bg="yellow")
    apppass1.pack(side=LEFT, padx=5)
    appEntry2 = Entry(qFrame2,textvariable=app7pass, justify=CENTER, font="impact 12", selectbackground="green", show='*',)
    appEntry2.pack(side=LEFT)

    """"""
    qFrame3 = Frame(qFrame2, bd=2, relief=SUNKEN, pady=5)
    qFrame3.pack(side=TOP, pady=9, padx=5)
    applab2 = Label(qFrame2, text="App 8 :", font="arial 12", bg="orange")
    applab2.pack(side=LEFT, padx=5)
    appEntry3 = Entry(qFrame2,textvariable=app8, justify=CENTER, font="impact 12", selectbackground="green")
    appEntry3.pack(side=LEFT)

    apppass2 = Label(qFrame2, text="App8`password:", font="arial 12", bg="orange")
    apppass2.pack(side=LEFT, padx=5)
    appEntry4 = Entry(qFrame2,textvariable=app8pass, justify=CENTER, font="impact 12", selectbackground="green", show='*')
    appEntry4.pack(side=LEFT)

    """make two"""
    qFrame2 = Frame(mainFrame, bd=2, relief=SUNKEN,bg="#000040")
    qFrame2.pack(side=TOP, pady=9, padx=5)
    applab1 = Label(qFrame2, text="App 9 :", font="arial 12", bg="yellow")
    applab1.pack(side=LEFT, padx=5)
    appEntry1 = Entry(qFrame2,textvariable=app9, justify=CENTER, font="impact 12", selectbackground="green")
    appEntry1.pack(side=LEFT)

    apppass1 = Label(qFrame2, text="App9`password:", font="arial 12", bg="yellow")
    apppass1.pack(side=LEFT, padx=5)
    appEntry2 = Entry(qFrame2,textvariable=app9pass, justify=CENTER, font="impact 12", selectbackground="green", show='*')
    appEntry2.pack(side=LEFT)

    """"""
    qFrame3 = Frame(qFrame2, bd=2, relief=SUNKEN, pady=5)
    qFrame3.pack(side=TOP, pady=9, padx=5)
    applab2 = Label(qFrame2, text="App 10:", font="arial 12", bg="orange")
    applab2.pack(side=LEFT, padx=5)
    appEntry3 = Entry(qFrame2,textvariable=app10, justify=CENTER, font="impact 12", selectbackground="green")
    appEntry3.pack(side=LEFT)

    apppass2 = Label(qFrame2, text="App10`password:", font="arial 12", bg="orange")
    apppass2.pack(side=LEFT, padx=5)
    appEntry4 = Entry(qFrame2,textvariable=app10pass, justify=CENTER, font="impact 12", selectbackground="green", show='*')
    appEntry4.pack(side=LEFT)

    """make 3"""
    qFrame2 = Frame(mainFrame, bd=2, relief=SUNKEN,bg="#000040")
    qFrame2.pack(side=TOP, pady=9, padx=5)
    applab1 = Label(qFrame2, text="App 11:", font="arial 12", bg="yellow")
    applab1.pack(side=LEFT, padx=5)
    appEntry1 = Entry(qFrame2, textvariable=app11,justify=CENTER, font="impact 12", selectbackground="green")
    appEntry1.pack(side=LEFT)

    apppass1 = Label(qFrame2, text="App11`password:", font="arial 12", bg="yellow")
    apppass1.pack(side=LEFT, padx=5)
    appEntry2 = Entry(qFrame2,textvariable=app11pass, justify=CENTER, font="impact 12", selectbackground="green", show='*')
    appEntry2.pack(side=LEFT)

    """"""
    qFrame3 = Frame(qFrame2, bd=2, relief=SUNKEN, pady=5)
    qFrame3.pack(side=TOP, pady=9, padx=5)
    applab2 = Label(qFrame2, text="App 12:", font="arial 12", bg="orange")
    applab2.pack(side=LEFT, padx=5)
    appEntry3 = Entry(qFrame2,textvariable=app12, justify=CENTER, font="impact 12", selectbackground="green")
    appEntry3.pack(side=LEFT)

    apppass2 = Label(qFrame2, text="App12`password:", font="arial 12", bg="orange")
    apppass2.pack(side=LEFT, padx=5)
    appEntry4 = Entry(qFrame2,textvariable=app12pass, justify=CENTER, font="impact 12", selectbackground="green", show='*')
    appEntry4.pack(side=LEFT)

    """for the text area"""
    textFrame=Frame(mainFrame)
    textFrame.pack(side=TOP)

    Label(textFrame,text="Important Notes").pack(side=TOP)

    text=Text(textFrame,width="140",height="10",wrap=WORD,insertofftime=100,insertontime=100,
              insertbackground="red",font="times 13")
    text.pack(side=LEFT,fill=X)

    """buttons for submit and asking email for the recovery password"""

    lastFrame=Frame(mainFrame,bg="#000040")
    lastFrame.pack(side=TOP,pady=5)

    qlab1 = Label(lastFrame, text="Email :", font="arial 15", bg="red")
    qlab1.pack(side=LEFT, padx=10)
    qentry1 = Entry(lastFrame,textvariable=email, justify=CENTER, font="arial 15", selectbackground="green")
    qentry1.pack(side=LEFT,anchor=E,padx=5)

    Button(lastFrame,text="Submit Data",width=20,bg="green" ,font="arial 15",fg="white"
           ,command=lambda :Confirmation(name.get(),password.get(),CNFpassword.get(),email.get(),app1.get(),app1pass.get(),app2.get(),app2pass.get(),
                                         app3.get(),app3pass.get(),app4.get(),app4pass.get(),app5.get(),app5pass.get()
                                         ,app6.get(),app6pass.get(),app7.get(),app7pass.get(),app8.get(),app8pass.get(),
                                         app9.get(),app9pass.get(),app10.get(),app10pass.get(),app11.get(),app11pass.get(),app12.get(),app12pass.get(),text.get(1.0,END))).pack(side=LEFT,padx=5)
    Button(lastFrame,text="Exit",width=20,bg="red",command=quitit,font="arial 15").pack(side=LEFT,padx=5)








    form.mainloop()
# basic gui coding, the execution of code will start from here
root =Tk()

root.iconbitmap('icons\\trust.ico')
root.title("Trust me ")
# root.config(bg="#000040")
root.geometry("1000x600")
root.minsize(550,500)
      
# menubar
__mainmenu =Menu(root)
menuFirst =Menu(__mainmenu,tearoff=0)
menuFirst.add_command(label="New Users",command=NewRegistration)
menuFirst.add_command(label="Existing User")
menuFirst.add_command(label="Change Theme",command=changingColor)
menuFirst.add_command(label="Feedback",activebackground="#090",command=feedback)

__mainmenu.add_cascade(label="Users",menu=menuFirst)
__mainmenu.add_cascade(label="Backup")
__mainmenu.add_cascade(label="About",command=about)
__mainmenu.add_cascade(label="Exit",command=quit)
root.config(menu =__mainmenu)

"""menu`s coding done"""

"""side frame"""
imgFram=Image.open("images\\imgUser.png")
imginsertFrame=ImageTk.PhotoImage(imgFram)

f2=Frame(root,width=50)
f2.pack(side=LEFT,anchor=W,fill=Y)
picFrame=Label(f2,image=imginsertFrame)
picFrame.pack(side=TOP,pady=5)
b3=Button(f2,text="BACKUP",bd=2,relief=SUNKEN,padx=3,pady=4,command=exit)
b3.pack(side=TOP,fill=X)
b4=Button(f2,text="RESTORE",bd=2,relief=SUNKEN,padx=3,pady=4)
b4.pack(side=TOP,fill=X)
b5=Button(f2,text="HELP",bd=2,relief=SUNKEN,padx=3,pady=4,command=help)
b5.pack(side=TOP,fill=X)
b4=Button(f2,text="Exit",bd=2,relief=SUNKEN,padx=3,pady=4,command=quit)
b4.pack(side=TOP,fill=X)

"""Label For the trust me app"""
trust =Label(root,text="Trust Me",bd=0,relief=GROOVE,font="times 36 underline")
trust.pack(padx=10,pady=10,anchor=CENTER)

"""Now importing image for the gui"""
img =Image.open("images\\glowing.png")
insertImg =ImageTk.PhotoImage(img)
pic=Label(root,image=insertImg)
pic.pack(padx=10,anchor=N)

"""frame for side view"""


"""image for buttons"""
login =Image.open("images\\login.jpg")
user=Image.open("images\\user.jpg")

loginInser=ImageTk.PhotoImage(login)
userInsert=ImageTk.PhotoImage(user)

"""now buttons will be added here"""
f1=Frame(root,)
f1.pack(padx=5,pady=5,anchor=N,side=TOP)

b1=Button(f1,image=userInsert ,width="300" ,height="80" ,padx=8,command=NewRegistration)
b1.pack(side=LEFT,fill=X,padx=20)
b2=Button(f1,image=loginInser ,width="300" ,height="80",padx=8)
b2.pack(side=LEFT,fill=X,padx=20)
"""End button coding"""



root.mainloop()
