import customtkinter as ctk

def solve_100():
    try:
        data = text_area.get("1.0", "end-1c")
        matrix = [[int(x) for x in line.split()] for line in data.strip().split('\n')]
        
        zeros = sum(row.count(0) for row in matrix)
        total = len(matrix) * len(matrix[0])
        
        if zeros > total / 2:
            label_res.configure(text=f"Ma trận thưa ({zeros}/{total} số 0)", text_color="green")
        else:
            label_res.configure(text=f"Không thưa ({zeros}/{total} số 0)", text_color="yellow")
    except:
        label_res.configure(text="Lỗi định dạng ma trận!", text_color="red")

app = ctk.CTk()
app.title("Bài 100: Ma trận thưa")
app.geometry("400x400")
ctk.CTkLabel(app, text="Nhập ma trận (dùng khoảng trắng và xuống dòng):").pack(pady=5)
text_area = ctk.CTkTextbox(app, height=200); text_area.pack(pady=10)
ctk.CTkButton(app, text="Kiểm tra", command=solve_100).pack(pady=10)
label_res = ctk.CTkLabel(app, text=""); label_res.pack()
app.mainloop()