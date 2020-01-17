from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder
from django import forms
from .models import EventType, HomePage
from tinymce import models as tinymce_models
from tinymce.widgets import TinyMCE


class EventForm(forms.ModelForm):

    class Meta:
        model = EventType
        fields = ['title', 'background_image', 'text_over_image', 'priority', 'content', 'colour', 'text_box_background_image', 'subsection_name1', 'subsection_content1', 'subsection_name2', 'subsection_content2', 'subsection_name3', 'subsection_content3', 'subsection_name4', 'subsection_content4']

    class Media:
        js = ('static/tiny_mce/tinymce.min.js',)

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    'Function',
                    'title',
                    'content',
                    'text_over_image',
                    'priority',
                ),
                Tab(
                    'Aesthetic',
                    'background_image',
                    'text_box_background_image',
                    'colour'
                ),
                Tab(
                    'Subsections',
                    'subsection_name1',
                    'subsection_content1',
                    'subsection_name2',
                    'subsection_content2',
                    'subsection_name3',
                    'subsection_content3',
                    'subsection_name4',
                    'subsection_content4'
                ),
            )

        )
        self.helper.layout.append(Submit('submit', 'Submit'))


class UpdateHomeForm(forms.ModelForm):

    class Meta:
        model = HomePage
        fields = ['title', 'background_image', 'text_over_image', 'content', 'text_box_colour', 'title_colour', 'top_bar_colour', 'website_body_colour', 'footer_colour', 'nav_bar_text_colour']

    class Media:
        js = ('static/tiny_mce/tinymce.min.js',)

    def __init__(self, *args, **kwargs):
        super(UpdateHomeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    'Function',
                    'title',
                    'content',
                    'text_over_image'
                ),
                Tab(
                    'Aesthetic',
                    'background_image',
                    'top_bar_colour',
                    'nav_bar_text_colour',
                    'title_colour',
                    'text_box_colour',
                    'website_body_colour',
                    'footer_colour'
                ),
            )

        )
        self.helper.layout.append(Submit('submit', 'Submit'))
