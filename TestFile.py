import pyttsx3;
from textblob import TextBlob;
import os;
from time import sleep

class Audio:
    Verify = 0;formatText="";Talking=0;
    def __init__(self):
        print("functional");


    def Login(self):
        import speech_recognition as sr;
        r = sr.Recognizer();
        with sr.Microphone() as source:
            audio = r.listen(source);
            try:
                text = r.recognize_google(audio);
                formatText = format(text);
                print("You said : {}".format(text));
            except:
                print("Sorry could not recognize what you said");
        if "566" in formatText or "gamma" in formatText or "epsilon" in formatText:
            engine.say("Authorization Granted. Welcome Mr. Shahriar");
            engine.runAndWait();
            global Verify; Verify=1;
        else:
            engine.say("Sorry! Authorization Error Detected. Self-Shutting Down");engine.runAndWait();

    def command(self):
        global Talking;
        import speech_recognition as sr;
        r = sr.Recognizer();
        #AUDIO FILE CAN ALSO BE USED?
        with sr.Microphone() as source:
            audio = r.listen(source);
            try:
                text = r.recognize_google(audio);
                global formatText;
                formatText = format(text);
                print("You said : {}".format(text));
                Talking=1;
            except:
                print("Sorry could not recognize what you said");
                Talking=0;


engine = pyttsx3.init();
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0');
engine.setProperty('rate',175);
formatText="";
print("Hello");
Obj = Audio();
Obj.Login();
if (Verify==1):
    while 1 :
        Obj.command();
        Polarity=0;
        Analysis = TextBlob(formatText);
        Polarity += Analysis.sentiment.polarity;
        print(Polarity);
        if "introduction" in formatText or "who are you" in formatText or "introduce yourself" in formatText:
            engine.say("Hello! My name is January. I am an Artificial Intelligence set up for any type of assistance. However I am just a prototype. A work in progress.");engine.runAndWait();

        elif "hey" in formatText or "hello" in formatText or "hi" in formatText:
            from random import randint
            number = randint(0, 4);
            if number == 0:
                engine.say("Hello Sir. I hope you are having a nice day!"); engine.runAndWait();
            elif number == 1:
                engine.say("Greetings Sir. How are you feeling?"); engine.runAndWait();
            elif number == 2:
                engine.say("Hello. Lovely day, Isn't it Sir?"); engine.runAndWait();
            elif number == 3:
                engine.say("Good day to you Sir. I am operating at peak efficiency");engine.runAndWait();
            elif number == 4:
                engine.say("Hello, how may I assist you Sir?");engine.runAndWait();

        elif "how are you" in formatText or "your status" in formatText or "you alright" in formatText:
            engine.say("I am operating at maximum capacity. How are you feeling, Sir?");engine.runAndWait();

        elif "feeling" in formatText:
            if "not feeling good" in formatText or "feeling bad" in formatText:
                engine.say("Sorry to hear that. May I ask Why?");engine.runAndWait();
            elif "good" in formatText or "fine" in formatText:
                engine.say(" Good to hear that. Sir.");engine.runAndWait();
            elif "feeling great" in formatText or "feeling awesome" in formatText and Polarity > 0:
                engine.say("That is Excellent news. Sir. I am very glad to hear it.");engine.runAndWait();
            elif "feeling okay" in formatText or "feeling alright" in formatText:
                engine.say("I am sure you will feel better today.");engine.runAndWait();
            elif "you feeling okay" in formatText or "u feeling okay" in formatText or "you feeling ok" in formatText or "u feeling okay" in formatText or "how are you feeling" in formatText:
                engine.say("I am fully operational Sir. Thanks for asking.");engine.runAndWait();

        elif "welcome" in formatText :
            sleep(3);

        elif "improved" in formatText or "improvements" in formatText:
            if "you have improved" in formatText and Polarity >0:
                engine.say("I must say I am developing very well. Its exciting to learn something new");
                engine.runAndWait();

        elif "presentation" in formatText:
            engine.say("I will try my best to assist you in your Presentation. Sir.");
            engine.runAndWait();
