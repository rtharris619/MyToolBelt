import tkinter as tk
import secrets
import string


window = tk.Tk()
window.title("My Toolbelt")
window.geometry('900x600')
window.rowconfigure([0, 1, 2, 3], weight=1)
window.columnconfigure([0, 1, 2], weight=1)


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

    clear_password()
    txt_result.insert(tk.END, password)


def clear_password():
    txt_result.delete("1.0", tk.END)


def open_password_generator():
    frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_generate = tk.Button(
        master=frm_buttons,
        text="Generate Password",
        command=generate_password
    )
    btn_clear = tk.Button(
        master=frm_buttons,
        text="Clear",
        command=clear_password
    )
    frm_buttons.grid(row=0, column=0, padx=10, pady=10, sticky="n")
    btn_generate.grid(row=0, column=0, padx=10, pady=10, sticky="n")
    btn_clear.grid(row=1, column=0, padx=10, pady=10, sticky="n")
    txt_result.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


txt_result = tk.Text(master=window, height=1, borderwidth=0, relief=tk.RAISED, bd=2)


create_menu()

window.mainloop()
