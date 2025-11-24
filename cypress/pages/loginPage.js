export class LoginPage {
    elements = {
        emailInput: () => cy.get('#field-email'),
        passInput: () => cy.get('#field-password'),
        forgotPassBtn: () => cy.get('div[class="forgot-password"] > a'),
        signInBtn: () => cy.get('#submit-login'),
        noAccountBtn: () => cy.get('div[class="no-account"] > a')
    }

    typeEmail(email) {
        return this.elements.emailInput().clear().type(email);
    }

    typePass(pass) {
        return this.elements.passInput().clear().type(pass);
    }

    clickSignIn() {
        this.elements.signInBtn().click();
    }

    clickForgotPass() {
        this.elements.forgotPassBtn().click();
    }

    clickNoAccountBtn() {
        this.elements.noAccountBtn().click();
    }
}

export default new LoginPage()