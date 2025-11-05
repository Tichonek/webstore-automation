const { defineConfig } = require("cypress");
const fs = require("fs-extra");
const path = require("path");

function cleanReportsAndScreenshots() {
  const reportsDir = path.join(__dirname, 'cypress', 'reports');
  const screenshotDir = path.join(__dirname, 'cypress', 'screenshots');

  if (fs.existsSync(reportsDir)) {
    console.log('Cleaning reports folder');
    fs.emptyDirSync(reportsDir);
  }

  if (fs.existsSync(screenshotDir)) {
    console.log('Cleaning screenshots folder');
    fs.emptyDirSync(screenshotDir);
  }
}

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    baseUrl: 'https://teststore.automationtesting.co.uk/index.php',
    specPattern: 'cypress/e2e/**/*.cy.js',

    //  TO DO
    setupNodeEvents(on, config) {

      on('before:run', () => {
        cleanReportsAndScreenshots();
      });

      return config;
    },

    defaultCommandTimeout: 8000,
    pageLoadTimeout: 60000,
    requestTimeout: 15000,
    responseTimeout: 30000,
    execTimeout: 60000,
    taskTimeout: 60000,

    screenshotsFolder: 'cypress/screenshots',
    screenshotOnRunFailure: true,

    retires: {
      runMode: 2,
      openMode: 0
    },

    chromeWebSecurity: false,
    testIsolation: true,

    viewportWidth: 1440,
    viewportHeight: 900,

    reporter: 'mochawesome',
    reporterOptions: {
      reportDir: 'cypress/reports/mochawesome',
      overwrite: false,
      html: true,
      json: true,
      charts: true,
      embeddedScreenshots: true,
      inlineAssets: true

    }
  },
});
