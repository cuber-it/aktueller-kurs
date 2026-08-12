/**
 * Tippreihen fuer Tests.
 *
 * Bewusst deterministisch: Ein Test taugt nur dann als Orakel, wenn das
 * erwartete Ergebnis vorher feststeht. Zufallszahlen waeren hier schaedlich.
 */

/** Fuenf gueltige Tipps, paarweise ueberschneidungsfrei. */
export const FUENF_TIPPS: number[][] = [
  [1, 2, 3, 4, 5, 6],
  [7, 8, 9, 10, 11, 12],
  [13, 14, 15, 16, 17, 18],
  [19, 20, 21, 22, 23, 24],
  [25, 26, 27, 28, 29, 30],
];

/** Erzeugt n gueltige, voneinander verschiedene Tipps. */
export function tippreihen(anzahl: number): number[][] {
  return Array.from({ length: anzahl }, (_, i) =>
    [1, 2, 3, 4, 5, 6].map((n) => ((n + i) % 49) + 1),
  );
}

/** Grenzwerte und Negativfaelle fuer die Tippvalidierung. */
export const GRENZFAELLE = {
  kleinsteZahl: [1, 2, 3, 4, 5, 6],
  groessteZahl: [44, 45, 46, 47, 48, 49],
  zuKlein: [0, 1, 2, 3, 4, 5],
  zuGross: [1, 2, 3, 4, 5, 50],
  doppelt: [7, 7, 12, 18, 23, 31],
} as const;
