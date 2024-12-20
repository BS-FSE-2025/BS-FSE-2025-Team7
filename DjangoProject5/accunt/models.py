from django.db import models


class Rating(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Rating")
    comment = models.TextField(blank=True, null=True, verbose_name="Comment")  # Optional comment
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Created At")  # Timestamp when the rating was created

    def __str__(self):
        return f"Rating: {self.rating} - {self.comment[:50]}"  # Display the first 50 characters of the comment

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        ordering = ['-created_at']  # Order ratings by creation date (newest first)
