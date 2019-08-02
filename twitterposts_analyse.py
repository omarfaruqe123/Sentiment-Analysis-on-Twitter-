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
