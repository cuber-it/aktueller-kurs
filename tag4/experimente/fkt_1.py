"""Aus zwei gleich langen Folgen eine benannte Zuordnung erzeugen."""


def erstelle_adresse(felder, werte):
    """Liefert ein Dictionary; unterschiedliche Längen erzeugen ValueError."""
    return dict(zip(felder, werte, strict=True))


if __name__ == "__main__":
    profil = erstelle_adresse(["name", "kenntnis"], ["Anna", "Python"])
    print(profil)
