import { Locator, expect } from '@playwright/test';
import { BasisSeite } from './basis-seite';

/** Uebersicht der eigenen Tippscheine (LOTTO-102). */
export class MeineTippsSeite extends BasisSeite {
  get pfad(): string {
    return '/meine-tipps';
  }

  private ueberschrift(scheinnummer: string): Locator {
    return this.page.getByRole('heading', {
      name: 'Tippschein ' + scheinnummer,
      level: 2,
    });
  }

  /** Kopfzeile eines Tippscheins mit Ziehung, Status und Quelle. */
  angaben(scheinnummer: string): Locator {
    return this.ueberschrift(scheinnummer).locator('xpath=following-sibling::p[1]');
  }

  tabelle(scheinnummer: string): Locator {
    return this.ueberschrift(scheinnummer).locator('xpath=following-sibling::table[1]');
  }

  async erwarteStatus(scheinnummer: string, status: string): Promise<void> {
    await expect(this.angaben(scheinnummer)).toContainText(status);
  }

  async erwarteZiehung(scheinnummer: string, datum: string): Promise<void> {
    await expect(this.angaben(scheinnummer)).toContainText(datum);
  }

  async erwarteQuelle(scheinnummer: string, quelle: 'WEB' | 'CSV'): Promise<void> {
    await expect(this.angaben(scheinnummer)).toContainText('Quelle ' + quelle);
  }

  async erwarteAnzahlTipps(scheinnummer: string, anzahl: number): Promise<void> {
    await expect(this.tabelle(scheinnummer).locator('tbody tr')).toHaveCount(anzahl + 1);
  }

  /** Sichtbare Tippscheinnummern - nuetzlich fuer Berechtigungspruefungen. */
  async sichtbareScheinnummern(): Promise<string[]> {
    const ueberschriften = await this.page.getByRole('heading', { level: 2 }).allTextContents();
    return ueberschriften.map((text) => text.replace(/\D/g, '')).filter(Boolean);
  }

  async erwarteHinweisAnmeldung(): Promise<void> {
    await expect(this.page.locator('main')).toContainText('Bitte zuerst');
  }
}
