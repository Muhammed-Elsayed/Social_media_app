document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('loginForm');

  loginForm.addEventListener('submit', async (event) => {
      event.preventDefault(); // Prevent the default form submission

      // Get the form field values
      const email = document.getElementById('loginEmail').value.trim();
      const password = document.getElementById('loginPassword').value.trim();

      

      // Basic validation (you can add more robust validation as needed)
      if (!email || !password) {
          alert('Please enter both email and password.');
          return;
      }

      // Create form data object
      const formData = {
          email,
          password
      };

      try {
          // Send the data to the server
          const response = await fetch('http://127.0.0.1:8000/api/login', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json'
              },
              body: JSON.stringify(formData)
          });

          // Handle response
          if (response.ok) {
              const result = await response.json();
              console.log('Login successful:', result);
              // Optionally redirect to another page or update the UI
              window.location.href = ''; // Redirect after successful login
          } else {
              console.error('Login failed:', response.status, await response.text());
              alert('Login failed. Please check your email/phone number and password.');
          }
      } catch (error) {
          console.error('Error during login:', error);
          alert('An error occurred while trying to log in. Please try again later.');
      }
  });
});
