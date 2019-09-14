# Graphical User Interface a.k.a GUI - Quiz.
from tkinter import *
from PIL import ImageTk, Image
import webbrowser
import tkinter.messagebox
import random

ok = Tk()
ok.geometry("960x540+0+0")  # or 1440x810
ok.title("Random Quiz Generator")
# ok.config(bg="#212030") # maybe some other day. maybe not.
ok.resizable(0, 0)

# doing this makes a whole lotta convenient to do stuff.
ff_bold = ("Trebuchet MS", 32, "bold")
ff_normal = ("Trebuchet MS", 12)
ff_nor = ("Trebuchet MS", 11)
color_base = "#494f5c"  # Slate Grey, looks sax af.
color_01 = "#c6cddb"  # Light Slate Grey
color_02 = "#838c98"  # Somewhat Light Slate Grey
color_03 = "#b3bbc9"  # Steel Blue
color_high = "#dadbde"  # more light, not a fan of. still.


def home():
    frame1 = Frame(ok, width=960, height=540)
    frame1.pack()
    # frame1.config(bg=color_base)
    bg_photo = ImageTk.PhotoImage(Image.open("quiz_bg.jpg"))
    Label(frame1, image=bg_photo, width=960, height=540).pack()
    Label(frame1, text="a python project by", font=ff_normal, bg=color_base, fg=color_01).place(x=150, y=75)
    Label(frame1, text="ARSHIT PALIWAL", font=("Trebuchet MS", 24), bg=color_base, fg=color_01).place(x=150, y=105)
    Label(frame1, text="© 2019 Arshit Paliwal (arshitpaliwal)", font=("Trebuchet MS", 8), bg=color_base, fg=color_02).place(x=395, y=500)
    Button(frame1, text="Login", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: login(frame1, usr_entry, pass_entry)).place(x=200, y=400)
    Button(frame1, text="Sign Up", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03).place(x=310, y=400)  # will do this some other day, probably.
    Button(frame1, text="exit", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: exit_fun()).place(x=810, y=460)
    Button(frame1, text="about", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: about(frame1)).place(x=720, y=50)
    Button(frame1, text="contact", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: contact(frame1)).place(x=785, y=50)

    Label(frame1, text="Username: ", font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=307.5)
    Label(frame1, text="Password: ", font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=347.5)
    usr_entry = Entry(frame1, font=ff_nor, bg=color_base, fg=color_high)  # username entry
    pass_entry = Entry(frame1, show='*', font=ff_nor, bg=color_base, fg=color_high)  # password entry
    usr_entry.place(x=250, y=310.5)
    pass_entry.place(x=250, y=348.5)

    def exit_fun():
        exit_f = tkinter.messagebox.askyesno("ok", "Like seriously?")
        if exit_f > 0:
            ok.destroy()
            return

    frame1.mainloop()


def about(frame1):
    frame1.destroy()
    frame2 = Frame(ok, width=960, height=540)
    frame2.config(bg=color_base)
    frame2.pack()
    Label(frame2, text="About", font=ff_bold, bg=color_base, fg=color_01).place(x=150, y=75)
    Label(frame2, text="Welcome here!", font=ff_normal, bg=color_base, fg=color_01).place(x=150, y=150)
    Label(frame2, text="This about page is currently WIP and will be completed soon™.", font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=187.5)
    Label(frame2, text="© 2019 Arshit Paliwal ", font=("Trebuchet MS", 8), bg=color_base, fg=color_02).place(x=395, y=500)
    Button(frame2, text="back", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: back_f()).place(x=810, y=460)

    def back_f():  # about section's back func
        frame2.destroy()
        home()

    frame2.mainloop()


def contact(frame1):
    frame1.destroy()
    frame3 = Frame(ok, width=960, height=540)
    frame3.config(bg=color_base)
    frame3.pack()
    Label(frame3, text="Contact", font=("Trebuchet MS", 36, "bold"), bg=color_base, fg=color_01).place(x=390, y=200)
    global icon_01, icon_02, icon_03, icon_04, icon_05
    icon_01 = ImageTk.PhotoImage(Image.open("icon_01.jpg"))
    icon_02 = ImageTk.PhotoImage(Image.open("icon_02.jpg"))
    icon_03 = ImageTk.PhotoImage(Image.open("icon_03.jpg"))
    icon_04 = ImageTk.PhotoImage(Image.open("icon_04.jpg"))
    icon_05 = ImageTk.PhotoImage(Image.open("icon_05.jpg"))
