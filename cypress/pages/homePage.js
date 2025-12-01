export class HomePage {
    elements = {
        signInLink: () => cy.get('a[title="Log in to your customer account"] > span'),
        usernameBtn: () => cy.get('a.account span.hidden-sm-down'),
    }

    goToLoginPage() {
        this.elements.signInLink().click();
    }

    clickUsernameBtn() {
        this.elements.usernameBtn().click();
    }

    getUsernameBtn() {
        return this.elements.usernameBtn();
    }
}

export default new HomePage()