import customtkinter as ctk

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None: return Node(val)
    if val < root.data: root.left = insert(root.left, val)
    else: root.right = insert(root.right, val)
    return root

def nlr(root, res):
    if root:
        res.append(str(root.data))
        nlr(root.left, res)
        nlr(root.right, res)

def lnr(root, res):
    if root:
        lnr(root.left, res)
        res.append(str(root.data))
        lnr(root.right, res)

def lrn(root, res):
    if root:
        lrn(root.left, res)
        lrn(root.right, res)
        res.append(str(root.data))

def solve_222():
    try:
        nums = [int(x) for x in entry_nodes.get().split()]
        root = None
        for n in nums: root = insert(root, n)
        
        r_nlr, r_lnr, r_lrn = [], [], []
        nlr(root, r_nlr); lnr(root, r_lnr); lrn(root, r_lrn)
        
        label_res.configure(text=f"NLR: {' '.join(r_nlr)}\nLNR: {' '.join(r_lnr)}\nLRN: {' '.join(r_lrn)}")
    except: pass

app = ctk.CTk()
app.title("Bài 222: Duyệt cây BST")
app.geometry("400x300")
entry_nodes = ctk.CTkEntry(app, width=300, placeholder_text="Nhập các node (vd: 9 3 16 2 5)"); entry_nodes.pack(pady=20)
ctk.CTkButton(app, text="Duyệt cây", command=solve_222).pack(pady=10)
label_res = ctk.CTkLabel(app, text="", justify="left"); label_res.pack()
app.mainloop()