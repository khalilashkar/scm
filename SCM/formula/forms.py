from django import forms
from django.shortcuts import render
from .models import Registration
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from bootstrap3_datetime.widgets import DateTimePicker
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.layout import Field, HTML,Div, Row, Column
from .models import Registration
from bootstrap_datepicker_plus import DatePickerInput


class RegistrationForm(forms.ModelForm):
    """
    Formulaire d'inscription
    """
    city_CHOICES = (
        ('aleppo', 'Aleppo'),
        ('damascus', 'Damascus'),('daraa', 'Daraa'),('deir ez-Zor','Deir ez-Zor'),
        ('hama', 'Hama'),('al-Hasakah', 'Al-Hasakah'),('homs', 'Homs'),
        ('idlib', 'Idlib'),  ('latakia', 'Latakia'), ('quneitra', 'Quneitra'),
         ('raqqa', 'Raqqa'),('as-Suwayda', 'As-Suwayda'),('tartus', 'Tartus'),
        ('other', 'other'),

    )
    gender_CHOICES = (
        ('female', 'Female'),
        ('male', 'Male'),
        ('prefer not to say', 'prefer not to say'),

    )
    
    city_options = forms.CharField(max_length=255, widget=forms.Select(choices=city_CHOICES))
    educatton_level = forms.CharField(label='Eduction_level',  widget=forms.TextInput(attrs={'placeholder': 'اكتب القائمة'}))    
    # Ici, tu vas rajouter les champs supplémentaires au modèle
    # Tu définis le captcha
    # Tu ajoutes un mail de confirmation
    confirmation_mail = forms.EmailField(label=" confirmation of mail ")
    gender= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=gender_CHOICES))

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
                    'Step 1                                                                             ',
                    # Liste des champs du modèle à afficher dans l'onglet
                    'gender',
                    'first_name',
                    'last_name',
                     'nick_name',
                    'birth_date',
                    'birth_place',
                    'country',
                    'city_options',
                    'city',
                    #connection information
                    'phone',
                    'mail',
                    'confirmation_mail',
                    # Tu rajoutes un bouton "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % "Next",
                        type='button',
                        css_class='btn-default col-md-offset-9 btnNext',
                    )

                ),
                # Deuxième onglet
                Tab(
                    # Label de l'onglet
                    'Step 2                                     ',
                    'educatton_level',
                    'job',
                   'adress1',
                 
                  'country_rec',
                  #'Sdate_of_job',
                #     'city_recent',
                 # 'start_date',  
           
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
                # Tab(
                #     # Label de l'onglet
                #     'Step 3 ',
                #     # person who applay
                #     # 'app_owner',
                #     'educatton',
                #     'job',
                #     'start_date',  
                #    ' rcently_adress',
                #     'country_recent',
                #     'city_recent',
            
                #     # Tu rajoutes des boutons "Précédent" et "Suivant"
                #     StrictButton(
                #         '<span class="glyphicon glyphicon-arrow-left" \
                #         aria-hidden="true"></span> %s' % 'Previous',
                #         type='button',
                #         css_class='btn-default btnPrevious',
                #     ),
                #     StrictButton(
                #         '<span class="glyphicon glyphicon-arrow-right" \
                #         aria-hidden="true"></span> %s' % 'Next',
                #         type='button',
                #         css_class='btn-default col-md-offset-8 btnNext',
                #     )
                # ),
                # Troisième onglet
                Tab(
                    # Label de l'onglet
                    'Step 4 - Validation                               ',
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
                    
                    'comments',
                    #'document_1',

                    
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
            'birth_date': DatePickerInput(), # default date-format %m/%d/%Y will be used
           #'start_date': DatePickerInput(), # default date-format %m/%d/%Y will be used
        } 
        