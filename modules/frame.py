import customtkinter as ctk
from modules.event import *

def init_menu(window):
    window.menu = ctk.CTkFrame(window, corner_radius=0)
    window.menu.grid(row=0, column=0, sticky="nsew")
    window.menu.grid_rowconfigure(6, weight=1)

    window.menu_label = ctk.CTkLabel(window.menu, text="", image=window.logo_image, compound="left", font=ctk.CTkFont(size=15, weight="bold"))
    window.menu_label.grid(row=0, column=0, padx=20, pady=20)

    window.home_button = ctk.CTkButton(window.menu, corner_radius=0, height=40, border_spacing=10, text="Home", fg_color="transparent", text_color=("#ac2f10", "#f4540f"), hover_color=("gray70", "gray30"), image=window.home_image, anchor="w", command=lambda: home_button_event(window))
    window.home_button.grid(row=1, column=0, sticky="ew")

    window.df_website_button = ctk.CTkButton(window.menu, corner_radius=0, height=40, border_spacing=10, text="Website", fg_color="transparent", text_color=("#ac2f10", "#f4540f"), hover_color=("gray70", "gray30"), image=window.df_website_image, anchor="w", command=df_website_event)
    window.df_website_button.grid(row=2, column=0, sticky="ew")

    window.discord_button = ctk.CTkButton(window.menu, corner_radius=0, height=40, border_spacing=10, text="Discord", fg_color="transparent", text_color=("#ac2f10", "#f4540f"), hover_color=("gray70", "gray30"), image=window.discord_image, anchor="w", command=discord_invite_event)
    window.discord_button.grid(row=3, column=0, sticky="ew")

    window.donate_button = ctk.CTkButton(window.menu, corner_radius=0, height=40, border_spacing=10, text="Donate", fg_color="transparent", text_color=("#ac2f10", "#f4540f"), hover_color=("gray70", "gray30"), image=window.donate_image, anchor="w", command=donation_link_event)
    window.donate_button.grid(row=4, column=0, sticky="ew")

    window.play_button = ctk.CTkButton(window.menu, corner_radius=0, height=40, border_spacing=10, text="Play", fg_color="transparent", text_color=("#ac2f10", "#f4540f"), hover_color=("gray70", "gray30"), image=window.play_image, anchor="w", command=lambda: play_button_event(window))
    window.play_button.grid(row=5, column=0, sticky="ew")

    window.theme_menu = ctk.CTkOptionMenu(window.menu, values=["Dark", "Light"], text_color="gray100", fg_color="#ac2f10",  dropdown_fg_color="#ac2f10", dropdown_hover_color="#ac2f10", button_color="#ac2f08", button_hover_color="#ac2f08", command=lambda mode: change_theme_event(window, mode))
    window.theme_menu.grid(row=6, column=0, padx=20, pady=(50, 10), sticky="ew")

def init_frames(window):
    window.home_frame = ctk.CTkFrame(window, corner_radius=0, fg_color="transparent")
    window.home_frame.grid_columnconfigure(0, weight=1)

    window.df_website_frame = ctk.CTkFrame(window, corner_radius=0, fg_color="transparent")
    window.discord_frame = ctk.CTkFrame(window, corner_radius=0, fg_color="transparent")
    window.donate_frame = ctk.CTkFrame(window, corner_radius=0, fg_color="transparent")
    window.play_frame = ctk.CTkFrame(window, corner_radius=0, fg_color="transparent")

def set_frame(window, name):
    window.home_frame.grid_forget()
    window.df_website_frame.grid_forget()
    window.discord_frame.grid_forget()
    window.donate_frame.grid_forget()
    window.play_frame.grid_forget()

    if name == "home":
        window.home_frame.grid(row=0, column=1, sticky="nsew")
        return
    if name == "website":
        window.df_website_frame.grid(row=0, column=1, sticky="nsew")
        return
    if name == "discord":
        window.discord_frame.grid(row=0, column=1, sticky="nsew")
        return
    if name == "donate":
        window.donate_frame.grid(row=0, column=1, sticky="nsew")
        return
    if name == "play":
        window.play_frame.grid(row=0, column=1, sticky="nsew")