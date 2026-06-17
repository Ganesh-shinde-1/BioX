from django.contrib import admin
from .models import Research , Blog , News  , AboutUs , ContactMessage , Post , Site_Active_models  
from django.utils.html import format_html

from .models import ExamCategory, Exam, AdmitCard, Result


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'publish_by',
        'publish',
        'image_preview',
        'created_at'
    )

    search_fields = (
        'title',
        'publish_by',
        'short_description'
    )

    list_filter = (
        'publish',
        'publish_by'
    )

    prepopulated_fields = {"slug": ("title",)}

    readonly_fields = ('image_preview', 'created_at')

    fields = (
        'title',
        'slug',
        'image',
        'image_preview',
        'short_description',
        'publish',
        'publish_by',
        'content',
        'active',
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" style="border-radius:6px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Preview"


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title','active')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'subject', 'created_at')

    search_fields = ('name', 'email', 'subject')

    list_filter = ('created_at',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'reported_by',
        'date',
        'source_display',
        'image_preview',
        'created_at'
    )

    search_fields = (
        'title',
        'reported_by',
        'short_description'
    )

    list_filter = (
        'date',
        'reported_by'
    )

    prepopulated_fields = {"slug": ("title",)}

    readonly_fields = ('image_preview', 'created_at')

    fields = (
        'title',
        'slug',
        'short_description',
        'reported_by',
        'image',
        'image_preview',
        'content',
        'sources',
        'date',
        'active'
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" style="border-radius:6px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Preview"

    def source_display(self, obj):
        return obj.sources if obj.sources else "N/A"

    source_display.short_description = "Source"


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'research_by',
        'published_date',
        'image_preview'
    )

    search_fields = (
        'title',
        'research_by',
        'short_description'
    )

    list_filter = (
        'published_date',
        'research_by'
    )

    prepopulated_fields = {"slug": ("title",)}

    readonly_fields = ('image_preview',)

    fields = (
        'title',
        'slug',
        'short_description',
        'image',
        'image_preview',
        'research_by',
        'content',
        'published_date',
        'active'
    )

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="80" style="border-radius:5px;" />'
        return "No Image"

    image_preview.allow_tags = True
    image_preview.short_description = "Preview"


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'written_by',
        'date_of_publish',
        'image_preview',
        'created_at'
    )

    search_fields = (
        'title',
        'written_by',
        'short_description'
    )

    list_filter = (
        'date_of_publish',
        'written_by'
    )

    prepopulated_fields = {"slug": ("title",)}

    readonly_fields = ('image_preview', 'created_at')

    fields = (
        'title',
        'slug',
        'short_description',
        'written_by',
        'image',
        'image_preview',
        'content',
        'date_of_publish',
        'active'
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" style="border-radius:6px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Preview"






@admin.register(Site_Active_models)
class SiteActiveAdmin(admin.ModelAdmin):



    list_filter = ( "home", "post", "blog", "news")

    search_fields = ("id",)

    ordering = ("id",)

    list_per_page = 10


from django.contrib import admin
from .models import ExamCategory, Exam


@admin.register(ExamCategory)
class ExamCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'active',
        'created_at'
    )

    list_filter = (
        'active',
        'created_at'
    )

    search_fields = (
        'name',
        'short_description'
    )

    list_editable = (
        'active',
    )

    ordering = ('-created_at',)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'vacancies',
        'qualification',
        'application_start',
        'last_date',
        'active',
        'created_at'
    )

    list_filter = (
        'active',
        'category',
        'application_start',
        'last_date',
        'created_at'
    )

    search_fields = (
        'title',
        'short_description',
        'qualification',
        'vacancies'
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    list_editable = (
        'active',
    )

    date_hierarchy = 'created_at'

    ordering = (
        '-created_at',
    )

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'category',
                'title',
                'slug',
                'image',
                'short_description'
            )
        }),

        ('Links', {
            'fields': (
                'apply_online',
                'official_website'
            )
        }),

        ('Recruitment Details', {
            'fields': (
                'vacancies',
                'qualification',
                'application_start',
                'last_date',
                'exam_date'
            )
        }),

        ('Educational Qualification', {
            'fields': (
                'educational_qualification',
            )
        }),

        ('Age Limit', {
            'fields': (
                'age_limit',
            )
        }),

        ('Status', {
            'fields': (
                'active',
            )
        }),
    )



@admin.register(AdmitCard)
class AdmitCardAdmin(admin.ModelAdmin):

    list_display = (
        'exam',
        'official_link',
        'active',
        'created_at',
    )

    search_fields = (
        'exam',
    )

    list_filter = (
        'active',
        'created_at',
    )

    ordering = ('-created_at',)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = (
        'exam',
        'official_link',
        'active',
        'created_at',
    )

    search_fields = (
        'exam',
    )

    list_filter = (
        'active',
        'created_at',
    )

    ordering = ('-created_at',)
