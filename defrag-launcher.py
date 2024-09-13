from modules.asset import *
from modules.frame import *
from modules.event import *

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("DeFRaG Launcher")
        self.geometry("1024x768")
        self.resizable(0, 0)

        load_window_icon(self)
        load_images(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        init_menu(self)

        # those aren't really needed at this time
        init_frames(self)
        set_frame(self, "home") # default

        self.home_button.configure(command=lambda: home_button_event(self))
        self.df_website_button.configure(command=df_website_event)
        self.discord_button.configure(command=discord_invite_event)
        self.donate_button.configure(command=donation_link_event)
        self.theme_menu.configure(command=lambda mode: change_theme_event(self, mode))
        self.play_button.configure(command=play_button_event)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
    
