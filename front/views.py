from django.shortcuts import get_object_or_404, render, redirect
from urlparse import urlsplit
from django import forms
from django.http import (
    Http404,
    HttpResponseRedirect,
    JsonResponse,
    HttpResponse,
)
from django.db import connection
from django.db.models import Q

from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

from front.models import (
    Teacher,
    Skill,
)
from front.forms import TeacherForm
import account.views

import front.forms


@csrf_exempt
@login_required
def ajax_new_skill(request):
    """ It gets a name and creates a skill with the name given
    """
    skill = None
    if request.method == 'POST':
        skill_name = request.POST.get('skillName', None)
        if skill_name:
            skill, created = Skill.objects.get_or_create(name=skill_name)
        return JsonResponse(
            {'skill_name': skill.name,
             'skill_id': skill.pk,
             'created': created}
        )


class SignupTeacherView(account.views.SignupView):


   def get_success_url(self, **kwargs):
        
        return "/newteacherprofile/"


@login_required
def newteacherprofile(request):
    """
       Manage singup of second step to teacher
    """
    teachform = TeacherForm(request.POST or None, request.FILES or None)


    if request.method == 'POST':
        if teachform.is_valid():
            try:
                teacherM = Teacher.objects.get(user=request.user)
            except:
                teacherM = teachform.save(commit=False)
                teacherM.user = request.user
                teacherM.save()
                skills = teachform.cleaned_data['skills']
                for skill in skills:
                    teacherM.skills.add(skill)
            else:
                teachform = TeacherForm(request.POST or None, request.FILES or None, instance=teacherM)
                teachform.save()
                           

            return HttpResponseRedirect(reverse('teacherprofile', args=(teacherM.id,)))
    return render(request, "newteacherprofile.html", locals())



def comment_posted( request ):
    referer = request.META.get('HTTP_REFERER', None)
    if referer is None:
        pass
    try:
        redirect_to = urlsplit(referer, 'http', False)[2]
    except IndexError:
       pass
    return HttpResponseRedirect(redirect_to)



def teacherprofile(request, teacher_id):
    """
        return teacher profile
    """
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    teachers = Teacher.objects.all()    # this is to get information of all users for display comments.

    return render(request, "teacherprofile.html", locals())



@csrf_exempt
def recieve_comment(request):
    teachers = Teacher.objects.all()
    return render(request, "recieve_form.html", locals())




@login_required
def editteacherprofile(request):
    """
       Edit teacher profile
    """
    if hasattr(request.user, "teacher"):
        usrform = TeacherForm(instance=request.user)
        teacher = Teacher.objects.get(user=request.user)
        teachform = TeacherForm(instance=teacher)

    return render(request, "newteacherprofile.html", locals())

def studentprofile(request):
    """
        return how it works page
    """
    return render(request, "studentprofile.html", locals())


def searchoffer(request):
    """
        return how it works page
    """

    teachers = Teacher.objects.all()#.order_by('-lastseen')
    if request.GET.get("search", False):
        if connection.vendor == "postgresql":
            teachers = Teacher.objects.filter(Q(skills__name__unaccent__contains=request.GET.get("search")) |
                                              Q(about__unaccent__contains=request.GET.get("search")) |
                                             # Q(neighborhood__unaccent__contains=request.GET.get("search")) |
                                              Q(headline__unaccent__contains=request.GET.get("search"))
                                              ).distinct()
        else:

            teachers = Teacher.objects.filter(Q(skills__name__contains=request.GET.get("search")) |
                                              Q(about__contains=request.GET.get("search")) |
                                             # Q(neighborhood__contains=request.GET.get("search")) |
                                              Q(headline__contains=request.GET.get("search"))
                                              ).distinct()

    return render(request, "searchoffer.html", locals())

def searchneed(request):
    """
        return how it works page
    """
    return render(request, "searchneed.html", locals())

def home(request):
    """
        return how it works page
    """
    return render(request, "home.html", locals())





