describe('Dashboard Test', () => {
  it('files show ho rahe hain', () => {
    cy.visit('http://127.0.0.1:5000/dashboard')
    cy.get('table').should('exist')
  })
})