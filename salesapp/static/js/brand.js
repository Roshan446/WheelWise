    // Get all card bodies
    const cardBodies = document.querySelectorAll('.card-body');

    // Loop through each card body
    cardBodies.forEach(cardBody => {
        // Add mouseenter event listener
        cardBody.addEventListener('mouseenter', function() {
            // Change background color to a darker shade on hover
            this.style.backgroundColor = '#0c2861'; // Change this color as desired
        });

        // Add mouseleave event listener
        cardBody.addEventListener('mouseleave', function() {
            // Change background color back to the original color when not hovered
            this.style.backgroundColor = '#0f62fe'; // Change this color to match the original color
        });
    });
