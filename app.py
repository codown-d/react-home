import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

# 创建主窗口
root = tk.Tk()
root.title("Tkinter Example")

# 创建一个标签
label = tk.Label(root, text="Hello, World!")
label.pack(pady=10)

# 创建一个按钮
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# 运行主循环
root.mainloop()
