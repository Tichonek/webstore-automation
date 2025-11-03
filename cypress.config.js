const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    baseUrl: 'https://teststore.automationtesting.co.uk/index.php',
    specPattern: 'cypress/e2e/**/*.cy.js'
  },
});
