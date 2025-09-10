import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x300")
root.title("Geri Sayım")
root.config(bg="blue")

running = False
remaining = 0

# --- Sadece 0-9 ve en fazla 2 hane kabul et ---
def only_digits(P):
    return P.isdigit() and len(P) <= 2 or P == ""

vcmd = (root.register(only_digits), "%P")

hour   = StringVar(value="00")
minute = StringVar(value="00")
second = StringVar(value="00")

hourEntry = Entry(root, width=5, font=("Arial",18,"bold"),
                  textvariable=hour, justify="center", bd=5, fg="black", bg="yellow",
                  validate="key", validatecommand=vcmd)
hourEntry.place(x=45, y=20)

minuteEntry = Entry(root, width=5, font=("Arial",18,"bold"),
                    textvariable=minute, justify="center", bd=5, fg="black", bg="yellow",
                    validate="key", validatecommand=vcmd)
minuteEntry.place(x=117, y=20)

secondEntry = Entry(root, width=5, font=("Arial",18,"bold"),
                    textvariable=second, justify="center", bd=5, fg="black", bg="yellow",
                    validate="key", validatecommand=vcmd)
secondEntry.place(x=190, y=20)

def tick():
    global remaining, running
    if not running:
        return
    if remaining <= 0:
        running = False
        # Doğru kullanım: title, message
        messagebox.showinfo("Geri Sayım", "Süre doldu!")
        return

    mins, secs = divmod(remaining, 60)
    hours, mins = divmod(mins, 60)

    hour.set(f"{hours:02d}")
    minute.set(f"{mins:02d}")
    second.set(f"{secs:02d}")

    remaining -= 1
    root.after(1000, tick)

def submit():
    global running, remaining
    if running:
        return
    try:
        h = int(hour.get() or "0")
        m = int(minute.get() or "0")
        s = int(second.get() or "0")
        if m > 59 or s > 59:
            raise ValueError
    except ValueError:
        messagebox.showerror("Hata", "Lütfen doğru değer gir (hh:mm:ss, 0-59 arası).")
        return

    remaining = h*3600 + m*60 + s
    if remaining <= 0:
        messagebox.showwarning("Uyarı", "Süre 0 olamaz.")
        return

    running = True
    tick()

def stop_timer():
    global running
    running = False

btn = Button(root, text='Start Countdown', font=("Arial",14,"bold"), justify="center",
             fg="black", bg="orange", relief="raised", bd=5, width=15, height=2,
             command=submit)
btn.place(x=55, y=120)

btn_stop = Button(root, text=' Stop ', font=("Arial",14,"bold"), justify="center",
                  fg="black", bg="red", relief="raised", bd=5, width=10, height=1,
                  command=stop_timer)
btn_stop.place(x=85, y=190)

root.mainloop()
