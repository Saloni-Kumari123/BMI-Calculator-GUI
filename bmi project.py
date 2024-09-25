#BMI Calculator Project 

import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        bmi_label.config(text=f"BMI: {bmi:.2f}")
        if bmi < 18.5:
            category_label.config(text="Category: Underweight")
        elif 18.5 <= bmi < 25:
            category_label.config(text="Category: Normal weight")
        elif 25 <= bmi < 30:
            category_label.config(text="Category: Overweight")
        else:
            category_label.config(text="Category: Obese")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid weight and height.")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry('500x400')
root.configure(bg="cyan")


font1=("arial",30,"bold")
font2=("arial",18,"bold")
font3=("arial",15,"bold")


title_lable=tk.Label(root,font=font1,text="BMI Calculator",fg="black",bg="pink")
title_lable.pack()


weight_lable=tk.Label(root,font=font2,text="Weight (kg):",fg="black",bg="light pink")
weight_lable.pack()
weight_entry=tk.Entry(root,font=font3,fg="#000",bg="#fff",width=40)
weight_entry.pack()


height_lable=tk.Label(root,font=font2,text="Height (m):",fg="black",bg="light pink")
height_lable.pack()
height_entry=tk.Entry(root,font=font3,fg="#000",bg="#fff",width=40)
height_entry.pack()


calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, font=font2)
calculate_button.pack()


bmi_label = tk.Label(root, text="BMI: ",bg="light pink", font=font2)
bmi_label.pack()


category_label = tk.Label(root, text="Category: ",bg="light pink", font=font2)
category_label.pack()


root.mainloop()

