export class HomePage {
    elements = {
        signInLink: () => cy.get('a[title="Log in to your customer account"] > span'),
    }

    goToLoginPage() {
        this.elements.signInLink().click();
    }
}

export default new HomePage()