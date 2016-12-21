from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView



from django.contrib import admin

from front.views import (
    teacherprofile,
    studentprofile,
    recieve_comment,
    searchoffer,
    searchneed,
    home,
    comment_posted,
    SignupTeacherView,
    newteacherprofile,
    editteacherprofile,
    ajax_new_skill,


)


urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^account/signup/teacher/$", SignupTeacherView.as_view(), name="teacher_signup"), 
    url(r"^newteacherprofile/$", newteacherprofile, name="new_teacher_profile"),      
    url(r"^account/", include("account.urls")), #pinax urls

    url(r"^recieve_data/", recieve_comment, name="recieve_comment"),
    
    url(r"^teacherprofile/(?P<teacher_id>\d+)/$", teacherprofile, name="teacherprofile"),
    url(r'^editteacherprofile/$', editteacherprofile, name="editteacherprofile"),
    url(r"^studentprofile/$", studentprofile, name="studentprofile"),
    url(r"^searchoffer/$", searchoffer, name="searchoffer"),
    url(r"^searchneed/$", searchneed, name="searchneed"),
    url(r"^home/$", home, name="homesite"),
    url(r'^comments/posted/$', comment_posted, name="commentposted"),
    url(r'^comments/', include("django_comments_xtd.urls")),
    url(r'^ajax/skills/new/$', ajax_new_skill, name="ajax-new-skill"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
