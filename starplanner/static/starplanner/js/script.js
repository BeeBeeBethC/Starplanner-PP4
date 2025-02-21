console.log('Custom JavaScript is loaded and working!');

/* jshint esversion: 6 */
function showPermissionModal() {
    document.getElementById('permissionModal').style.display = 'block';
}

function closePermissionModal() {
    document.getElementById('permissionModal').style.display = 'none';
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('permissionModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
};
