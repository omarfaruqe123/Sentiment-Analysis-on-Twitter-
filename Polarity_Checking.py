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
