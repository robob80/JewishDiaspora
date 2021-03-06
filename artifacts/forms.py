import pdb

from django import forms
from django.forms import inlineformset_factory
from django_countries.widgets import CountrySelectWidget, LazySelectMultiple
from django.utils.translation import ugettext as _
from jewishdiaspora.fields import ILPhoneNumberMultiWidget
from users.models import User
from .models import Artifact, ArtifactImage, OriginArea, ArtifactMaterial, ArtifactType


class UserArtifactForm(forms.ModelForm):
    class Meta:
        model = Artifact
        fields = [
            'name_he',
            'origin_country',
            'origin_area',
            'year_from',
            'year_to',
            'description_he',
            'artifact_type',
            'artifact_materials',
            'technical_data_he',
            'donor_name_he',
        ]
        widgets = {
            'name_he': forms.TextInput(attrs={'class': 'form-control'}),
            'origin_country': CountrySelectWidget(attrs={'class': 'form-control'}),
            'origin_area': forms.Select(attrs={'class': 'form-control'}),
            'year_from': forms.TextInput(attrs={'class': 'form-control'}),
            'year_to': forms.TextInput(attrs={'class': 'form-control'}),
            'description_he': forms.Textarea(attrs={'class': 'form-control'}),
            'artifact_type': forms.Select(attrs={'class': 'form-control'}),
            'artifact_materials': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'technical_data_he': forms.Textarea(attrs={'class': 'form-control'}),
            'donor_name_he': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name_he': _('Title'),
            'origin_country': _('Item origin'),
            'origin_area': _('Area or continent'),
            'year_from': _('Year from'),
            'year_to': _('Year to'),
            'description_he': _('Item story'),
            'artifact_type': _('Artifact type'),
            'artifact_materials': _('Material'),
            'technical_data_he': _('Technical data of the item'),
            'donor_name_he': _('Credit'),
        }

    def __init__(self, *args, **kwargs):
        super(UserArtifactForm, self).__init__(*args, **kwargs)

        if self.errors:
            for field in self.fields:
                if field in self.errors:
                    classes = self.fields[field].widget.attrs.get('class', '')
                    classes += ' is-invalid'
                    self.fields[field].widget.attrs['class'] = classes


class ArtifactForm(UserArtifactForm):
    class Meta(UserArtifactForm.Meta):
        fields = [
            'name_he',
            'name_en',
            'slug',
            'origin_country',
            'origin_city_he',
            'origin_city_en',
            'origin_area',
            'year_from',
            'year_to',
            'description_he',
            'description_en',
            'artifact_type',
            'artifact_materials',
            'technical_data_he',
            'technical_data_en',
            'donor_name_he',
            'donor_name_en',
            'display_donor_name',
            'is_featured',
            'is_displayed',
            'displayed_at',
            'route_map',
            'route_he',
            'route_en',
        ]
        widgets = {
            'name_he': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr'}),
            'origin_country': CountrySelectWidget(attrs={'class': 'form-control'}),
            'origin_area': forms.Select(attrs={'class': 'form-control'}),
            'year_from': forms.TextInput(attrs={'class': 'form-control'}),
            'year_to': forms.TextInput(attrs={'class': 'form-control'}),
            'description_he': forms.Textarea(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'description_en': forms.Textarea(attrs={'class': 'form-control', 'dir': 'ltr'}),
            'artifact_type': forms.Select(attrs={'class': 'form-control'}),
            'artifact_materials': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'technical_data_he': forms.Textarea(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'technical_data_en': forms.Textarea(attrs={'class': 'form-control', 'dir': 'ltr'}),
            'donor_name_he': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'donor_name_en': forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'origin_city_he': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'origin_city_en': forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'is_displayed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'displayed_at': forms.TextInput(attrs={'class': 'form-control'}),
            'display_donor_name': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'route_map': forms.FileInput(attrs={'class': 'form-control-file'}),
            'route_he': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'route_en': forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr'}),
        }


class UserArtifactImageForm(forms.ModelForm):
    class Meta:
        model = ArtifactImage
        fields = [
            'image',
            'description_he',
            'location_he',
            'year_era_he',
            'credit_he',
        ]
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description_he': forms.TextInput(attrs={'class': 'form-control'}),
            'location_he': forms.TextInput(attrs={'class': 'form-control'}),
            'year_era_he': forms.TextInput(attrs={'class': 'form-control'}),
            'credit_he': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserArtifactImageForm, self).__init__(*args, **kwargs)
        if self.errors:
            for field in self.fields:
                if field in self.errors:
                    classes = self.fields[field].widget.attrs.get('class', '')
                    classes += ' is-invalid'
                    self.fields[field].widget.attrs['class'] = classes


class ArtifactImageForm(UserArtifactImageForm):
    class Meta(UserArtifactImageForm.Meta):
        fields = [
            'image',
            'description_he',
            'description_en',
            'location_he',
            'location_en',
            'year_era_he',
            'year_era_en',
            'credit_he',
            'credit_en',
            'is_cover',
        ]
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description_he': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'description_en': forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr'}),
            'credit_he': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'credit_en': forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr'}),
            'year_era_he': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'year_era_en': forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr'}),
            'location_he': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'location_en': forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr'}),
            'is_cover': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


