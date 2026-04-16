import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Bài 167 - Nhân đa thức")
app.geometry("500x500")

# ===== TITLE =====
ctk.CTkLabel(app, text="NHÂN HAI ĐA THỨC", font=("Arial",18,"bold")).pack(pady=10)

# ===== INPUT =====
e1 = ctk.CTkEntry(app, placeholder_text="Đa thức 1 (vd: 5 -4 7 -2)")
e2 = ctk.CTkEntry(app, placeholder_text="Đa thức 2 (vd: 3 -2 7)")
ex = ctk.CTkEntry(app, placeholder_text="Nhập x")

e1.pack(pady=5)
e2.pack(pady=5)
ex.pack(pady=5)

# ===== RESULT =====
kq = ctk.CTkLabel(app, text="", justify="left")
kq.pack(pady=10)

# ===== LOGIC =====
def multiply(p1, p2):
    res = [0]*(len(p1)+len(p2)-1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            res[i+j] += p1[i]*p2[j]
    return res

def eval_poly(p, x):
    result = 0
    for coef in p:
        result = result*x + coef
    return result

def poly_to_string(p):
    deg = len(p)-1
    s = ""
    for i,coef in enumerate(p):
        if coef == 0: continue
        power = deg - i
        if coef > 0 and s: s += "+"
        if power == 0:
            s += f"{coef}"
        elif power == 1:
            s += f"{coef}x"
        else:
            s += f"{coef}x^{power}"
    return s if s else "0"

def solve():
    try:
        p1 = list(map(int, e1.get().split()))
        p2 = list(map(int, e2.get().split()))
        x = int(ex.get())

        res = multiply(p1, p2)
        value = eval_poly(res, x)

        kq.configure(text=
            f"p1(x) = {poly_to_string(p1)}\n"
            f"p2(x) = {poly_to_string(p2)}\n\n"
            f"Kết quả:\n"
            f"p(x) = {poly_to_string(res)}\n\n"
            f"p({x}) = {value:.4f}"
        )
    except:
        kq.configure(text="❌ Lỗi nhập (đúng format: 5 -4 7 -2)")

# ===== BUTTON =====
ctk.CTkButton(app, text="TÍNH", command=solve).pack(pady=10)

app.mainloop()