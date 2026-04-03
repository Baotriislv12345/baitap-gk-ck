import customtkinter as ctk

def get_pascal(n):
    res = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = res[i-1][j-1] + res[i-1][j]
        res.append(row)
    return res

def solve_146():
    try:
        n = int(entry_n.get())
        if n < 1 or n > 15: raise ValueError
        triangle = get_pascal(n)
        output = ""
        for i, row in enumerate(triangle):
            output += "  " * (n - i) + " ".join(f"{x:2d}" for x in row) + "\n"
        text_res.delete("1.0", "end"); text_res.insert("1.0", output)
    except:
        text_res.insert("1.0", "Nhập n từ 1-15!")

app = ctk.CTk()
app.title("Bài 146: Tam giác Pascal")
app.geometry("500x450")
entry_n = ctk.CTkEntry(app, placeholder_text="Chiều cao n"); entry_n.pack(pady=10)
ctk.CTkButton(app, text="Hiển thị", command=solve_146).pack(pady=5)
text_res = ctk.CTkTextbox(app, height=300, font=("Courier", 12)); text_res.pack(pady=10, padx=10, fill="both")
app.mainloop()