console.log('Custom JavaScript is loaded and working!');

function showPermissionModal() {
    var myModal = new bootstrap.Modal(document.getElementById('permissionModal'));
    myModal.show();
}

function closePermissionModal() {
    var myModal = bootstrap.Modal.getInstance(document.getElementById('permissionModal'));
    myModal.hide();
}


// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('permissionModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
};