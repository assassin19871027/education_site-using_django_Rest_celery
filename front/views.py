from django.shortcuts import render

# Create your views here.



def profile(request):
    """
        return how it works page
    """
    return render(request, "profile.html", locals())


def searchoffer(request):
    """
        return how it works page
    """
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
