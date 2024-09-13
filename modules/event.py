import os
import time
import subprocess
import webbrowser
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

def home_button_event(window):
    from modules.frame import set_frame
    set_frame(window, "home")

def df_website_event():
    webbrowser.open("https://defrag.racing")

def discord_invite_event():
    webbrowser.open("https://discord.defrag.racing")

def donation_link_event():
    webbrowser.open("https://www.paypal.com/donate/?hosted_button_id=WH6GY4PDGU8FA")

def change_theme_event(window, theme):
    if theme == "Light":
        new_theme = "Light"
    else:
        new_theme = "Dark"

    ctk.set_appearance_mode(new_theme)

def play_button_event():
    exe_name = "oDFe.x64.exe"
    try:
        subprocess.run(exe_name, shell=True, check=True)
    except subprocess.CalledProcessError:
        CTkMessagebox(title="Error", message=f"Failed to start {exe_name}", icon="cancel", option_1="OK")

