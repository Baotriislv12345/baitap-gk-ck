import customtkinter as ctk

def solve_24():
    s_n = entry_n.get()
    if not s_n.isdigit():
        label_res.configure(text="Vui lòng nhập số tự nhiên!", text_color="red")
        return
    
    n = int(s_n)
    digits = [int(d) for d in s_n]
    res = (f"Số chữ số: {len(s_n)}\n"
           f"Chữ số cuối: {digits[-1]}\n"
           f"Chữ số đầu: {digits[0]}\n"
           f"Tổng chữ số: {sum(digits)}\n"
           f"Số đảo ngược: {s_n[::-1]}")
    label_res.configure(text=res, text_color="dark")

app = ctk.CTk()
app.title("Bài 24: Phân tích số n")
app.geometry("300x300")

ctk.CTkLabel(app, text="Nhập n:").pack(pady=10)
entry_n = ctk.CTkEntry(app)
entry_n.pack()

ctk.CTkButton(app, text="Tính toán", command=solve_24).pack(pady=20)
label_res = ctk.CTkLabel(app, text="", justify="left")
label_res.pack()

app.mainloop()