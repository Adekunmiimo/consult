from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    meta_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class HeroSection(models.Model):
    page = models.OneToOneField(Page, on_delete=models.CASCADE, related_name='hero_section')
    breadcrumb_text = models.CharField(max_length=200)
    header_text = models.CharField(max_length=200)

    def __str__(self):
        return self.header_text

class InfoSection(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='info_sections')
    image = models.ImageField(upload_to='info_images/')
    header_text = models.CharField(max_length=200)
    body_text = models.TextField()

    def __str__(self):
        return self.header_text

class Card(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='cards')
    icon_class = models.CharField(max_length=50)
    header_text = models.CharField(max_length=100)
    body_text = models.TextField()
    button_text = models.CharField(max_length=50)
    button_link = models.URLField()

    def __str__(self):
        return self.header_text

class Partner(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='partners')
    image = models.ImageField(upload_to='partner_images/')

    def __str__(self):
        return f"Partner image for {self.page.title}"

class Insight(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='insights')
    image = models.ImageField(upload_to='insight_images/')
    category = models.CharField(max_length=50)
    header_text = models.CharField(max_length=200)
    body_text = models.TextField()
    link_text = models.CharField(max_length=50)
    link_url = models.URLField()

    def __str__(self):
        return self.header_text
