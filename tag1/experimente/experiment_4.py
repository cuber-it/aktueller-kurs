import tkinter as tk
from tkinter import filedialog
from io import BytesIO
from PIL import Image, ImageTk

fenster = tk.Tk()
fenster.withdraw()

dateiname = filedialog.askopenfilename(parent=fenster)

if dateiname:
    with open(dateiname, "rb") as datei:
        inhalt = datei.read()

    if inhalt.startswith(b"\xff\xd8\xff"):
        with Image.open(BytesIO(inhalt)) as bild:
            foto = ImageTk.PhotoImage(bild)

        fenster.title("JPEG")
        tk.Label(fenster, image=foto).pack()
        fenster.deiconify()
        fenster.mainloop()
    else:
        print("Keine JPEG-Signatur")

fenster.destroy()
