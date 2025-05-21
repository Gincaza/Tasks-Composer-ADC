function hideAllAndShowForm(formId) {
    document.getElementById('taskContent').style.display = 'none';
    document.getElementById(formId).style.display = 'block';
}

document.getElementById('addTaskButton').addEventListener('click', function() {
    hideAllAndShowForm('addTaskForm');
});

document.querySelectorAll('.cancelTaskButton').forEach(button => {
    button.addEventListener('click', function () {
        document.getElementById('addTaskForm').style.display = 'none';
        document.getElementById('editTaskForm').style.display = 'none';
        document.getElementById('taskContent').style.display = 'block';
    });
});

document.querySelectorAll('.editTaskButton').forEach(button => {
    button.addEventListener('click', function() {
        const taskId = this.getAttribute('data-task-id');
        const taskTitle = this.getAttribute('data-task-title');
        const taskDescription = this.getAttribute('data-task-description');
        const taskDueDate = this.getAttribute('data-task-due-date');

        document.getElementById('editTaskId').value = taskId;
        document.getElementById('editTitle').value = taskTitle;
        document.getElementById('editDescription').value = taskDescription;
        document.getElementById('editDueDate').value = taskDueDate;

        hideAllAndShowForm('editTaskForm');
    });
});

let taskIdToDelete = null;

document.querySelectorAll('.deleteTaskButton').forEach(button => {
    button.addEventListener('click', function() {
        taskIdToDelete = this.getAttribute('data-task-id');
        const deleteModal = new bootstrap.Modal(document.getElementById('deleteTaskModal'));
        deleteModal.show();
    });
});

document.getElementById('confirmDeleteButton').addEventListener('click', function() {
    if (taskIdToDelete) {
        fetch(`/tasks/${taskIdToDelete}/delete/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
            },
        })
        .then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert('Erro ao excluir a tarefa.');
            }
        });
    }
});

document.querySelectorAll('.markCompleted').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        const taskId = this.getAttribute('data-task-id');
        const isCompleted = this.checked;

        fetch(`/tasks/${taskId}/mark_completed/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ completed: isCompleted })
        })
        .then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert('Erro ao atualizar o status da tarefa.');
            }
        });
    });
});

// Função para obter o token CSRF do cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verifica se este cookie começa com o nome desejado
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');