import tkinter as tk

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Währungsrechner")

        # Entry-Feld
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.value = {"Yen": 162, "VD": 29379, "BR": 6.49}

        self.button_yen = tk.Button(root, text="Yen", command=lambda: self.anzeigen("Yen"))
        self.button_yen.pack(pady=10)

        self.button_vd = tk.Button(root, text="Vietnamese Dong", command=lambda: self.anzeigen("VD"))
        self.button_vd.pack(pady=10)

        self.button_br = tk.Button(root, text="Brazilian Real", command=lambda: self.anzeigen("BR"))
        self.button_br.pack(pady=10)

        # Label für Ausgabe
        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)

    def anzeigen(self, key):
        value = self.entry.get()
        try:
            euro = float(value)
            result = euro * self.value[key]
            if key == "Yen":
                text = f"{euro} Euro sind {result:.2f} Yen"

            elif key == "VD":
                text = f"{euro} Euro sind {result:.2f} Vietnamesische Dong"

            elif key == "BR":
                text = f"{euro} Euro sind {result:.2f} Brasilianische Real"

            self.output_label.config(text=text)
        except ValueError:
            self.output_label.config(text="Bitte gültige Zahl eingeben.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()