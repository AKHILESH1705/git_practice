import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty('voice',voices[0].id)



def speak(audio):
     engine.say(audio)
     engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)     
    if hour>=0 and hour<12:
        speak("good morning!")
     
    elif hour>=12 and hour<18:
        speak(" good afternoon!")

    else:
        speak("good evening!")   

    speak(" i am akhil your personal assistent sir , please tell me how may io help you ") 
def takecommand():
    #it take input and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing............")
        query = r.recognize_google(audio,language='en-in')
        print(f'user said : {query}\n')
    except Exception as e:
        print(e)
        print("say that again please........")
        return 'None'
    return query 
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('akhileshkushwah17@gmail.com','Akhilesh@99')
    server.sendmail('akhileshkushwah17@gmail.com',to,content)
    server.close()

if __name__=='__main__':
    wishMe() 
    while True:
        query =takecommand().lower()   
    
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak('acording to wikipedia')
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com') 
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com') 
        
        elif 'play music' in query:
            music_dir = 'F:\\deepak\\Music\\Jism-2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir,the time is {strTime}")

        elif 'open code' in query:
            codePath = 'C:\\Users\\akhilesh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
            os.startfile(codePath)

        elif 'email to akhilesh' in query:
            try:
                speak("what should i say?")
                content=takecommand()
                to = 'princeverma1705@gmail.com' 
                sendEmail(to,content)
                speak('email has been sent!')
            except Exception as e:
                print(e)
                speak("sorry akhil there may be some problem with your system please run again this program")    
        elif 'quit' in query:
            exit()        