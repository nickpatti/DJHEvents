from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class HomePage(models.Model):
    title = models.CharField(max_length=50)
    background_image = models.ImageField(default=None, verbose_name="Background Image")
    text_over_image = RichTextUploadingField(blank=True, null=True, verbose_name="Text Over Image")
    content = RichTextUploadingField(blank=True, null=True)
    top_bar_colour = models.CharField(max_length=20, default="#343a40", verbose_name="Navigation Bar Colour")
    brand_colour = models.CharField(max_length=20, default="#ffffff", verbose_name="Brand Colour")
    nav_bar_text_colour = models.CharField(max_length=20, default="#ffffff", verbose_name="Navigation Bar Text Colour")
    title_colour = models.CharField(max_length=20, default="#000000", verbose_name="Title Colour")
    text_box_background_image = models.ImageField(default=None, blank=True, null=True, verbose_name="Text Box Background Image")
    text_box_colour = models.CharField(max_length=20, default="#ffffff", verbose_name="Text Box Colour")
    website_body_colour = models.CharField(max_length=20, default="#e5e5e5", verbose_name="Website Body Colour")
    footer_colour = models.CharField(max_length=20, default="#343a40", verbose_name="Footer Colour")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home-detail', kwargs={'pk': self.pk})


class EventType(models.Model):
    title = models.CharField(max_length=50)
    background_image = models.ImageField(default=None, verbose_name="Background Image")
    text_over_image = RichTextUploadingField(blank=True, null=True, verbose_name="Text Over Image")
    content = RichTextUploadingField(blank=True, null=True)
    text_box_background_image = models.ImageField(default=None, blank=True, null=True, verbose_name="Text Box Background Image")
    colour = models.CharField(max_length=20, default="#ffffff")
    priority = models.IntegerField(default=1)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subsection_name1 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Subsection Name 1")
    subsection_content1 = RichTextUploadingField(blank=True, null=True, verbose_name="Subsection Content 1")
    subsection_name2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Subsection Name 2")
    subsection_content2 = RichTextUploadingField(blank=True, null=True, verbose_name="Subsection Content 2")
    subsection_name3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Subsection Name 3")
    subsection_content3 = RichTextUploadingField(blank=True, null=True, verbose_name="Subsection Content 3")
    subsection_name4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Subsection Name 4")
    subsection_content4 = RichTextUploadingField(blank=True, null=True, verbose_name="Subsection Content 4")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['priority']


class ContactPost(models.Model):
    title = models.CharField(max_length=50)
    contact_text = RichTextUploadingField(blank=True, null=True)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['priority']
