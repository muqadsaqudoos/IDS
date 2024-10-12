// Contact Form Submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents the form from submitting the traditional way

    // Display a success message
    const responseMessage = document.getElementById('form-response');
    responseMessage.textContent = 'Thank you for your message! We will get back to you shortly.';
    
    // Reset the form
    this.reset();
});
