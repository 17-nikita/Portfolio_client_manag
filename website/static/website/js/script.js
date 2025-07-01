

document.addEventListener('DOMContentLoaded', function () {

    // Function to get CSRF token from cookie
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    // Form submission handler using FormData
    async function handleFormSubmit(event, url, messageDiv) {
        event.preventDefault();

        const form = event.target;
        const formData = new FormData(form);

        // Visual feedback
        const submitButton = form.querySelector('button[type="submit"]');
        const originalButtonText = submitButton.textContent;
        submitButton.textContent = 'Processing...';
        submitButton.disabled = true;

        messageDiv.style.display = 'none';
        messageDiv.classList.remove('text-success', 'text-danger');

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: { 'X-CSRFToken': csrftoken },
                body: formData, 
            });

            const result = await response.json();
            messageDiv.style.display = 'block';

            if (response.ok) {
                messageDiv.textContent = result.message || 'Success!';
                messageDiv.classList.add('text-success');
                form.reset();
            } else {
                messageDiv.textContent = result.message || 'Error occurred.';
                messageDiv.classList.add('text-danger');
            }

        } catch (error) {
            console.error('Form submission error:', error);
            messageDiv.style.display = 'block';
            messageDiv.textContent = 'An unexpected error occurred. Please try again.';
            messageDiv.classList.add('text-danger');
        } finally {
            submitButton.textContent = originalButtonText;
            submitButton.disabled = false;
        }
    }

    // Contact Form Setup
    const contactForm = document.getElementById('contact-form');
    const contactMessageDiv = document.getElementById('contact-form-message');

    if (contactForm && contactMessageDiv) {
        const submitUrl = contactForm.dataset.submitUrl;
        if (submitUrl) {
            contactForm.addEventListener('submit', function (event) {
                handleFormSubmit(event, submitUrl, contactMessageDiv);
            });
        } else {
            console.error("Contact form submit URL data attribute is missing!");
        }
    }

    // Newsletter Form Setup
    const newsletterForm = document.getElementById('newsletter-form');
    const newsletterMessageDiv = document.getElementById('newsletter-message');

    if (newsletterForm && newsletterMessageDiv) {
        const submitUrl = newsletterForm.dataset.submitUrl;
        if (submitUrl) {
            newsletterForm.addEventListener('submit', function (event) {
                handleFormSubmit(event, submitUrl, newsletterMessageDiv);
            });
        } else {
            console.error("Newsletter form submit URL data attribute is missing!");
        }
    }

});
