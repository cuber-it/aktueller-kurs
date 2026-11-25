konto = {
    "kontoinhaber": "Max Mustermann",
    "iban": "DE00 0000 0000 0000 0000 00",
    "bic": "MUSTDEHHXXX",
    "bank": "Musterbank",
    "kontotyp": "Girokonto",
    "waehrung": "EUR",
    "kontostand": 2450.75,
    "dispolimit": 1000.00,
    "aktiv": True,
    "eroeffnet_am": "2024-01-15",
    "buchungen": [
        {
            "datum": "2026-11-23",
            "beschreibung": "Gehalt",
            "betrag": 3200.00
        },
        {
            "datum": "2026-11-24",
            "beschreibung": "Miete",
            "betrag": -950.00
        },
        {
            "datum": "2026-11-25",
            "beschreibung": "Supermarkt",
            "betrag": -74.25
        }
    ]
}

print(konto["buchungen"])
print(konto["buchungen"][-1])

konto["buchungen"].append({
            "datum": "2026-11-30",
            "beschreibung": "Supermarkt",
            "betrag": -174.25
        })

print(konto["buchungen"])

import json
with open("konto.json", "w") as fd:
    json.dump(konto, fd)
