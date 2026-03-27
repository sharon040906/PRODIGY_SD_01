import tkinter as tk

def convert():
    temp = float(entry.get())
    u = unit.get()

    if u == "C":
        f = (temp * 9/5) + 32
        k = temp + 273.15
        result.config(text=f"F: {f:.2f} | K: {k:.2f}")

    elif u == "F":
        c = (temp - 32) * 5/9
        k = c + 273.15
        result.config(text=f"C: {c:.2f} | K: {k:.2f}")

    elif u == "K":
        c = temp - 273.15
        f = (c * 9/5) + 32
        result.config(text=f"C: {c:.2f} | F: {f:.2f}")

def reset():
    entry.delete(0, tk.END)
    result.config(text="")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x250")

tk.Label(root, text="Enter Temperature").pack()

entry = tk.Entry(root)
entry.pack()

unit = tk.StringVar(value="C")

tk.Radiobutton(root, text="Celsius", variable=unit, value="C").pack()
tk.Radiobutton(root, text="Fahrenheit", variable=unit, value="F").pack()
tk.Radiobutton(root, text="Kelvin", variable=unit, value="K").pack()

tk.Button(root, text="Convert", command=convert).pack()

result = tk.Label(root, text="")
result.pack()

tk.Button(root, text="Reset", command=reset).pack()

root.mainloop()