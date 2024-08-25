document.addEventListener('DOMContentLoaded', () => {
    const logoutBtn = document.getElementById('logoutBtn');
    const followBtn = document.getElementById('followBtn');
    const notificationBtn = document.getElementById('notificationBtn');
    const followPage = document.getElementById('followPage');
    const notifications = document.getElementById('notifications');

    // Logout button functionality
    logoutBtn.addEventListener('click', () => {
        window.location.href = 'login.html'; // Redirect to login page
    });

    // Toggle follow page
    followBtn.addEventListener('click', () => {
        followPage.style.display = followPage.style.display === 'none' ? 'block' : 'none';
    });

    // Toggle notifications dropdown
    notificationBtn.addEventListener('click', () => {
        notifications.style.display = notifications.style.display === 'none' ? 'block' : 'none';
    });

    // Handle follow/unfollow button
    document.querySelectorAll('.followBtn').forEach(button => {
        button.addEventListener('click', () => {
            if (button.textContent === 'Follow') {
                button.textContent = 'Unfollow';
            } else {
                button.textContent = 'Follow';
            }
        });
    });

    // Handle like/unlike button
    document.querySelectorAll('.likeBtn').forEach(button => {
        button.addEventListener('click', () => {
            if (button.textContent === 'Like') {
                button.textContent = 'Unlike';
            } else {
                button.textContent = 'Like';
            }
        });
    });

    // Handle post creation
    const postBtn = document.getElementById('postBtn');
    postBtn.addEventListener('click', () => {
        const postContent = document.getElementById('postContent').value;
        const postImage = document.getElementById('postImage').files[0];
        
        if (postContent || postImage) {
            const postsContainer = document.getElementById('postsContainer');

            const newPost = document.createElement('div');
            newPost.classList.add('post');

            const postHeader = document.createElement('h4');
            postHeader.textContent = 'Your Name'; // Replace with actual user name
            newPost.appendChild(postHeader);

            const postText = document.createElement('p');
            postText.textContent = postContent;
            newPost.appendChild(postText);

            if (postImage) {
                const imgElement = document.createElement('img');
                imgElement.src = URL.createObjectURL(postImage);
                newPost.appendChild(imgElement);
            }

            const likeButton = document.createElement('button');
            likeButton.textContent = 'Like';
            likeButton.classList.add('likeBtn');
            newPost.appendChild(likeButton);

            const commentButton = document.createElement('button');
            commentButton.textContent = 'Comment';
            commentButton.classList.add('commentBtn');
            newPost.appendChild(commentButton);

            const commentsSection = document.createElement('div');
            commentsSection.classList.add('comments-section');
            newPost.appendChild(commentsSection);

            postsContainer.insertBefore(newPost, postsContainer.firstChild);

            // Reset post form
            document.getElementById('postContent').value = '';
            document.getElementById('postImage').value = '';

            // Attach event listeners to new buttons
            likeButton.addEventListener('click', () => {
                if (likeButton.textContent === 'Like') {
                    likeButton.textContent = 'Unlike';
                } else {
                    likeButton.textContent = 'Like';
                }
            });
        }
    });
});
