import homePage from "../pages/homePage";
import loginPage from "../pages/loginPage";
import registerPage from "../pages/RegisterAccountPage";

describe('Register new account', () => {
    beforeEach(() => {
        cy.clearCookies();
        cy.clearLocalStorage();
        cy.task('runPythonGenerator');
        cy.visit('/');
    });

    it('Valid register new account', () => {
        homePage.goToLoginPage();

        loginPage.clickNoAccountBtn();

        // fill register form
        registerPage.checkMrTitle().click().should('be.checked')

        cy.readFile('cypress/test_data.json').then((data) => {
            registerPage.typeFirstName(data.firstName).should('have.value', data.firstName);
            registerPage.typeLastName(data.lastName).should('have.value', data.lastName);
            registerPage.typeEmail(data.email).should('have.value', data.email);
            registerPage.typePass(data.password).should('have.value', data.password);
        });

        registerPage.checkPrivacyPolicy().check().should('be.checked');

        registerPage.clickSaveBtn();

        // add assertion to check logged user name on homepage
    })
})