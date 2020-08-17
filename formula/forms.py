from django import forms
from django.shortcuts import render
from .models import Registration, WorkDetail
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from bootstrap3_datetime.widgets import DateTimePicker
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.layout import Field, HTML, Div, Row, Column
from .models import Registration, WorkDetail
from bootstrap_datepicker_plus import DatePickerInput
from django.utils.translation import ugettext_lazy as _
# from betterforms.multiform import MultiModelForm
# from multiform import MultiForm


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkDetail
        fields = [
            'org_name',
            'job_title',
            'job_location',
            'start_date',
            'until_now',
            'end_date',
            'if_salary',
            'salary',
        ]
        after = 'experience'


class RegistrationForm(forms.ModelForm):
    """
    Formulaire d'inscription
    """
    city_CHOICES = (
        ('aleppo', 'Aleppo'),
        ('damascus', 'Damascus'), ('daraa',
                                   'Daraa'), ('deir ez-Zor', 'Deir ez-Zor'),
        ('hama', 'Hama'), ('al-Hasakah', 'Al-Hasakah'), ('homs', 'Homs'),
        ('idlib', 'Idlib'),  ('latakia', 'Latakia'), ('quneitra', 'Quneitra'),
        ('raqqa', 'Raqqa'), ('as-Suwayda', 'As-Suwayda'), ('tartus', 'Tartus'),
        ('other', 'other'),

    )
    gender_CHOICES = (
        ('female', 'Female'),
        ('male', 'Male'),
        ('prefer not to say', 'prefer not to say'),
    )
    family_CHOICES = (
        ('متزوج', 'متزوج/ة'),
        ('أرمل', 'أرمل/ة'),
        ('مطلق', 'مطلق/ة'),
        ('عازب', 'عازب/ة'),
    )
    demand_CHOICES = (
        ('0', 'دعم معيشي'),
        ('1', 'إيجاد فرصة عمل'),
        ('2', 'خروج آمن'),
        ('3', 'دعم ملف اللجوء - تأشيرات خروج'),
        ('4', 'دعم تقني وبطاقات صحفية'),
        ('5', 'دعم طبي'),
        ('6', 'غير ذلك'),
    )
    YESandNO_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),


    )

    city_options = forms.CharField(
        label="City", max_length=255, widget=forms.Select(choices=city_CHOICES))
    educatton_level = forms.CharField(label='Eduction_level',  widget=forms.TextInput(
        attrs={'placeholder': 'اذكر مستواك التعليمي هنا'}))
    job = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'اذكر اخر عمل قمت به'}))
    #org_memeber = forms.ChoiceField(label='Are you a member of any media gathering, or signatories to media covenants of honor or other joint initiatives?',widget=forms.RadioSelect, choices=YESandNO_CHOICES)
    training_media = forms.ChoiceField(
        label='هل سبق أن شاركت بأي ورشات أو دورات لتطوير الخبرات الإعلامية أو الحقوقية', widget=forms.RadioSelect, choices=YESandNO_CHOICES)
    violations = forms.ChoiceField(
        label='هل سبق أن تعرضت لأي نوع من أنواع الانتهاكات؟', widget=forms.RadioSelect, choices=YESandNO_CHOICES)
    relation_with_org = forms.ChoiceField(
        label='هل لديك أي ارتباطات تنظيمية مع أي فصيل عسكري أو ديني أو تجمع سياسي أو ديني؟', widget=forms.RadioSelect, choices=YESandNO_CHOICES)
    have_kids = forms.ChoiceField(
        label='هل لديك أولاد؟', choices=Registration.app_CHOICES)
    other_org_demand = forms.ChoiceField(
        label='هل تقدمت بطلب مساعدة لأي منظمة سابقاً؟', widget=forms.RadioSelect, choices=YESandNO_CHOICES)

    # Ici, tu vas rajouter les champs supplémentaires au modèle
    # Tu définis le captcha
    # Tu ajoutes un mail de confirmation
    confirmation_mail = forms.EmailField(label=" Confirmation of mail ")
    gender = forms.CharField(
        label=_('الجنس'), widget=forms.Select(choices=gender_CHOICES))
    type_of_dmande = forms.CharField(
        label=_('طبيعة المساعدة المطلوب'), widget=forms.Select(choices=demand_CHOICES))
    family_state = forms.CharField(
        label=_('الوضع العائلي'), widget=forms.Select(choices=family_CHOICES))
    current_city = forms.CharField(
        label="In which city ? ", widget=forms.Select(choices=city_CHOICES))

    def __init__(self, *args, **kwargs):
        """
        Surcharge de l'initialisation du formulaire
        """
        super().__init__(*args, **kwargs)
        # Tu modifies le label de la date de naissance pour rajouter le format
        #self.fields['birth_date'].label = "%s (JJ/MM/AAAA)" % "birth date"
        # self.fields['birth_date'].widget.attrs['id'] = ' DateTimePicker'
        # Tu utilises FormHelper pour customiser ton formulaire
        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'registration-form'
        # Tu définis la taille des labels et des champs sur la grille
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        # Tu crées l'affichage de ton formulaire
        self.helper.layout = Layout(
            # Le formulaire va contenir 3 onglets
            TabHolder(
                # Premier onglet
                Tab(
                    # Label de l'onglet
                    _('step1'),
                    # Liste des champs du modèle à afficher dans l'onglet
                    'gender',
                    'first_name',
                    'last_name',

                    'birth_date',
                    'birth_place',
                    'country',
                    # 'city_options',
                    'city',
                    'region',
                    # connection information
                    'mail',
                    'confirmation_mail',
                    'phone_state_inf',
                    'phone',
                    'facebook_state_inf',
                    'facebook',
                    # current address
                    'country_rec',
                    'current_city',
                    # medical info
                    'medical_state_inf',
                    'medical_note_inf',



                    # Tu rajoutes un bouton "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % "Next",
                        type='button',
                        css_class='btn-default col-md-offset-9 btnNext',
                    )

                ),
                Tab(
                    # Label de l'onglet
                    'step 2 ',
                    # person who applay
                    # 'app_owner',
                    'family_state',
                    'have_kids',
                    'number_kids',
                    'summary_of_recsituation',

                    # Tu rajoutes des boutons "Précédent" et "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % 'Previous',
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % 'Next',
                        type='button',
                        css_class='btn-default col-md-offset-8 btnNext',
                    )
                ),

                # Deuxième onglet
                Tab(
                    # Label de l'onglet
                    'step 3',
                    'educatton_level',
                    'job',
                    'experience',


                    'org_memeber',
                    'details',

                    # 'start_date',
                    # 'document_1',
                    # 'document_2',
                    # 'document_3',
                    # 'current_org_comp',
                    # 'Previous_employers',


                    # 'training_media',
                    # 'details_traning_media',
                    # 'violations',
                    # 'date_of_violations',
                    # 'kind_of_violation',


                    # ' document_3',




                    #     'city_recent',

                    # Tu rajoutes des boutons "Précédent" et "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % 'Previous',
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % 'Next',
                        type='button',
                        css_class='btn-default col-md-offset-8 btnNext',
                    )
                ),
                Tab(
                    # Label de l'onglet
                    'Step 4',
                    # person who applay
                    # 'app_owner',
                    'type_of_dmande',
                    'resaon_for_help',
                    'list_of_tools',
                    'last_job_salary',
                    'reason_stopping_job',
                    'other_org_demand',
                    'name_org',
                    'date_of_demand_org',
                    'tyoe_of_demand_other_org',
                    'result_of_demand_other_org',


                    # Tu rajoutes des boutons "Précédent" et "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % 'Previous',
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % 'Next',
                        type='button',
                        css_class='btn-default col-md-offset-8 btnNext',
                    )
                ),
                # Troisième onglet
                Tab(
                    # Label de l'onglet
                    'Step 5                               ',
                    # Liste des champs à afficher dont les champs supplémentaires
                    # Div( HTML("""
                    #   {% load crispy_forms_tags %}
                    #    <div class="">Type
                    #              <select name="refer" id="id_refer" >
                    #              <option ame="l_letter" value="l_letter">Large Letter</option>
                    #              <option name="letter" value="letter">Letter</option>
                    #              <option name="parcel" value="parcel">Parcel</option>
                    #              {{ as_crispy_field }}
                    #              </select>
                    #    </div>
                    #    <div class="" id="other" >
                    #       <input type="text" name="length"  class="dimension" placeholder="Length" maxlength="20">
                    #    </div> """), css_class='col-md-10 col-xs-9' ),
                    'relation_with_org',
                    'summary_of_relations',
                    'articls_link',
                    'recmond_1',
                    'phon_1',
                    'email_1',
                    'recmond_2',
                    'phon_2',
                    'email_2',


                    # Tu rajoutes des boutons "Précédent" et "Valider"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % "Previous",
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-ok" \
                        aria-hidden="true"></span> %s' % "Valide",
                        type='submit',
                        css_class='btn-default col-md-offset-8'
                    )
                ),
            ),
        )

    def clean_confirmation_mail(self):
        """
        Méthode pour vérifier que le mail correspond bien au
        mail de confirmation lors de la validation du formulaire
        """
        confirmation_mail = self.cleaned_data['confirmation_mail']
        mail = self.cleaned_data['mail']
        if mail != confirmation_mail:
            raise forms.ValidationError(
                "Le mail et le mail de confirmation ne sont pas identiques")
        return confirmation_mail

    class Meta:
        # Tu définis le modèle utilisé
        model = Registration
        exclude = []
        widgets = {
            'birth_date': DatePickerInput(),  # default date-format %m/%d/%Y will be used
            'start_date': DatePickerInput(),  # default date-format %m/%d/%Y will be used
            'date_of_violations': DatePickerInput(),
        }
        # child_model = WorkDetail
        # child_form_class = ExperienceForm
