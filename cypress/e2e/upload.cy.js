describe('File Upload', () => {

  it('user file upload kare', () => {

    cy.visit('http://127.0.0.1:5000/dashboard')

    cy.get('input[type="file"]')
      .selectFile('cypress/fixtures/test.pdf')

    cy.get('button[type="submit"]').click()

    cy.url().should('include', '/dashboard')
  })

})