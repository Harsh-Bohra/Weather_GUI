import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def exit_program():
    root.destroy()

def run_program():
    import subprocess
    import os

    # Get the current working directory and construct the script path
    script_path = os.path.join(os.getcwd(), 'main_weather.py')

    try:
        # Run the script and capture the output
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, check=True)
        # Display the output in a message box
        messagebox.showinfo("Weather Report", result.stdout)
    except subprocess.CalledProcessError as e:
        # If an error occurs, display a message box with the error message
        messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()
root.attributes('-fullscreen', True)  # Open window in full screen mode
root.title("Weather Display Application")

# Set background color to light blue
root.configure(bg='#FFFF00')

# Create a frame to hold the buttons and output screen
frame = tk.Frame(root, bg='#2c3e50')
frame.pack(fill='both', expand=True, padx=50, pady=50)

# Create a frame to hold the output screen
output_frame = tk.Frame(frame, bg='#c0e9f0')
output_frame.pack(fill='both', expand=True, side='left', padx=50, pady=50)

# Create a label widget to display output
output = tk.Label(output_frame, text="WEATHER \n DISPLAY \n APPLICATION", bg='#c0e9f0', font=("Arial Bold", 40), justify='center')
output.pack(fill='both', expand=True)

# Create a frame to hold the buttons
button_frame = tk.Frame(frame, bg='#2c3e50')
button_frame.pack(fill='both', expand=True, side='right', padx=50, pady=50)

# Create the buttons
button2 = tk.Button(button_frame, text=" WEATHER REPORT SEARCH ", bg='#00FF00', fg='black', font=("Arial Bold", 20), command=run_program)
button2.pack(fill='both', expand=True, padx=10, pady=10)

button3 = tk.Button(button_frame, text=" EXIT ", command=exit_program, bg='#FF0000', fg='black', font=("Arial Bold", 20))
button3.pack(fill='both', expand=True, padx=10, pady=10)

root.mainloop()
