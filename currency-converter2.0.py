import tkinter as tk

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Meine Tkinter GUI")
        self.languages = ["Deutsch", "English"]
        self.current_language = "de"  # Startsprache

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.value = {"Yen": 162, "VD": 29379, "BR": 6.49}

        # Buttons
        self.button_yen = tk.Button(root, text="Yen", command=lambda: self.anzeigen("Yen"))
        self.button_yen.pack(pady=10)

        self.button_vd = tk.Button(root, text="Vietnamesische Dong", command=lambda: self.anzeigen("VD"))
        self.button_vd.pack(pady=10)

        self.button_br = tk.Button(root, text="Brasilianische Real", command=lambda: self.anzeigen("BR"))
        self.button_br.pack(pady=10)

        self.button_language = tk.Button(root, text="Translation to English", command=self.translation)
        self.button_language.pack(pady=10)

        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)

    def anzeigen(self, key):
        value = self.entry.get()
        try:
            euro = float(value)
            result = euro * self.value[key]
            if self.current_language == "de":
                if key == "Yen":
                    text = f"{euro} Euro sind {result:.2f} Yen"
                elif key == "VD":
                    text = f"{euro} Euro sind {result:.2f} Vietnamesische Dong"
                elif key == "BR":
                    text = f"{euro} Euro sind {result:.2f} Brasilianische Real"

            else: 
                if key == "Yen":
                    text = f"{euro} Euros are {result:.2f} Yen"
                elif key == "VD":
                    text = f"{euro} Euros are {result:.2f} Vietnamese Dong"
                elif key == "BR":
                    text = f"{euro} Euros are {result:.2f} Brazilian Real"

            self.output_label.config(text=text)
        except ValueError:
            if self.current_language == "de":
                self.output_label.config(text="Bitte gültige Zahl eingeben.")

            else:
                self.output_label.config(text="Please enter a valid number.")

    def translation(self):
        if self.current_language == "de":
            self.current_language = "en"
            self.button_yen.config(text="Yen")
            self.button_vd.config(text="Vietnamese Dong")
            self.button_br.config(text="Brazilian Real")
            self.button_language.config(text="Übersetzung auf Deutsch")

        else:
            self.current_language = "de"
            self.button_yen.config(text="Yen")
            self.button_vd.config(text="Vietnamesische Dong")
            self.button_br.config(text="Brasilianische Real")
            self.button_language.config(text="Translation to English")

if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()
