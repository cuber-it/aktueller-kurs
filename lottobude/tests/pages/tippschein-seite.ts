import { expect } from '@playwright/test';
import { BasisSeite } from './basis-seite';

/**
 * Maske "Tipp abgeben": Tippschein anlegen, Tipps erfassen, abgeben.
 *
 * Hinweis: Die Schaltflaechen tragen in der Oberflaeche keine Umlaute
 * ("Tipp hinzufuegen"). Aendert sich das, muss nur diese Klasse angefasst
 * werden, nicht die Tests.
 */
export class TippscheinSeite extends BasisSeite {
  get pfad(): string {
    return '/tippschein';
  }

  private get zahlenfelder() {
    return this.page.locator('.zahlen input');
  }

  private get tippzeilen() {
    return this.page.locator('main table tbody tr');
  }

  async neuenTippscheinAnlegen(): Promise<string> {
    await this.page.getByRole('button', { name: 'Neuen Tippschein anlegen' }).click();
    return this.scheinnummer();
  }

  /** Nummer des angezeigten Tippscheins - zur Laufzeit gelesen, nie verdrahtet. */
  async scheinnummer(): Promise<string> {
    const ueberschrift = this.page.getByRole('heading', { level: 2 }).first();
    await expect(ueberschrift).toContainText('Tippschein');
    return (await ueberschrift.textContent())!.replace(/\D/g, '');
  }

  async tippErfassen(zahlen: number[]): Promise<void> {
    for (const [position, zahl] of zahlen.entries()) {
      await this.zahlenfelder.nth(position).fill(String(zahl));
    }
    await this.page.getByRole('button', { name: 'Tipp hinzufuegen' }).click();
  }

  /** Erfasst mehrere Tipps und prueft nach jedem, dass er uebernommen wurde. */
  async tippsErfassen(tipps: number[][]): Promise<void> {
    for (const [index, zahlen] of tipps.entries()) {
      await this.tippErfassen(zahlen);
      await expect(this.tippzeilen).toHaveCount(index + 2);
    }
  }

  async erwarteTipps(tipps: number[][]): Promise<void> {
    for (const [index, zahlen] of tipps.entries()) {
      await expect(this.tippzeilen.nth(index + 1)).toContainText(zahlen.join(' - '));
    }
  }

  async anzahlTipps(): Promise<number> {
    return (await this.tippzeilen.count()) - 1;
  }

  async abgeben(): Promise<void> {
    await this.page.getByRole('button', { name: 'Tippschein abgeben' }).click();
  }

  /** Fehlermeldung der Maske, z.B. LOTTO_NUMBER_OUT_OF_RANGE. */
  get fehlermeldung() {
    return this.page.locator('main .fehler');
  }

  async erwarteFehlercode(code: string): Promise<void> {
    await expect(this.fehlermeldung).toContainText(code);
  }

  async erwarteKeinenFehler(): Promise<void> {
    await expect(this.fehlermeldung).toHaveCount(0);
  }
}
