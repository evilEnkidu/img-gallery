document.addEventListener('DOMContentLoaded', function() {
    const modals = document.querySelectorAll('.modal');
    const totalImages = document.querySelectorAll('.image-class').length;
    
    document.addEventListener('keydown', function(e) {
        const activeModal = document.querySelector('.modal.show');
        if (!activeModal) return;
        
        const currentId = parseInt(activeModal.id.replace('imageModal', ''));
        
        if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
            let nextId;
            
            if (e.key === 'ArrowRight') {
                nextId = currentId < totalImages ? currentId + 1 : 1;
            } else {
                nextId = currentId > 1 ? currentId - 1 : totalImages;
            }
            
            const currentModal = bootstrap.Modal.getInstance(activeModal);
            const nextModal = new bootstrap.Modal(document.getElementById(`imageModal${nextId}`));
            
            currentModal.hide();
            nextModal.show();
        }
    });
});