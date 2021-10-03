import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

if __name__ == '__main__':
    def LoginButton():
        identity = rt.identity.get()
        u = rt.username.get()
        p = rt.password.get()
        if len(u) == 0 or len(p) == 0:
            messagebox.showerror('提示:', '输入信息为空')
        else:
            messagebox.showinfo('提示:', '身份: %s\n用户名: %s\n密码为: %s\n' % (identity, u, p))


    def GetIdentity(*args):
        identity = rt.identity.get()
        print(identity)


    # 主窗口
    rt = tk.Tk()
    rt.geometry('300x300')

    # 变量
    rt.username = tk.StringVar()
    rt.password = tk.StringVar()
    rt.identity = tk.StringVar()
    # 身份下拉框
    f0 = tk.Frame(rt)
    tk.Label(f0, text='身份:  ').grid(row=0, column=0, padx=(5,30))
    identityBox = ttk.Combobox(f0, textvariable=rt.identity, values=['管理员', '用户', '其他'],width=10)
    identityBox.grid(row=0, column=1)
    identityBox.current(1)
    identityBox.bind("<<ComboboxSelected>>", GetIdentity)
    f0.grid(padx=0,pady=20)
    # 账号
    f1 = tk.Frame(rt)
    tk.Label(f1, text='账号:  ').grid(row=0, column=0, padx=30)
    tk.Entry(f1, textvariable=rt.username).grid(row=0, column=1)
    f1.grid(pady=20)

    # 密码
    f2 = tk.Frame(rt)
    tk.Label(f2, text='密码:  ').grid(row=1, column=0, padx=30)
    tk.Entry(f2, show='*', textvariable=rt.password).grid(row=1, column=1)
    f2.grid(pady=20)

    # 登录按钮
    tk.Button(rt, text='登录', command=LoginButton).grid(pady=30)
    rt.mainloop()
