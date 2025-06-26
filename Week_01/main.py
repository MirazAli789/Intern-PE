import tkinter as tk
from datetime import datetime
import time

class DigitalClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Digital Clock")
        self.root.geometry("600x150")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        self.center_window()
        
        self.time_label = tk.Label(
            self.root,
            font=('Courier', 48, 'bold'),
            bg='black',
            fg='#00FFFF',
            text="01:32:03 AM",
            relief='flat',
            bd=0
        )
        self.time_label.pack(expand=True, fill='both')
        
        try:
            self.time_label.config(font=('DS-Digital', 48, 'bold'))
        except:
            try:
                self.time_label.config(font=('Digital-7', 48, 'bold'))
            except:
                try:
                    self.time_label.config(font=('LCD', 48, 'bold'))
                except:
                    self.time_label.config(font=('Courier New', 48, 'bold'))
        
        self.update_time()
        
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def update_time(self):
        current_time = datetime.now()
        
        time_string = current_time.strftime("%I:%M:%S %p")
        
        self.time_label.config(text=time_string)
        
        self.root.after(1000, self.update_time)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    clock = DigitalClock()
    clock.run()
