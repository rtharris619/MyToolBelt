import tkinter as tk
import secrets
import string


window = tk.Tk()
window.title("My Toolbelt")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


def create_menu():
    menu_bar = tk.Menu(master=window)
    window.config(menu=menu_bar)

    file_menu = tk.Menu(master=menu_bar)
    file_menu.add_command(label="Exit", command=quit)

    tools_menu = tk.Menu(master=menu_bar)
    tools_menu.add_command(label="Password Generator", command=open_password_generator)

    menu_bar.add_cascade(label="File", menu=file_menu)
    menu_bar.add_cascade(label="Tools", menu=tools_menu)


def generate_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))

    txt_result.delete("1.0", tk.END)
    txt_result.insert(tk.END, password)


def open_password_generator():
    frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_generate = tk.Button(
        master=frm_buttons,
        text="Generate Password",
        command=generate_password
    )
    frm_buttons.grid(row=0, column=0, sticky="ns")
    btn_generate.grid(row=0, column=0, padx=20, pady=20)
    txt_result.grid(row=1, column=0)


txt_result = tk.Text(master=window, height=1, borderwidth=0)


create_menu()

window.mainloop()
