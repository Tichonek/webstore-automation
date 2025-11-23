import { HomePage } from "../pages/homePage";
import { LoginPage } from "../pages/loginPage";

const homePage = new HomePage();
const loginPage = new LoginPage();

describe('Open Homepage', () => {
    beforeEach(() => {
        cy.visit('/')
    })
    it('Should contain a header', () => {
        cy.get('h1').should('exist');
    });

    it('Should open login page', () => {
        homePage.goToLoginPage();
        cy.get('#content').should('be.visible')
    });

    it('Should type email and password', () => {
        homePage.goToLoginPage();
        loginPage.typeEmail('email').should('have.value', 'email');
        loginPage.typePass('pass').should('have.value', 'pass');
        loginPage.clickSignIn();
    });

    it('Should click Forgot password button', () => {
        homePage.goToLoginPage();
        loginPage.clickForgotPass();
        cy.url().should('include', 'controller=password');
    })

    it('Should click No account button', () => {
        homePage.goToLoginPage();
        loginPage.clickNoAccountBtn();
        cy.url().should('include', 'controller=registration');
    })

    it('Run data generator', () => {
        cy.task('runPythonGenerator')

        cy.readFile('cypress/test_data.json').then((data) => {
            cy.log('Firs name: ', data.firstName)
        })
    })
})