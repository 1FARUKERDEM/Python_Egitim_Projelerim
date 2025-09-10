import tkinter
from tkinter import PhotoImage, messagebox, END
import base64

# --- Vigenere-benzeri basit şifreleme ---
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

# --- Callback'lar ---
def save_and_encrypt_notes():
    title = title_entry.get()
    message = input_text.get("1.0", END).strip()
    master_secret = master_secret_entry.get()

    if not title or not message or not master_secret:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
        return

    try:
        message_encrypted = encode(master_secret, message)
    except Exception as e:
        messagebox.showinfo(title="Error!", message=f"Encrypt failed: {e}")
        return

    try:
        with open("mysecret.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{title}\n{message_encrypted}")
        messagebox.showinfo(title="Saved", message="Encrypted note saved to mysecret.txt")
    except Exception as e:
        messagebox.showinfo(title="Error!", message=f"File write failed: {e}")
    finally:
        title_entry.delete(0, END)
        master_secret_entry.delete(0, END)
        input_text.delete("1.0", END)

def decrypt_notes():
    message_encrypted = input_text.get("1.0", END).strip()
    master_secret = master_secret_entry.get()

    if not message_encrypted or not master_secret:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
        return

    try:
        decrypted_message = decode(master_secret, message_encrypted)
        input_text.delete("1.0", END)
        input_text.insert("1.0", decrypted_message)
    except Exception:
        messagebox.showinfo(title="Error!", message="Please make sure of encrypted info.")

# --- UI ---
window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(width=400, height=700)

# Logo (dosya yoksa bu iki satırı yorumla)
try:
    image = PhotoImage(file="Secretlogo.png")
    logo_label = tkinter.Label(window, image=image)
    logo_label.image = image
    logo_label.place(x=90, y=20)
except Exception:
    pass

notes_label_title = tkinter.Label(window, text="Enter your notes title")
notes_label_title.place(x=140, y=260)

title_entry = tkinter.Entry(window, width=40)
title_entry.place(x=80, y=280)

secret_notes_label = tkinter.Label(window, text="Secret your notes")
secret_notes_label.place(x=145, y=300)

input_text = tkinter.Text(window, width=40, height=13, font=("Arial", 12))
input_text.place(x=20, y=330)

master_key_label = tkinter.Label(window, text="Enter Master Key")
master_key_label.place(x=150, y=580)

master_secret_entry = tkinter.Entry(window, width=40, show="*")
master_secret_entry.place(x=80, y=600)

save_encrypt_button = tkinter.Button(window, text="Save & Encrypt", command=save_and_encrypt_notes)
save_encrypt_button.place(x=150, y=630)

decrypt_button = tkinter.Button(window, text="Decrypt", command=decrypt_notes)
decrypt_button.place(x=167, y=660)

window.mainloop()
