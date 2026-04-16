import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Bài 202 - Linked List")
app.geometry("500x400")

# ===== TITLE =====
ctk.CTkLabel(app, text="CHÈN 0 SAU SỐ CHẴN (ĐỆ QUY)", 
             font=("Arial",18,"bold")).pack(pady=10)

# ===== INPUT =====
entry = ctk.CTkEntry(app, width=300, 
                     placeholder_text="Nhập dãy (vd: 1 2 4 3 6)")
entry.pack(pady=10)

# ===== RESULT =====
result = ctk.CTkLabel(app, text="", justify="left")
result.pack(pady=10)

# ===== RECURSION LOGIC =====
def insert_zero_recursive(arr, i=0):
    if i >= len(arr):
        return arr
    
    if arr[i] % 2 == 0:
        arr.insert(i+1, 0)
        return insert_zero_recursive(arr, i+2)
    else:
        return insert_zero_recursive(arr, i+1)

# ===== SOLVE =====
def solve():
    try:
        arr = list(map(int, entry.get().split()))
        res = insert_zero_recursive(arr.copy())

        result.configure(text=
            f"Ban đầu: {arr}\n"
            f"Kết quả: {res}"
        )
    except:
        result.configure(text="❌ Lỗi nhập")

# ===== BUTTON =====
ctk.CTkButton(app, text="XỬ LÝ", command=solve).pack(pady=10)

app.mainloop()