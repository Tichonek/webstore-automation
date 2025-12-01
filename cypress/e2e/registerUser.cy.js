import homePage from "../pages/homePage";
import loginPage from "../pages/loginPage";
import registerPage from "../pages/RegisterAccountPage";

describe("Register new account", () => {
  beforeEach(() => {
    cy.clearCookies();
    cy.clearLocalStorage();
    cy.task("runPythonGenerator");
    cy.readFile("cypress/test_data.json").as("userData");
    cy.visit("/");
  });

  it("Valid register new account", function () {
    homePage.goToLoginPage();

    loginPage.clickNoAccountBtn();

    // fill register form
    registerPage.checkMrTitle().click().should("be.checked");

    registerPage
      .typeFirstName(this.userData.firstName)
      .should("have.value", this.userData.firstName);
    registerPage
      .typeLastName(this.userData.lastName)
      .should("have.value", this.userData.lastName);
    registerPage
      .typeEmail(this.userData.email)
      .should("have.value", this.userData.email);
    registerPage
      .typePass(this.userData.password)
      .should("have.value", this.userData.password);

    registerPage.checkPrivacyPolicy().check().should("be.checked");

    registerPage.clickSaveBtn();

    // add assertion to check logged user name on homepage
    cy.get("@userData").then((user) => {
      const fullName = `${user.firstName} ${user.lastName}`;

      homePage.getUsernameBtn().should("have.text", fullName);
    });
  });
});