#    Label(frame3, image=icon_01, width=50, height=50, bg=color_base).place(x=355, y=280)
#    Label(frame3, image=icon_02, width=50, height=50, bg=color_base).place(x=405, y=280)
#    Label(frame3, image=icon_03, width=50, height=50, bg=color_base).place(x=455, y=280)  # better to comment out rather than removing.
#    Label(frame3, image=icon_04, width=50, height=50, bg=color_base).place(x=505, y=280)
#    Label(frame3, image=icon_05, width=50, height=50, bg=color_base).place(x=555, y=280)
    Button(frame3, image=icon_01, bd=0, highlightthickness=0, bg=color_base, fg=color_high, command=lambda: callback("mailto:arshitpaliwal9@mail.com")).place(x=355, y=280)
    Button(frame3, image=icon_02, bd=0, highlightthickness=0, bg=color_base, fg=color_high, command=lambda: callback("https://www.facebook.com/profile.php?id=100006403455611")).place(x=405, y=280)
    Button(frame3, image=icon_03, bd=0, highlightthickness=0, bg=color_base, fg=color_high, command=lambda: callback("https://twitter.com/arshitpaliwal9")).place(x=455, y=280)
    Button(frame3, image=icon_04, bd=0, highlightthickness=0, bg=color_base, fg=color_high, command=lambda: callback("https://t.me/arshitpaliwal")).place(x=505, y=280)
    Button(frame3, image=icon_05, bd=0, highlightthickness=0, bg=color_base, fg=color_high, command=lambda: callback("https://github.com/paliwalarshit")).place(x=555, y=280)

    Label(frame3, text="© 2019 Arshit Paliwal ", font=("Trebuchet MS", 8), bg=color_base, fg=color_02).place(x=395, y=500)
    Button(frame3, text="back", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: back_f()).place(x=810, y=460)

    def callback(url):
        webbrowser.open_new(url)

    def back_f():  # contact section's back func
        frame3.destroy()
        home()


