from django.db import models

import static_pages

class ToplevelEntry(models.Model):
    text = models.CharField(max_length=128)

    def __str__(self):
        return self.text