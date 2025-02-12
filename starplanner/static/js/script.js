console.log('Custom JavaScript is loaded and working!');

document.addEventListener('DOMContentLoaded', function () {
console.log('DOM LOADED CALLING FUNCTION...')
    function filterTasksByUser() {
        // Get current user from the page
        const currentUser = document.body.dataset.username;
        const taskElements = document.querySelectorAll('[data-task-user]');
        taskElements.forEach(element => {
            const taskAuthor = element.dataset.taskUser;
            

            // If current user doesn't match task user, disable controls
            if (currentUser !== taskAuthor) {
                const editButtons = element.querySelectorAll('.edit-task');
                const deleteButtons = element.querySelectorAll('.delete-task');
            
                editButtons.forEach(button => {
                    button.classList.remove('active');
                    button.classList.add('disabled');
                    button.setAttribute('disabled', 'disabled');
                    button.setAttribute('aria-disabled', 'true');
                    button.setAttribute('title', 'You can only edit your own tasks');
                });

                deleteButtons.forEach(button => {
                    button.classList.remove('active');
                    button.classList.add('disabled');
                    button.setAttribute('disabled', 'disabled');
                    button.setAttribute('aria-disabled', 'true');
                    button.setAttribute('title', 'You can only delete your own tasks');
                });
            }
        });
    }
console.log('TASK FILTER COMPLETE RUNNING FUNCTION...')
    filterTasksByUser();
}); 