UserArtifactImageFormSet = inlineformset_factory(
    Artifact,
    ArtifactImage,
    form=UserArtifactImageForm,
    extra=1,
    max_num=5,
    can_delete=False
)

ArtifactImageFormSet = inlineformset_factory(
    Artifact,
    ArtifactImage,
    form=ArtifactImageForm,
    extra=1,
    max_num=5,
    can_delete=False
)


class ArtifactImagesForm(forms.Form):
    approval = forms.BooleanField(label=_('I approve that I have all the rights to uplaod the image'),
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), initial=True)
    newsletter = forms.BooleanField(label=_('I would love to get info'),
                                    widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        approval = cleaned_data.get('approval')

        if not approval:
            raise forms.ValidationError(
                _("You must approve that you have the rights for the pictures"),
                code='invalid'
            )
        return cleaned_data


class OriginAreaForm(forms.ModelForm):
    class Meta:
        model = OriginArea
        fields = [
            'title_he',
            'title_en',
            'countries'
        ]
        widgets = {
            'title_he': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'title_en': forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr'}),
            'countries': LazySelectMultiple(attrs={'class': 'form-control'}),
        }


class UserForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': _('First and last name')
        }
    ))
    phone_number = forms.CharField(widget=ILPhoneNumberMultiWidget(
        area_attrs={'class': 'form-control'},
        number_attrs={'class': 'form-control', 'size': '7', 'maxlength': '7', 'placeholder': _('Mobile preferred')},
    ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('We will never send you spam')
            }
        ), help_text=_(
            'These information is for contact reference only, it won\'t submitted to 3rd party without your consent')
    )

    def __init__(self, *args, **kwargs):
        self.logged = kwargs.pop('logged')
        super(UserForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if User.objects.filter(email__iexact=email.lower()) and not self.logged:
            raise forms.ValidationError(
                _("There is an existing account with that email address, please login first"),
                code='invalid'
            )
        return cleaned_data


class ArtifactFormImages(forms.Form):
    imageDescription = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    imageLocation = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    imageTime = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    photographerName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


class ArtifactMaterialForm(forms.ModelForm):
    class Meta:
        model = ArtifactMaterial
        fields = ['title_he', 'title_en']
        widgets = {
            'title_he': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'title_en': forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr'}),
        }


class ArtifactTypeForm(forms.ModelForm):
    class Meta:
        model = ArtifactType
        fields = ['title_he', 'title_en']
        widgets = {
            'title_he': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'title_en': forms.TextInput(attrs={'class': 'form-control', 'dir': 'ltr'}),
        }


class YearForm(forms.Form):
    filter = forms.CharField(widget=forms.HiddenInput)
    year_from = forms.CharField(label=_('Year from'), widget=forms.NumberInput, required=False)
    year_to = forms.CharField(label=_('Year to'), widget=forms.NumberInput, required=False)


class LocationForm(forms.Form):
    filter = forms.CharField(widget=forms.HiddenInput)
    location = forms.CharField(label=_('Location'), widget=forms.TextInput, required=False)


class EmptyForm(forms.Form):
    def is_valid(self):
        return True