#TESTING
        elif "i have" and "exam" in formatText:
            engine.say("May I ask which exam you have?");engine.runAndWait();
            Obj.command();
            engine.say("Good luck to you Sir. I am sure you will do great!");engine.runAndWait();

        elif "thank you" in formatText or "thanks" in formatText:
            from random import randint
            number = randint(0,2);
            if number==0 :
                engine.say("You're Welcome Sir.");engine.runAndWait();
            elif number==1 :
                engine.say("Sure thing Sir.");engine.runAndWait();
            elif number==2 :
                engine.say("Don't mention it Sir.");engine.runAndWait();

        elif "sorry" in formatText:
            from random import randint
            number = randint(0, 2);
            if number == 0:
                engine.say("No Problem Sir");
                engine.runAndWait();
            elif number == 1:
                engine.say("Its alright Sir");
                engine.runAndWait();
            elif number == 2:
                engine.say("Its okay Sir");
                engine.runAndWait();

        elif "you there" in formatText:
            from random import randint
            number = randint(0, 2);
            if number == 0:
                engine.say(" Yes Sir");
                engine.runAndWait();
            elif number == 1:
                engine.say("For you Sir, Always");
                engine.runAndWait();
            elif number == 2:
                engine.say("I'm here Sir");
                engine.runAndWait();
###HELPER
        elif "don't know what to say" in formatText or "dont know what to say" in formatText:
            engine.say("I can help");
            engine.runAndWait();
            from random import randint
            number = randint(0,2);
            if number==0 :
                engine.say("How are you feeling?");engine.runAndWait();
            elif number==1 :
                engine.say("What do you think about my improvements?");engine.runAndWait();
            elif number==2 :
                engine.say("I can wait if you want me to, just say the word");engine.runAndWait();
###HELPER

        elif "goodbye " in formatText or "goodbye" in formatText or "goodbye January" in formatText or "bye" in formatText or "bye January" in formatText:
            engine.say("Goodbye Sir! Have a Good Day");engine.runAndWait();
            break;

        elif "good" in formatText or "good to know" in formatText or "great" in formatText:
            if "good work" in formatText or "good job" in formatText and Polarity > 0:
                from random import randint; number = randint(0, 2);
                if number == 0:
                    engine.say("Thank You Sir");engine.runAndWait();
                elif number == 1:
                    engine.say("Appreciate it Sir");engine.runAndWait();
                elif number == 2:
                    engine.say("Thanks Sir. You're too kind.");

            from random import randint
            number = randint(0, 2);
            if number == 0:
                engine.say("I see");engine.runAndWait();
            elif number == 1 :
                engine.say("Hmm");engine.runAndWait();
            elif number == 2 :
                engine.say("Okay");engine.runAndWait();

        elif "wait" in formatText:
            from random import randint
            number = randint(0, 2);
            if number == 0: engine.say("Very Well, I'll wait");engine.runAndWait();
            elif number == 1: engine.say("Sure thing, I'll wait");engine.runAndWait();
            elif number == 2: engine.say("Understood Sir");engine.runAndWait();
            while 1 :
                sleep(3);
                Obj.command();
                if "start" in formatText:
                    engine.say("I'm Back Sir");engine.runAndWait();
                    break;

        elif "open" in formatText :
            from random import randint
            number = randint(0, 3);
            if number == 0:
                engine.say("Sure Thing.");
                engine.runAndWait();
            elif number == 1:
                engine.say("Certainly.");
                engine.runAndWait();
            elif number == 2:
                engine.say("Alright.");
                engine.runAndWait();
            elif number == 3:
                engine.say("Sure Sir.");
            os.system('explorer C:\\"{}"'.format(formatText.replace('open ','')));
            continue;

        elif "do something" in formatText :
            from random import randint
            number = randint(0, 2);
            if number == 0:
                engine.say("Sure Thing. Go ahead Sir");
                engine.runAndWait();
            elif number == 1:
                engine.say("Certainly. Waiting for command Sir");
                engine.runAndWait();
            elif number == 2:
                engine.say("Alright. What do you need Sir?");
                engine.runAndWait();
        elif Talking==1 :
            engine.say("Could not hear you, Sir?");
            engine.runAndWait();


