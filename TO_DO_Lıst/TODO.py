import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x600")

# === Tema renkleri ===
BG_COLOR = "#fff9c4"   # açık sarı sticky notes rengi
FG_COLOR = "#333333"   # koyu gri yazı
BTN_COLOR = "#ffe082"  # buton için biraz daha koyu sarı

root.configure(bg=BG_COLOR)

# --- Giriş kutusu (Entry) ---
entry = tk.Entry(root, font=("Arial", 12),
                 bg="white", fg=FG_COLOR, relief="flat")
entry.pack(fill="x", padx=10, pady=10)

# --- Liste (Listbox) ---
listbox = tk.Listbox(root, font=("Arial", 12),
                     bg=BG_COLOR, fg=FG_COLOR,
                     selectbackground="#fdd835",             # seçili satır rengi
                     relief="flat", activestyle="none")      # "flat" kenarlıkları kaldırıp sade bir görüntü veriyor
listbox.pack(fill="both", expand=True, padx=10, pady=10)

edit_index = None

def ekle(event=None):
    global edit_index
    text = entry.get().strip()
    if not text:
        return
    if edit_index is None:
        num = listbox.size() + 1  # liste boyu + 1 = yeni sıra no
        listbox.insert("end", f"{num}. {text}")
    else:
        listbox.delete(edit_index)
        listbox.insert(edit_index, text)
        edit_index = None
        btn_ekle.config(text="Ekle")
    entry.delete(0, "end")
    entry.focus_set()

def sil(event=None):
    global edit_index
    secim = listbox.curselection()
    if not secim: return
    listbox.delete(secim[0])
    edit_index = None
    btn_ekle.config(text="Ekle")

def duzenle(event=None):
    global edit_index
    secim = listbox.curselection()
    if not secim: return
    edit_index = secim[0]
    entry.delete(0, "end")
    entry.insert(0, listbox.get(edit_index))
    btn_ekle.config(text="Güncelle")
    entry.focus_set()
    entry.icursor("end")

# --- Butonlar (sticky notes renkli) ---
btn_ekle = tk.Button(root, text="Ekle", command=ekle,
                     font=("Arial", 14, "bold"),
                     width=15, height=2,
                     bg=BTN_COLOR, fg=FG_COLOR, relief="flat")
btn_ekle.pack(pady=5)

btn_sil = tk.Button(root, text="Sil", command=sil,
                    font=("Arial", 14, "bold"),
                    width=15, height=2,
                    bg=BTN_COLOR, fg=FG_COLOR, relief="flat")
btn_sil.pack(pady=5)

# --- Kısayollar ---
entry.bind("<Return>", ekle)
listbox.bind("<Delete>", sil)
listbox.bind("<Double-Button-1>", duzenle)

entry.focus_set()
root.mainloop()





