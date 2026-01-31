import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import os

# --- PARTEA 1: LOGICA DE CALCUL ---
class UniversalConverter:
    DATA = {
        "Lungime": {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0, "inch": 0.0254, "foot": 0.3048, "mile": 1609.34},
        "Greutate": {"g": 1.0, "kg": 1000.0, "lb": 453.592, "oz": 28.3495, "ton": 1000000.0},
        "Viteză": {"m/s": 1.0, "km/h": 0.277778, "mph": 0.44704},
        "Volum": {"ml": 0.001, "l": 1.0, "gallon": 3.78541, "cup": 0.24}
    }

    @staticmethod
    def convert_standard(value, unit_from, unit_to, category):
        factors = UniversalConverter.DATA[category]
        base_value = value * factors[unit_from]
        return base_value / factors[unit_to]

    @staticmethod
    def convert_temperature(value, unit_from, unit_to):
        if unit_from == unit_to: return value
        temp_c = value
        if unit_from == "F": temp_c = (value - 32) * 5/9
        elif unit_from == "K": temp_c = value - 273.15
        if unit_to == "C": return temp_c
        if unit_to == "F": return (temp_c * 9/5) + 32
        if unit_to == "K": return temp_c + 273.15

# --- PARTEA 2: SALVARE ISTORIC ---
def save_to_history(cat, val_in, u_in, res, u_out):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {cat}: {val_in} {u_in} = {res:.4f} {u_out}\n"
    with open("history.log", "a", encoding="utf-8") as f:
        f.write(line)

# --- PARTEA 3: INTERFAȚA GRAFICĂ ---
class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertor Universal Pro")
        self.root.geometry("400x400")
        self.converter = UniversalConverter()
        self.setup_ui()

    def setup_ui(self):
        # Stil si fonturi
        ttk.Label(self.root, text="CATEGORIE", font=("Arial", 10, "bold")).pack(pady=10)
        self.cat_var = tk.StringVar(value="Lungime")
        self.cat_menu = ttk.Combobox(self.root, textvariable=self.cat_var, state="readonly")
        self.cat_menu['values'] = list(self.converter.DATA.keys()) + ["Temperatură"]
        self.cat_menu.pack()
        self.cat_menu.bind("<<ComboboxSelected>>", self.update_units)

        ttk.Label(self.root, text="VALOARE:").pack(pady=10)
        self.val_entry = ttk.Entry(self.root)
        self.val_entry.pack()

        self.u_from = ttk.Combobox(self.root, state="readonly", width=15)
        self.u_from.pack(pady=10)
        ttk.Label(self.root, text="↓ transformă în ↓").pack()
        self.u_to = ttk.Combobox(self.root, state="readonly", width=15)
        self.u_to.pack(pady=10)

        ttk.Button(self.root, text="CALCULEAZĂ", command=self.do_calc).pack(pady=20)
        self.res_label = ttk.Label(self.root, text="REZULTAT: -", font=("Arial", 12, "bold"))
        self.res_label.pack()
        self.update_units()

    def update_units(self, event=None):
        cat = self.cat_var.get()
        units = ["C", "F", "K"] if cat == "Temperatură" else list(self.converter.DATA[cat].keys())
        self.u_from['values'] = units
        self.u_to['values'] = units
        self.u_from.current(0)
        self.u_to.current(1)

    def do_calc(self):
        try:
            val = float(self.val_entry.get().replace(',', '.'))
            cat, uf, ut = self.cat_var.get(), self.u_from.get(), self.u_to.get()
            if cat == "Temperatură":
                res = self.converter.convert_temperature(val, uf, ut)
            else:
                res = self.converter.convert_standard(val, uf, ut, cat)
            
            self.res_label.config(text=f"REZULTAT: {res:.4f} {ut}")
            save_to_history(cat, val, uf, res, ut)
        except ValueError:
            messagebox.showerror("Eroare", "Introdu un număr valid!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop() 