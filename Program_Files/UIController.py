import customtkinter

class UIController(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

    def run_build(self, sourceFilePath: str, destFilePath: str) -> bool: 
        try:
            return True
        except: 
            return False