document.getElementById('add-more-btn').addEventListener('click', function() {
    const formGroup = document.querySelector('.image-form-group').cloneNode(true);
    formGroup.querySelectorAll('input').forEach(input => {
        input.value = '';
        if (input.type === 'number') {
            input.value = '0';
        }
    });
    document.getElementById('image-forms').appendChild(formGroup);
});