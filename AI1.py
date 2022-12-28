import pyttsx3
import speech_recognition as rec
import datetime


robot_hear = rec.Recognizer()
robot_speak = pyttsx3.init()
robot_brain = ""

voices = robot_speak.getProperty('voices')
robot_speak.setProperty('voice', voices[1].id)




while True:
    with rec.Microphone() as mic :
        print("Robot : I'm listening ")
        audio = robot_hear.listen(mic)

    try :
        you = robot_hear.recognize_google(audio)
    except:
        you = ""

    print("You :" + you)

    if you == "":   
        robot_brain = "I can't hear you"
    elif you == "hello":
        robot_brain = "hello tan"
    elif "today" in you:
        today = datetime.date.today()
        today = today.strftime("%B %d,%Y")
        robot_brain = "Today is " + today
    elif "time" in you :
        time = datetime.datetime.now()
        time = time.strftime("%H,%M")
        robot_brain = time
    elif "bye" in you :
        robot_brain = " Goodbye Tan"
        print("Robot : " + robot_brain)
        robot_speak.say(robot_brain)
        robot_speak.runAndWait()
        break
    else:
        robot_brain = "ok"

    print("Robot : " + robot_brain)
    robot_speak.say(robot_brain)
    robot_speak.runAndWait()