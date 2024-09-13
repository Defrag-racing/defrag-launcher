import os
from PIL import Image
import customtkinter as ctk

def load_window_icon(window):
    icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets", "logo.ico")
    window.iconbitmap(default=icon_path)

def load_images(window):
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
    window.logo_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "logo_dark.png")), dark_image=Image.open(os.path.join(image_path, "logo_light.png")), size=(130, 64))
    window.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")), dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
    window.discord_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "discord_dark.png")), dark_image=Image.open(os.path.join(image_path, "discord_light.png")), size=(20, 20))
    window.donate_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "donate_dark.png")), dark_image=Image.open(os.path.join(image_path, "donate_light.png")), size=(20, 20))  
    window.df_website_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "website_dark.png")), dark_image=Image.open(os.path.join(image_path, "website_light.png")), size=(20, 20))
    window.play_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "play_dark.png")), dark_image=Image.open(os.path.join(image_path, "play_light.png")), size=(20, 20))

