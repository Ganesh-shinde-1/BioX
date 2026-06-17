from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.utils import timezone




class Site_Active_models(models.Model):
    home=models.BooleanField(default=True)
    post=models.BooleanField(default=True)
    reasearch=models.BooleanField(default=True)
    news=models.BooleanField(default=True)
    update=models.BooleanField(default=True)
    blog=models.BooleanField(default=True)
    about=models.BooleanField(default=True)
    contanct=models.BooleanField(default=True)
        

    def __str__(self):
        return f'Site modules is under the maintainance'



class Post(models.Model):
    active=models.BooleanField(default=False)
    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True, blank=True)

    image = models.ImageField(upload_to='posts/')

    short_description = models.TextField()

    publish = models.DateTimeField()

    publish_by = models.CharField(max_length=150)

    content = HTMLField()

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-publish']


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title} - {self.id}')
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class Research(models.Model):
    active=models.BooleanField(default=False)

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    short_description = models.TextField()

    image = models.ImageField(upload_to='research_images/' )

    research_by = models.CharField(max_length=200)

    content = HTMLField()


    published_date = models.DateTimeField(null=True )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-published_date']


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class Blog(models.Model):
    active=models.BooleanField(default=False)

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    short_description = models.TextField()

    written_by = models.CharField(max_length=150)

    image = models.ImageField(upload_to='blog_images/')

    content = HTMLField()

    date_of_publish = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date_of_publish']


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title




class News(models.Model):
    active=models.BooleanField(default=False)

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    short_description = models.TextField()

    reported_by = models.CharField(max_length=150)

    image = models.ImageField(upload_to='news_images/')

    content = HTMLField()

    sources = models.CharField(max_length=255)

    date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date']


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title







class AboutUs(models.Model):

    
    short_description = models.TextField(blank=True)

    title = models.CharField(max_length=255 , blank=True)

    image = models.ImageField(upload_to='about/' , blank=True)

    content = HTMLField(  blank=True)

    phone = models.CharField(max_length=20 , null=True , blank=True)

    email = models.EmailField(null=True , blank=True)

    address = models.TextField(null=True , blank=True)
    
    facebook = models.URLField( default=True , blank=True)
    twitter = models.URLField( default=True, blank=True)
    # whatsapp = models.URLField()
    insta = models.URLField( blank=True )
    company = models.URLField( blank=True)
    active=models.BooleanField( blank=True)


    def __str__(self):
        return self.title



class ContactMessage(models.Model):

    
    active=models.BooleanField(default=False)

    name = models.CharField(max_length=150)

    email = models.EmailField()

    subject = models.CharField(max_length=255)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} - {self.subject}"
    





class ExamCategory(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        default=timezone.now
    )
    def __str__(self):
        return self.name


class Exam(models.Model):


    category = models.ForeignKey(
        ExamCategory,
        on_delete=models.CASCADE,
        related_name='exams', null=True
    )

    title = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500)

    slug = models.SlugField(
        max_length=600,
        unique=True,
        blank=True
    )

    apply_online = models.URLField(
        blank=True,
        null=True
    )

    official_website = models.URLField(
        blank=True,
        null=True
    )

   

    vacancies = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    qualification = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )

    application_start = models.DateField(
        blank=True,
        null=True
    )

    last_date = models.DateField(
        blank=True,
        null=True
    )

    exam_date = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    image = models.ImageField(upload_to='exam/')


    educational_qualification = HTMLField(  blank=True, null=True)

    age_limit = HTMLField(  blank=True, null=True)



    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        default=timezone.now
    )
    publish = models.DateTimeField(
    )
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class AdmitCard(models.Model):

    exam = models.CharField(max_length=255)

    official_link = models.URLField()

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        default=timezone.now
    )
    def __str__(self):
        return f"{self.exam.title} Admit Card"


class Result(models.Model):

    exam = models.CharField(max_length=255)

    official_link = models.URLField()

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        default=timezone.now
    )
    def __str__(self):
        return f"{self.exam.title} Result"
