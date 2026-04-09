import customtkinter as ctk

def solve_13():
    try:
        d = int(entry_d.get())
        m = int(entry_m.get())
        y = int(entry_y.get())
        
        if y < 1582:
            label_res.configure(text="Lịch Gregorian bắt đầu từ 1582", text_color="red")
            return
            
        # Xác định số ngày tối đa trong tháng
        top = 31
        if m in [4, 6, 9, 11]: top = 30
        elif m == 2:
            top = 29 if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else 28
            
        if m < 1 or m > 12 or d < 1 or d > top:
            label_res.configure(text="Ngày/tháng không hợp lệ!", text_color="red")
            return

        # Công thức Zeller
        a = (14 - m) // 12
        y0 = y - a
        m0 = m + 12 * a - 2
        dayofweek = (d + y0 + y0//4 - y0//100 + y0//400 + (31*m0)//12) % 7
        
        days = ["Chúa nhật", "Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy"]
        label_res.configure(text=f"Hợp lệ - {days[dayofweek]}", text_color="green")
    except:
        label_res.configure(text="Vui lòng nhập số nguyên!", text_color="red")

app = ctk.CTk()
app.title("Bài 13: Lịch Gregorian")
app.geometry("300x350")

ctk.CTkLabel(app, text="Ngày:").pack(pady=5)
entry_d = ctk.CTkEntry(app)
entry_d.pack()

ctk.CTkLabel(app, text="Tháng:").pack(pady=5)
entry_m = ctk.CTkEntry(app)
entry_m.pack()

ctk.CTkLabel(app, text="Năm:").pack(pady=5)
entry_y = ctk.CTkEntry(app)
entry_y.pack()

ctk.CTkButton(app, text="Kiểm tra", command=solve_13).pack(pady=20)
label_res = ctk.CTkLabel(app, text="")
label_res.pack()

app.mainloop() 