import tkinter as tk
from tkinter import messagebox
import hashlib

def show_selected_courses(courses):
    root = tk.Tk()
    root.title("Selecione quantos cursos quiser")

    checkboxes = []
    selected_courses = []

    def on_ok():
        selected_courses[:] = [course for course, var in zip(courses, checkboxes) if var.get()]
        if selected_courses:
            messagebox.showinfo("Selected Courses", f"You selected: {', '.join(selected_courses)}")
        else:
            messagebox.showwarning("No Selection", "No courses selected!")
        root.destroy()

    for course in courses:
        var = tk.BooleanVar()
        checkboxes.append(var)
        cb = tk.Checkbutton(root, text=course, variable=var)
        cb.pack(anchor='w')

    ok_button = tk.Button(root, text="OK", command=on_ok)
    ok_button.pack(pady=10)

    root.mainloop()

    return selected_courses