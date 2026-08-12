import { Locator, Page, expect } from '@playwright/test';

export type Thema = 'black' | 'white' | 'sepia';

/**
 * Gemeinsame Bestandteile aller Seiten: Kopfzeile, Navigation, Themenwahl.
 * Jede konkrete Seitenklasse erbt davon.
 */
export abstract class BasisSeite {
  readonly kopfzeile: Locator;
  readonly navigation: Locator;

  constructor(protected readonly page: Page, protected readonly basis: string) {
    this.kopfzeile = page.locator('.benutzer');
    this.navigation = page.getByRole('navigation');
  }

  /** Pfad der Seite, z.B. "/login". */
  abstract get pfad(): string;

  async oeffnen(): Promise<void> {
    await this.page.goto(this.basis + this.pfad);
  }

  async istGeoeffnet(): Promise<void> {
    await expect(this.page).toHaveURL(this.basis + this.pfad);
  }

  // --- Anmeldezustand ---------------------------------------------------

  async erwarteAngemeldetAls(anzeigename: string): Promise<void> {
    await expect(this.kopfzeile).toContainText(anzeigename);
  }

  async erwarteAbgemeldet(): Promise<void> {
    await expect(this.kopfzeile).toContainText('anmelden');
  }

  async abmelden(): Promise<void> {
    await this.page.getByRole('link', { name: 'abmelden' }).click();
  }

  // --- Navigation -------------------------------------------------------

  async gehZu(menuepunkt: string): Promise<void> {
    await this.navigation.getByRole('link', { name: menuepunkt }).click();
  }

  /** Menuepunkte, die einem Benutzer nicht angezeigt werden duerfen. */
  async erwarteMenuepunktFehlt(menuepunkt: string): Promise<void> {
    await expect(this.navigation.getByRole('link', { name: menuepunkt })).toHaveCount(0);
  }

  // --- Themenwahl -------------------------------------------------------

  async waehleThema(thema: Thema): Promise<void> {
    const beschriftung = { black: 'Black', white: 'White', sepia: 'Sepia' }[thema];
    await this.page.getByRole('button', { name: beschriftung }).click();
  }

  async erwarteThema(thema: Thema): Promise<void> {
    await expect(this.page.locator('html')).toHaveAttribute('data-theme', thema);
  }

  /** Liest das dauerhaft gespeicherte Thema aus der Browserablage. */
  async gespeichertesThema(): Promise<string | null> {
    return this.page.evaluate(() => localStorage.getItem('lottobude-thema'));
  }
}
