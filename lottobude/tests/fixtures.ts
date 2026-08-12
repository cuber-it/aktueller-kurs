import { test as basisTest } from '@playwright/test';
import { LoginSeite } from './pages/login-seite';
import { MeineTippsSeite } from './pages/meine-tipps-seite';
import { StartSeite } from './pages/start-seite';
import { TippscheinSeite } from './pages/tippschein-seite';
import type { Benutzer } from './daten/benutzer';

/**
 * Stellt die Seitenklassen als Fixtures bereit, damit Tests sie nicht
 * selbst zusammenbauen muessen.
 *
 * Die Zieladresse kommt aus der Playwright-Konfiguration (baseURL) und ist
 * ueber die Umgebungsvariable LOTTOBUDE_URL umstellbar - so laeuft dieselbe
 * Suite gegen TN 1, TN 2 oder die Review-Instanz.
 */

interface Seiten {
  basisAdresse: string;
  startSeite: StartSeite;
  loginSeite: LoginSeite;
  tippscheinSeite: TippscheinSeite;
  meineTippsSeite: MeineTippsSeite;
  /** Meldet den Benutzer an und liefert die Startseite zurueck. */
  angemeldetAls: (benutzer: Benutzer) => Promise<StartSeite>;
}

export const test = basisTest.extend<Seiten>({
  basisAdresse: async ({ baseURL }, verwende) => {
    await verwende((baseURL ?? 'https://playground.uc-it.de').replace(/\/$/, ''));
  },

  startSeite: async ({ page, basisAdresse }, verwende) => {
    await verwende(new StartSeite(page, basisAdresse));
  },

  loginSeite: async ({ page, basisAdresse }, verwende) => {
    await verwende(new LoginSeite(page, basisAdresse));
  },

  tippscheinSeite: async ({ page, basisAdresse }, verwende) => {
    await verwende(new TippscheinSeite(page, basisAdresse));
  },

  meineTippsSeite: async ({ page, basisAdresse }, verwende) => {
    await verwende(new MeineTippsSeite(page, basisAdresse));
  },

  angemeldetAls: async ({ loginSeite, startSeite }, verwende) => {
    await verwende(async (benutzer: Benutzer) => {
      await loginSeite.oeffnen();
      await loginSeite.anmelden(benutzer);
      await startSeite.erwarteAngemeldetAls(benutzer.anzeigename);
      return startSeite;
    });
  },
});

export { expect } from '@playwright/test';
