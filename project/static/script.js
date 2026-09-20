document.addEventListener('DOMContentLoaded', function() {
    const deleteForms = document.querySelectorAll('.delete-form');
    deleteForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!confirm('Delete this session?')) {
                event.preventDefault();
            }
        });
    });
});
