from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django_comments_xtd.admin import XtdCommentsAdmin
from front.models import SlimComment

from front.models import Teacher, Skill


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False
    verbose_name_plural = 'teachers'

class SlimCommentAdmin(XtdCommentsAdmin):
    list_display = ('thread_level', 'title', 'cid', 'name', 'content_type',
                    'object_pk', 'submit_date', 'followup', 'is_public',
                    'is_removed')
    list_display_links = ('cid', 'title')
    fieldsets = (
        (None,          {'fields': ('content_type', 'object_pk', 'site')}),
        (_('Content'),  {'fields': ('title', 'user', 'user_name', 'user_email',
                                  'user_url', 'comment', 'followup')}),
        (_('Metadata'), {'fields': ('submit_date', 'ip_address',
                                    'is_public', 'is_removed')}),
    )

admin.site.register(SlimComment, SlimCommentAdmin)


admin.site.register(Teacher)
admin.site.register(Skill)