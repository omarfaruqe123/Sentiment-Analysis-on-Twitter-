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
        photoImage = PhotoImage(file="#2.png");
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
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);
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
        #print("Well done");
        self.MainMenuWindow = Tk();
        self.MainMenuWindow.title("Sentiment Analysis Menu");
        self.MainMenuWindow.geometry("600x600");
        photoImage = PhotoImage(file="#8.png", master=self.MainMenuWindow);
        BgImage = Label(self.MainMenuWindow, image=photoImage);
        BgImage.pack();
        #LabelWelcome = Label(self.MainMenuWindow, text="Sentiment Analysis System", bg="#7c0000", fg="#00d2f7",font=("Agency FB bold", 25), width="48", height="1");
        #LabelWelcome.place(relx="0.005", rely="0.115");
        #LabelAnalysisBySentence = Label(self.MainMenuWindow, text="Analyze A Single Sentence", bg="#7c0000", fg="#00d2f7",font=("Agency FB bold", 25), width="25", height="1");
        #LabelAnalysisBySentence.place(relx="0.055", rely="0.315");
        #LabelAnalysisTwitterPostA = Label(self.MainMenuWindow, text="Analyze All Tweets (User A)", bg="#7c0000",fg="#00d2f7", font=("Agency FB bold", 25), width="25", height="1");
        #LabelAnalysisTwitterPostA.place(relx="0.055", rely="0.415");
        #LabelAnalysisTwitterPostB = Label(self.MainMenuWindow, text="Analyze All Tweets (User B)", bg="#7c0000",fg="#00d2f7", font=("Agency FB bold", 25), width="25", height="1");
        #LabelAnalysisTwitterPostB.place(relx="0.055", rely="0.515");
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
        #ButtonSelection1 = Button(self.MainMenuWindow, image=ImgButton1, command=self.AnalyzeSentenceAction);
        #ButtonSelection1["bg"] = "#7c0000"; ButtonSelection1["border"]="0";
        #ButtonSelection1.place(relx="0.0005", rely="0.315");
        #ButtonSelection2 = Button(self.MainMenuWindow, image=ImgButton1);  # command required
        #ButtonSelection2["bg"] = "#7c0000";
        #ButtonSelection2["border"] = "0";
        #ButtonSelection2.place(relx="0.0005", rely="0.415");
        #ButtonSelection3 = Button(self.MainMenuWindow, image=ImgButton1);  # command required
        #ButtonSelection3["bg"] = "#7c0000";
        #ButtonSelection3["border"] = "0";
        #ButtonSelection3.place(relx="0.0005", rely="0.515");
        #ButtonSelection0 = Button(self.MainMenuWindow, image=ImgButton1, command=self.AnalysisViewHistory);
        #ButtonSelection0["bg"] = "#7c0000";
        #ButtonSelection0["border"] = "0";
        #ButtonSelection0.place(relx="0.0005", rely="0.815");
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
        self.AnalyzeSingleSentenceWindow.mainloop();

    def ActivateMenu(self):
        import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);self.AnalyzeSingleSentenceWindow.destroy();

    def ActivateMenu2(self):
        import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);self.AnalysisTwitterWindow.destroy();

    def AnalyzeSentenceProcess(self):   #GET OR RECIVER OUTPUT WINDOW
        import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);
        self.AnalyzeSentenceProcessWindow = Tk();
        self.AnalyzeSentenceProcessWindow.title("Analysis Result");
        self.AnalyzeSentenceProcessWindow.geometry("700x400");photoImages = PhotoImage(file="#9.png", master=self.AnalyzeSentenceProcessWindow);
        BgImages = Label(self.AnalyzeSentenceProcessWindow, image=photoImages);
        BgImages.pack();
        TextSentence = self.TextSentence.get();
        print(TextSentence);
