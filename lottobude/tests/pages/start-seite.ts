import { expect } from '@playwright/test';
import { BasisSeite } from './basis-seite';

/** Startseite mit der naechsten Ziehung und der Ziehungsuebersicht. */
export class StartSeite extends BasisSeite {
  get pfad(): string {
    return '/';
  }

  /** Datum der offenen Ziehung, wie es die Startseite ausweist. */
  async offenesZiehungsdatum(): Promise<string> {
    const feld = this.page.locator('main p strong').first();
    await expect(feld).toHaveText(/\d{4}-\d{2}-\d{2}/);
    return (await feld.textContent())!.trim();
  }

  /** Eine Zeile der Ziehungstabelle, ueber das Datum angesteuert. */
  ziehungszeile(datum: string) {
    return this.page.locator('main table tbody tr', { hasText: datum });
  }

  async erwarteZiehungsstatus(datum: string, status: string): Promise<void> {
    await expect(this.ziehungszeile(datum)).toContainText(status);
  }

  async erwarteGewinnzahlen(datum: string, zahlen: number[]): Promise<void> {
    await expect(this.ziehungszeile(datum)).toContainText(zahlen.join(' - '));
  }
}
