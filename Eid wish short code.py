import tkinter as tk
import time

def animate_greeting(label, text, delay=100, final_delay=500):
    def update_text(index=0):
        if index < len(text):
            label.config(text=text[:index + 1])
            label.after(delay, update_text, index + 1)
        else:
            label.after(final_delay, lambda: label.config(text=text))
    update_text()

def main():
    root = tk.Tk()
    root.title("Eid Greeting")
    root.geometry("400x200")
    
    label = tk.Label(root, text="", font=("Arial", 24, "bold"), fg="green")
    label.pack(expand=True)
    
    animate_greeting(label, "EID MUBARAK")
    
    root.mainloop()

if __name__ == "__main__":
    main()
