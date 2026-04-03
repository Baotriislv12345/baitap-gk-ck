import customtkinter as ctk
import random

def solve_105():
    try:
        n = int(entry_n.get())
        m = int(entry_m.get())
        A = [[random.randint(-10, 10) for _ in range(m)] for _ in range(n)]
        total_sum = sum(sum(row) for row in A)
        
        row_sums = [sum(row) for row in A]
        col_sums = [sum(A[i][j] for i in range(n)) for j in range(m)]
        
        B = [[total_sum - (row_sums[i] + col_sums[j] - A[i][j]) for j in range(m)] for i in range(n)]
        
        res = "Ma trận A:\n" + "\n".join([str(r) for r in A])
        res += "\n\nMa trận B:\n" + "\n".join([str(r) for r in B])
        text_res.delete("1.0", "end"); text_res.insert("1.0", res)
    except: pass

app = ctk.CTk()
app.title("Bài 105: Tính ma trận B")
app.geometry("450x500")
entry_n = ctk.CTkEntry(app, placeholder_text="Số dòng"); entry_n.pack(pady=5)
entry_m = ctk.CTkEntry(app, placeholder_text="Số cột"); entry_m.pack(pady=5)
ctk.CTkButton(app, text="Tạo & Tính", command=solve_105).pack(pady=10)
text_res = ctk.CTkTextbox(app, height=300); text_res.pack(pady=10, fill="both", padx=10)
app.mainloop()