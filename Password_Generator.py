import tkinter as tk
from tkinter import StringVar, IntVar
from tkinter import messagebox
import random
import string

class PassGen:
    def __init__(self, master):
        self.m = master
        self.m.title("Password Generator")

        self.l = IntVar()
        self.l.set(12)
        self.u = IntVar()
        self.lc = IntVar()
        self.d = IntVar()
        self.s = IntVar()
        self.p = StringVar()

        self.create_widgets()

    def create_widgets(self):

        tk.Label(self.m, text="Password Length:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.m, textvariable=self.l).grid(row=0, column=1, padx=10, pady=5)

        tk.Checkbutton(self.m, text="Uppercase", variable=self.u).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Checkbutton(self.m, text="Lowercase", variable=self.lc).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        tk.Checkbutton(self.m, text="Digits", variable=self.d).grid(row=3, column=0, sticky="w", padx=10, pady=5)
        tk.Checkbutton(self.m, text="Symbols", variable=self.s).grid(row=4, column=0, sticky="w", padx=10, pady=5)

        tk.Button(self.m, text="Generate Password", command=self.gen_pass).grid(row=5, column=0, columnspan=2, pady=10)

        tk.Entry(self.m, textvariable=self.p, state='readonly', justify='center').grid(row=6, column=0, columnspan=2, pady=5)

        tk.Button(self.m, text="Copy to Clipboard", command=self.copy).grid(row=7, column=0, columnspan=2, pady=10)

    def gen_pass(self):

        u_chars = string.ascii_uppercase if self.u.get() else ""
        lc_chars = string.ascii_lowercase if self.lc.get() else ""
        d_chars = string.digits if self.d.get() else ""
        s_chars = string.punctuation if self.s.get() else ""

        all_chars = u_chars + lc_chars + d_chars + s_chars

        if not all_chars:
            messagebox.showwarning("Warning", "Select at least one complexity option.")
            return

        generated_password = ''.join(random.choice(all_chars) for _ in range(self.l.get()))

        self.p.set(generated_password)

    def copy(self):

        self.m.clipboard_clear()
        self.m.clipboard_append(self.p.get())
        self.m.update()
        messagebox.showinfo("Copied", "Password copied to clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PassGen(root)
    root.mainloop()