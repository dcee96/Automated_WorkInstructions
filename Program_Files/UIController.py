import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
from Utilities import *

class UIController(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("Automated_WorkInstructions\\Assets\\UI_Assets\\GUI_Theme.json")

        self.title("Automate Work Instruction Transfer.")
        self.geometry("600x400")
        self.frames = {}
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.show_frame(WelcomePage)

    def show_frame(self, frame_class):
        """Show a specific frame and hide the current one"""
        # Remove the current frame if there is one
        for frame in self.frames.values():
            frame.pack_forget()

        # If the frame doesn't exist yet, create it
        if frame_class not in self.frames:
            frame = frame_class(self.container, self)
            self.frames[frame_class] = frame
            frame.pack(fill="both", expand=True)

        # Show the requested frame
        self.frames[frame_class].pack(fill="both", expand=True)

    def remove_frame(self, frame_class):
        """Remove a frame from the UI controller"""
        if frame_class in self.frames:
            self.frames[frame_class].destroy()
            del self.frames[frame_class]

# Example of a simple Welcome Page UI
class WelcomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = ctk.CTkLabel(self, text="Automated Excel Transfer", font=("Arial", 24))
        label.pack(pady=20)

        btn_file_selector = ctk.CTkButton(self, text="File Selector", command=lambda: controller.show_frame(File_Selector))
        btn_file_selector.pack(pady=10)

        btn_qrcode = ctk.CTkButton(self, text="QR Code Generator", command=lambda: controller.show_frame(QR_Generator))
        btn_qrcode.pack(pady=10)

        label = ctk.CTkLabel(self, text="Designed by Dylan Cooley", font=("Arial", 10))
        label.pack(pady=20, anchor="s")

class File_Selector(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # UI Elements
        self.label_files = ctk.CTkLabel(self, text="Selected Files:")
        self.label_files.pack(pady=10)

        self.file_listbox = ctk.CTkTextbox(self, height=100, width=400)
        self.file_listbox.pack(pady=10)

        self.btn_select_files = ctk.CTkButton(self, text="Select Excel Files", command= self.select_files)
        self.btn_select_files.pack(pady=10)

        self.btn_extract = ctk.CTkButton(self, text="Extract Data", command= self.extract_data)
        self.btn_extract.pack(pady=10)

        self.btn_go_back = ctk.CTkButton(self, text="Go Back", command=lambda: controller.show_frame(WelcomePage))
        self.btn_go_back.pack(pady=10)

        self.excel_files = []
    
    def select_files(self):
        """Function to select Excel files using a file dialog"""
        files = filedialog.askopenfilenames(filetypes=[("Excel files", "*.xls *.xlsx")])
        if files:
            self.excel_files = files
            self.file_listbox.delete(1.0, tk.END)  # Clear listbox
            for file in files:
                self.file_listbox.insert(tk.END, f"{file}\n")
    
    def extract_data(self):
        """Function to trigger data extraction"""
        if not self.excel_files:
            messagebox.showerror("Error", "No Excel files selected.")
            return
        
        # Call the extraction function and display the results
        try:
            data = extract_data_from_excel(
                self.excel_files,
                "I2:M2")
            messagebox.showinfo("Extraction Complete", "All of the data has been extracted successfully!\nAny image files will be stored in the same folder\nthe orginal excel file was stored in")
        except Exception as e:
            messagebox.showerror("Error", str(e))


class QR_Generator(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.url = ""
        self.destination = ""
        self.name = ""

        self.label_frame = ctk.CTkLabel(self, text="QR Code Generator ", font=("arial", 24))
        self.label_frame.pack(pady=10)

        self.url_input = ctk.CTkEntry(self, placeholder_text="pdf url", textvariable=self.url)
        self.url_input.pack(pady=10)

        self.name_input = ctk.CTkEntry(self, placeholder_text="file name", textvariable=self.name)
        self.name_input.pack(pady=10)

        self.destination_input = ctk.CTkEntry(self, placeholder_text="file destination", textvariable=self.destination)
        self.destination_input.pack(pady=10)

        self.btn_generate = ctk.CTkButton(self, text="Generate", command=lambda: create_qrcode())
        self.btn_generate.pack(pady=10)

        self.btn_go_back = ctk.CTkButton(self, text="Go Back", command=lambda: controller.show_frame(WelcomePage))
        self.btn_go_back.pack(pady=10)

        def create_qrcode(self):
            generate_qr_code(self.url, self.name, self.destination)

# Running the application
if __name__ == "__main__":
    app = UIController()
    app.mainloop()
