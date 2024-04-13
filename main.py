import tkinter as tk


calculation = ""


def append_to_calculation(add):
    global calculation
    calculation += str(add)
    text_result.insert(tk.END, add)

def evaluate():
    global calculation
    txtin = text_result.get(1.0, "end-1c")
    calculation += str(txtin)

    try:
        calculation = str(eval(txtin))
        text_result.delete(1.0, "end")
        text_result.insert(1.0,calculation)
    except:
        clear()
        text_result.insert(1.0, "Error")

def clear():
    global calculation
    calculation=""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x275")
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

btn1 = tk.Button(root, text = "1", command = lambda: append_to_calculation(1), width=5, font=("Arial",14))
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text = "2", command = lambda: append_to_calculation(2), width=5, font=("Arial",14))
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text = "3", command = lambda: append_to_calculation(3), width=5, font=("Arial",14))
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text = "4", command = lambda: append_to_calculation(4), width=5, font=("Arial",14))
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text = "5", command = lambda: append_to_calculation(5), width=5, font=("Arial",14))
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text = "6", command = lambda: append_to_calculation(6), width=5, font=("Arial",14))
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text = "7", command = lambda: append_to_calculation(7), width=5, font=("Arial",14))
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text = "8", command = lambda: append_to_calculation(8), width=5, font=("Arial",14))
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text = "9", command = lambda: append_to_calculation(9), width=5, font=("Arial",14))
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text = "0", command = lambda: append_to_calculation(0), width=5, font=("Arial",14))
btn0.grid(row=5, column=2)
btn_p = tk.Button(root, text = "+", command = lambda: append_to_calculation("+"), width=5, font=("Arial",14))
btn_p.grid(row=2, column=4)
btn_s = tk.Button(root, text = "-", command = lambda: append_to_calculation("-"), width=5, font=("Arial",14))
btn_s.grid(row=3, column=4)
btn_m = tk.Button(root, text = "*", command = lambda: append_to_calculation("*"), width=5, font=("Arial",14))
btn_m.grid(row=4, column=4)
btn_d = tk.Button(root, text = "/", command = lambda: append_to_calculation("/"), width=5, font=("Arial",14))
btn_d.grid(row=5, column=4)
btn_ob = tk.Button(root, text="(", command = lambda: append_to_calculation("("), width=5, font=("Arial",14))
btn_ob.grid(row=5, column=1)
btn_cb = tk.Button(root, text=")", command=lambda: append_to_calculation(")"), width=5, font=("Arial",14))
btn_cb.grid(row=5, column=3)
btn_e = tk.Button(root, text = "=", command = lambda: evaluate(), width=11, font=("Arial",14))
btn_e.grid(row=6, column=3 ,columnspan=2)
btn_c = tk.Button(root, text = "C", command=clear, width=5, font=("Arial",14))
btn_c.grid(row=6, column=1 ,columnspan=1)
btn_dp = tk.Button(root, text = ".", command = lambda: append_to_calculation("."), width=5, font=("Arial",14))
btn_dp.grid(row=6, column=2)
root.mainloop()




