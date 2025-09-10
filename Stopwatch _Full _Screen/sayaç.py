import time
import tkinter as tk

# ---- DURUM ----
running = False
elapsed = 0.0
last_ts = time.monotonic()

def format_time(sec: float) -> str:
    """Saniyeyi 00:00 veya 00:00:00 formatına çevirir."""
    if sec < 0:
        sec = 0
    total = int(sec)
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    return f"{h:02d}:{m:02d}:{s:02d}" if h > 0 else f"{m:02d}:{s:02d}"

def refresh_label():
    """Label içindeki yazıyı günceller."""
    label.config(text=format_time(elapsed))

def start():
    """Kronometreyi başlatır / devam ettirir."""
    global running, last_ts
    if not running:
        running = True
        last_ts = time.monotonic()

def pause():
    """Kronometreyi duraklatır."""
    global running
    running = False

def reset():
    """Süreyi sıfırlar."""
    global running, elapsed
    running = False
    elapsed = 0.0
    refresh_label()

def tick():
    """~100 ms'de bir çağrılır; çalışıyorsa süreyi arttırır."""
    global last_ts, elapsed
    now = time.monotonic()
    if running:
        dt = now - last_ts
        elapsed += dt
        refresh_label()
    last_ts = now
    root.after(100, tick)

# ---- UI ----
root = tk.Tk()
root.title("Kronometre")
root.configure(bg="black")
root.geometry("900x500")

label = tk.Label(root, text="00:00", fg="white", bg="black",
                 font=("Helvetica", 120, "bold"))
label.pack(expand=True, fill="both")

btn_bar = tk.Frame(root, bg="#111")
btn_bar.pack(side="bottom", fill="x")

def make_btn(text, cmd):
    return tk.Button(btn_bar, text=text, command=cmd,
                     bg="#222", fg="white",
                     activebackground="#333", activeforeground="white",
                     relief="flat", padx=12, pady=10)

btn_start  = make_btn("Başlat", start)
btn_pause  = make_btn("Duraklat", pause)
btn_reset  = make_btn("Sıfırla", reset)

for b in (btn_start, btn_pause, btn_reset):
    b.pack(side="left", expand=True, fill="x", padx=4, pady=6)

refresh_label()
tick()
root.mainloop()
