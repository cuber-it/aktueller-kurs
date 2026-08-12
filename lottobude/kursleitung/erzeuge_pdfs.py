# -*- coding: utf-8 -*-
"""Erzeugt je Story ein PDF. Inhalte woertlich aus LB_04_EPICS_AND_STORIES.md."""
import html
import subprocess
from pathlib import Path

ZIEL = Path(__file__).parent

STORIES = [
    {
        "epic": "EPIC-1 – Tipps abgeben",
        "id": "LOTTO-101",
        "titel": "Tippschein anlegen",
        "story": "Als Spieler möchte ich einen Tippschein für die nächste Ziehung "
                 "anlegen, damit ich am Spiel teilnehmen kann.",
        "beschreibung": "Ein Tippschein kann mehrere Tipps enthalten. "
                        "Jeder Tipp besteht aus sechs Lottozahlen.",
        "kriterien": [
            "Ein neuer Tippschein kann angelegt werden.",
            "Es können mehrere Tipps hinzugefügt werden.",
            "Ungültige Lottozahlen dürfen nicht gespeichert werden.",
            "Der Tippschein kann abgegeben werden.",
        ],
        "offen": "Bewusst nicht in der Story beantwortet.",
    },
    {
        "epic": "EPIC-1 – Tipps abgeben",
        "id": "LOTTO-102",
        "titel": "Abgegebene Tipps ansehen",
        "story": "Als Spieler möchte ich meine abgegebenen Tipps ansehen können.",
        "kriterien": [
            "Abgegebene Tippscheine werden angezeigt.",
            "Die zugehörige Ziehung ist erkennbar.",
            "Die Lottozahlen werden angezeigt.",
        ],
    },
    {
        "epic": "EPIC-2 – CSV-Import für Annahmestellen",
        "id": "LOTTO-201",
        "titel": "Tipps per CSV importieren",
        "story": "Als Annahmestelle möchte ich Lotto-Tipps per CSV-Datei hochladen, "
                 "damit die Tipps nicht einzeln erfasst werden müssen.",
        "beschreibung": "Eine Datei enthält Tippscheine mit jeweils einem oder "
                        "mehreren Tipps. Die Daten werden eingelesen und in der "
                        "Datenbank bereitgestellt.",
        "kriterien": [
            "Eine CSV-Datei kann hochgeladen werden.",
            "Gültige Tipps werden gespeichert.",
            "Ungültige Daten werden abgewiesen.",
            "Nach dem Import wird ein Ergebnis angezeigt.",
        ],
        "hinweise": "Das genaue CSV-Format ist separat beschrieben.",
    },
    {
        "epic": "EPIC-2 – CSV-Import für Annahmestellen",
        "id": "LOTTO-202",
        "titel": "Importfehler ansehen",
        "story": "Als Annahmestelle möchte ich sehen, welche Daten beim Import "
                 "nicht verarbeitet werden konnten.",
        "kriterien": [
            "Fehlerhafte Datensätze sind erkennbar.",
            "Ein Fehlergrund wird angezeigt.",
            "Die betroffene Stelle in der Datei soll nachvollziehbar sein.",
        ],
    },
    {
        "epic": "EPIC-2 – CSV-Import für Annahmestellen",
        "id": "LOTTO-203",
        "titel": "Importhistorie",
        "story": "Als Annahmestelle möchte ich frühere Importe sehen können.",
        "kriterien": [
            "Frühere Importe werden aufgelistet.",
            "Dateiname, Zeitpunkt und Ergebnis werden angezeigt.",
        ],
    },
    {
        "epic": "EPIC-3 – Ziehung",
        "id": "LOTTO-301",
        "titel": "Ziehung anlegen",
        "story": "Als Spielleitung möchte ich eine neue Ziehung anlegen.",
        "kriterien": [
            "Ein Ziehungstermin kann angelegt werden.",
            "Die Ziehung steht anschließend für Tippscheine zur Verfügung.",
        ],
    },
    {
        "epic": "EPIC-3 – Ziehung",
        "id": "LOTTO-302",
        "titel": "Gewinnzahlen erfassen",
        "story": "Als Spielleitung möchte ich die Gewinnzahlen einer Ziehung "
                 "erfassen, damit die Tipps ausgewertet werden können.",
        "kriterien": [
            "Sechs Gewinnzahlen können erfasst werden.",
            "Ungültige Gewinnzahlen werden nicht akzeptiert.",
            "Nach Abschluss gilt die Ziehung als durchgeführt.",
        ],
    },
    {
        "epic": "EPIC-4 – Auswertung",
        "id": "LOTTO-401",
        "titel": "Tipps auswerten",
        "story": "Als Spielleitung möchte ich nach einer Ziehung alle abgegebenen "
                 "Tipps auswerten lassen.",
        "kriterien": [
            "Alle Tipps der Ziehung werden berücksichtigt.",
            "Die Trefferzahl wird bestimmt.",
            "Der zugehörige Gewinn wird ermittelt.",
            "Das Ergebnis wird gespeichert.",
        ],
    },
    {
        "epic": "EPIC-4 – Auswertung",
        "id": "LOTTO-402",
        "titel": "Spielergebnis anzeigen",
        "story": "Als Spieler möchte ich nach der Auswertung sehen, wie meine "
                 "Tipps abgeschnitten haben.",
        "kriterien": [
            "Gewinnzahlen werden angezeigt.",
            "Für jeden Tipp wird die Trefferzahl angezeigt.",
            "Ein Gewinn wird angezeigt, sofern einer entstanden ist.",
        ],
    },
    {
        "epic": "EPIC-5 – Administration / Trainingsbetrieb",
        "id": "LOTTO-501",
        "titel": "Trainingsdaten zurücksetzen",
        "story": "Als Kursleitung möchte ich die Trainingsumgebung auf einen "
                 "definierten Ausgangszustand zurücksetzen können.",
        "kriterien": [
            "Trainingsdaten können vollständig zurückgesetzt werden.",
            "Definierte Benutzer, Annahmestellen und Ziehungen werden wiederhergestellt.",
            "Der Reset ist für normale Teilnehmer nicht verfügbar.",
        ],
    },
]

