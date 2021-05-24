import pyttsx3
import wikipedia
import datetime
import os
import webbrowser
import speech_recognition as sr
import smtplib
from playsound import playsound
from tkinter import *
from PIL import ImageTk, Image
print("INITIALIZING JARVIS....")

master = "PIYUSH SIR"

engine=pyttsx3.init('sapi5')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme(): 
    hour=int(datetime.datetime.now().hour)
    
    
    if hour>=0 and hour<12:
        speak("Good morning" +master)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" +master)
    else:
        speak("Good Evening" +master)     

    speak("I Am Your Personal Voice Assistant Jarvis, Tell Me What Can I Do For You??")   

def takecommmand():


    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio=r.listen(source)

    try:
        print("Recognizing......") 
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        speak("Say that again please, IF I CAN'T UNDERSTAND YOU FOR MANY TIMES THEN PLEASE RESTART ME.")
        query= None
    return query
 


class Widget:
    def __init__(self):
       root = Tk()
       root.title('Jarvis(Mark-1)')
       root.config(background='Red')
       root.geometry('1000x710')
       img = ImageTk.PhotoImage(Image.open(r"D:\man1.png"))
       panel = Label(root, image = img)
       panel.pack(side='right', fill='both',expand = "no")

       

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Click Listen Me to Give commands')

       userFrame = LabelFrame(root, text="User", font=('Black ops one',10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg='#3B3B98', fg='white')
       left2.config(font=("Century Gothic", 24, 'bold'))
       left2.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="Jarvis", font=('Black ops one',10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='#3B3B98',fg='white')
       left1.config(font=("Century Gothic", 24, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       btn = Button(root, text='Listen Me', font=('Black ops one', 10, 'bold'), bg='#4b4b4b', fg='white',command=self.clicked).pack(fill='x', expand='no')
       btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='#4b4b4b', fg='white',command=root.destroy).pack(fill='x', expand='no')

       speak("Please click the Listen Me Button To Give Me Commands, And close to quit me.")
       
       self.compText.set('Hello, I am Jarvis! What can i do for you Sir ??')

       root.bind("<Return>",self.clicked) # handle the enter key event of your keyboard
       root.mainloop()

    def clicked(self):
        speak("Listening....")
        query = takecommmand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()
       
        if 'tell me'in query:
            speak("Searching wikipedia......")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences =2)
            print(results)
            speak(results)

        elif 'launch whatsapp' in query:
            speak("Alright Sir, launching WhatsApp for you.")
            chat_path = 'C://Users//piyush//AppData//Local//WhatsApp//WhatsApp.exe'
            webbrowser.open(chat_path)
        elif 'launch amazon' in query:
            speak("opening amazon")
            url = "amazon.com"
            chrome_path = 'C://Program Files//Google//Chrome//Application//chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
    
        elif 'launch code' in query:
            speak("Alright Sir, launching Visual Studio Code For You.")
            code_path = 'C://Users//piyush//AppData//Local//Programs//Microsoft VS Code//Code.exe'
            webbrowser.open(code_path)

        elif 'launch flipkart' in query:
            speak("Alright Sir, opening flipkart for you.")  
            url = "flipkart.com"
            chrome_path = 'C://Program Files//Google//Chrome//Application//chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'shutdown pc' in query:
            speak("Sorry Sir, I can't Shut Down Pc because if i will shut down pc then i will get destroyed from your computer.")

        elif 'launch gmail' in query:
            speak("Alright Sir, opening g-mail for you.")  
            url = "gmail.com"
            chrome_path = 'C://Program Files//Google//Chrome//Application//chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'launch youtube' in query:
            speak("Alright Sir, opening youtube for you.")  
            url = "https://youtube.com/"
            chrome_path = 'C://Program Files//Google//Chrome//Application//chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'launch zoom' in query:
            speak("Alright Sir, Launching Zoom For You.")
            zoom_path = 'C://Users//piyush//AppData//Roaming//Zoom//bin//Zoom.exe'
            webbrowser.open(zoom_path)

        elif 'thank you' in query:
            speak("Its my pleasure sir to always help you")

        elif 'sorry' in query:
            speak("well if you really are then say it to my master") 

        elif 'please' in query:
            speak("Don't say please sir!!!... I'm always here to help you")

        elif 'ek hi nara ek hi naam' in query:
            speak("jai shree raam, jay shree raam")  

        elif 'bolo har har mahadev' in query:
            speak("har har mahadev")   

        elif 'who are you' in query:
            speak("I Am Your Personal Voice Assistant Jarvis, How can you forget me sir?")  
                
        elif 'what can you do' in query:
            speak("its better if you ask what kind of assistant are you")

        elif'what kind of assistant are you' in query:
            speak("kind of helpful")

        elif'help me'in query:
            speak("always ready to help you piyush sir")

        elif 'what is your name' in query:
            speak("jarvis sir")

        elif 'ok google' in query:
            speak("thats not me sir....i am jarvis")

        elif 'hey siri' in query:
            speak("i am jarvis sir,how can you forget something which is created by you sir") 

        elif 'i want to be rich' in query:
            speak("so do i") 

        elif 'launch word' in query:
            speak("Alright Sir, launching MS Word for you.")
            word_path = 'C://Program Files//Microsoft Office//root//Office16//WINWORD.EXE'
            webbrowser.open(word_path)

        elif 'launch new spreadsheet' in query:
            speak("Alright Sir, launching MS Excel for you.")
            excel_path = 'C://Program Files//Microsoft Office//root//Office16//EXCEL.EXE'
            webbrowser.open(excel_path)

        elif 'launch powerpoint' in query:
            speak("Alright Sir, launching MS PowerPoint for you.")
            point_path = 'C://Program Files//Microsoft Office//root//Office16//POWERPNT.EXE'
            webbrowser.open(point_path)

        elif 'launch outlook' in query:
            speak("Alright Sir, launching MS Outlook for you.")
            mail_path = 'C://Program Files//Microsoft Office//root//Office16//OUTLOOK.EXE'
            webbrowser.open(mail_path)

        elif 'launch onenote' in query:
            speak("Alright Sir, launching MS Onenote for you.")
            note_path = 'C://Program Files//Microsoft Office//root//Office16//ONENOTE.EXE'
            webbrowser.open(note_path)

        elif 'launch paint' in query:
            speak("Alright Sir, launching MS Paint for you.")
            paint_path = 'C://Windows//system32//mspaint.exe'
            webbrowser.open(paint_path)

        elif 'launch cmd' in query:
            speak("Alright Sir, launching Windows Command Prompt for you.")
            cmd_path = 'C://Windows//system32//cmd.exe'
            webbrowser.open(cmd_path)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            speak("Sir I Don't know the date because my master doesn't gave me the input of current date.")

        elif 'play music' in query:
            speak("Alright Sir, Playing Big B's Song for your Entertainment.")
            music_path = 'C://Users//piyush//Desktop//Music//O-Saathi-Re-Tere-Bina-Kishore-Kumar.mp3'
            webbrowser.open(music_path)
    



if __name__ == '__main__':
    speak("INITIALIZING JARVIS")

    speak("LOADING THE PROGRAM...")

    speak("INITIALIZED JARVIS SUCCESSFULLY...")
    wishme()
    widget = Widget() 

   
