import tkinter as tk

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Währungsrechner")
        Vietnamesische_Dong="Vietnamesische Dong"
        Brasillianische_Real="Brasilianische Real"
        # Entry-Feld
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.value = {"Yen": 162, "VD": 29379, "BR": 6.49}

        self.button_yen = tk.Button(root, text="Yen", command=lambda: self.anzeigen("Yen"))
        self.button_yen.pack(pady=10)

        self.button_vd = tk.Button(root, text=Vietnamesische_Dong, command=lambda: self.anzeigen("VD"))
        self.button_vd.pack(pady=10)

        self.button_br = tk.Button(root, text=Brasillianische_Real, command=lambda: self.anzeigen("BR"))
        self.button_br.pack(pady=10)

        self.language_en = tk.Button(root, text="English", command=self.change_to_english)
        self.language_en.pack(pady=10)

        # Label für Ausgabe
        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)

    def anzeigen(self, key):
        value = self.entry.get()
        try:
            euro = float(value)
            result = euro * self.value[key]
            language=self.language_en.cget('text')
            if language=="English":
                if key == "Yen":
                    text = f"{euro} Euro sind {result:.2f} Yen"

                elif key == "VD":
                    text = f"{euro} Euro sind {result:.2f} Vietnamesische Dong"

                elif key == "BR":
                    text = f"{euro} Euro sind {result:.2f} Brasilianische Real"

                self.output_label.config(text=text)

            if language == "Deutsch":
                if key == "Yen":
                    text = f"{euro} Euros are {result:.2f} Yen"
                elif key == "VD":
                    text = f"{euro} Euros are {result:.2f} Vietnamese Dong"
                elif key == "BR":
                    text = f"{euro} Euros are {result:.2f} Brazilian Real"

                self.output_label.config(text=text)
        except ValueError:
            self.output_label.config(text="Error")
    def change_to_english(self):
        lang=self.language_en.cget('text')
        if lang=="English":
            self.root.title("Currency Converter")
            self.button_vd.config(text="Vietnamese Dong")
            self.button_br.config(text="Brazilian Real")
            self.language_en.config(text="Deutsch")
        elif lang == "Deutsch":
            self.root.title("Währungsrechner")
            self.button_vd.config(text="Vietnamesische Dong")
            self.button_br.config(text="Brasilianische Real")
            self.language_en.config(text="English")

if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()