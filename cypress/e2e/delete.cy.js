describe('Delete File Test', () => {

  it('user file delete kare', () => {

    // Step 1: Login
    cy.visit('http://127.0.0.1:5000/login')

    cy.get('input[name="email"]').type('muhammadazeemshamim@gmail.com')
    cy.get('input[name="password"]').type('1234')
    cy.get('button').click()

    // Step 2: Upload file (so delete ke liye data ho)
    cy.visit('http://127.0.0.1:5000/dashboard')

    cy.get('input[type="file"]')
      .selectFile('cypress/fixtures/test.pdf')

    cy.get('button').click()

    // Step 3: Dashboard pe jao
    cy.visit('http://127.0.0.1:5000/dashboard')

    // Step 4: Delete button click
    cy.get('.delete-btn').first().click()

    // Step 5: Verify delete
    cy.contains('Deleted')
  })

})