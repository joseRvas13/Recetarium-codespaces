document.addEventListener('DOMContentLoaded', function() {
    const filterToggle = document.getElementById('filter-toggle');
    const filterDropdown = document.getElementById('filter-dropdown');
    const filterSubmit = document.getElementById('filter-submit');

    filterToggle.addEventListener('click', function() {
        filterDropdown.classList.toggle('show');
    });

    filterSubmit.addEventListener('click', function() {
        document.querySelector('form').submit();
    });
});