import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Bài 222 - BST DFS")
app.geometry("500x400")

# ===== TITLE =====
ctk.CTkLabel(app, text="DUYỆT BST (DFS - PREORDER)", 
             font=("Arial",18,"bold")).pack(pady=10)

# ===== INPUT =====
entry = ctk.CTkEntry(app, width=300, 
                     placeholder_text="Nhập dãy (vd: 5 3 7 2 4 6 8)")
entry.pack(pady=10)

# ===== RESULT =====
result = ctk.CTkLabel(app, text="", justify="left")
result.pack(pady=10)

# ===== NODE =====
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ===== INSERT BST =====
def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# ===== DFS PREORDER =====
def preorder(root, res):
    if root:
        res.append(root.val)
        preorder(root.left, res)
        preorder(root.right, res)

# ===== SOLVE =====
def solve():
    try:
        arr = list(map(int, entry.get().split()))
        root = None

        for x in arr:
            root = insert(root, x)

        res = []
        preorder(root, res)

        result.configure(text=
            f"Input: {arr}\n"
            f"DFS (Preorder): {res}"
        )
    except:
        result.configure(text="❌ Lỗi nhập")

# ===== BUTTON =====
ctk.CTkButton(app, text="DUYỆT DFS", command=solve).pack(pady=10)

app.mainloop()