STIL = """
@page {
  size: A4;
  margin: 22mm 20mm 20mm 20mm;
  @bottom-left {
    content: "Lottobude – Anforderung";
    font-family: "DejaVu Sans", sans-serif; font-size: 8pt; color: #8a8f98;
  }
  @bottom-right {
    content: counter(page) " / " counter(pages);
    font-family: "DejaVu Sans", sans-serif; font-size: 8pt; color: #8a8f98;
  }
}
body { font-family: "DejaVu Sans", sans-serif; font-size: 10.5pt;
       line-height: 1.55; color: #1c1f24; }
.epic { font-size: 8.5pt; letter-spacing: .09em; text-transform: uppercase;
        color: #6b7280; margin-bottom: 3mm; }
.kennung { display: inline-block; padding: 1.5mm 3mm; border-radius: 3pt;
           background: #1c3f66; color: #fff; font-size: 10pt;
           font-weight: bold; letter-spacing: .04em; }
h1 { font-size: 19pt; margin: 4mm 0 8mm 0; line-height: 1.25; }
h2 { font-size: 10pt; text-transform: uppercase; letter-spacing: .07em;
     color: #1c3f66; margin: 8mm 0 2.5mm 0;
     border-bottom: .6pt solid #d3d7de; padding-bottom: 1.5mm; }
.userstory { background: #f2f5f9; border-left: 2.5pt solid #1c3f66;
             padding: 4mm 5mm; font-size: 11.5pt; font-style: italic; }
ul.kriterien { margin: 0; padding-left: 0; list-style: none; }
ul.kriterien li { padding: 2.2mm 0 2.2mm 8mm; border-bottom: .4pt solid #e8eaee;
                  position: relative; }
ul.kriterien li:before { content: "\\25A1"; position: absolute; left: 1mm;
                         color: #1c3f66; font-size: 11pt; }
.notiz { color: #565c66; }
.raum { margin-top: 6mm; border: .5pt dashed #c2c7d0; border-radius: 3pt;
        min-height: 42mm; padding: 3mm 4mm; color: #9aa0aa; font-size: 8.5pt; }
"""


def als_html(story: dict) -> str:
    teile = [
        f'<div class="epic">{html.escape(story["epic"])}</div>',
        f'<div><span class="kennung">{html.escape(story["id"])}</span></div>',
        f'<h1>{html.escape(story["titel"])}</h1>',
        "<h2>User Story</h2>",
        f'<p class="userstory">{html.escape(story["story"])}</p>',
    ]
    if story.get("beschreibung"):
        teile.append("<h2>Beschreibung</h2>")
        teile.append(f'<p>{html.escape(story["beschreibung"])}</p>')

    teile.append("<h2>Akzeptanzkriterien</h2>")
    teile.append('<ul class="kriterien">')
    for kriterium in story["kriterien"]:
        teile.append(f"<li>{html.escape(kriterium)}</li>")
    teile.append("</ul>")

    if story.get("hinweise"):
        teile.append("<h2>Hinweise</h2>")
        teile.append(f'<p>{html.escape(story["hinweise"])}</p>')
    if story.get("offen"):
        teile.append("<h2>Offene Punkte für das Refinement</h2>")
        teile.append(f'<p class="notiz">{html.escape(story["offen"])}</p>')

    teile.append("<h2>Notizen</h2>")
    teile.append('<div class="raum">Platz für Testideen, Fragen an den '
                 'Product Owner, Risiken</div>')

    inhalt = "\n".join(teile)
    return (f'<!doctype html><html lang="de"><head><meta charset="utf-8">'
            f'<title>{html.escape(story["id"])} {html.escape(story["titel"])}</title>'
            f"<style>{STIL}</style></head><body>{inhalt}</body></html>")


def main() -> None:
    for story in STORIES:
        name = f'{story["id"]}_{story["titel"].replace(" ", "_")}'
        html_pfad = ZIEL / f"{name}.html"
        pdf_pfad = ZIEL / f"{name}.pdf"
        html_pfad.write_text(als_html(story), encoding="utf-8")
        subprocess.run(
            ["weasyprint", str(html_pfad), str(pdf_pfad)], check=True,
            capture_output=True,
        )
        html_pfad.unlink()
        print(f"{pdf_pfad.name}")


if __name__ == "__main__":
    main()
