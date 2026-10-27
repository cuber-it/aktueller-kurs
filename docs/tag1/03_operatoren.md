# Operatoren

## Worum geht's

Operatoren verknüpfen Werte zu einem neuen Wert oder vergleichen sie.

## Arithmetisch

| Op   | Bedeutung           | Beispiel  | Ergebnis |
|------|---------------------|-----------|----------|
| `+`  | Addition            | `7 + 3`   | `10`     |
| `-`  | Subtraktion         | `7 - 3`   | `4`      |
| `*`  | Multiplikation      | `7 * 3`   | `21`     |
| `/`  | Division (float!)   | `7 / 3`   | `2.333…` |
| `//` | Ganzzahldivision    | `7 // 3`  | `2`      |
| `%`  | Rest (Modulo)       | `7 % 3`   | `1`      |
| `**` | Potenz              | `2 ** 8`  | `256`    |

⚠️ `/` liefert IMMER `float`, auch bei zwei `int`s.

## Vergleich

Ergebnis ist immer `True` oder `False`.

| Op   | Bedeutung      |
|------|----------------|
| `==` | gleich         |
| `!=` | ungleich       |
| `<`  | kleiner        |
| `>`  | größer         |
| `<=` | kleiner-gleich |
| `>=` | größer-gleich  |

**Verkettung erlaubt:**

```python
0 < x < 10        # statt:  x > 0 and x < 10
```

## Logisch

| Op    | Bedeutung           |
|-------|---------------------|
| `and` | beide wahr          |
| `or`  | mindestens eins wahr|
| `not` | Negation            |

```python
True and False        # False
True or False         # True
not True              # False
```

## Zuweisungs-Kurzformen

| Op    | Entspricht       |
|-------|------------------|
| `+=`  | `x = x + …`      |
| `-=`  | `x = x - …`      |
| `*=`  | `x = x * …`      |
| `/=`  | `x = x / …`      |
| `//=` | `x = x // …`     |
| `%=`  | `x = x % …`      |
| `**=` | `x = x ** …`     |

```python
zaehler = 0
zaehler += 1
```

## Strings

| Op   | Bedeutung       | Beispiel                 |
|------|-----------------|--------------------------|
| `+`  | Verketten       | `"Hallo" + " Welt"`      |
| `*`  | Wiederholen     | `"ha" * 3` → `"hahaha"`  |
| `in` | enthält?        | `"Py" in "Python"`       |

## Vorrang (Auswahl, hoch → niedrig)

1. `**`
2. `*`, `/`, `//`, `%`
3. `+`, `-`
4. Vergleiche (`==`, `<`, …)
5. `not`
6. `and`
7. `or`

Im Zweifel: **Klammern setzen** — Lesbarkeit schlägt Kürze.

## Stolpersteine

- `7 / 3` → `2.333…`, `7 // 3` → `2` — Verwechslungsgefahr.
- `7 % 3` → `1` — kein Prozent!
- `==` zum Vergleichen, `=` zum Zuweisen — der Klassiker.
- `not 0` ist `True` (0 ist falsy).
- **String + Zahl** mit `+` → `TypeError`. Erst `str(zahl)`.

## Schnellreferenz

```python
# arithmetisch
+  -  *  /  //  %  **

# vergleichen
==  !=  <  >  <=  >=

# logisch
and  or  not

# kurzform
+=  -=  *=  /=  //=  %=  **=
```
