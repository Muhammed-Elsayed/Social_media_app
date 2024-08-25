document.addEventListener("DOMContentLoaded", function() {
    // Fetch data from the canfollow API
    fetch('http://127.0.0.1:8000/api/canfollow', {
        credentials: 'include', // This is equivalent to withCredentials: true
    })
    .then(response => response.json())
    .then(data => {
        const followContainer = document.querySelector('.follow-container');
        followContainer.innerHTML = ''; // Clear any existing content

        // Loop through the data and create person cards
        data.forEach(person => {
            const personCard = document.createElement('div');
            personCard.classList.add('person-card');

            // Create inner HTML for person info
            personCard.innerHTML = `
                <div class="person-info">
                    <h3>${person.first_name} ${person.last_name}</h3>
                    <p>${person.bio ? person.bio : "No bio available"}</p>
                    <button class="followBtn">Follow</button>
                </div>
            `;

            // Append the person card to the container
            followContainer.appendChild(personCard);
        });

        // Add event listeners to all follow buttons after they are added to the DOM
        document.querySelectorAll('.followBtn').forEach(button => {
            button.addEventListener('click', () => {
                if (button.textContent === 'Follow') {
                    button.textContent = 'Unfollow';
                } else {
                    button.textContent = 'Follow';
                }
            });
        });
    })
    .catch(error => console.error('Error fetching data:', error));
});
