import tkinter as tk

# login reading from file
def read_file():
    file = open("users.txt", "r")
    data = file.read()
    file.close()
    return data


def write_file(username, password):
    file = open("users.txt", "a")
    file.write(username + "," + password + "\n")
    file.close()


def main():

    def login():
        username = username_entry.get()
        password = password_entry.get()
        data = read_file()

        if username + "," + password in data:
            result_label.config(text="Login Successful")
        else:
            result_label.config(text="Invalid Username or Password")

    def signup():
        username = username_entry.get()
        password = password_entry.get()
        write_file(username, password)
        result_label.config(text="Account Created")

    tk.Label(root, text="Username").pack()

    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()

    password_entry = tk.Entry(root)
    password_entry.pack()

    tk.Button(root, text="Login", command=login).pack()
    tk.Button(root, text="Signup", command=signup).pack()

    result_label = tk.Label(root, text="")
    result_label.pack()


root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

main()

root.mainloop()