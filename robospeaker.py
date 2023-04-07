import pyttsx3

if __name__=="__main__":
    print("Welcome to robospeaker 1.2.1 created by Saga.")
    
    while True:
        text=input("Enter what you want robo to speak:\n")
        if text.strip()=="":
            print("Please provide the text to speak")
        else:
            speak=pyttsx3.init()
            speak.say(text)
            speak.runAndWait()
            choice=input("Do you wana continue (y or no)?\n")
            if choice.lower()!='y':
             break