########
        polarity = 0; neutral = 0; strongly_positive =0; positive = 0; weakly_positive =0; strongly_negative = 0;
        negative = 0; weakly_negative=0;
        analysis = TextBlob(TextSentence);
        polarity += analysis.sentiment.polarity;
        StringPolarityValue = str(polarity);

        LexiconResultFile = open("LexiconResults.txt", "a");
        LexiconHistoryFile = open("LexiconHistory.txt", "a");
        LexiconResultFile.write("\n");
        LexiconHistoryFile.write("\n");
        LexiconResultFile.write(StringPolarityValue);
        LexiconHistoryFile.write(TextSentence+" ("+StringPolarityValue+")");
        LexiconResultFile.close();
        LexiconHistoryFile.close();

        AppendTextForLabel ="The Polarity Value is : "+StringPolarityValue;
        LabelSentencePolarity = Label(self.AnalyzeSentenceProcessWindow, text=AppendTextForLabel, bg="#0484E4", fg="White",font=("Agency FB bold", 20), width="75", height="1")
        LabelSentencePolarity.place(relx="0.00325", rely="0.335");

        if (polarity > 0 and polarity <= 0.3):
            weakly_positive += 1;
        elif (polarity > 0.3 and polarity <= 0.6):
            positive+= 1;
        elif (polarity > 0.6 and polarity <=2):
            strongly_positive += 1;

        elif (polarity < 0 and polarity >= -0.3):
            weakly_negative += 1;
        elif (polarity < -0.3 and polarity >= -0.6):
            negative += 1;
        elif (polarity < -0.6 and polarity >= -2):
            strongly_negative += 1;

        if (neutral>strongly_positive and neutral>positive and neutral > weakly_positive and neutral> strongly_negative and neutral > negative and neutral> weakly_negative):
            LabelSentenceResult = Label(self.AnalyzeSentenceProcessWindow, text="The Lexical Analysis Result returns Neutral", bg="#0053B1",fg="White", font=("Agency FB bold", 18), width="78", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");
        elif (strongly_positive > neutral and strongly_positive > positive and strongly_positive > weakly_positive and strongly_positive > strongly_negative and strongly_positive > negative and strongly_positive > weakly_negative):
            LabelSentenceResult = Label(self.AnalyzeSentenceProcessWindow,
                                            text="The Lexical Analysis Result returns Strongly Positive", bg="#0053B1",
                                            fg="White", font=("Agency FB bold", 18), width="78", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");
        elif (positive > neutral and positive > strongly_positive and positive > weakly_positive and positive > strongly_negative and positive > negative and positive > weakly_negative):
            LabelSentenceResult = Label(self.AnalyzeSentenceProcessWindow,
                                            text="The Lexical Analysis Result returns Positive", bg="#0053B1",
                                            fg="White", font=("Agency FB bold", 18), width="78", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");
        elif (weakly_positive > neutral and weakly_positive > strongly_positive and weakly_positive > positive and weakly_positive > strongly_negative and weakly_positive > negative and weakly_positive > weakly_negative):
            LabelSentenceResult = Label(self.AnalyzeSentenceProcessWindow,
                                        text="The Lexical Analysis Result returns Weakly Positive", bg="#0053B1",
                                        fg="White", font=("Agency FB bold", 18), width="78", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");
        elif (strongly_negative > neutral and strongly_negative > strongly_positive and strongly_negative > positive and strongly_negative > weakly_positive and strongly_negative > negative and strongly_negative > weakly_negative):
            LabelSentenceResult = Label(self.AnalyzeSentenceProcessWindow,
                                        text="The Lexical Analysis Result returns Strongly Negative", bg="#0053B1",
                                        fg="White", font=("Agency FB bold", 18), width="78", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");
        elif (negative > neutral and negative > strongly_positive and negative > positive and negative > weakly_positive and negative > strongly_negative and negative > weakly_negative):
            LabelSentenceResult = Label(self.AnalyzeSentenceProcessWindow,
                                        text="The Lexical Analysis Result returns Negative", bg="#0053B1",
                                        fg="White", font=("Agency FB bold", 18), width="78", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");
        elif (weakly_negative > neutral and weakly_negative > strongly_positive and weakly_negative > positive and weakly_negative > weakly_positive and weakly_negative > strongly_negative and weakly_negative > negative):
            LabelSentenceResult = Label(self.AnalyzeSentenceProcessWindow,
                                        text="The Lexical Analysis Result returns Weakly Negative", bg="#0053B1",
                                        fg="White", font=("Agency FB bold", 18), width="78", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");
        ButtonGraphShow = Button(self.AnalyzeSentenceProcessWindow, text ="Graphical Representation", bg="#050529",fg = "#15AFAD",font=("Agency FB bold", 17), width="22", command=self.AnalysisGraphSelection1);
        ButtonGraphShow.place(relx="0.1750", rely="0.735");
        ButtonShowHistory = Button(self.AnalyzeSentenceProcessWindow, text="View History", bg="#050529",fg="#15AFAD", font=("Agency FB bold", 17), width="22",command=self.AnalysisViewHistory);
        ButtonShowHistory.place(relx="0.60", rely="0.735");
        self.AnalyzeSentenceProcessWindow.mainloop();

    ########
    def AnalysisGraphSelection1(self):
        import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);
        ArrayFetch = [];
        with open('LexiconResults.txt', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            iteration = 0;
            for row in csv_reader:
                fetchString = row["Attributes"];
                StringToFloat = float(fetchString);
                ArrayFetch.append(StringToFloat);
                print(ArrayFetch[iteration]);
                iteration += 1;
                line_count += 1;
            print(f'Processed {line_count} lines.')
            iteration = 0; wpositive = 0; positive = 0; spositive = 0; wnegative =0; negative = 0; snegative = 0 ; neutral = 0;
            while iteration < len(ArrayFetch):
                VariableStoreFromArray = ArrayFetch[iteration]
                Polarity = float(VariableStoreFromArray);
                if (Polarity > 0 and Polarity <= 0.3 ):
                    wpositive += 1;
                elif (Polarity > 0.3 and Polarity <= 0.6 ):
                    positive += 1;
                elif (Polarity > 0.6 and Polarity <= 2):
                    spositive += 1;
                elif (Polarity ==0):
                    neutral +=1;
                elif (Polarity < 0 and Polarity >= -0.3):
                    wnegative +=1;
                elif (Polarity < -0.3 and Polarity >= -0.6):
                    negative +=1;
                elif (Polarity < -0.6 and Polarity >= 2):
                    snegative +=1;
                iteration += 1;
            sum = iteration;
            WPositivePercent = (wpositive / sum) * 100;
            PositivePercent = (positive / sum) * 100;
            SPositivePercent = (spositive / sum) * 100;
            WNegativePercent = (wnegative / sum) *100;
            NegativePercent = (negative / sum) * 100;
            SNegativePercent = (snegative / sum) * 100;
            NeutralPercent = (neutral / sum) * 100;
            import matplotlib.pyplot as plt
            labels = 'Strongly Positive','Positive','Weakly Positive','Strongly Negative','Negative','Weakly Negative','Neutral';
            sizes = [SPositivePercent, PositivePercent,WPositivePercent,SNegativePercent, NegativePercent, WNegativePercent, NeutralPercent];
            explode = (0.1, 0, 0,0,0,0,0);
            fig1, ax1 = plt.subplots();
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90);
            ax1.axis('equal'); plt.show();


    def AnalysisViewHistory(self):
        import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);
        self.AnalysisViewHistoryWindow = Tk();
        self.AnalysisViewHistoryWindow.title("Analysis History");
        self.AnalysisViewHistoryWindow.geometry("900x700");
        photoImages = PhotoImage(file="#12.png", master=self.AnalysisViewHistoryWindow);
        BgImages = Label(self.AnalysisViewHistoryWindow, image=photoImages);

        #LabelHistoryWriter = Label(text="History", bg="#7c0000", fg="White", font=("Agency FB bold", 18), width="70", height="1")
        ArrayFetch = [];    words="";
        with open('LexiconHistory.txt', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0; iteration = 0;
            for row in csv_reader:
                fetchString = row["History"];
                ArrayFetch.append(fetchString);
                words=words+ArrayFetch[iteration]+"\n";
                #print(ArrayFetch[iteration]);   #DEBUGGER
                iteration += 1; line_count += 1;
            print(f'Processed {line_count} lines.');
            print(words);
            LabelView = Label(self.AnalysisViewHistoryWindow, text=words, bg="#0484E4",
                               fg="white",font=("Agency FB bold", 15));
            LabelView.place(relx="0.225", rely="0.095");
        BgImages.pack();
            #print(iteration);
            #iteration2=0;
            #while iteration2 < 10:
            #   words=ArrayFetch[iteration2]+"\n";

        self.AnalysisViewHistoryWindow.mainloop();

    def AnalyzeTwitterPosts(self):
        import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);
        self.AnalysisTwitterWindow = Tk();
        self.AnalysisTwitterWindow.title("Analysis History");
        self.AnalysisTwitterWindow.geometry("900x600");
        photoImages = PhotoImage(file="#11.png", master=self.AnalysisTwitterWindow);
        BgImages = Label(self.AnalysisTwitterWindow, image=photoImages);
        self.ButtonViewTweets = Button(self.AnalysisTwitterWindow, text="View Tweets", bg="#001745",fg="#00BAFF", font=("Agency FB bold", 17), width="20",command=self.ViewAllTweets);
        self.ButtonViewTweets.place(relx="0.065", rely="0.755");
        self.ButtonTweetResults = Button(self.AnalysisTwitterWindow, text="Back to Menu", bg="#001745", fg="#00BAFF",font=("Agency FB bold", 17), width="20", command=self.ActivateMenu2);
        self.ButtonTweetResults.place(relx="0.725", rely="0.755");
        BgImages.pack();
        TweetStorageFile = open('Tweets.txt', 'w');
        TweetStorageFile.write("tweets");
        TweetStorageFile.close();

        consumerKey = "e5QiuLWa3mJyricV2tYZh7L4D"
        consumerSecret = "d4cmR54P50QePxHR4SZcESYNk9g0D0ZElvwI3PKurbIn1xUgwg"
        accessToken = "1092337126773932034-SPqlH0oeldiBaaYmHSQaSGSbLzlcFB"
        accessTokenSecret = "JqRFzQ4voZIgz0pWA0SBomGr7zhYbzH9ItsfnLf073U56"
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)
        self.tweets = api.user_timeline();
        #search = api.GetSearch("happy"); # Replace happy with your search
        Polarity = 0;    positive = 0;      wpositive = 0;
        spositive = 0;  negative = 0;       wnegative = 0;
        snegative = 0;  neutral = 0;        iteration = 0;
        for tweet in self.tweets:
            #self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'));
            TweetStorageFile = open('Tweets.txt', 'a');
            #TweetWriter = csv.writer(TweetStorageFile);
            TweetStorageFile.write("\n");
            Analysis = TextBlob(tweet.text);
            Polarity += Analysis.sentiment.polarity  # adding up polarities to find the average later
            TweetStorageFile.write(tweet.text);
            TweetStorageFile.close();
            iteration=iteration+1;

            if (Analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                neutral += 1
            elif (Analysis.sentiment.polarity > 0 and Analysis.sentiment.polarity <= 0.3):
                wpositive += 1
            elif (Analysis.sentiment.polarity > 0.3 and Analysis.sentiment.polarity <= 0.6):
                positive += 1
            elif (Analysis.sentiment.polarity > 0.6 and Analysis.sentiment.polarity <= 2):
                spositive += 1
            elif (Analysis.sentiment.polarity > -0.3 and Analysis.sentiment.polarity <= 0):
                wnegative += 1
            elif (Analysis.sentiment.polarity > -0.6 and Analysis.sentiment.polarity <= -0.3):
                negative += 1
            elif (Analysis.sentiment.polarity > -2 and Analysis.sentiment.polarity <= -0.6):
                snegative += 1
        #print(Polarity);  #debugger
        sum = iteration;
        StronglyPositivePercent = (spositive / sum) * 100;
        PositivePercent = (positive / sum) * 100;
        WeaklyPositivePercent = (wpositive / sum) * 100;
        StronglyNegativePercent = (snegative / sum) * 100;
        NegativePercent = (negative / sum) * 100;
        WeaklyNegativePercent = (wnegative / sum) * 100;
        NeutralPercent = (neutral / sum) * 100;

        #print(positive);
        if (neutral > spositive and neutral > positive and neutral > wpositive and neutral > snegative and neutral > negative and neutral > wnegative):
            LabelSentenceResult = Label(self.AnalysisTwitterWindow,text="The Lexical Analysis Result returns Neutral", bg="#0053B1", fg="White",font=("Agency FB bold", 18), width="100", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");
        elif (spositive > positive and spositive > wpositive and spositive > neutral and spositive > snegative and spositive > negative and spositive > wnegative):
            LabelSentenceResult = Label(self.AnalysisTwitterWindow,text="The Lexical Analysis Result returns Strongly Positive", bg="#0053B1", fg="White",font=("Agency FB bold", 18), width="100", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");
        elif (positive > spositive and positive > wpositive and positive > neutral and positive > snegative and positive > negative and positive > wnegative):
            LabelSentenceResult = Label(self.AnalysisTwitterWindow,text="The Lexical Analysis Result returns Positive", bg="#0053B1", fg="White",font=("Agency FB bold", 18), width="100", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");
        elif (wpositive > spositive and wpositive > positive and wpositive > neutral and wpositive > snegative and wpositive > negative and wpositive > wnegative):
            LabelSentenceResult = Label(self.AnalysisTwitterWindow,text="The Lexical Analysis Result returns Weakly Positive", bg="#0053B1", fg="White",font=("Agency FB bold", 18), width="100", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");
        elif (snegative > spositive and snegative > positive and snegative > wpositive and snegative > neutral and snegative > negative and snegative > wnegative):
            LabelSentenceResult = Label(self.AnalysisTwitterWindow,text="The Lexical Analysis Result returns Strongly Negative", bg="#0053B1",fg="White",font=("Agency FB bold", 18), width="100", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");
        elif (negative > spositive and snegative > positive and snegative > wpositive and snegative > neutral and snegative > snegative and snegative > wnegative):
            LabelSentenceResult = Label(self.AnalysisTwitterWindow,text="The Lexical Analysis Result returns Negative", bg="#0053B1", fg="White",font=("Agency FB bold", 18), width="100", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");
        elif (wnegative > spositive and snegative > positive and snegative > wpositive and snegative > neutral and snegative > snegative and snegative > negative):
            LabelSentenceResult = Label(self.AnalysisTwitterWindow,text="The Lexical Analysis Result returns Weakly Negative", bg="#0053B1",fg="White",font=("Agency FB bold", 18), width="100", height="1")
            LabelSentenceResult.place(relx="0.0015", rely="0.435");

        import matplotlib.pyplot as plt
        labels = 'Strongly Postive', 'Positive', 'Weakly Positive', 'Strongly Negative', 'Negative', 'Weakly Negative', 'Neutral';
        sizes = [StronglyPositivePercent, PositivePercent, WeaklyPositivePercent, StronglyNegativePercent,
                 NegativePercent, WeaklyNegativePercent, NeutralPercent];
        explode = (0.1, 0, 0, 0, 0, 0, 0);
        fig1, ax1 = plt.subplots();
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90);
        ax1.axis('equal');
        plt.show();
        self.AnalysisTwitterWindow.mainloop();


    def ViewAllTweets(self):
        self.ViewAllTweetsWindow = Tk();
        self.ViewAllTweetsWindow.title("Tweets Display");
        self.ViewAllTweetsWindow.geometry("900x700");
        photoImages = PhotoImage(file="#13.png", master=self.ViewAllTweetsWindow);
        BgImages = Label(self.ViewAllTweetsWindow, image=photoImages);
        with open("Tweets.txt",mode="r") as csv_file:
            csv_reader= csv.DictReader(csv_file);
            iteration = 0;  ArrayFetch = []; AllTweets="";
            for row in csv_reader :
                fetchString = row["tweets"];
                ArrayFetch.append(fetchString);
                AllTweets = AllTweets+ArrayFetch[iteration]+"\n";
                iteration +=1;
            print(AllTweets); #DEBUGGERS
            LabelDisplayAlltweets = Label(self.ViewAllTweetsWindow,text=AllTweets, bg="#0053B1", fg="White",font=("Agency FB bold", 18))
            LabelDisplayAlltweets.place(relx="0.275", rely="0.185");
        BgImages.pack();
        self.ViewAllTweetsWindow.mainloop();

    #def DisplayTweetResults(self):

    def AnalyzeVRSSystem(self):
        import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);
        self.AnalyzeVRSSystemWindow = Tk();
        self.AnalyzeVRSSystemWindow.title("VRS Analysis");
        self.AnalyzeVRSSystemWindow.geometry("800x500");
        photoImages = PhotoImage(file="#9.png", master=self.AnalyzeVRSSystemWindow);
        BgImages = Label(self.AnalyzeVRSSystemWindow, image=photoImages);
        self.ButtonViewTweets = Button(self.AnalyzeVRSSystemWindow, text="Start VRS", bg="#001745", fg="#00BAFF",
                                       font=("Agency FB bold", 17), width="20", command=self.ActivateVRSSystem);
        self.ButtonViewTweets.place(relx="0.065", rely="0.755");
        BgImages.pack();
        self.AnalyzeVRSSystemWindow.mainloop();

    def ActivateVRSSystem(self):
        import winsound;
        winsound.PlaySound('BtnClick2.wav', winsound.SND_ASYNC);
        global VRS_Scan;
        VRS_Scan=1;print("Selection = ");print(Selection);
        self.AnalyzeVRSSystemWindow.destroy();

    def InititateVRSProcess(self):
        self.InititateVRSProcessWindow = Tk();
        self.InititateVRSProcessWindow.title("VRS Analysis");
        self.InititateVRSProcessWindow.geometry("800x500");
        photoImages = PhotoImage(file="#9.png", master=self.InititateVRSProcessWindow);
        BgImages = Label(self.InititateVRSProcessWindow, image=photoImages);BgImages.pack();

        import speech_recognition as sr;
        r = sr.Recognizer();
        with sr.Microphone() as source:
        #print("Speak Anything :");
            self.LabelViewSpeech = Label(self.InititateVRSProcessWindow,
                                         text="You Said", bg="#050529",
                                         fg="#15AFAD", font=("Agency FB bold", 20), width="45", height="1");
            self.LabelViewSpeech.place(relx="0.0325", rely="0.235");
            audio = r.listen(source);
        try:
            text = r.recognize_google(audio);
            formatText = format(text);
            self.LabelViewSpeech2 = Label(self.InititateVRSProcessWindow,
                                          text=formatText, bg="#050529",
                                          fg="#15AFAD", font=("Agency FB bold", 20), width="45", height="1");
            self.LabelViewSpeech2.place(relx="0.0325", rely="0.435");
            print("You said : {}".format(text))
        except:
            self.LabelViewSpeech3 = Label(self.InititateVRSProcessWindow,
                                          text="Sorry could not recognize what you said", bg="#050529",
                                          fg="#15AFAD", font=("Agency FB bold", 20), width="45", height="1");
            self.LabelViewSpeech3.place(relx="0.0325", rely="0.435");
            print("Sorry could not recognize what you said")

        Polarity=0
        Analysis = TextBlob(formatText);
        Polarity += Analysis.sentiment.polarity;
        if (Polarity == 0):
            self.LabelViewSpeech4 = Label(self.InititateVRSProcessWindow,
                                          text="VRS Analysis Returns Neutral", bg="#050529",
                                          fg="#15AFAD", font=("Agency FB bold", 20), width="45", height="1");
            self.LabelViewSpeech4.place(relx="0.0325", rely="0.635");
        elif (Polarity > 0 and Polarity <= 0.3):
            self.LabelViewSpeech4 = Label(self.InititateVRSProcessWindow,
                                          text="VRS Analysis Returns Weakly Positive", bg="#050529",
                                          fg="#15AFAD", font=("Agency FB bold", 20), width="45", height="1");
            self.LabelViewSpeech4.place(relx="0.0325", rely="0.635");
        elif (Polarity > 0.3 and Polarity <= 0.6):
            self.LabelViewSpeech4 = Label(self.InititateVRSProcessWindow,
                                          text="VRS Analysis Returns Positive", bg="#050529",
                                          fg="#15AFAD", font=("Agency FB bold", 20), width="45", height="1");
            self.LabelViewSpeech4.place(relx="0.0325", rely="0.635");

        elif (Polarity > 0.6 and Polarity <= 2):
            self.LabelViewSpeech4 = Label(self.InititateVRSProcessWindow,
                                          text="VRS Analysis Returns Strongly Positive", bg="#050529",
                                          fg="#15AFAD", font=("Agency FB bold", 20), width="45", height="1");
            self.LabelViewSpeech4.place(relx="0.0325", rely="0.635");
        elif (Polarity < 0 and Polarity >= -0.3):
            self.LabelViewSpeech4 = Label(self.InititateVRSProcessWindow,
                                          text="VRS Analysis Returns Weakly Negative", bg="#050529",
                                          fg="#15AFAD", font=("Agency FB bold", 20), width="45", height="1");
            self.LabelViewSpeech4.place(relx="0.0325", rely="0.635");
        elif (Polarity < -0.3 and Polarity >= -0.6):
            self.LabelViewSpeech4 = Label(self.InititateVRSProcessWindow,
                                          text="VRS Analysis Returns Negative", bg="#050529",
                                          fg="#15AFAD", font=("Agency FB bold", 20), width="45", height="1");
            self.LabelViewSpeech4.place(relx="0.0325", rely="0.635");
        elif (Polarity < -0.6 and Polarity >= -2):
            self.LabelViewSpeech4 = Label(self.InititateVRSProcessWindow,
                                          text="VRS Analysis Returns Negative", bg="#050529",
                                          fg="#15AFAD", font=("Agency FB bold", 20), width="45", height="1");
            self.LabelViewSpeech4.place(relx="0.0325", rely="0.635");

        StringPolarity = str(Polarity);
        StringCombine="Polarity Value is : "+StringPolarity;
        self.LabelViewSpeech5 = Label(self.InititateVRSProcessWindow,
                                      text=StringCombine, bg="#050529",
                                      fg="#15AFAD", font=("Agency FB bold", 20), width="45", height="1");
        self.LabelViewSpeech5.place(relx="0.0325", rely="0.835");
        self.InititateVRSProcessWindow.mainloop();


Object1 = SentimentApp();
Object1.SoundEffect1();
Object1.LoginMenu();
while 1 :
    if (VerifiedUser==1):
        Object1.SoundEffect1();
        Object1.MainMenu();
    else :
        print("Error Log");

    print("Selection = ");print(Selection);
    if (Selection==1):
        Object1.AnalyzeSingleSentence();
    elif (Selection==2):
        Object1.AnalyzeTwitterPosts();
    elif (Selection == 3):
        Object1.AnalyzeVRSSystem();
        if(VRS_Scan==1):
            Object1.InititateVRSProcess()
    else :
        print("Error Logss2");


