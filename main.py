
import tkinter as tk
from tkinter import messagebox

class StopwatchTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch and Timer")
        self.root.geometry("400x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        self.stopwatch_seconds = 0
        self.stopwatch_running = False
        self.stopwatch_job = None

        self.timer_seconds = 0
        self.timer_running = False
        self.timer_job = None

        title = tk.Label(
            root, text="STOPWATCH & TIMER",
            font=("Arial", 18, "bold"),
            bg="#1e1e2f", fg="white"
        )
        title.pack(pady=15)

        # Stopwatch display
        tk.Label(
            root, text="STOPWATCH",
            font=("Arial", 12, "bold"),
            bg="#1e1e2f", fg="#00d4ff"
        ).pack()

        self.stopwatch_display = tk.Label(
            root, text="00:00:00",
            font=("Arial", 30, "bold"),
            bg="#1e1e2f", fg="white"
        )
        self.stopwatch_display.pack(pady=5)

        sw_buttons = tk.Frame(root, bg="#1e1e2f")
        sw_buttons.pack(pady=5)

        tk.Button(
            sw_buttons, text="Start",
            command=self.start_stopwatch,
            width=8, bg="#28a745", fg="white"
        ).grid(row=0, column=0, padx=4)

        tk.Button(
            sw_buttons, text="Stop",
            command=self.stop_stopwatch,
            width=8, bg="#dc3545", fg="white"
        ).grid(row=0, column=1, padx=4)

        tk.Button(
            sw_buttons, text="Reset",
            command=self.reset_stopwatch,
            width=8, bg="#6c757d", fg="white"
        ).grid(row=0, column=2, padx=4)

        # Countdown timer
        tk.Label(
            root, text="COUNTDOWN TIMER",
            font=("Arial", 12, "bold"),
            bg="#1e1e2f", fg="#ffd166"
        ).pack(pady=(20, 5))

        input_frame = tk.Frame(root, bg="#1e1e2f")
        input_frame.pack()

        self.minutes_entry = tk.Entry(
            input_frame, width=6, justify="center",
            font=("Arial", 13)
        )
        self.minutes_entry.insert(0, "1")
        self.minutes_entry.grid(row=0, column=0, padx=5)

        tk.Label(
            input_frame, text="minutes",
            bg="#1e1e2f", fg="white"
        ).grid(row=0, column=1)

        self.seconds_entry = tk.Entry(
            input_frame, width=6, justify="center",
            font=("Arial", 13)
        )
        self.seconds_entry.insert(0, "0")
        self.seconds_entry.grid(row=0, column=2, padx=5)

        tk.Label(
            input_frame, text="seconds",
            bg="#1e1e2f", fg="white"
        ).grid(row=0, column=3)

        self.timer_display = tk.Label(
            root, text="01:00",
            font=("Arial", 28, "bold"),
            bg="#1e1e2f", fg="#ffd166"
        )
        self.timer_display.pack(pady=8)

        timer_buttons = tk.Frame(root, bg="#1e1e2f")
        timer_buttons.pack(pady=5)

        tk.Button(
            timer_buttons, text="Start",
            command=self.start_timer,
            width=9, bg="#28a745", fg="white"
        ).grid(row=0, column=0, padx=4)

        tk.Button(
            timer_buttons, text="Stop",
            command=self.stop_timer,
            width=9, bg="#dc3545", fg="white"
        ).grid(row=0, column=1, padx=4)

        tk.Button(
            timer_buttons, text="Reset",
            command=self.reset_timer,
            width=9, bg="#6c757d", fg="white"
        ).grid(row=0, column=2, padx=4)

    # Stopwatch functions
    def start_stopwatch(self):
        if not self.stopwatch_running:
            self.stopwatch_running = True
            self.update_stopwatch()

    def update_stopwatch(self):
        if self.stopwatch_running:
            self.stopwatch_seconds += 1
            hours = self.stopwatch_seconds // 3600
            minutes = (self.stopwatch_seconds % 3600) // 60
            seconds = self.stopwatch_seconds % 60

            self.stopwatch_display.config(
                text=f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            )
            self.stopwatch_job = self.root.after(
                1000, self.update_stopwatch
            )

    def stop_stopwatch(self):
        self.stopwatch_running = False
        if self.stopwatch_job is not None:
            self.root.after_cancel(self.stopwatch_job)
            self.stopwatch_job = None

    def reset_stopwatch(self):
        self.stop_stopwatch()
        self.stopwatch_seconds = 0
        self.stopwatch_display.config(text="00:00:00")

    # Countdown timer functions
    def start_timer(self):
        if self.timer_running:
            return

        if self.timer_seconds <= 0:
            try:
                minutes = int(self.minutes_entry.get())
                seconds = int(self.seconds_entry.get())

                if minutes < 0 or not 0 <= seconds <= 59:
                    raise ValueError

                self.timer_seconds = minutes * 60 + seconds

                if self.timer_seconds <= 0:
                    raise ValueError

            except ValueError:
                messagebox.showerror(
                    "Invalid Input",
                    "Enter valid minutes and seconds (0-59)."
                )
                return

        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.timer_running:
            minutes = self.timer_seconds // 60
            seconds = self.timer_seconds % 60

            self.timer_display.config(
                text=f"{minutes:02d}:{seconds:02d}"
            )

            if self.timer_seconds <= 0:
                self.timer_running = False
                self.timer_job = None
                messagebox.showinfo(
                    "Timer Finished", "Time is up!"
                )
                return

            self.timer_seconds -= 1
            self.timer_job = self.root.after(
                1000, self.update_timer
            )

    def stop_timer(self):
        self.timer_running = False
        if self.timer_job is not None:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

    def reset_timer(self):
        self.stop_timer()
        self.timer_seconds = 0

        try:
            minutes = int(self.minutes_entry.get())
            seconds = int(self.seconds_entry.get())

            if minutes < 0 or not 0 <= seconds <= 59:
                raise ValueError

            self.timer_display.config(
                text=f"{minutes:02d}:{seconds:02d}"
            )

        except ValueError:
            self.timer_display.config(text="00:00")


if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchTimer(root)
    root.mainloop()
