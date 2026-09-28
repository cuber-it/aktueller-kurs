```python
import re
from functools import total_ordering
from math import gcd


@total_ordering
class Dec:
    """Exakte Dezimalzahl: Wert = _coef * 10**-_scale. Unveränderlich."""

    __slots__ = ("_coef", "_scale")
    _PATTERN = re.compile(r"([+-]?)(\d+)(?:\.(\d+))?")

    def __init__(self, value: "int | str | Dec" = 0) -> None:
        if isinstance(value, Dec):
            coef, scale = value._coef, value._scale
        elif isinstance(value, int):
            coef, scale = value, 0
        elif isinstance(value, str):
            m = self._PATTERN.fullmatch(value.strip())
            if not m:
                raise ValueError(f"invalid decimal literal: {value!r}")
            sign, whole, frac = m.groups()
            frac = frac or ""
            coef = int(whole + frac)
            coef = -coef if sign == "-" else coef
            scale = len(frac)
        else:
            raise TypeError(f"unsupported type: {type(value).__name__}")
        self._coef, self._scale = self._normalize(coef, scale)

    # --- intern ---------------------------------------------------------
    @staticmethod
    def _normalize(coef: int, scale: int) -> tuple[int, int]:
        if scale < 0:
            return coef * 10**-scale, 0
        if coef == 0:
            return 0, 0
        while scale and coef % 10 == 0:
            coef //= 10
            scale -= 1
        return coef, scale

    @classmethod
    def _make(cls, coef: int, scale: int) -> "Dec":
        obj = cls.__new__(cls)
        obj._coef, obj._scale = cls._normalize(coef, scale)
        return obj

    @staticmethod
    def _coerce(other: object) -> "Dec | None":
        if isinstance(other, Dec):
            return other
        if isinstance(other, int):
            return Dec(other)
        return None

    def _align(self, other: "Dec") -> tuple[int, int, int]:
        s = max(self._scale, other._scale)
        return (self._coef * 10 ** (s - self._scale),
                other._coef * 10 ** (s - other._scale), s)

    def _div(self, other: "Dec") -> "Dec":
        if other._coef == 0:
            raise ZeroDivisionError("division by zero")
        num = self._coef * 10**other._scale
        den = other._coef * 10**self._scale
        g = gcd(num, den)
        num, den = num // g, den // g
        if den < 0:
            num, den = -num, -den
        rest, twos, fives = den, 0, 0
        while rest % 2 == 0:
            rest //= 2
            twos += 1
        while rest % 5 == 0:
            rest //= 5
            fives += 1
        if rest != 1:
            raise ArithmeticError(f"{self} / {other} has no finite decimal representation")
        k = max(twos, fives)
        return Dec._make(num * 10**k // den, k)

    # --- Darstellung ----------------------------------------------------
    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self}')"

    def __str__(self) -> str:
        sign = "-" if self._coef < 0 else ""
        digits = str(abs(self._coef))
        if self._scale == 0:
            return sign + digits
        digits = digits.rjust(self._scale + 1, "0")
        return f"{sign}{digits[:-self._scale]}.{digits[-self._scale:]}"

    # --- Vergleich / Hash -----------------------------------------------
    def __eq__(self, other: object) -> bool:
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return (self._coef, self._scale) == (o._coef, o._scale)

    def __lt__(self, other: object) -> bool:
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        a, b, _ = self._align(o)
        return a < b

    def __hash__(self) -> int:
        return hash(self._coef) if self._scale == 0 else hash((self._coef, self._scale))

    def __bool__(self) -> bool:
        return self._coef != 0

    # --- Arithmetik -----------------------------------------------------
    def __add__(self, other: object) -> "Dec":
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        a, b, s = self._align(o)
        return Dec._make(a + b, s)

    __radd__ = __add__

    def __sub__(self, other: object) -> "Dec":
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        a, b, s = self._align(o)
        return Dec._make(a - b, s)

    def __rsub__(self, other: object) -> "Dec":
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return o - self

    def __mul__(self, other: object) -> "Dec":
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return Dec._make(self._coef * o._coef, self._scale + o._scale)

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "Dec":
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return self._div(o)

    def __rtruediv__(self, other: object) -> "Dec":
        o = self._coerce(other)
        if o is None:
            return NotImplemented
        return o._div(self)

    def __neg__(self) -> "Dec":
        return Dec._make(-self._coef, self._scale)

    def __pos__(self) -> "Dec":
        return self

    def __abs__(self) -> "Dec":
        return Dec._make(abs(self._coef), self._scale)

    # --- Konvertierung --------------------------------------------------
    def __int__(self) -> int:
        q = abs(self._coef) // 10**self._scale
        return -q if self._coef < 0 else q

    def __float__(self) -> float:
        return self._coef / 10**self._scale

    def __round__(self, ndigits: int | None = None) -> "int | Dec":
        n = 0 if ndigits is None else ndigits
        if self._scale <= n:
            return int(self) if ndigits is None else self
        factor = 10 ** (self._scale - n)
        q, r = divmod(self._coef, factor)
        if 2 * r > factor or (2 * r == factor and q % 2):
            q += 1  # banker's rounding wie builtin round()
        return q if ndigits is None else Dec._make(q, n)


if __name__ == "__main__":
    a, b = Dec("0.1"), Dec("0.2")
    print(a + b == Dec("0.3"))      # True
    print(repr(Dec("1") / 8))       # Dec('0.125')
    print(round(Dec("2.675"), 2))   # 2.68
    print(sorted([Dec("1.5"), 1, Dec("-0.25")]))
    print({Dec("2"): "x"}[2])       # x
```