def login(frame1, usr_entry, pass_entry):
    username = "123"  # that's the given username
    password = "123"  # that's the given password
    usr2 = "arshitpaliwal9"  # that's the given username
    pass2 = "9660610881"  # that's the given password
    if username == usr_entry.get() and password == pass_entry.get() or usr2 == usr_entry.get() and pass2 == pass_entry.get():
        print("Wow, Access granted.")
        frame1.destroy()
        frame4 = Frame(ok, width=960, height=540)
        frame4.config(bg=color_base)
        frame4.pack()
        Label(frame4, text="Hey", font=ff_bold, bg=color_base, fg=color_01).place(x=150, y=75)
        Label(frame4, text="Welcome here!", font=ff_normal, bg=color_base, fg=color_01).place(x=150, y=150)
        Label(frame4, text="Start quiz?", font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=460)
        Button(frame4, text="Yes", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_high, command=lambda: yes()).place(x=230, y=460)
        Button(frame4, text="exit", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: exit_fun()).place(x=810, y=460)
        ran = random.randrange(1, 6)

        if ran == 1:
            file = open("ques_set_001.txt", 'r')
            f = file.readlines()
            topic = "Basic CS Stuff"
        elif ran == 2:
            file = open("ques_set_002.txt", 'r')
            f = file.readlines()
            topic = "Computer Science : Linux"
        elif ran == 3:
            file = open("ques_set_003.txt", 'r')
            f = file.readlines()
            topic = "Basic General Knowledge"
        elif ran == 4:
            file = open("ques_set_004.txt", 'r')
            f = file.readlines()
            topic = "General Science"
        elif ran == 5:
            file = open("ques_set_005.txt", 'r')
            f = file.readlines()
            topic = "National - Latest Current Affairs"
        else:
            file = open("ques_set_006.txt", 'r')
            f = file.readlines()
            topic = "Technology - Latest Current Affairs"

        Label(frame4, text="Topic :: " + str(topic), font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=200)
        Label(frame4, text="Instructions:", font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=275)
        Label(frame4, text="Total number of questions : 10", font=("Trebuchet MS", 10), bg=color_base, fg=color_01).place(x=150, y=315)
        Label(frame4, text="Time allotted : 5 minutes", font=("Trebuchet MS", 10), bg=color_base, fg=color_01).place(x=150, y=350)  # for some other day
        Label(frame4, text="Each question carry 1 mark, no negative marks.", font=("Trebuchet MS", 10), bg=color_base, fg=color_01).place(x=150, y=385)

        def exit_fun():
            exit_f = tkinter.messagebox.askyesno("ok", "Like seriously?")
            if exit_f > 0:
                ok.destroy()
                return
            frame4.mainloop()

        def yes():
            frame4.destroy()
            frame5 = Frame(ok, width=960, height=540)
            frame5.config(bg=color_base)
            frame5.pack()
            global d1
            d1 = IntVar()
            Label(text=f[1], font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=75)
            Radiobutton(text=f[2], font=ff_nor, bg=color_base, fg="#EC979A", variable=d1, value=1).place(x=150, y=175)
            r2 = Radiobutton(text=f[3],  font=ff_nor, bg=color_base, fg="#EC979A", variable=d1, value=2)
            r2.place(x=150, y=225)
            Radiobutton(text=f[4], font=ff_nor, bg=color_base, fg="#EC979A", variable=d1, value=3).place(x=150, y=275)
            Radiobutton(text=f[5], font=ff_nor, bg=color_base, fg="#EC979A", variable=d1, value=4).place(x=150, y=325)
            Button(frame5, text="Next", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: nxt(frame5)).place(x=810, y=460)
            frame5.mainloop()

        def nxt(frame5):
            frame5.destroy()
            frame8 = Frame(ok, width=960, height=540)
            frame8.config(bg=color_base)
            frame8.pack()
            global d2
            d2 = IntVar()
            Label(text=f[7], font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=75)
            Radiobutton(text=f[8], font=ff_nor, bg=color_base, fg="#EC979A", variable=d2, value=1).place(x=150, y=175)
            Radiobutton(text=f[9], font=ff_nor, bg=color_base, fg="#EC979A", variable=d2, value=2).place(x=150, y=225)
            Radiobutton(text=f[10], font=ff_nor, bg=color_base, fg="#EC979A", variable=d2, value=3).place(x=150, y=275)
            Radiobutton(text=f[11], font=ff_nor, bg=color_base, fg="#EC979A", variable=d2, value=4).place(x=150, y=325)
            Button(frame8, text="Next", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: nxt2(frame8)).place(x=810, y=460)
            frame8.mainloop()

        def nxt2(frame8):
            frame8.destroy()
            frame9 = Frame(ok, width=960, height=540)
            frame9.config(bg=color_base)
            frame9.pack()
            global d3
            d3 = IntVar()
            Label(text=f[13], font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=75)
            Radiobutton(text=f[14], font=ff_nor, bg=color_base, fg="#EC979A", variable=d3, value=1).place(x=150, y=175)
            Radiobutton(text=f[15],  font=ff_nor, bg=color_base, fg="#EC979A", variable=d3, value=2).place(x=150, y=225)
            Radiobutton(text=f[16], font=ff_nor, bg=color_base, fg="#EC979A", variable=d3, value=3).place(x=150, y=275)
            Radiobutton(text=f[17], font=ff_nor, bg=color_base, fg="#EC979A", variable=d3, value=4).place(x=150, y=325)
            Button(frame9, text="Next", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: nxt3(frame9)).place(x=810, y=460)
            frame9.mainloop()

        def nxt3(frame9):
            frame9.destroy()
            frame10 = Frame(ok, width=960, height=540)
            frame10.config(bg=color_base)
            frame10.pack()
            global d4
            d4 = IntVar()
            Label(text=f[19], font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=75)
            Radiobutton(text=f[20], font=ff_nor, bg=color_base, fg="#EC979A", variable=d4, value=1).place(x=150, y=175)
            Radiobutton(text=f[21], font=ff_nor, bg=color_base, fg="#EC979A", variable=d4, value=2).place(x=150, y=225)
            Radiobutton(text=f[22], font=ff_nor, bg=color_base, fg="#EC979A", variable=d4, value=3).place(x=150, y=275)
            Radiobutton(text=f[23], font=ff_nor, bg=color_base, fg="#EC979A", variable=d4, value=4).place(x=150, y=325)
            Button(frame10, text="Next", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: nxt4(frame10)).place(x=810, y=460)
            frame10.mainloop()

        def nxt4(frame10):
            frame10.destroy()
            frame11 = Frame(ok, width=960, height=540)
            frame11.config(bg=color_base)
            frame11.pack()
            global d5
            d5 = IntVar()
            Label(text=f[25], font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=75)
            Radiobutton(text=f[26], font=ff_nor, bg=color_base, fg="#EC979A", variable=d5, value=1).place(x=150, y=175)
            Radiobutton(text=f[27], font=ff_nor, bg=color_base, fg="#EC979A", variable=d5, value=2).place(x=150, y=225)
            Radiobutton(text=f[28], font=ff_nor, bg=color_base, fg="#EC979A", variable=d5, value=3).place(x=150, y=275)
            Radiobutton(text=f[29], font=ff_nor, bg=color_base, fg="#EC979A", variable=d5, value=4).place(x=150, y=325)
            Button(frame11, text="Next", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: nxt5(frame11)).place(x=810, y=460)
            frame11.mainloop()

        def nxt5(frame11):
            frame11.destroy()
            frame12 = Frame(ok, width=960, height=540)
            frame12.config(bg=color_base)
            frame12.pack()
            global d6
            d6 = IntVar()
            Label(text=f[31], font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=75)
            Radiobutton(text=f[32], font=ff_nor, bg=color_base, fg="#EC979A", variable=d6, value=1).place(x=150, y=175)
            Radiobutton(text=f[33],  font=ff_nor, bg=color_base, fg="#EC979A", variable=d6, value=2).place(x=150, y=225)
            Radiobutton(text=f[34], font=ff_nor, bg=color_base, fg="#EC979A", variable=d6, value=3).place(x=150, y=275)
            Radiobutton(text=f[35], font=ff_nor, bg=color_base, fg="#EC979A", variable=d6, value=4).place(x=150, y=325)
            Button(frame12, text="Next", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: nxt6(frame12)).place(x=810, y=460)
            frame12.mainloop()

        def nxt6(frame12):
            frame12.destroy()
            frame13 = Frame(ok, width=960, height=540)
            frame13.config(bg=color_base)
            frame13.pack()
            global d7
            d7 = IntVar()
            Label(text=f[37], font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=75)
            Radiobutton(text=f[38], font=ff_nor, bg=color_base, fg="#EC979A", variable=d7, value=1).place(x=150, y=175)
            Radiobutton(text=f[39], font=ff_nor, bg=color_base, fg="#EC979A", variable=d7, value=2).place(x=150, y=225)
            Radiobutton(text=f[40], font=ff_nor, bg=color_base, fg="#EC979A", variable=d7, value=3).place(x=150, y=275)
            Radiobutton(text=f[41], font=ff_nor, bg=color_base, fg="#EC979A", variable=d7, value=4).place(x=150, y=325)
            Button(frame13, text="Next", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: nxt7(frame13)).place(x=810, y=460)
            frame13.mainloop()

        def nxt7(frame13):
            frame13.destroy()
            frame14 = Frame(ok, width=960, height=540)
            frame14.config(bg=color_base)
            frame14.pack()
            global d8
            d8 = IntVar()
            Label(text=f[43], font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=75)
            Radiobutton(text=f[44], font=ff_nor, bg=color_base, fg="#EC979A", variable=d8, value=1).place(x=150, y=175)
            Radiobutton(text=f[45],  font=ff_nor, bg=color_base, fg="#EC979A", variable=d8, value=2).place(x=150, y=225)
            Radiobutton(text=f[46], font=ff_nor, bg=color_base, fg="#EC979A", variable=d8, value=3).place(x=150, y=275)
            Radiobutton(text=f[47], font=ff_nor, bg=color_base, fg="#EC979A", variable=d8, value=4).place(x=150, y=325)
            Button(frame14, text="Next", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: nxt8(frame14)).place(x=810, y=460)
            frame14.mainloop()

        def nxt8(frame14):
            frame14.destroy()
            frame15 = Frame(ok, width=960, height=540)
            frame15.config(bg=color_base)
            frame15.pack()
            global d9
            d9 = IntVar()
            Label(text=f[49], font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=75)
            Radiobutton(text=f[50], font=ff_nor, bg=color_base, fg="#EC979A", variable=d9, value=1).place(x=150, y=175)
            Radiobutton(text=f[51], font=ff_nor, bg=color_base, fg="#EC979A", variable=d9, value=2).place(x=150, y=225)
            Radiobutton(text=f[52], font=ff_nor, bg=color_base, fg="#EC979A", variable=d9, value=3).place(x=150, y=275)
            Radiobutton(text=f[53], font=ff_nor, bg=color_base, fg="#EC979A", variable=d9, value=4).place(x=150, y=325)
            Button(frame15, text="Next", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: nxt_last(frame15)).place(x=810, y=460)
            frame15.mainloop()

        def nxt_last(frame15):
            frame15.destroy()
            frame6 = Frame(ok, width=960, height=540)
            frame6.config(bg=color_base)
            frame6.pack()
            global d10
            d10 = IntVar()
            Label(text=f[55], font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=75)
            Radiobutton(text=f[56], font=ff_nor, bg=color_base, fg="#EC979A", variable=d10, value=1).place(x=150, y=175)
            Radiobutton(text=f[57], font=ff_nor, bg=color_base, fg="#EC979A", variable=d10, value=2).place(x=150, y=225)
            Radiobutton(text=f[58], font=ff_nor, bg=color_base, fg="#EC979A", variable=d10, value=3).place(x=150, y=275)
            Radiobutton(text=f[59], font=ff_nor, bg=color_base, fg="#EC979A", variable=d10, value=4).place(x=150, y=325)
            Button(frame6, text="Next", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: submit(frame6)).place(x=810, y=460)
            frame6.mainloop()

        def submit(frame6):
            frame6.destroy()
            frame7 = Frame(ok, width=960, height=540)
            frame7.config(bg=color_base)
            frame7.pack()
            Button(frame7, text="exit", bd=0, highlightthickness=0, font=ff_nor, bg=color_base, fg=color_03, command=lambda: exit_f()).place(x=810, y=460)
            Label(frame7, text="Stay Alive, Stay Connected.", font=("Trebuchet MS", 9), bg=color_base, fg=color_02).place(x=402, y=500)

            tot = 0
            if d1.get() == int(f[6]):
                tot += 1
            if d2.get() == int(f[12]):
                tot += 1
            if d3.get() == int(f[18]):
                tot += 1
            if d4.get() == int(f[24]):
                tot += 1
            if d5.get() == int(f[30]):
                tot += 1
            if d6.get() == int(f[36]):
                tot += 1
            if d7.get() == int(f[42]):
                tot += 1
            if d8.get() == int(f[48]):
                tot += 1
            if d9.get() == int(f[54]):
                tot += 1
            if d10.get() == int(f[60]):
                tot += 1
            # print("Total no. of correct ans:", tot)
            Label(frame7, text="Result", font=ff_bold, bg=color_base, fg=color_01).place(x=150, y=75)
            Label(frame7, text="Thank you for answering the questions.", font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=150)
            Label(frame7, text=str(tot) + " of 10 questions answered right.", font=ff_nor, bg=color_base, fg=color_01).place(x=150, y=200)
            # Label(frame7, text=tot, font=ff_nor, bg=color_base, fg=color_01).place(x=383, y=200)
            if tot <= 4:
                Label(frame7, text="You failed, better luck next time. ", font=ff_nor, bg=color_base, fg=color_01).place(x=365, y=337)
            else:
                Label(frame7, text="    Well done, You have passed.    ", font=ff_nor, bg=color_base, fg=color_01).place(x=365, y=337)

            def exit_f():
                ok.destroy()
                return

            file.close()
            frame7.mainloop()

    else:
        tkinter.messagebox.showwarning("// Authentication error //", "Entered detail(s) didn't matched, try again!")
        # Label(frame1, text="Wrong, try again", font=ff_10, bg=color_base, fg=color_high).place(x=565, y=327)
        #  print("Wrong, try again")


home()
