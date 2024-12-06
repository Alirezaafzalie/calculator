import tkinter as tk

# تابع برای افزودن اعداد یا علائم به ورودی
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# تابع برای پاک کردن ورودی
def clear():
    entry.delete(0, tk.END)

# تابع برای محاسبه نتیجه
def calculate():
    try:
        result = eval(entry.get())  # محاسبه ورودی
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ساخت پنجره اصلی
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# ویجت ورودی
entry = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# لیست دکمه‌ها
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0)
]

# ساخت و قرار دادن دکمه‌ها
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=20, height=2, font=("Arial", 14), command=calculate).grid(row=row, column=col, columnspan=4)
    elif text == "C":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: button_click(t)).grid(row=row, column=col)

# اجرای برنامه
root.mainloop()
