import customtkinter as ctk

def solve_48():
    try:
        n = int(entry_n.get())
        if n <= 0: raise ValueError
        
        # Ước lẻ lớn nhất
        odd_max = n
        while odd_max % 2 == 0:
            odd_max //= 2
            
        # Ước lớn nhất là lũy thừa của 2
        pow2_max = 1
        while n % (pow2_max * 2) == 0:
            pow2_max *= 2
            
        label_res.configure(text=f"Ước lẻ lớn nhất: {odd_max}\nƯớc lũy thừa 2 lớn nhất: {pow2_max}")
    except:
        label_res.configure(text="Nhập số nguyên dương!", text_color="red")

app = ctk.CTk()
app.title("Bài 48: Ước số đặc biệt")
app.geometry("300x250")
ctk.CTkLabel(app, text="Nhập n:").pack(pady=10)
entry_n = ctk.CTkEntry(app); entry_n.pack()
ctk.CTkButton(app, text="Tìm", command=solve_48).pack(pady=20)
label_res = ctk.CTkLabel(app, text=""); label_res.pack()
app.mainloop()