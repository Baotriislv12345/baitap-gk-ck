import customtkinter as ctk

def solve_202():
    try:
        nums = [int(x) for x in entry_list.get().split()]
        res = []
        for x in nums:
            res.append(x)
            if x % 2 == 0:
                res.append(0)
        label_res.configure(text=f"Kết quả: {' -> '.join(map(str, res))}")
    except: pass

app = ctk.CTk()
app.title("Bài 202: LinkedList chèn 0")
app.geometry("400x250")
entry_list = ctk.CTkEntry(app, width=300, placeholder_text="Nhập dãy số cách nhau khoảng trắng"); entry_list.pack(pady=20)
ctk.CTkButton(app, text="Thực hiện", command=solve_202).pack(pady=10)
label_res = ctk.CTkLabel(app, text=""); label_res.pack()
app.mainloop()