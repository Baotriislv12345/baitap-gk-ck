import customtkinter as ctk

class Employee:
    def __init__(self, id_num, first_name, last_name, birthday, salary):
        self.id = id_num
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.salary = salary

def solve_199():
    data = text_input.get("1.0", "end-1c").strip().split('\n')
    employees = []
    try:
        for line in data:
            # Định dạng: ID: Firstname Lastname: Birthday: Salary
            parts = line.split(':')
            name_parts = parts[1].strip().split()
            fname = name_parts[0]
            lname = " ".join(name_parts[1:])
            employees.append(Employee(parts[0], fname, lname, parts[2], parts[3]))
        
        # Sắp xếp theo firstname, sau đó lastname
        employees.sort(key=lambda x: (x.first_name, x.last_name))
        
        res = "Danh sách sau khi sắp xếp:\n"
        for e in employees:
            res += f"{e.id}: {e.first_name} {e.last_name}: {e.birthday}: {e.salary}\n"
        label_res.configure(text=res)
    except:
        label_res.configure(text="Lỗi định dạng dữ liệu!", text_color="red")

app = ctk.CTk()
app.title("Bài 199: Sắp xếp nhân viên")
app.geometry("500x500")

ctk.CTkLabel(app, text="Nhập liệu (ID: First Last: Birth: Salary):").pack(pady=5)
text_input = ctk.CTkTextbox(app, height=150)
text_input.pack(pady=5, padx=10, fill="x")
text_input.insert("1.0", "4424: Tom Jones: 5/12/66:54335\n1654: Jackie Chan: 7/22/54:65000\n5346: Mary Adams: 11/4/63:28765")

ctk.CTkButton(app, text="Sắp xếp (qsort)", command=solve_199).pack(pady=10)
label_res = ctk.CTkLabel(app, text="", justify="left")
label_res.pack(pady=10)

app.mainloop()