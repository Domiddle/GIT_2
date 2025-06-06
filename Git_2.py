import tkinter as tk

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Meine Tkinter GUI")

        # Label
        self.label = tk.Label(root, text="Gib einen gewünschten Betrag zum umrechnen ein:")
        self.label.pack(pady=10)

        # Entry-Feld
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        self.choice = tk.Label(root, text="Wählen sie die gewünschte Umrechnungswährung: ")
        self.choice.pack(pady=5)

        # Dropdown für Währungsauswahl
        self.währungen = ["Vietnamese Dong","Yen","Brazilian Real"]
        self.auswahl = tk.StringVar()
        self.auswahl.set(self.währungen[0])
        self.dropdown = tk.OptionMenu(root, self.auswahl, *self.währungen)
        self.dropdown.pack(pady=5)

        # Button
        self.button = tk.Button(root, text="Umrechnen", command=self.anzeigen)
        self.button.pack(pady=10)

        # Label für Ausgabe
        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)
        
        # Umrechnungskurse
        self.kurse = {
            "Vietnamese Dong": 29423.77,
            "Yen": 162.39,
            "Brazilian Real": 6.4893
            }

    def anzeigen(self):
        betrag = float(self.entry.get())
        währung = self.auswahl.get()
        ergebnis = betrag * self.kurse[währung]
        self.output_label.config(text=f"{betrag} EUR = {ergebnis:.2f} {währung}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()
    
