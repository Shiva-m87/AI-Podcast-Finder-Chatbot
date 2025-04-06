import tkinter as tk
from tkinter import ttk
import google.generativeai as genai

# Configure the Gemini API
genai.configure(api_key="AIzaSyASaAnluwOqFg30KT-VCyAMszfeu6Dle2k")  # type: ignore # Replace with your actual API key

# Function to fetch podcast recommendations
def get_podcast_recommendations():
    user_mood = mood_entry.get()
    user_interest = interest_entry.get()

    if not user_mood or not user_interest:
        output_label.config(text="Please enter both mood and interest.")
        return

    model = genai.GenerativeModel("gemini-1.5-flash") # type: ignore
    prompt = f"Give me 5 podcast channel names based on interest: {user_interest} and mood: {user_mood}. Provide a brief summary of each."

    try:
        response = model.generate_content(prompt)
        recommendations = response.text if response.text else "No recommendations found."

        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, recommendations)
        output_text.config(state=tk.DISABLED)
        output_label.config(text="")  # Clear any previous error
    except Exception as e:
        output_label.config(text=f"Error: {str(e)}")

# Main Application Window
root = tk.Tk()
root.title("AI Podcast Finder")
root.geometry("700x650")
root.configure(bg="#E3F2FD")

# Title Label
title_label = tk.Label(
    root, text="🎧 AI Personalized Podcast Finder", font=("Arial", 18, "bold"),
    bg="#1565C0", fg="white", pady=12
)
title_label.pack(fill=tk.X)

# Frame for Inputs
input_frame = tk.Frame(root, bg="#E3F2FD")
input_frame.pack(pady=20)

# Mood Input
mood_label = tk.Label(input_frame, text="Mood:", font=("Arial", 12), bg="#E3F2FD")
mood_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
mood_entry = ttk.Entry(input_frame, font=("Arial", 12), width=30)
mood_entry.grid(row=0, column=1, padx=10, pady=10)

# Interest Input
interest_label = tk.Label(input_frame, text="Interest:", font=("Arial", 12), bg="#E3F2FD")
interest_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
interest_entry = ttk.Entry(input_frame, font=("Arial", 12), width=30)
interest_entry.grid(row=1, column=1, padx=10, pady=10)

# Search Button
search_button = tk.Button(
    root, text="🎯 Find Podcast", font=("Arial", 12, "bold"),
    bg="#1976D2", fg="white", padx=12, pady=6,
    command=get_podcast_recommendations
)
search_button.pack(pady=10)

# Output Display Box
output_text = tk.Text(root, height=15, width=80, font=("Arial", 12), wrap=tk.WORD, state=tk.DISABLED, bg="white", fg="black")
output_text.pack(padx=10, pady=10)

# Output Label for Errors
output_label = tk.Label(root, text="", font=("Arial", 12), fg="red", bg="#E3F2FD")
output_label.pack()

# Footer Frame
footer_frame = tk.Frame(root, bg="#1565C0")
footer_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

footer_text = tk.Label(
    footer_frame,
    text="Designed by     Akash Kumar                Shivam     \n                   12303953                   12305957",
    font=("Arial", 10, "italic"),
    bg="#1565C0", fg="white"
)
footer_text.pack(pady=5)

# Run the Application
root.mainloop()
