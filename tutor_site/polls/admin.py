from django.contrib import admin

from .models import Question, Choice

# Register your models here.


class ChoiceInlineStacked(admin.StackedInline):
    """Inline Choices inside the Question form in the admin site"""
    model = Choice
    extra = 1


class ChoiceInlineTabular(admin.TabularInline):
    """Inline Choices inside the Question form in the admin site in a more compact form"""
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    """
    Customize how the admin site form for Question looks and works
    """
    # fields = ["pub_date", "question_text"]  # or better yet, use fieldsets as shown next line
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInlineTabular]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]  # add a right bar to the admin to quickly filter the question list
    search_fields = ["question_text"]  # add a search bar


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
