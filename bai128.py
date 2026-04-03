import customtkinter as ctk

def solve_128():
    s = entry_s.get()
    words = s.split()
    if not words: return
    max_len = max(len(w) for w in words)
    longest = [f"{w}[{len(w)}]" for w in words if len(w) == max_len]
    label_res.configure(text=" ".join(longest))

app = ctk.CTk()
app.title("Bài 128: Từ dài nhất")
app.geometry("400x200")
entry_s = ctk.CTkEntry(app, width=300, placeholder_text="Nhập chuỗi..."); entry_s.pack(pady=20)
ctk.CTkButton(app, text="Tìm từ", command=solve_128).pack(pady=10)
label_res = ctk.CTkLabel(app, text=""); label_res.pack()
app.mainloop()