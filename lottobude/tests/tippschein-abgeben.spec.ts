import { expect, test } from './fixtures';
import { SPIELER_EINS } from './daten/benutzer';
import { FUENF_TIPPS } from './daten/tipps';

/**
 * Durchstich "Tippschein abgeben" (LOTTO-101, LOTTO-102).
 *
 * Bildet den Ablauf nach, der am 2026-08-12 manuell durchgespielt wurde.
 */

test.describe('Tippschein abgeben', () => {
  test('Thema Sepia bleibt ueber den Seitenwechsel erhalten', async ({
    startSeite,
    loginSeite,
  }) => {
    await startSeite.oeffnen();
    await startSeite.waehleThema('sepia');
    await startSeite.erwarteThema('sepia');
    expect(await startSeite.gespeichertesThema()).toBe('sepia');

    await loginSeite.oeffnen();
    await loginSeite.erwarteThema('sepia');
  });

  test('Spieler legt einen Tippschein mit fuenf Tipps an und gibt ihn ab', async ({
    startSeite,
    tippscheinSeite,
    meineTippsSeite,
    angemeldetAls,
  }) => {
    await startSeite.oeffnen();
    const ziehungsdatum = await startSeite.offenesZiehungsdatum();

    await angemeldetAls(SPIELER_EINS);

    // Ein Spieler darf die Spielleitung nicht im Menue sehen.
    await startSeite.erwarteMenuepunktFehlt('Spielleitung');

    await startSeite.gehZu('Tipp abgeben');
    await tippscheinSeite.istGeoeffnet();

    const schein = await tippscheinSeite.neuenTippscheinAnlegen();
    await tippscheinSeite.tippsErfassen(FUENF_TIPPS);
    await tippscheinSeite.erwarteTipps(FUENF_TIPPS);
    await tippscheinSeite.erwarteKeinenFehler();

    await tippscheinSeite.abgeben();
    await meineTippsSeite.istGeoeffnet();

    await meineTippsSeite.erwarteStatus(schein, 'ABGEGEBEN');
    await meineTippsSeite.erwarteZiehung(schein, ziehungsdatum);
    await meineTippsSeite.erwarteQuelle(schein, 'WEB');
    await meineTippsSeite.erwarteAnzahlTipps(schein, FUENF_TIPPS.length);
  });

  test('Abmelden beendet die Sitzung wirklich', async ({
    meineTippsSeite,
    angemeldetAls,
  }) => {
    const start = await angemeldetAls(SPIELER_EINS);
    await start.abmelden();

    // Nicht nur die Weiterleitung pruefen, sondern den Zugriff danach.
    await meineTippsSeite.oeffnen();
    await meineTippsSeite.erwarteHinweisAnmeldung();
    await meineTippsSeite.erwarteAbgemeldet();
  });
});
