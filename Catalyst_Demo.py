from tkinter import *
import random

class Catalyst_Demo :

    def __init__(self):
        print("hello");

    def type(self):
        print("yay")


    def WelcomeScreen(self):
        self.WindowWelcome = Tk();
        self.WindowWelcome.title("Security Menu");
        #self.WindowWelcomeattributes('-fullscreen', True);
        #w,h = self.WindowWelcome.winfo_screenwidth(), self.WindowWelcome.winfo_screenheight()
        self.WindowWelcome.geometry("1920x1080");
        self.WindowWelcome.state('zoomed');
        photoImage = PhotoImage(file="CatalystV2 Files/Bg (1).png",master=self.WindowWelcome);

        self.canvasWelcome = Canvas(self.WindowWelcome, height=1080, width=1920);
        self.canvasWelcome.create_image(0,0,image=photoImage, anchor=NW);
        self.canvasWelcome.place(relx=0, rely=0);

        self.Button= Button(self.WindowWelcome,width="15", height="5", borderwidth=0, command=self.type);
        self.Button.place(relx="0.265", rely="0.735");

        self.WindowWelcome.mainloop();


CatObj = Catalyst_Demo();
CatObj.WelcomeScreen();




