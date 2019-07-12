from tkinter import *
from winsound import *

from matplotlib import *
import csv
import tweepy
import time

#tweepy, textblob, matplotlib, speechRecognition, pyaudio
#py -m pip install xxx

try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen

class SentimentApp:
    Selection = 0;
    VerifiedUser = 0;
    GraphSelection1 = 0;
    VRS_Scan = 0


    def __init__(self):
        print("hello");
        self.tweets = [];
        self.tweetText = [];

    def LoginMenu(self):
        import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);
        self.LoginWindow = Tk();
        self.LoginWindow.title("Security Menu");
        self.LoginWindow.geometry("600x600");
        photoImage = PhotoImage(file=" ");
        BgImage = Label(self.LoginWindow, image=photoImage);BgImage.pack();
        LabelUsername = Label(self.LoginWindow, text="Username", bg="#050529",fg = "#15AFAD",font=("Agency FB bold", 14), width="15", height="1");
        LabelUsername.place(relx="0.135", rely="0.419");
        LabelPassword = Label(self.LoginWindow, text="Password", bg="#050529", fg="#15AFAD", font=("Agency FB bold", 14),width="15", height="1");
        LabelPassword.place(relx="0.135", rely="0.489");
        self.TextUsername = StringVar();
        EntryUsername = Entry(self.LoginWindow, textvariable=self.TextUsername, bg="#15AFAD",fg = "#050529",font=("Agency FB bold", 13), width="25");
        EntryUsername.place(relx="0.331", rely="0.419");
        self.TextPassword = StringVar();
        EntryPassword = Entry(self.LoginWindow, textvariable=self.TextPassword, bg="#15AFAD",show="•", fg="#050529", font=("Agency FB bold", 13), width="25");
        EntryPassword.place(relx="0.331", rely="0.489");
        ButtonLogin = Button(self.LoginWindow, text="Login", bg="#050529",fg = "#15AFAD",font=("Agency FB bold", 13), width="10", command=self.LoginCheck);
        ButtonLogin.place(relx="0.455", rely="0.555");
        RefreshButton = Button(self.LoginWindow, text=" ♦ ",bg="#050529",fg = "#15AFAD",command=self.SoundEffect1); RefreshButton.place(relx="0.005", rely="0.005");
        self.LoginWindow.mainloop();

    def LoginCheck(self):
        import winsound;
        winsound.PlaySound('', winsound.SND_ASYNC);
        username = self.TextUsername.get();
        password = self.TextPassword.get();
        print(username);
        print(password);
        if (username=="a" and password=="1"):
            global VerifiedUser;
            VerifiedUser=1;
            self.LoginWindow.destroy();
        else :
            LoginError = Tk();
            LoginError.title("Login Error");
            LoginError.geometry("500x500");
            photoImage1 = PhotoImage(file="Error.png", master=LoginError);
            BgImage1 = Label(LoginError, image=photoImage1);
            BgImage1.pack();
            LabelLoginError = Label(LoginError, text="Verification Failed!", bg="#EECA00", fg="#050529",font=("Agency FB bold", 25), width="15", height="1");
            LabelLoginError.place(relx="0.36", rely="0.453");
            DestroyButton = Button(LoginError, text=" X ", bg="#EECA00", fg="#BF4300", command=LoginError.destroy);
            DestroyButton.place(relx="0.95", rely="0.005");
            LoginError.mainloop();

    def SoundEffect1(self): #DUMMY FUNCTION
        import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);

    def MainMenu(self): #MENU WITH ALL OPTIONS
        
        self.MainMenuWindow = Tk();
        self.MainMenuWindow.title("Sentiment Analysis Menu");
        self.MainMenuWindow.geometry("600x600");
        photoImage = PhotoImage(file="#8.png", master=self.MainMenuWindow);
        BgImage = Label(self.MainMenuWindow, image=photoImage);
        BgImage.pack();
        
        ImgButton0 = PhotoImage(file="btn#2.png");
        ImgButton1 = PhotoImage(file="btn#1.png");
        ButtonQuitApp = Button(self.MainMenuWindow, image=ImgButton0, command=quit);
        ButtonQuitApp["bg"] = "#0089D8";
        ButtonQuitApp["border"] = "0";
        ButtonQuitApp.place(relx="0.0335", rely="0.028");
        ButtonSelection1 = Button(self.MainMenuWindow, image=ImgButton1, command=self.AnalyzeSentenceAction);
        ButtonSelection1["bg"] = "#0089D8"; ButtonSelection1["border"]="0";
        ButtonSelection1.place(relx="0.0655", rely="0.848");
        ButtonSelection2 = Button(self.MainMenuWindow, image=ImgButton1, command=self.AnalyzeTwitterAction);####
        ButtonSelection2["bg"] = "#0089D8"; ButtonSelection2["border"]="0";
        ButtonSelection2.place(relx="0.3355", rely="0.848");
        ButtonSelection3 = Button(self.MainMenuWindow, image=ImgButton1, command=self.AnalyzeVRSAction);####
        ButtonSelection3["bg"] = "#0089D8"; ButtonSelection3["border"]="0";
        ButtonSelection3.place(relx="0.5855", rely="0.848");
       
        self.MainMenuWindow.mainloop();

    def AnalyzeSentenceAction(self): #OPTION #1 SELECTED IN MENU
         import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);
        global Selection;
        Selection=1;print("Selection = ");print(Selection);
        self.MainMenuWindow.destroy();
        
    def AnalyzeTwitterAction(self): #OPTION #2 SELECTED IN MENU
         import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);
        global Selection;
        Selection = 2;
        print("Selection = ");
        print(Selection);
        self.MainMenuWindow.destroy();

        

    def AnalyzeVRSAction(self): #OPTION #3 SELECTED IN MENU
         import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);global Selection;
        Selection = 3;
        print("Selection = ");
        print(Selection);
        self.MainMenuWindow.destroy();
        
    def AnalyzeSingleSentence(self): #SET OR DRIVER INPUT WINDOW
          import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);
        self.AnalyzeSingleSentenceWindow = Tk();
        self.AnalyzeSingleSentenceWindow.title("Sentence Analysis");
        self.AnalyzeSingleSentenceWindow.geometry("500x300");photoImages = PhotoImage(file="#5.png", master=self.AnalyzeSingleSentenceWindow);
        BgImages = Label(self.AnalyzeSingleSentenceWindow, image=photoImages);
        BgImages.pack();
        self.LabelAnalyzeSingleSentence = Label(self.AnalyzeSingleSentenceWindow,text="Write a Sentence or a Word for Lexicon Analysis :", bg="#050529",fg = "#15AFAD",font=("Agency FB bold", 20), width="45", height="1");
        self.LabelAnalyzeSingleSentence.place(relx="0.0325", rely="0.335");
        self.TextSentence = StringVar();
        self.EntrySentence = Entry(self.AnalyzeSingleSentenceWindow,textvariable=self.TextSentence, bg="#15AFAD",fg = "#050529",font=("Agency FB bold", 20),width="38");
        self.EntrySentence.place(relx="0.0325", rely="0.535");
        self.ButtonAnalysisSentence = Button(self.AnalyzeSingleSentenceWindow, text="Analyze", bg="#050529",fg = "#15AFAD",font=("Agency FB bold", 17), width="10", command=self.AnalyzeSentenceProcess);
        self.ButtonAnalysisSentence.place(relx="0.265", rely="0.735");
        self.ButtonMenu = Button(self.AnalyzeSingleSentenceWindow, text="Main menu", bg="#050529",fg="#15AFAD", font=("Agency FB bold", 17), width="10",command=self.ActivateMenu);
        self.ButtonMenu.place(relx="0.515", rely="0.735");
        self.AnalyzeSingleSentenceWindow.mainloop()
        
    def ActivateMenu(self):
        
    def ActivateMenu2(self):
        import winsound;
        winsound.PlaySound(' ', winsound.SND_ASYNC);self.AnalysisTwitterWindow.destroy();

    def AnalyzeSentenceProcess(self):   #GET OR RECIVER OUTPUT WINDOW
     
    
    def AnalysisGraphSelection1(self):
      

    def AnalysisViewHistory(self):
       ;

    def AnalyzeTwitterPosts(self):
       
        consumerKey = "e5QiuLWa3mJyricV2tYZh7L4D"
        consumerSecret = "d4cmR54P50QePxHR4SZcESYNk9g0D0ZElvwI3PKurbIn1xUgwg"
        accessToken = "1092337126773932034-SPqlH0oeldiBaaYmHSQaSGSbLzlcFB"
        accessTokenSecret = "JqRFzQ4voZIgz0pWA0SBomGr7zhYbzH9ItsfnLf073U56"
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)
        self.tweets = api.user_timeline();
      

    def ViewAllTweets(self):
       

    def AnalyzeVRSSystem(self):
        ;

    def ActivateVRSSystem(self):
       ;

    def InititateVRSProcess(self):
       
