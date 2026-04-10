import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
def solve_167():
    try:
        # Giả sử nhập hệ số cách nhau bằng dấu phẩy, bậc từ cao đến thấp
        p1 = [float(x) for x in entry_p1.get().split(',')]
        p2 = [float(x) for x in entry_p2.get().split(',')]
        
        m, n = len(p1)-1, len(p2)-1
        res_coeffs = [0] * (m + n + 1)
        
        for i in range(m + 1):
            for j in range(n + 1):
                res_coeffs[i + j] += p1[i] * p2[j]
        
        # Tính trị đa thức tại x bằng Horner
        x = float(entry_x.get())
        val = 0
        for c in res_coeffs:
            val = val * x + c
            
        label_res.configure(text=f"Hệ số kết quả: {res_coeffs}\nTrị tại x={x}: {val:.4f}")
    except:
        label_res.configure(text="Lỗi nhập liệu!", text_color="red")

app = ctk.CTk()
app.title("Bài 167: Đa thức")
app.geometry("400x400")
entry_p1 = ctk.CTkEntry(app, placeholder_text="P1 (vd: 5,-4,7,-2)"); entry_p1.pack(pady=5)
entry_p2 = ctk.CTkEntry(app, placeholder_text="P2 (vd: 3,-2,7)"); entry_p2.pack(pady=5)
entry_x = ctk.CTkEntry(app, placeholder_text="Giá trị x"); entry_x.pack(pady=5)
ctk.CTkButton(app, text="Nhân & Tính", command=solve_167).pack(pady=10)
label_res = ctk.CTkLabel(app, text="", wraplength=350); label_res.pack()
app.mainloop()