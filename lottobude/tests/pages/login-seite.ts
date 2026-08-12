import { expect } from '@playwright/test';
import { BasisSeite } from './basis-seite';
import type { Benutzer } from '../daten/benutzer';

/** Anmeldemaske. */
export class LoginSeite extends BasisSeite {
  get pfad(): string {
    return '/login';
  }

  async anmelden(benutzer: Benutzer): Promise<void> {
    await this.page.getByRole('textbox', { name: 'Benutzername' }).fill(benutzer.name);
    await this.page.getByRole('textbox', { name: 'Passwort' }).fill(benutzer.kennwort);
    await this.page.getByRole('button', { name: 'Anmelden' }).click();
  }

  /** Anmeldung mit frei waehlbaren Werten - fuer Negativfaelle. */
  async anmeldenMit(name: string, kennwort: string): Promise<void> {
    await this.page.getByRole('textbox', { name: 'Benutzername' }).fill(name);
    await this.page.getByRole('textbox', { name: 'Passwort' }).fill(kennwort);
    await this.page.getByRole('button', { name: 'Anmelden' }).click();
  }

  /** Fehlermeldung der Maske, z.B. LOGIN_INVALID oder USER_INACTIVE. */
  get fehlermeldung() {
    return this.page.locator('main .fehler');
  }

  async erwarteFehlercode(code: string): Promise<void> {
    await expect(this.fehlermeldung).toContainText(code);
  }
}
