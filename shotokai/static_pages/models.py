from django.db import models

from menu import models as menu_model

class StaticPage(models.Model):
    top_level_menu = models.ForeignKey(menu_model.ToplevelEntry, on_delete=models.SET_NULL, null=True)
    menu_caption = models.CharField(max_length=128)
    content = models.TextField()

    def __str__(self):
        return self.menu_caption
