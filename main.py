
import openai
import speech_recognition as sr
from personal_model import func
import pyttsx3
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import scrolledtext
import nltk
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import google.generativeai as genai
from tkcalendar import Calendar 
from datetime import datetime
from datetime import datetime, timedelta
from wtforms import DateField, SubmitField
from wtforms.validators import DataRequired
from scheduling import extract_datetime
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
GEMINI_API_KEY = "my_api_key"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")




def schedule_meeting(date):
    if date:
        chat_history.insert(tk.END, f"AI: Meeting scheduled on {date['raw_date']}\n", "ai")
        c2.insert(tk.END, f"Meeting scheduled on {date['raw_date']}\n")
        cal.calevent_create(date['raw_date'], "Meeting", "reminder")
   
def save_info(new_data):
    result = func(new_data)
    info_text.insert(tk.END, result["Names"] + "\n")
    payment_text.insert(tk.END, result["Amounts Paid"] + "\n")
    need_text.insert(tk.END, result["Needs"] + "\n")
    
def limit_sentences(text, max_sentences):
    sentences = text.split('.')
    limited_text = '. '.join(sentences[:max_sentences]) + '.' if len(sentences) > max_sentences else text
    return limited_text

    
   
             

def send_message():
    global img
    user_message = user_input.get()
    save_info(user_message)
    
 
    
    output = sia.polarity_scores(user_message)
    
    if output['compound']>= 0.05:
        img = Image.open(r"C:\Users\deepa\Downloads\h2.jpeg")
    elif output['compound'] <= -0.01:
        img = Image.open(r"C:\Users\deepa\Downloads\s1.jpeg")
    else:
        img = Image.open(r"C:\Users\deepa\Downloads\n1.jpeg")
   
    img = img.resize((200, 200))  
    img_tk = ImageTk.PhotoImage(img)  
    
    emoji_label.config(image=img_tk)
    emoji_label.image = img_tk
    
    if  user_message:
      
        
        chat_history.insert(tk.END, "You: " + user_message + "\n", "user")
        if "meet"  in user_message or "meeting" in user_message:
            result = extract_datetime(user_message)
            schedule_meeting(result)
            return
      
        response = model.generate_content(user_message)
       
        ai_reply = response.text
        limited_reply = limit_sentences(ai_reply, 3)
        chat_history.insert(tk.END, "AI: " + limited_reply + "\n", "ai")
        text_to_speech(limited_reply)
    user_input.delete(0, tk.END)


def speech_to_text():
    user_input.delete(0, tk.END)
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            user_input.insert(0, text)
        except sr.UnknownValueError:
            chat_history.insert(tk.END, "AI: Sorry, I didn't catch that.\n", "ai")


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def navigate_to_home():
    pass

def navigate_to_feature1():
    pass

def navigate_to_feature2():
    pass




def create_circular_button(frame,text, command):
    btn = tk.Button(frame, text=text, command=command, font=("Helvetica", 14), width=10, height=3, bg="lightgreen", fg="white", relief="raised")
    btn.config(borderwidth=0, highlightthickness=0)
    btn.pack(padx=4,side ='left')
    return btn


root = tk.Tk()
root.title("Hinglish AI Assistant")
root.geometry("500x600")
root.configure(bg="black")


top_nav = tk.Frame(root, bg="black", height=50)
top_nav.pack(side="top", fill="x")
home_button = tk.Button(top_nav ,text="Home", command=navigate_to_home, font=("Arial", 12), bg="green", fg="white", relief="raised")
home_button.pack(side=tk.LEFT, padx=10, pady=10)

feature1_button = tk.Button(top_nav, text="Feature 1", command=navigate_to_feature1, font=("Arial", 12), bg="green", fg="white", relief="raised")
feature1_button.pack(side=tk.LEFT, padx=10, pady=10)

feature2_button = tk.Button(top_nav, text="Feature 2", command=navigate_to_feature2, font=("Arial", 12), bg="green", fg="white", relief="raised")
feature2_button.pack(side=tk.LEFT, padx=10, pady=10)
main_frame = tk.Frame(root, bg="lightgray")
main_frame.pack(side="top", fill="both", expand=True)

left_frame = tk.Frame(main_frame, bg="white", width=300)
left_frame.pack(side="left", fill="y", padx=5, pady=5)
background_image = Image.open(r"C:\Users\deepa\Downloads\webpage.jpeg")  
background_image = background_image.resize((1700, 1100))  
background_img = ImageTk.PhotoImage(background_image)

background_label = tk.Label(left_frame, image=background_img)
background_label.place(relwidth=1, relheight=1) 


cal = Calendar(left_frame, selectmode="day", year=2025, month=datetime.now().month, day=datetime.now().day)
cal.pack(pady=20, padx=10)
tk.Label(left_frame, text="NOTIFICATIONS", font=("Arial", 14, "bold")).pack(pady=10)
c2= scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=20, height=10, bg="white", fg="black", font=("Arial", 14))
c2.pack(pady=10)
c2.tag_config("user", foreground="black")
c2.tag_config("ai", foreground="lightgreen")


center_frame = tk.Frame(main_frame, bg="white")
center_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
background_image = Image.open(r"C:\Users\deepa\Downloads\webpage2.webp")  
background_image = background_image.resize((1700, 1100)) 
background_img = ImageTk.PhotoImage(background_image)

background_label = tk.Label(center_frame, image=background_img)
background_label.place(relwidth=1, relheight=1)  

img = Image.open(r"C:\Users\deepa\Downloads\n1.jpeg")
img = img.resize((200, 200))  
img_tk = ImageTk.PhotoImage(img)  
emoji_label = tk.Label(center_frame, image=img_tk, bg="black")
emoji_label.pack(pady=20)

chat_history = scrolledtext.ScrolledText(center_frame, wrap=tk.WORD, width=50, height=10, bg="lightblue", fg="black", font=("Arial", 14))
chat_history.pack(pady=10)
chat_history.tag_config("user", foreground="black")
chat_history.tag_config("ai", foreground="green")

user_input = tk.Entry(center_frame, width=50, font=("Arial", 14), bg="white", fg="black")
user_input.pack(pady=5)

btn_frame = tk.Frame(center_frame, bg="white")
btn_frame.pack(pady=5)
mic_button = create_circular_button(btn_frame, "🎤 Speak", speech_to_text)
send_button = create_circular_button(btn_frame, "📤 Send", send_message)

right_frame = tk.Frame(main_frame, bg="lightblue", width=300)
right_frame.pack(side="left", fill="y", padx=5, pady=5)

tk.Label(right_frame, text="Personal Info", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=5)
info_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, width=40, height=5, font=("Arial", 12))
info_text.pack(pady=5)

tk.Label(right_frame, text="Payment Status", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=5)
payment_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, width=40, height=5, font=("Arial", 12))
payment_text.pack(pady=5)

tk.Label(right_frame, text="Business Need", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=5)
need_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, width=40, height=5, font=("Arial", 12))
need_text.pack(pady=5)




root.mainloop()

