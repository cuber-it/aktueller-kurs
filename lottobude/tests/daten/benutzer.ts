/**
 * Testbenutzer der Lottobude.
 * Entsprechen dem Ausgangszustand, den der Reset herstellt.
 */

export interface Benutzer {
  readonly name: string;
  readonly kennwort: string;
  readonly anzeigename: string;
  readonly gesperrt?: boolean;
  readonly spielleitung?: boolean;
}

export const SPIELER_EINS: Benutzer = {
  name: 'spieler1',
  kennwort: 'lotto123',
  anzeigename: 'Spieler Eins',
};

export const SPIELER_ZWEI: Benutzer = {
  name: 'spieler2',
  kennwort: 'lotto123',
  anzeigename: 'Spieler Zwei',
};

export const GESPERRTER_SPIELER: Benutzer = {
  name: 'gesperrt',
  kennwort: 'lotto123',
  anzeigename: 'Gesperrter Spieler',
  gesperrt: true,
};

export const SPIELLEITUNG: Benutzer = {
  name: 'admin',
  kennwort: 'spielleitung2026',
  anzeigename: 'Spielleitung',
  spielleitung: true,
};
