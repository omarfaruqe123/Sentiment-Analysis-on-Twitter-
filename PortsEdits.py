import pyttsx3;

engine = pyttsx3.init();
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0');
engine.setProperty('rate',160);
formatText="";
print("Hello")


if "Alpha Epsilon" in formatText:
    engine.say("Hello Sir! This is January as your Artificial Intelligence");
    engine.runAndWait();
else :
    engine.say("Sorry! Authorization Error Detected. Self-Shutting Down")
    engine.runAndWait();


#voices = engine.getProperty('voices');
#for voice in voices :
#    print(voice.id);