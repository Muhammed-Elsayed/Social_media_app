document.addEventListener('DOMContentLoaded', () => {
    const signupForm = document.querySelector('.signup_form');

    signupForm.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent the default form submission

        // Get form data
        const first_name = document.getElementById('firstName').value;
        const username = document.getElementById('userName').value.trim();
        const last_name = document.getElementById('lastName').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('newPassword').value;
        const month = document.getElementById('month').value;
        const day = document.getElementById('day').value;
        const year = document.getElementById('year').value;
        const gender = document.querySelector('input[name="fav_language"]:checked')?.value;

        // Basic validation
        if (!first_name || !last_name || !email || !password || !month || !day || !year || !gender || !username) {
            alert('Please fill in all fields.');
            return;
        }

        // Construct the data object
        const formData = {
            first_name,
            last_name,
            username,
            email,
            password,
            date_of_birth: `${year}-${month}-${day}`,
            gender
        };
        console.log(formData);
        console.log(first_name);
        try {
            // Send the data to the server
            const response = await fetch('http://127.0.0.1:8000/api/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            // Handle the response
            if (response.ok) {
                const result = await response.json();
                // Handle success (e.g., show a success message, redirect, etc.)
                console.log('Registration successful:', result);
                alert('Registration successful!');
                // Optionally, redirect to another page or clear the form
                signupForm.reset(); // Clear the form fields
            } else {
                const error = await response.json();
                // Handle errors (e.g., show an error message)
                console.error('Registration failed:', error);
                alert('Registration failed: ' + error.message);
            }
        } catch (error) {
            console.error('Error during registration:', error);
            alert('An error occurred: ' + error.message);
        }
    });
});
