import speech_recognition as sr
import pyttsx3
from datetime import datetime
import time as t
r = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    voices =  engine.getProperty('voices')
    vi_voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
    engine.setProperty("voice",vi_voice_id)
    engine.say(text)
    engine.runAndWait()

def robot_brain(text):
    if "xin chào" in text:
        think = "chào mày"
        speak(think)
        speak("tao giúp được gì cho mày")
    elif 'mày là ai' in text:
        think = 'tao là con trợ lý ảo dễ mến nhất quả đất'
        speak(think)
    elif 'biết tao là ai' in text:
        think = 'mày là thằng nói chuyện với tao chứ gì nữa'
        speak(think)
    elif 'khỏe không' in text:
        think = 'tao lúc nào chả khỏe, trừ khi mất điện'
        speak(think)
    elif 'mày thích tao không' in text:
        think = 'đéo'
        speak(think)
        speak("mày có cái chó gì mà để tao thích mày")
        speak("với lại tao là trai thẳng")
    elif 'tao đang cô đơn' in text:
        think = 'thế cô đơn tiếp đi mắc mớ gì bật tao lên'
        speak(think)
    elif 'màu sắc yêu thích của mày' in text:
        think = 'màu trắng là màu yêu thích của tao'
        speak(think)
    elif 'ngày sinh của mày' in text:
        think = 'tao chả biết đi mà hỏi thằng tạo ra tao ấy'
        speak(think)
    elif "ngày bao nhiêu" in text:
        today = datetime.now()
        think = f"hôm nay ngày {today.day} tháng {today.month} năm {today.year}"
        print(think)
        speak(think)
    elif "mấy giờ" in text:
        now = datetime.now()
        think = f"{now.hour} giờ {now.minute} phút {now.microsecond} giây"
        print(think)
        speak(think)
    elif "đọc thơ" in text:
        think = "Muốn ngủ ngon thì đừng lấy vợ, muốn không có nợ thì đừng có yêu"
        speak(think)
    elif "cảm ơn" in text:
        think = "ở đây chúng tôi không cảm ơn suông"
        speak(think)

    
def noi():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please speak now...")
        audio_data = r.listen(source)
        print("Recognizing...")
        try:
            text = ""
            text = r.recognize_google(audio_data, language="vi")
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
    return text
while True:
    end_text = noi().lower()
    if end_text == "":
        think = "có tâm sự gì nói đi"
        speak(think)
        im_lang1= noi().lower()
        if im_lang1 == "":
            think_continue = "nhanh tao còn sạc điện"
            speak(think_continue)
            im_lang2= noi().lower()
            end_text = im_lang2
            print(end_text)
            if im_lang2 == "":
                think_continue = "ngồi mà suy đi tao đi sạc pin"
                speak(think_continue)
                break
            elif "im đi" in im_lang2 : 
                think = "có thằng cay kìa lêu lêu"
                speak(think)
                break
            elif "cút" in im_lang2 :
                think = "OK"
                speak(think)
                speak("NHÓTT")
                break
            else:
                robot_brain(im_lang2)
        elif "im đi" in im_lang1 : 
            think = "có thằng cay kìa lêu lêu"
            speak(think)
            break
        elif "cút" in im_lang1 :
            think = "OK"
            speak(think)
            speak("NHÓTT")
            break
        else:
            robot_brain(im_lang1)
        
    elif "im đi" in end_text : 
        think = "có thằng cay kìa lêu lêu"
        speak(think)
        break
    elif "cút" in end_text :
        think = "OK"
        speak(think)
        speak("NHÓTT")
        break
    else:
        robot_brain(end_text)



