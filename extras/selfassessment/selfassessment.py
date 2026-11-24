"""Desktop-Anwendung zum Python-Grundlagenkurs."""
from collections import Counter
from pathlib import Path
import random
import tkinter as tk
from tkinter import ttk, messagebox

from engine import load_questions, select_questions, score
from storage import Storage

BASE = Path(__file__).resolve().parent
BG = "#f1f5f9"
NAVY = "#172b4d"
BLUE = "#2365ad"
INK = "#243447"
MUTED = "#53677c"
WHITE = "#ffffff"


class Assessment:
    def __init__(self, root, questions, storage):
        self.root = root
        self.questions = questions
        self.storage = storage
        self.session = []
        self.answers = {}
        self.index = 0
        self.checked = set()
        self.active = False
        root.title("Python | Self-Assessment")
        root.geometry("1080x850")
        root.minsize(800, 620)
        root.configure(bg=BG)
        root.protocol("WM_DELETE_WINDOW", self.close)
        style = ttk.Style(root)
        style.theme_use("clam")
        root.option_add("*Font", ("TkDefaultFont", 12))
        style.configure("TFrame", background=BG)
        style.configure("Card.TFrame", background=WHITE)
        style.configure("TLabel", background=BG, foreground=INK, padding=0)
        style.configure("Card.TLabel", background=WHITE, foreground=INK)
        style.configure("TButton", padding=(15, 9))
        style.configure("Primary.TButton", background=BLUE, foreground=WHITE)
        style.map("Primary.TButton", background=[("active", "#194d86"), ("disabled", "#aabbd0")])
        style.configure("TCheckbutton", background=WHITE, foreground=INK, padding=5)
        style.configure("TRadiobutton", background=WHITE, foreground=INK, padding=5)
        style.configure("Horizontal.TProgressbar", background=BLUE, troughcolor="#dce5ee", thickness=8)
        style.configure("Treeview", rowheight=28)
        header = tk.Frame(root, bg=NAVY, padx=28, pady=17)
        header.pack(fill="x")
        tk.Label(header, text="PYTHON  /  GRUNDLAGEN", bg=NAVY, fg="#a8c9ee",
                 font=("TkDefaultFont", 10, "bold")).pack(anchor="w")
        tk.Label(header, text="Self-Assessment", bg=NAVY, fg=WHITE,
                 font=("TkDefaultFont", 23, "bold")).pack(anchor="w")
        self.body = ttk.Frame(root, padding=(24, 18))
        self.body.pack(fill="both", expand=True)
        self.home()

    def clear(self):
        for child in self.body.winfo_children():
            child.destroy()

    def label(self, parent, text, size=12, bold=False, card=False, **kw):
        return ttk.Label(parent, text=text, font=("TkDefaultFont", size, "bold" if bold else "normal"),
                         style="Card.TLabel" if card else "TLabel", **kw)

    def home(self):
        self.active = False
        self.clear()
        self.label(self.body, "Training zusammenstellen", 20, True).pack(anchor="w")
        self.label(self.body, "Wähle Themen und Umfang. Die Fragen werden neu gemischt.").pack(anchor="w", pady=(4, 18))
        card = ttk.Frame(self.body, style="Card.TFrame", padding=22)
        card.pack(fill="x")
        self.label(card, "Kurstage", 14, True, True).grid(row=0, column=0, sticky="w")
        self.days = [tk.BooleanVar(value=True) for _ in range(4)]
        for i, text in enumerate(("1 · Grundlagen", "2 · Kontrollstrukturen und Dateien",
                                  "3 · Datenstrukturen", "4 · Funktionen und Module")):
            ttk.Checkbutton(card, text=text, variable=self.days[i], command=self.refresh_topics).grid(row=i+1, column=0, sticky="w")
        settings = ttk.Frame(card, style="Card.TFrame")
        settings.grid(row=0, column=1, rowspan=5, sticky="nsew", padx=(35, 0))
        card.columnconfigure(1, weight=1)
        self.topic = tk.StringVar(value="Alle")
        self.level = tk.StringVar(value="Alle")
        self.count = tk.StringVar(value="20")
        self.mode = tk.StringVar(value="Lernmodus")
        self.topic_box = self.combo(settings, "Thema", self.topic, ["Alle"])
        self.combo(settings, "Schwierigkeit", self.level, ["Alle", "Grundlagen", "Anwendung", "Vertiefung"])
        self.combo(settings, "Fragenzahl (maximal)", self.count, ["10", "20", "30", "60", "120"])
        self.combo(settings, "Modus", self.mode, ["Lernmodus", "Prüfungsmodus"])
        self.refresh_topics()
        row = ttk.Frame(self.body)
        row.pack(fill="x", pady=18)
        ttk.Button(row, text="Training starten", style="Primary.TButton", command=self.start).pack(side="left")
        ttk.Button(row, text="Fehler wiederholen", command=lambda: self.start(True)).pack(side="left", padx=10)
        ttk.Button(row, text="Verlauf", command=self.history).pack(side="right")
        self.label(self.body, f"{len(self.questions)} Fragen · lokale Auswertung · keine Internetverbindung nötig").pack(anchor="w")

    def combo(self, parent, label, var, values):
        self.label(parent, label, 11, True, True).pack(anchor="w")
        widget = ttk.Combobox(parent, textvariable=var, values=values, state="readonly", width=30)
        widget.pack(fill="x", pady=(3, 10))
        return widget

    def refresh_topics(self):
        days = {i+1 for i, v in enumerate(self.days) if v.get()}
        values = ["Alle"] + sorted({q.topic for q in self.questions if q.day in days})
        self.topic_box.configure(values=values)
        if self.topic.get() not in values:
            self.topic.set("Alle")

    def start(self, retry=False):
        days = {i+1 for i, v in enumerate(self.days) if v.get()}
        try:
            wrong = self.storage.wrong_ids() if retry else None
        except Exception as exc:
            messagebox.showerror("Verlauf", str(exc), parent=self.root)
            return
        self.session = select_questions(self.questions, days, self.topic.get(), self.level.get(),
                                        int(self.count.get()), wrong)
        if not self.session:
            messagebox.showinfo("Keine Fragen", "Für diese Auswahl sind keine Fragen vorhanden.", parent=self.root)
            return
        self.session_mode = self.mode.get()
        self.answers = {}
        self.checked = set()
        self.index = 0
        self.order = {}
        for q in self.session:
            indices = list(range(len(q.options)))
            random.shuffle(indices)
            self.order[q.id] = indices
        self.active = True
        self.show_question()

    def scroll_card(self):
        outer = ttk.Frame(self.body)
        outer.pack(fill="both", expand=True, pady=12)
        canvas = tk.Canvas(outer, bg=WHITE, highlightthickness=0)
        scroll = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        card = ttk.Frame(canvas, style="Card.TFrame", padding=22)
        window = canvas.create_window(0, 0, window=card, anchor="nw")
        card.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", lambda e: canvas.itemconfigure(window, width=e.width))
        def wheel(event):
            delta = -1 if event.num == 4 else 1 if event.num == 5 else -int(event.delta / 120)
            canvas.yview_scroll(delta, "units")
        canvas.bind("<Enter>", lambda e: [canvas.bind_all(k, wheel) for k in ("<MouseWheel>", "<Button-4>", "<Button-5>")])
        canvas.bind("<Leave>", lambda e: [canvas.unbind_all(k) for k in ("<MouseWheel>", "<Button-4>", "<Button-5>")])
        canvas.bind("<Destroy>", lambda e: [canvas.unbind_all(k) for k in ("<MouseWheel>", "<Button-4>", "<Button-5>")])
        self.canvas = canvas
        return card

    def code_block(self, parent, code):
        if not code:
            return
        widget = tk.Text(parent, height=len(code.splitlines()), wrap="none",
                         font=("TkFixedFont", 12), background="#e4eef9", foreground=NAVY,
                         relief="flat", padx=12, pady=10, borderwidth=0)
        widget.insert("1.0", code)
        widget.configure(state="disabled")
        widget.pack(fill="x", pady=(12, 14))

    def show_question(self, review=False):
        self.clear()
        q = self.session[self.index]
        top = ttk.Frame(self.body)
        top.pack(fill="x")
        self.label(top, f"Frage {self.index+1} von {len(self.session)}", 15, True).pack(side="left")
        self.label(top, f"{self.session_mode} · {len(self.answers)} beantwortet").pack(side="right")
        ttk.Progressbar(self.body, maximum=len(self.session), value=self.index+1).pack(fill="x", pady=(8, 0))
        footer = ttk.Frame(self.body)
        footer.pack(side="bottom", fill="x", pady=(6, 0))
        card = self.scroll_card()
        kinds = {"single": "Eine Antwort", "multiple": "Mehrere Antworten möglich", "fill": "Lückentext", "output": "Programmausgabe"}
        self.label(card, f"TAG {q.day}  /  {q.topic}  /  {q.level}  /  {kinds[q.kind]}", 11, True, True,
                   wraplength=720).pack(anchor="w")
        prompt = self.label(card, q.prompt, 17, True, True, wraplength=720)
        prompt.pack(anchor="w", pady=(12, 0))
        self.code_block(card, q.code)
        self.response_vars = []
        self.text_response = None
        self.radio = None
        previous = self.answers.get(q.id)
        locked = review or q.id in self.checked
        state = "disabled" if locked else "normal"
        if q.kind == "single":
            self.radio = tk.IntVar(value=previous[0] if previous else -1)
            for i in self.order[q.id]:
                ttk.Radiobutton(card, text=q.options[i], variable=self.radio, value=i, state=state).pack(anchor="w", fill="x", pady=2)
        elif q.kind == "multiple":
            for i in self.order[q.id]:
                var = tk.BooleanVar(value=i in (previous or []))
                self.response_vars.append((i, var))
                ttk.Checkbutton(card, text=q.options[i], variable=var, state=state).pack(anchor="w", fill="x", pady=2)
        else:
            self.label(card, "Nur die Lücke ergänzen." if q.kind == "fill" else
                       "Ausgabe exakt eingeben, ohne zusätzliche Anführungszeichen.", card=True).pack(anchor="w", pady=(4, 5))
            self.text_response = tk.Text(card, height=2 if q.kind == "fill" else 5,
                                         font=("TkFixedFont", 12), relief="solid", borderwidth=1,
                                         padx=10, pady=8, wrap="none", undo=True)
            self.text_response.pack(fill="x")
            if previous is not None:
                self.text_response.insert("1.0", previous)
            if locked:
                self.text_response.configure(state="disabled")
            else:
                self.text_response.focus_set()
        if locked:
            self.feedback(card, q)
        ttk.Button(footer, text="Übersicht" if review else "Abbrechen",
                   command=self.results if review else self.cancel).pack(side="left")
        if self.index > 0:
            ttk.Button(footer, text="Zurück", command=lambda: self.navigate(-1, review)).pack(side="left", padx=8)
        if not review and self.session_mode == "Lernmodus" and not locked:
            ttk.Button(footer, text="Antwort prüfen", style="Primary.TButton",
                       command=self.check).pack(side="right")
        else:
            if self.index + 1 < len(self.session):
                ttk.Button(footer, text="Weiter", style="Primary.TButton",
                           command=lambda: self.navigate(1, review)).pack(side="right")
            elif not review:
                ttk.Button(footer, text="Auswerten", style="Primary.TButton", command=self.finish).pack(side="right")
        if not review and self.session_mode == "Prüfungsmodus" and self.index + 1 < len(self.session):
            ttk.Button(footer, text="Vorzeitig abgeben", command=self.finish).pack(side="right", padx=8)
        if not review and self.session_mode == "Lernmodus" and not locked:
            ttk.Button(footer, text="Überspringen", command=self.skip).pack(side="right", padx=8)

    def current_response(self):
        if self.radio is not None:
            value = self.radio.get()
            return [] if value == -1 else [value]
        if self.text_response is not None:
            return self.text_response.get("1.0", "end-1c")
        return [i for i, var in self.response_vars if var.get()]

    def capture(self):
        q = self.session[self.index]
        if q.id not in self.checked:
            answer = self.current_response()
            if answer or (isinstance(answer, str) and answer != ""):
                self.answers[q.id] = answer
            else:
                self.answers.pop(q.id, None)

    def check(self):
        self.capture()
        q = self.session[self.index]
        if q.id not in self.answers:
            messagebox.showinfo("Antwort fehlt", "Bitte zuerst eine Antwort eingeben oder auswählen.", parent=self.root)
            return
        self.checked.add(q.id)
        self.show_question()

    def skip(self):
        self.answers.pop(self.session[self.index].id, None)
        self.checked.add(self.session[self.index].id)
        self.show_question()

    def navigate(self, delta, review):
        if not review:
            self.capture()
        self.index += delta
        self.show_question(review)

    def feedback(self, card, q):
        answer = self.answers.get(q.id)
        good = answer is not None and q.correct(answer)
        color = "#e5f4eb" if good else "#fff0e3"
        panel = tk.Frame(card, bg=color, padx=14, pady=12)
        panel.pack(fill="x", pady=(16, 4))
        tk.Label(panel, text="Richtig" if good else "Nicht beantwortet" if answer is None else "Nicht richtig",
                 bg=color, fg="#17663c" if good else "#944819", font=("TkDefaultFont", 14, "bold")).pack(anchor="w")
        tk.Label(panel, text="Lösung: " + q.solution(), bg=color, fg=INK, justify="left", wraplength=700,
                 font=("TkFixedFont", 11)).pack(anchor="w", pady=(8, 4))
        tk.Label(panel, text=q.explanation, bg=color, fg=INK, justify="left", wraplength=700).pack(anchor="w")

    def finish(self):
        self.capture()
        missing = len(self.session) - len(self.answers)
        if missing and not messagebox.askyesno("Abgeben", f"{missing} Fragen sind unbeantwortet und zählen als falsch. Abgeben?", parent=self.root):
            return
        try:
            self.storage.save(self.session_mode, self.session, self.answers)
        except Exception as exc:
            messagebox.showerror("Speichern fehlgeschlagen", str(exc), parent=self.root)
            return
        self.active = False
        self.results()

    def results(self):
        self.clear()
        stats = score(self.session, self.answers)
        correct = sum(a for a, b in stats.values())
        total = len(self.session)
        self.label(self.body, "Dein Ergebnis", 20, True).pack(anchor="w")
        self.label(self.body, f"{correct} / {total} richtig  ·  {correct/total:.0%}", 26, True).pack(anchor="w", pady=12)
        ttk.Progressbar(self.body, maximum=total, value=correct).pack(fill="x", pady=(0, 16))
        table = ttk.Treeview(self.body, columns=("day", "topic", "score"), show="headings", height=10)
        for key, title, width in (("day", "Tag", 65), ("topic", "Thema", 350), ("score", "Richtig / Gesamt", 155)):
            table.heading(key, text=title)
            table.column(key, width=width, anchor="w")
        for (day, topic), (a, b) in sorted(stats.items()):
            table.insert("", "end", values=(day, topic, f"{a} / {b}"))
        table.pack(fill="both", expand=True)
        row = ttk.Frame(self.body)
        row.pack(fill="x", pady=14)
        ttk.Button(row, text="Antworten ansehen", command=self.review, style="Primary.TButton").pack(side="left")
        ttk.Button(row, text="Neues Training", command=self.home).pack(side="right")

    def review(self):
        self.index = 0
        self.show_question(True)

    def history(self):
        try:
            records = self.storage.history()
        except Exception as exc:
            messagebox.showerror("Verlauf", str(exc), parent=self.root)
            return
        self.clear()
        self.label(self.body, "Bisherige Ergebnisse", 20, True).pack(anchor="w", pady=(0, 12))
        table = ttk.Treeview(self.body, columns=("date", "mode", "result"), show="headings")
        for key, label in (("date", "Zeit (UTC)"), ("mode", "Modus"), ("result", "Richtig / Gesamt")):
            table.heading(key, text=label)
        for date, mode, correct, total in records:
            table.insert("", "end", values=(date[:16].replace("T", " "), mode, f"{correct} / {total}"))
        table.pack(fill="both", expand=True)
        ttk.Button(self.body, text="Zurück", command=self.home).pack(anchor="w", pady=12)

    def cancel(self):
        if messagebox.askyesno("Training abbrechen", "Das aktuelle Training wird nicht gespeichert. Abbrechen?", parent=self.root):
            self.home()

    def close(self):
        if not self.active or messagebox.askyesno("Beenden", "Das aktuelle Training wird nicht gespeichert. Beenden?", parent=self.root):
            self.root.destroy()


def main():
    root = tk.Tk()
    try:
        questions = load_questions(BASE / "fragen")
        storage = Storage(Path.home() / ".python-selfassessment" / "progress.sqlite3")
        Assessment(root, questions, storage)
    except (OSError, ValueError) as exc:
        messagebox.showerror("Start fehlgeschlagen", str(exc), parent=root)
        root.destroy()
        return
    root.mainloop()


if __name__ == "__main__":
    main()
