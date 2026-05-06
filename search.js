document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('job-search');
    const jobCards = document.querySelectorAll('.job-card-item');

    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();

            jobCards.forEach(card => {
                const title = card.querySelector('.card-title').textContent.toLowerCase();
                const location = card.querySelector('.job-location').textContent.toLowerCase();
                const category = card.querySelector('.job-category').textContent.toLowerCase();
                const description = card.querySelector('.job-description').textContent.toLowerCase();

                if (title.includes(searchTerm) || 
                    location.includes(searchTerm) || 
                    category.includes(searchTerm) ||
                    description.includes(searchTerm)) {
                    card.style.display = '';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }
});
