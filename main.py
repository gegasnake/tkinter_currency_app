import tkinter as tk
from tkinter import ttk

# currency for GEL, EURO AND USD
exchange_rates = {
    "USD": {"EUR": 0.93, "GEL": 2.85},
    "EUR": {"USD": 1.08, "GEL": 3.07},
    "GEL": {"USD": 0.35, "EUR": 0.33}
}


def convert_currency():
    """
    this is a static function which helps us to convert from one currency to another,
    :argument: takes nothing
    :return: returns None
    """
    try:
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        amount = float(amount_entry.get())

        if from_currency == to_currency:
            converted_amount = amount
        else:
            converted_amount = amount * exchange_rates[from_currency][to_currency]

        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError:
        print("please enter something in the box")


def clear():
    """This function clears the screen of tkinter app and returns it to its first condition"""
    from_currency_var.set("GEL")
    to_currency_var.set("EUR")
    amount_entry.delete(0, tk.END)
    result_label.config(text="")


root = tk.Tk()
# Window Title
root.title("Currency Converter")
root.geometry("700x700")
root.configure(bg="#282c34")

# Header(MAIN TITLE)
header_label = tk.Label(root, text="Currency Converter", font=("Helvetica", 20, "bold"), bg="#61afef", fg="white",
                        pady=20)
header_label.pack(fill=tk.X)


from_currency_var = tk.StringVar(value="GEL")
to_currency_var = tk.StringVar(value="EUR")

# converting from
from_currency_label = tk.Label(root, text="From Currency:", font=("Helvetica", 14), bg="#282c34", fg="white")
from_currency_label.pack(pady=10)
from_currency_menu = ttk.Combobox(root, textvariable=from_currency_var, values=list(exchange_rates.keys()),
                                  font=("Helvetica", 12))
from_currency_menu.pack()

# converting to
to_currency_label = tk.Label(root, text="To Currency:", font=("Helvetica", 14), bg="#282c34", fg="white")
to_currency_label.pack(pady=10)
to_currency_menu = ttk.Combobox(root, textvariable=to_currency_var, values=list(exchange_rates.keys()),
                                font=("Helvetica", 12))
to_currency_menu.pack()

# Insert the amount field
amount_label = tk.Label(root, text="Amount:", font=("Helvetica", 14), bg="#282c34", fg="white")
amount_label.pack(pady=10)
amount_entry = tk.Entry(root, font=("Helvetica", 12), width=15, justify='center')
amount_entry.pack()

# convert button
convert_button = tk.Button(root, text="Convert", font=("Helvetica", 14, "bold"), bg="#98c379", fg="white",
                           command=convert_currency)
convert_button.pack(pady=20)

# clear button to clear the app
clear_button = tk.Button(root, text="Clear", font=("Helvetica", 14, "bold"), bg="#e06c75", fg="white", command=clear)
clear_button.pack(pady=10)

# This is shown when the result is calculated under the clear button
result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#282c34", fg="#61afef")
result_label.pack(pady=20)

root.mainloop()
