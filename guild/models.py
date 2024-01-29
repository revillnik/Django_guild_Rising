from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class all_information(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="Slug"
    )
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        default=None,
        blank=True,
        null=True,
        verbose_name="Фото",
    )
    link = models.TextField(verbose_name="Ссылки", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
