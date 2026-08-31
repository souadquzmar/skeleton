from services.email_service import send_email


def complete_task(task):
    task.completed = True
    task.save(update_fields=["completed"])

    send_email(
        subject="Task Completed",
        message=f'Your task "{task.title}" has been completed.',
        recipient=task.created_by.email,
    )

    return task