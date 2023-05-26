describe('connectie controleren', () => {
  it('passes', () => {
    cy.visit('http://127.0.0.1:8000/')
  })
})

describe('Tests van int btns', () => {
  it('should submit the form', () => {
    // Visit the page that contains the form
    cy.visit('http://127.0.0.1:8000/');

    //Click the Regio button
    cy.get(`a[href="/1/"]`).should('have.text', "Regio's").click();
    // Click the submit button
    cy.get('input[type="submit"][value="haal statistieken op"]').click();

    // Assert the correct page 
    cy.url().should('include', '/1/statistieken') // => true
  });
});
