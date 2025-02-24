console.log('Custom JavaScript is loaded and working!');

/* jshint esversion: 6 */
/* exported showPermissionModal, closePermissionModal */
/* global bootstrap */

function showPermissionModal() {
    const myModal = new bootstrap.Modal(document.getElementById('permissionModal'));
    myModal.show();
}

function closePermissionModal() {
    const myModal = bootstrap.Modal.getInstance(document.getElementById('permissionModal'));
    myModal.hide();
}


// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('permissionModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};