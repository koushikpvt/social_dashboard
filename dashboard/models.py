from django.db import models


class Post(models.Model):
    """A user-created post displayed on the dashboard."""
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post at {self.created_at.strftime('%Y-%m-%d %H:%M')} - {self.content[:30]}"

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['-created_at']


class UserActivity(models.Model):
    """Logs user activity such as post creation or login."""
    username = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.action} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "User Activity"
        verbose_name_plural = "User Activities"
        ordering = ['-timestamp']


class UserProfile(models.Model):
    threads_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    profile_picture = models.URLField(null=True, blank=True)