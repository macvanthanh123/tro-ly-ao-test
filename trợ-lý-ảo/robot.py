import speech_recognition as sr
import pyttsx3
from datetime import date, datetime

robot_ear = sr.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:  # cái này để mình và robot giao tiếp liên tục thay vì nói 1 câu chương trình đã kết thúc.
    with sr.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    
    print("Robot:...")
 
    try:
        you = robot_ear.recognize_google(audio, language="vi")
        print("You: " + you)
    except:
        you = ""

    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you.lower():  # Kiểm tra xem "hello" có trong câu nói hay không
        robot_brain = "xin chào"
    elif "today" in you.lower():
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you.lower():
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "goodbye" in you.lower():  # Đoạn này khi nói goodbye thì chương trình sẽ tắt thay vì mở liên tục khi ở phía trên
        robot_brain = "Good Bye"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm fine thank you and you"

    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
