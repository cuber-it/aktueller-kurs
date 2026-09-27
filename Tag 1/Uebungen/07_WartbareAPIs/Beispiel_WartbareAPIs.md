# Beispiel · Eine Schnittstelle festlegen – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Eine Rezeptverwaltung. Rezepte werden gespeichert und für eine gewünschte Personenzahl umgerechnet. Das Modul heißt `kitchen_utils.py`.

```python
class RecipeManager:
    def __init__(self):
        self.recipes = {}

    def add(self, n, ingr, srv):
        """Adds a recipe."""
        self.recipes[n] = {"ingredients": ingr, "servings": srv}

    def calc(self, n, p):
        """Calculates."""
        recipe = self.recipes[n]
        factor = p / recipe["servings"]
        return [self._scale(i, factor) for i in recipe["ingredients"]]

    def _scale(self, ingredient, factor):
        name, amount, unit = ingredient
        return (name, round(amount * factor, 1), unit)
```

Zwei Stellen der Anwendung verwenden das Modul:

```python
# Einkaufsliste: rechnet eine einzelne Zutat um
flour = manager._scale(("Mehl", 500, "g"), 1.5)

# Wochenplan: stellt ein Rezept dauerhaft auf zwei Personen um
manager.recipes["Pfannkuchen"]["servings"] = 2
```

---

## Schritt 1 · Wer verwendet was?

| Name | öffentlich nach Konvention | verwendet von | Zweck |
|---|---|---|---|
| `add` | ja | Rezepterfassung | Rezept speichern |
| `calc` | ja | Rezeptansicht | Zutaten für n Personen |
| `_scale` | nein | Einkaufsliste | eine Zutat umrechnen |
| `recipes` | ja | Wochenplan | Rezept verändern |

**Zwei Befunde:** Die Einkaufsliste braucht die Umrechnung einer einzelnen Zutat, dafür gibt es keinen öffentlichen Weg. Der Wochenplan verändert gespeicherte Rezepte, obwohl er nur eine Umrechnung braucht. War das Rezept für vier Personen gespeichert, liefert `calc("Pfannkuchen", 4)` nach diesem Zugriff doppelt so viel Mehl wie vorher.

---

## Schritt 2 · Namen, die Absicht zeigen

| Vorher | Nachher | Grund |
|---|---|---|
| `RecipeManager` | `RecipeBook` | „Manager" sagt nichts über die Aufgabe |
| `add(n, ingr, srv)` | `add_recipe(recipe)` | ein Rezept als ein Wert statt drei Abkürzungen |
| `calc(n, p)` | `ingredients_for(recipe_name, servings)` | sagt, was herauskommt |
| `_scale(ingredient, factor)` | `Ingredient.scaled(factor)` | die Umrechnung gehört zur Zutat |

---

## Schritt 3 · Datenträger statt Tupel und Dictionaries

Eine Zutat und ein Rezept sind Daten ohne eigenen Lebenszyklus. Dafür passt `@dataclass(frozen=True)`.

```python
"""Rezepte speichern und für eine gewünschte Personenzahl umrechnen."""

from dataclasses import dataclass, replace

__all__ = ["Ingredient", "Recipe", "RecipeBook"]


@dataclass(frozen=True)
class Ingredient:
    name: str
    amount: float
    unit: str

    def scaled(self, factor: float) -> "Ingredient":
        """Neue Zutat mit umgerechneter Menge, gerundet auf eine Nachkommastelle."""
        return replace(self, amount=round(self.amount * factor, 1))


@dataclass(frozen=True)
class Recipe:
    name: str
    ingredients: tuple[Ingredient, ...]
    servings: int
```

`frozen=True` bewirkt, dass eine Zuweisung wie `recipe.servings = 2` mit `FrozenInstanceError` abbricht. Der Wochenplan kann das gespeicherte Rezept nicht mehr verändern.

Die Zutaten stehen in einem Tupel, nicht in einer Liste. Eine Liste in einer eingefrorenen Dataclass bliebe von außen veränderbar, und das Objekt wäre nicht mehr hashbar.

---

## Schritt 4 · Die öffentliche Schnittstelle

```python
class RecipeBook:
    """Sammlung von Rezepten, auffindbar über ihren Namen."""

    def __init__(self) -> None:
        self._recipes: dict[str, Recipe] = {}

    def add_recipe(self, recipe: Recipe) -> None:
        """Speichert ein Rezept. Ein Rezept gleichen Namens wird ersetzt."""
        self._recipes[recipe.name] = recipe

    def ingredients_for(self, recipe_name: str, servings: int) -> list[Ingredient]:
        """Zutaten eines Rezepts, umgerechnet auf ``servings`` Personen.

        Das gespeicherte Rezept bleibt unverändert.

        Raises:
            KeyError: wenn kein Rezept mit diesem Namen existiert.
        """
        recipe = self._recipes[recipe_name]
        factor = servings / recipe.servings
        return [ingredient.scaled(factor) for ingredient in recipe.ingredients]
```

Die Aufrufstellen:

```python
flour = Ingredient("Mehl", 500, "g").scaled(1.5)
shopping = book.ingredients_for("Pfannkuchen", servings=2)
```

**Was sich geändert hat:**

- Das Dictionary heißt `_recipes`. Es ist kein Vertrag mehr.
- Die Docstrings sagen, was die Methode zusichert: Ersetzen bei gleichem Namen, das Rezept bleibt unverändert, `KeyError` bei unbekanntem Namen.
- `__all__` nennt die drei Namen, die das Modul anbietet.

---

## Schritt 5 · Der Modulname

`kitchen_utils.py` sagt, dass es um die Küche geht und dass es sich um Hilfsfunktionen handelt. Beides hilft beim Suchen nicht.

```text
recipes.py      Ingredient, Recipe, RecipeBook
```

Kämen später Einkaufslisten dazu, bekämen sie ein eigenes Modul `shopping.py`, statt in `recipes.py` oder einer neuen `utils.py` zu landen.

---

## Schritt 6 · Eine Regel ableiten

Aus dem Beispiel ergibt sich ein Regelkandidat:

> **SHOULD:** Öffentliche Funktionen und Methoden sind typannotiert.

| Frage | Antwort |
|---|---|
| Warum nicht MUST? | kurze Skripte und Prototypen dürfen darauf verzichten |
| Wer prüft? | ein Linter oder Type Checker in der CI |
| Welche Ausnahme ist legitim? | Code, der ohnehin bald entfernt wird |

---

## Was dieses Beispiel zeigt

**Ein Zugriff auf `_name` zeigt ein fehlendes Angebot.** Die Einkaufsliste brauchte die Umrechnung einer Zutat. Nachdem sie öffentlich angeboten wird, ist der Zugriff überflüssig.

**Namen sind Teil des Vertrags.** `ingredients_for(recipe_name, servings)` erklärt sich, `calc(n, p)` nicht.

**Unveränderliche Datenträger schützen die Sammlung.** Der Wochenplan kann Rezepte nicht mehr versehentlich verändern.

**Ein Docstring lohnt sich dort, wo er etwas sagt, das nicht im Namen steht.** „Das gespeicherte Rezept bleibt unverändert" ist so ein Satz.
