# -*- coding: utf-8 -*-


from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.files.images import get_image_dimensions

from django_comments_xtd.forms import XtdCommentForm
from django_comments_xtd.models import TmpXtdComment
from django.contrib.auth.models import User
from front.models import Teacher

import account.forms

from django.shortcuts import get_object_or_404

from django import forms


import account.forms
from django.forms.extras.widgets import SelectDateWidget

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('photo', 'headline', 'about', 'fee', 'skills')
        widgets = {
            'photo': forms.FileInput(),
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'skills': forms.SelectMultiple(attrs={'class': 'chosen-select',
                                                  'data-placeholder': "Selecciona tus habilidades...",
                                                  'style': "width:450px;",
                                                  'tabindex': "2"}),
            'fee': forms.NumberInput(attrs={'class': 'touchspin2'}),
   #         'neighborhood': forms.TextInput(attrs={'class': 'form-control', 
   #                                         'placeholder': "Por ejemplo: Ñuñoa, Las condes, Santiago Centro",}),

        }
        error_messages = {
            'photo': {'required': 'Debe proporcionar una Imagen para su perfil.',
                      'invalid': 'Imagen Invalida'
                      },
            'headline': {'required': 'Debe proporcionar un Extracto para su perfil.',
                         },
            'about': {'required': 'Debe proporcionar Información sobre sus conocimientos.',
                      },
            'skills': {'required': 'Debe proporcionar por lo menos una Habilidad.',
                       'invalid': 'Habilidad Invalida'
                       },
            'fee': {'required': 'Debe proporcionar una tarifa por hora.',
                    'invalid': 'Tarifa Invalida'
                    }
        }

    def clean_fee(self):
        fee = float(self.cleaned_data.get('fee', False))
        if fee < 2000:
            raise forms.ValidationError("El monto minimo es $CL2000")
        elif fee > 50000:
            raise forms.ValidationError("El monto maximo es $CL50000")
        return fee

    def clean_photo(self):
        image = self.cleaned_data.get('photo', False)
        if image:
            if image.size > 2*1024*1024:
                raise forms.ValidationError("La imagen es muy grande, debe tener un tamaño menor a 2 mb")
            w, h = get_image_dimensions(image)
            if w > 1280 or h > 1280:
                raise forms.ValidationError("La imagen debe tener una resolución maxima de 1280x1280 pixeles")

        return image



class SlimCommentForm(XtdCommentForm):


    def get_comment_create_data(self):
        data = super(SlimCommentForm, self).get_comment_create_data()
        return data


    def clean_url(self):

        message = self.cleaned_data['url']
        message = "http://www.mejorpromedio.cl"
        return message

    def clean_name(self):
        data = self.cleaned_data['object_pk']
        user=User.objects.get(pk=data)
        #teacher = get_object_or_404(Teacher, "1")
        message = user.username
        #message = teacher.user.username
        return message

    def clean_userpk(self):
        data = self.cleaned_data['object_pk']
        user=User.objects.get(pk=data)
        #teacher = get_object_or_404(Teacher, "1")
        message = user.id
        #message = teacher.user.username
        return message

SlimCommentForm.base_fields.pop('url')
