describe('Open Homepage', () => {
    it('Should contain a header', () => {
        cy.visit('/');
        cy.get('h1').should('exist');
    });
})