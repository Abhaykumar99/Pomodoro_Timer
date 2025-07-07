from tkinter import *

# ── Constants ─────────────────────────────
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


def count_down(count):
    global timer
    mins = count // 60
    secs = count % 60
    canvas.itemconfig(timer_text, text=f"{mins:02}:{secs:02}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # Add a checkmark after each work session
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        check_marks.config(text=marks)


# ── Window ────────────────────────────────
window = Tk()
window.title("Day 28 – Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Title label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

# Canvas with tomato emoji as background
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(103, 130, text="00:00",
                                fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons
start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

# Checkmarks for completed sessions
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_marks.grid(row=3, column=1)

window.mainloop()
