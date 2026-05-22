describe('Flask Login Test', () => {

  it('User login successfully kare', () => {
    
    // Flask login page open
    cy.visit('http://127.0.0.1:5000/login')
    
    // Email input
    cy.get('#email').type('muhammadazeemshamim@gmail.com')
    
    // Password input
    cy.get('#password').type('1234')
    
    // Login button click
    cy.get('button[type="submit"]').click()
    
    // Success check (apne page ke hisaab se change kar lena)
    cy.contains('Dashboard')
  })

})