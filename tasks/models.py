from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class Task(models.Model):
    """
    This model stores the information of the tasks
    """

    IN_PROGRESS = 1
    DONE = 2
    ACCEPTED_BUT_NOT_STARTED = 3
    PENDING_FOR_APPROVAL = 4
    NEXT_PRIORITY = 5
    IRRELEVANT = 6
    COMPLETED_IN_OTHER = 7

    STATUS_CHOICES = [
        (IN_PROGRESS, _("In progress")),
        (DONE, _("Done")),
        (ACCEPTED_BUT_NOT_STARTED, _("Accepted but not started")),
        (PENDING_FOR_APPROVAL, _("Pending for approval")),
        (NEXT_PRIORITY, _("Next priority")),
        (IRRELEVANT, _("Irrelevant")),
        (COMPLETED_IN_OTHER, _("Completed in some other task")),
    ]

    # Task information
    assignee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    task_detail = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING_FOR_APPROVAL)

    # Timestamp fields
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    to_be_completed_by = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.task_detail + " for " + self.assignee.first_name
