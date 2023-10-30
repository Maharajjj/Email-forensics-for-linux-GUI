import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk  # Import Pillow

def browse_input_folder():
    input_folder = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, input_folder)

def browse_output_folder():
    output_folder = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, output_folder)

def process_files():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    
    # Replace with the actual command to run your shell script
    # subprocess.run(["bash", "process_script.sh", input_folder, output_folder])

window = tk.Tk()
window.title("Email Processing App")
window.geometry("1000x400")  # Larger window size

# Use a modern theme
window.style = ttk.Style()
window.style.theme_use("clam")

# Load and set a background image
bg_image = Image.open("background.png")
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = ttk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Add custom styling for labels
window.style.configure("Title.TLabel", font=("Helvetica", 20), background="#333", foreground="white")

input_folder_label = ttk.Label(window, text="Select input folder:", style="Title.TLabel")
input_folder_label.grid(row=0, column=0, padx=20, pady=20)

input_folder_entry = ttk.Entry(window, width=50)
input_folder_entry.grid(row=0, column=1, padx=20, pady=20)

browse_input_button = ttk.Button(window, text="Browse", command=browse_input_folder)
browse_input_button.grid(row=0, column=2, padx=20, pady=20)

output_folder_label = ttk.Label(window, text="Select output folder:", style="Title.TLabel")
output_folder_label.grid(row=1, column=0, padx=20, pady=20)

output_folder_entry = ttk.Entry(window, width=50)
output_folder_entry.grid(row=1, column=1, padx=20, pady=20)

browse_output_button = ttk.Button(window, text="Browse", command=browse_output_folder)
browse_output_button.grid(row=1, column=2, padx=20, pady=20)

process_button = ttk.Button(window, text="Process Files", command=process_files)
process_button.grid(row=2, column=1, padx=20, pady=20)

window.mainloop()
