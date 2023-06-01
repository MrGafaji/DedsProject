describe('connectie controleren', () => {
  it('passes', () => {
    cy.visit('http://127.0.0.1:8000/')
  })
})

describe('Tests of homepage buttons', () => {
  it('should submit the Regio form', () => {
    // Visit the page that contains the form (homepage)
    cy.visit('http://127.0.0.1:8000/');

    //Click the Regio button
    cy.get('a[href="/1/"]').should('have.text', "Regio's").click();

    // Assert the correct page 
    cy.url().should('include', '/1/') // == true

  });

  it('should submit the Klanten form', () => {
  //Visit home page
  cy.visit('http://127.0.0.1:8000/');

    //Click the Klanten button
    cy.get('a[href="/2/"]').should('have.text', "Klanten").click();

    // Assert the correct page 
    cy.url().should('include', '/2/') // == true

  })

  it('should submit the Leveranciers form', () => {
    //Visit home page
    cy.visit('http://127.0.0.1:8000/');
  
      //Click the Leveranciers button
      cy.get('a[href="/5/"]').should('have.text', "Leveranciers").click();
  
      // Assert the correct page 
      cy.url().should('include', '/5/') // == true
  
    })

    it('should submit the Producten form', () => {
      //Visit home page
      cy.visit('http://127.0.0.1:8000/');
    
        //Click the Producten button
        cy.get('a[href="/3/"]').should('have.text', "Producten").click();
    
        // Assert the correct page 
        cy.url().should('include', '/3/') // == true
    
      })

      it('should submit the Medewerkers form', () => {
        //Visit home page
        cy.visit('http://127.0.0.1:8000/');
      
          //Click the Medewerkers button
          cy.get('a[href="/4/"]').should('have.text', "Medewerkers").click();
      
          // Assert the correct page 
          cy.url().should('include', '/4/') // == true
      
        })
});

describe('Tests of haal statistieken buttons', () => {
  it("get the models for Regio's", () => {
    cy.visit('http://127.0.0.1:8000/1/');

    //Click the submit button
    cy.get('input[type="submit"][value="haal statistieken op"]').click();

    // Assert the correct page 
    cy.url().should('include', '/1/statistieken') // == true

  })

  it("get the models for Klanten", () => {

    cy.visit('http://127.0.0.1:8000/2/');

    // Click the submit button
    cy.get('input[type="submit"][value="haal statistieken op"]').click();

    // Assert the "You didn't select a choice" message
    cy.get('p').should('have.text', 'klantenYou didn\'t select a choice.');

    // Assert the correct page 
    cy.url().should('include', '/2/statistieken');

  })

  it('get models for Leveranciers', () => {
    //Visit Leveranciers page
    cy.visit('http://127.0.0.1:8000/5/');

    // Click the submit button
    cy.get('input[type="submit"][value="haal statistieken op"]').click();

     // Assert the "You didn't select a choice" message
     cy.get('p').should('have.text', 'LeveranciersYou didn\'t select a choice.');

     // Assert the correct page 
     cy.url().should('include', '/5/statistieken');

  })

  it('get models for Producten', () => {
    //Visit Leveranciers page
    cy.visit('http://127.0.0.1:8000/3/');

    // Click the submit button
    cy.get('input[type="submit"][value="haal statistieken op"]').click();

     // Assert the "You didn't select a choice" message
     cy.get('p').should('have.text', 'ProductenYou didn\'t select a choice.');

     // Assert the correct page 
     cy.url().should('include', '/3/statistieken');

  })

  it('get models for Medewerkers', () => {
    //Visit Leveranciers page
    cy.visit('http://127.0.0.1:8000/4/');

    // Click the submit button
    cy.get('input[type="submit"][value="haal statistieken op"]').click();

    // Assert the "You didn't select a choice" message
    cy.get('p').should('have.text', 'MedewerkersYou didn\'t select a choice.');

     // Assert the correct page 
     cy.url().should('include', '/4/statistieken');

  })

});