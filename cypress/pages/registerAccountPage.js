export class RegisterAccountPage {
    elements = {
        socialTitleMrRadio: () => cy.get('#field-id_gender-1'),
        socialTitleMrsRadio: () => cy.get('label[for="field-id_gender-2"]'),
        firstNameInput: () => cy.get('#field-firstname'),
        lastNameInput: () => cy.get('#field-lastname'),
        emailInput: () => cy.get('#field-email'),
        passInput: () => cy.get('#field-password'),
        birthdateInput: () => cy.get('#field-birthday'),
        reciveOffersCheckbox: () => cy.get('input[name="optin"]'),
        privacyPolicyCheckbox: () => cy.get('input[name="psgdpr"]'),
        newsletterCheckbox: () => cy.get('input[name="newsletter"]'),
        saveBtn: () => cy.get('button[type="submit"]')
    }

    checkMrTitle() {
        return this.elements.socialTitleMrRadio();
    }

    checkMrsTitle() {
        return this.elements.socialTitleMrsRadio();
    }

    typeFirstName(firstName) {
        return this.elements.firstNameInput().clear().type(firstName);
    }

    typeLastName(lastName) {
        return this.elements.lastNameInput().clear().type(lastName);
    }

    typeEmail(email) {
        return this.elements.emailInput().clear().type(email);
    }

    typePass(pass) {
        return this.elements.passInput().clear().type(pass);
    }

    typeBirhtdate(birthdate) {
        return this.elements.birthdateInput().clear().type(birthdate);
    }

    checkReciveOffers() {
       return this.elements.reciveOffersCheckbox();
    }

    checkPrivacyPolicy() {
       return this.elements.privacyPolicyCheckbox();
    }

    checkNewsletter() {
        return this.elements.newsletterCheckbox();
    }
    
    clickSaveBtn() {
        this.elements.saveBtn().click();
    }
}
export default new RegisterAccountPage();
