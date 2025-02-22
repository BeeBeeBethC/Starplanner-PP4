console.log('Custom JavaScript is loaded and working!');

document.addEventListener('DOMContentLoaded', function () {
    const modalElement = document.getElementById('permissionModal');
    const modal = new bootstrap.Modal(modalElement, {
        keyboard: true,
        backdrop: 'static' // Ensure the backdrop is set correctly
    });

    window.showPermissionModal = function () {
        console.log("Opening modal...");
        modal.show();
    };

    window.closePermissionModal = function () {
        console.log("Closing modal...");
        modal.hide();
    };

    modalElement.addEventListener('hidden.bs.modal', function () {
        console.log("Modal is now hidden.");
    });
});