import tkinter as tk
from tkinter import ttk, messagebox
import time

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pomodoro Timer")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg='#2C3E50')
        
        # Pomodoro technique constants (in seconds)
        self.work_time = 25 * 60  # 25 minutes
        self.short_break = 5 * 60  # 5 minutes
        self.long_break = 15 * 60  # 15 minutes
        
        self.current_time = self.work_time
        self.is_running = False
        self.current_session = "Work"
        self.session_count = 0
        
        self.setup_ui()
        self.update_display()
    
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2C3E50')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Pomodoro Timer",
            font=('Arial', 20, 'bold'),
            fg='#ECF0F1',
            bg='#2C3E50'
        )
        title_label.pack(pady=(0, 20))
        
        # Timer display
        self.time_display = tk.Label(
            main_frame,
            text="25:00",
            font=('Arial', 48, 'bold'),
            fg='#E74C3C',
            bg='#2C3E50'
        )
        self.time_display.pack(pady=10)
        
        # Session label
        self.session_label = tk.Label(
            main_frame,
            text="Work Session",
            font=('Arial', 14),
            fg='#BDC3C7',
            bg='#2C3E50'
        )
        self.session_label.pack()
        
        # Session counter
        self.counter_label = tk.Label(
            main_frame,
            text="Sessions completed: 0",
            font=('Arial', 10),
            fg='#95A5A6',
            bg='#2C3E50'
        )
        self.counter_label.pack(pady=(0, 20))
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg='#2C3E50')
        button_frame.pack(pady=10)
        
        # Start/Pause button
        self.start_button = ttk.Button(
            button_frame,
            text="Start",
            command=self.toggle_timer,
            width=10
        )
        self.start_button.grid(row=0, column=0, padx=5)
        
        # Reset button
        self.reset_button = ttk.Button(
            button_frame,
            text="Reset",
            command=self.reset_timer,
            width=10
        )
        self.reset_button.grid(row=0, column=1, padx=5)
        
        # Skip button
        self.skip_button = ttk.Button(
            button_frame,
            text="Skip",
            command=self.skip_session,
            width=10
        )
        self.skip_button.grid(row=0, column=2, padx=5)
        
        # Session buttons frame
        session_frame = tk.Frame(main_frame, bg='#2C3E50')
        session_frame.pack(pady=10)
        
        # Session type buttons
        ttk.Button(
            session_frame,
            text="Work (25 min)",
            command=lambda: self.set_session("Work", self.work_time)
        ).grid(row=0, column=0, padx=5)
        
        ttk.Button(
            session_frame,
            text="Short Break (5 min)",
            command=lambda: self.set_session("Short Break", self.short_break)
        ).grid(row=0, column=1, padx=5)
        
        ttk.Button(
            session_frame,
            text="Long Break (15 min)",
            command=lambda: self.set_session("Long Break", self.long_break)
        ).grid(row=0, column=2, padx=5)
    
    def toggle_timer(self):
        if not self.is_running:
            self.start_timer()
        else:
            self.pause_timer()
    
    def start_timer(self):
        self.is_running = True
        self.start_button.config(text="Pause")
        self.countdown()
    
    def pause_timer(self):
        self.is_running = False
        self.start_button.config(text="Resume")
    
    def reset_timer(self):
        self.is_running = False
        self.start_button.config(text="Start")
        
        if self.current_session == "Work":
            self.current_time = self.work_time
        elif self.current_session == "Short Break":
            self.current_time = self.short_break
        else:
            self.current_time = self.long_break
            
        self.update_display()
    
    def skip_session(self):
        self.is_running = False
        self.start_button.config(text="Start")
        
        if self.current_session == "Work":
            # Move to break
            self.session_count += 1
            if self.session_count % 4 == 0:
                self.set_session("Long Break", self.long_break)
            else:
                self.set_session("Short Break", self.short_break)
        else:
            # Move to work
            self.set_session("Work", self.work_time)
    
    def set_session(self, session_type, duration):
        self.current_session = session_type
        self.current_time = duration
        self.is_running = False
        self.start_button.config(text="Start")
        self.update_display()
    
    def countdown(self):
        if self.is_running and self.current_time > 0:
            self.current_time -= 1
            self.update_display()
            self.root.after(1000, self.countdown)
        elif self.current_time == 0:
            self.session_complete()
    
    def session_complete(self):
        self.is_running = False
        self.start_button.config(text="Start")
        
        # Show completion message
        if self.current_session == "Work":
            self.session_count += 1
            messagebox.showinfo("Session Complete!", 
                              f"Work session finished! Take a break.\nSessions completed: {self.session_count}")
            
            # Auto-start break
            if self.session_count % 4 == 0:
                self.set_session("Long Break", self.long_break)
            else:
                self.set_session("Short Break", self.short_break)
        else:
            messagebox.showinfo("Break Over!", "Break finished! Ready to work?")
            self.set_session("Work", self.work_time)
        
        self.update_display()
    
    def update_display(self):
        """Update the timer display and session information"""
        minutes = self.current_time // 60
        seconds = self.current_time % 60
        time_string = f"{minutes:02d}:{seconds:02d}"
        
        # Update timer display with color coding
        if self.current_session == "Work":
            color = '#E74C3C'  # Red
        else:
            color = '#2ECC71'  # Green
        
        self.time_display.config(text=time_string, fg=color)
        self.session_label.config(text=f"{self.current_session} Session")
        self.counter_label.config(text=f"Sessions completed: {self.session_count}")
    
    def run(self):
        self.root.mainloop()

# Run the application
if __name__ == "__main__":
    app = PomodoroTimer()
    app.run()