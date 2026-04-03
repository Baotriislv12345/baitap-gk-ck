import customtkinter as ctk
import random
import math

def solve_62():
    try:
        n = int(entry_n.get())
        a = [random.randint(10, 20) for _ in range(n)]
        
        s1 = sum(a[i] for i in range(n) if i % 2 != 0 and a[i] % 2 == 0)
        s2 = sum(a[i] for i in range(n) if i % 2 == 0 and a[i] % 2 != 0)
        
        coprimes = []
        for i in range(n):
            for j in range(i + 1, n):
                if math.gcd(a[i], a[j]) == 1:
                    coprimes.append(f"({a[i]}, {a[j]})")
        
        res = f"Mảng: {a}\n"
        res += f"Tổng chẵn vị trí lẻ: {s1}\n"
        res += f"Tổng lẻ vị trí chẵn: {s2}\n"
        res += f"Cặp nguyên tố cùng nhau: {', '.join(coprimes) if coprimes else 'Không có'}"
        label_res.configure(text=res)
    except:
        label_res.configure(text="Nhập n hợp lệ!", text_color="red")

app = ctk.CTk()
app.title("Bài 62: Mảng Coprime")
app.geometry("400x350")
ctk.CTkLabel(app, text="Nhập n:").pack(pady=5)
entry_n = ctk.CTkEntry(app); entry_n.pack()
ctk.CTkButton(app, text="Tạo mảng & Kiểm tra", command=solve_62).pack(pady=15)
label_res = ctk.CTkLabel(app, text="", wraplength=350); label_res.pack()
app.mainloop()