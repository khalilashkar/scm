from django.contrib import admin
from .models import Registration, Checking, CaseFile, SupportOrg, SupportOrgchild, Support_descrption, Violation, docs, WorkDetail
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.contrib.admin.models import LogEntry
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display
from django.http import HttpResponse
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
import csv
import codecs
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum, Avg
from django_admin_listfilter_dropdown.filters import DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
# function to compute the sum and average total in list_change


class TotalAveragesChangeList(ChangeList):
    # provide the list of fields that we need to calculate averages and totals
    fields_to_total = ['cost']

    def get_total_values(self, queryset):
        """
        Get the totals
        """
        # basically the total parameter is an empty instance of the given model
        total = SupportOrgchild()
        total.custom_alias_name = "Totals"  # the label for the totals row
        for field in self.fields_to_total:
            setattr(total, field, queryset.aggregate(Sum(field)))

        return total

    def get_results(self, request):
        """
        The model admin gets queryset results from this method
        and then displays it in the template
        """
        super(TotalAveragesChangeList, self).get_results(request)
        # first get the totals from the current changelist
        total = self.get_total_values(self.queryset)
        # then get the averages
        #average = self.get_average_values(self.query_set)
        # small hack. in order to get the objects loaded we need to call for
        # queryset results once so simple len function does it
        len(self.result_list)
        # and finally we add our custom rows to the resulting changelist
        self.result_list._result_cache.append(total)


pdfmetrics.registerFont(TTFont('Arabic', 'account/static/fonts/arabtype.ttf'))
ar = arabic_reshaper.reshape(u' العربية')
ar = get_display(ar)


def write_pdf_view1(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    doc = SimpleDocTemplate(response)
    Catalog = []
    styles = getSampleStyleSheet()
    style_right = ParagraphStyle(name='right', fontName='Arabic', parent=styles[
        'Normal'], alignment=2, direction='RTL', encoding='utf8')
    header = Paragraph(ar, style_right)
    Catalog.append(header)
    #style = styles['Normal']
    img = 'C:/Users/SCM_User/test2/test3/static/test3/image/logo1.jpg'
    im = Image(img, 2*inch, 2*inch)
    Catalog.append(im)
    queryset = queryset.values_list('gender', 'last_name', 'first_name', 'nick_name', 'birth_date', 'birth_place', 'country', 'city', 'medical_state_inf', 'medical_note_inf',
                                    'educatton_level', 'job', 'start_date', 'document_1', 'document_2', 'org_memeber', 'details', 'paid_job', 'name_of_company_paid',
                                    'educatton_level', 'job', 'start_date', 'document_1', 'document_2', 'org_memeber', 'details', 'paid_job', 'name_of_company_paid',
                                    'family_state', 'have_kids', 'number_kids', 'summary_of_recsituation',
                                    'type_of_dmande', 'resaon_for_help', 'list_of_tools', 'last_job_salary', 'reason_stopping_job',
                                    'violations', 'kind_of_violation', 'date_of_violations', 'relation_with_org', 'summary_of_relations',
                                    'other_org_demand', 'name_org', 'date_of_demand_org', 'tyoe_of_demand_other_org', 'result_of_demand_other_org',
                                    'recmond_1', 'phon_1', 'email_1', 'recmond_2', 'phon_2', 'email_2',)
    #titles=['id', 'الاسم الاخير','الاسم الاول','هل لديك وضع صحي خاص']
    for product in queryset:
        for i in range(30):
            ar1 = arabic_reshaper.reshape(str(product[i]))
            ar1 = get_display(ar1)
            #ar2 = arabic_reshaper.reshape(str(titles[i]))
           # ar1=get_display(ar2)
           # p = Paragraph("%s" % ar2, style_right)
            p1 = Paragraph("%s" % ar1, style_right)
            # Catalog.append(p)
            Catalog.append(p1)
            s = Spacer(1, 0.25*inch)
            Catalog.append(s)
    doc.build(Catalog)
    return response


def export_books(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response)
    writer.writerow(['gender', 'last_name', 'first_name', 'nick_name', 'birth_date', 'birth_place', 'country', 'city', 'medical_state_inf', 'medical_note_inf',
                     'educatton_level', 'job', 'start_date', 'document_1', 'document_2', 'org_memeber', 'details', 'paid_job', 'name_of_company_paid',
                     'educatton_level', 'job', 'start_date', 'document_1', 'document_2', 'org_memeber', 'details', 'paid_job', 'name_of_company_paid',
                     'family_state', 'have_kids', 'number_kids', 'summary_of_recsituation',
                     'type_of_dmande', 'resaon_for_help', 'list_of_tools', 'last_job_salary', 'reason_stopping_job',
                     'violations', 'kind_of_violation', 'date_of_violations', 'relation_with_org', 'summary_of_relations',
                     'other_org_demand', 'name_org', 'date_of_demand_org', 'tyoe_of_demand_other_org', 'result_of_demand_other_org',
                     'recmond_1', 'phon_1', 'email_1', 'recmond_2', 'phon_2', 'email_2', ])
    books = queryset.values_list('gender', 'last_name', 'first_name', 'nick_name', 'birth_date', 'birth_place', 'country', 'city', 'medical_state_inf', 'medical_note_inf',
                                 'educatton_level', 'job', 'start_date', 'document_1', 'document_2', 'org_memeber', 'details', 'paid_job', 'name_of_company_paid',
                                 'educatton_level', 'job', 'start_date', 'document_1', 'document_2', 'org_memeber', 'details', 'paid_job', 'name_of_company_paid',
                                 'family_state', 'have_kids', 'number_kids', 'summary_of_recsituation',
                                 'type_of_dmande', 'resaon_for_help', 'list_of_tools', 'last_job_salary', 'reason_stopping_job',
                                 'violations', 'kind_of_violation', 'date_of_violations', 'relation_with_org', 'summary_of_relations',
                                 'other_org_demand', 'name_org', 'date_of_demand_org', 'tyoe_of_demand_other_org', 'result_of_demand_other_org',
                                 'recmond_1', 'phon_1', 'email_1', 'recmond_2', 'phon_2', 'email_2')
    for book in books:
        writer.writerow(book)
    return response


export_books.short_description = 'Export to csv'
# add the attacement files case in admin page as inline fields


class CaseFileInline(admin.StackedInline):
    model = CaseFile
    extra = 0
    fieldsets = [
        [' ', {

            'classes': ['upload_files', ],
            'fields': [('file', 'descrpiton')]
        }],


    ]
# class to add the docs in jobs subform


class DocsInline(admin.TabularInline):
    model = docs
    insert_after = 'details'
    extra = 0
# add the support  org


class SupportInlinechild(admin.StackedInline):
    model = SupportOrgchild
    extra = 0

    fieldsets = [
        ['', {

            'classes': ['supportchild', ],
            'fields': [('support1',)]
        }],
        ['', {

            'classes': ['supportchild_cost', ],
            'fields': [('cost',)]
        }],

    ]
# add the violations inline


class ViolationInline(admin.TabularInline):
    model = Violation
    insert_after = 'violations'
    extra = 0


# WORK DETAILS INLINE
class WorkDetailsInline(admin.TabularInline):
    model = WorkDetail
    insert_after = "experience"
    extra = 0

    fieldsets = [
        ['الخبرات السابقة', {
            # 'classes': ['work_detail'],
            'fields': [('org_name', 'job_title', 'job_location'), ('start_date', 'until_now', 'end_date'), ('if_salary', 'salary')]
        }],
    ]

# add the child support form


class SupportInline(admin.StackedInline):
    model = SupportOrg

    fieldsets = [
        [' بيانات الاستجابة', {

            'classes': ['support'],
            'fields': [('date_of_response', 'result_of_org', 'date_of_result')]
        }],

    ]


class CheckingInline1(admin.StackedInline):
    model = Checking
    fieldsets = [
        ['المعالجة', {
            'fields': [('tiitle_of_state', 'urg_mark', 'confirm_stat'), ('date_of_updat', 'total_of_note')]
        }],
        ['الخطوة الأولى من التحقق', {
            'classes': ['first_step', 'collapse'],
            'fields': [('family_state_1', 'medical_state', 'medical_state_note', 'educatton_level_1',), ('cruntly_adre', 'traning_partcipate', 'member_in_journal',), ('hase_violants', 'is_related_with_media', 'number_of_year_exprince', 'note_of_year_experince'), ('note_paid_job', 'manitry_realtion', 'note_manitry_realtion'), ('is_thier_info_correct'), ]
        }],
        ['الخطوة الثانية من التحقق', {
            'classes': ['second_step', 'collapse'],
            'fields': [('is_thier_heate_speech', 'is_thier_heate_speech_note', 'type_heate_speech'), ('note_type_heate_speech', 'rspect_legal_coppyright', 'note_rspect_legal_coppyright',),
                       ('mark_rspect_legal_coppyright', 'rspect_coppyright',
                        'note_rspect_coppyright', 'mark_rspect_coppyright'),
                       ('rspect_right_human', 'note_rspect_right_human', 'mark_rspect_right_human'), ('prof_media'), ]
        }],
        ['الخطوة الثالثة من التحقق', {
            'classes': ['third_step', 'collapse'],
            'fields': [('first_recmond_name', 'here_speech_1', 'recmond_1att'), ('second_recmond_name', 'here_speech_2', 'recmond_2_att'), ]


        }],
        ['الخطوة الرابعة من التحقق', {
            'classes': ['forth_step', 'collapse'],
            'fields': ['check_responsabl_group_opnion', 'date_of_verficaton', 'result_of_verfication', 'sumary_of_study']


        }],

    ]
    readonly_fields = ('date_of_updat',)
    show_change_link = True


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('Application_number', 'last_name', 'first_name', 'educatton_level',
                    'support_org_state_1', 'city', 'Application_date', 'created_by', 'state_step',)
    # group fields in sub groups
    fieldsets = [
        ['المعالجة', {
            'classes': ['collapse'],
            'fields': [('created_by', 'state_step', 'support_org_state_1'), ]
        }],
        ['معلومات شخصية', {
            'classes': ['collapse'],
            'fields': [('gender'), ('first_name', 'last_name'), ('birth_date', 'birth_place'), ('country', 'city', 'region'), ('mail'), ('phone_state_inf', 'phone'), ('facebook_state_inf', 'facebook'), ('medical_state_inf', 'medical_note_inf'), ]
        }],
        ['الوضع العائلي', {
            'classes': ['collapse'],
            'fields': ['family_state', 'have_kids', 'number_kids', 'summary_of_recsituation']
        }],
        ['معلومات العمل', {
            'classes': ['collapse'],

            'fields': [('educatton_level', 'job'), ('experience'), ('org_memeber', 'details')]
        }],
        ['ملخص يشرح حالتك وروابط من عملك', {
            'classes': ['collapse'],
            'fields': [('if_article_linke', 'articls_link_1'), ('if_stop_work', 'date_stop_work'), ('resource_prof'), ('recmond_1', 'phon_1', 'email_1'), ('recmond_2', 'phon_2', 'email_2'), ("training_media", "details_traning_media"), ('summary_of_your_state')]
        }],
        ['الانتهاكات', {
            'classes': ['collapse'],
            'fields': [('violations'), ('relation_with_org', 'summary_of_relations')]
        }],
        ['معلومات اخرى', {
            'classes': ['collapse'],
            'fields': [('other_org_demand'), ('name_org', 'date_of_demand_org'), ('tyoe_of_demand_other_org', 'result_of_demand_other_org'), ('know_support_programme')]
        }],

        ['نوع الدعم', {
            'classes': ['collapse'],
            'fields': [('type_of_dmande'), ('resaon_for_help'), ('list_of_tools'), ('last_job_salary', 'reason_stopping_job'), ('summary_of_help')]
        }],
    ]
    inlines = [
        CheckingInline1, SupportInline, SupportInlinechild, CaseFileInline, ViolationInline, DocsInline, WorkDetailsInline
    ]
    # custom for add inlinfrorm after sp field
    change_form_template = 'admin/custom/change_form.html'
    # filtering
    list_filter = (('city'), ('gender', ChoiceDropdownFilter), ('Application_date', DateRangeFilter), ('state_step', ChoiceDropdownFilter), 'created_by', ('type_of_dmande',
                                                                                                                                                           ChoiceDropdownFilter), ('educatton_level', ChoiceDropdownFilter), ('family_state', ChoiceDropdownFilter), ('medical_state_inf', ChoiceDropdownFilter))
    search_fields = ('city', 'mail', 'first_name', 'last_name',
                     'Application_number', 'type_of_dmande')
    actions = [write_pdf_view1, export_books, ]
    # def has_change_permission(self, request, obj=None):
    #       return False
    # function to get the user name after any action
    # Action=None

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

       # function to add placeholder to admin model without jquery
    # def render_change_form(self, request, context, *args, **kwargs):
    #     form_instance = context['adminform'].form
    #     form_instance.fields['nick_name'].widget.attrs['placeholder'] = 'Your street'

    #     return super().render_change_form(request, context, *args, **kwargs)
    # def get_readonly_fields(self, request, obj=None):
    #         if obj: #This is the case when obj is already created i.e. it's an edit
    #           return [ 'last_name','educatton_level','city','Application_date','nick_name','educatton_level','job','start_date','document_1','document_2','document_3']
    #         else:
    #           return []

    class Media:
        js = ('//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
              'formula/js/test_olde.js', 'formula/js/work.js',)
        css = {
            'all': (
                '/static/formula/js/css/admin.css',
            )
        }


class CheckingAdmin(admin.ModelAdmin):
    list_display = ('registration', 'tiitle_of_state',
                    'urg_mark', 'confirm_stat', 'result_of_verfication')
    # group fields in sub groups
    list_filter = ('result_of_verfication', ('date_of_updat',
                                             DateRangeFilter), 'manitry_realtion')
    search_fields = ('tiitle_of_state', 'urg_mark')


class LogAdmin(admin.ModelAdmin):
    """Create an admin view of the history/log table"""
    list_display = ('action_time', 'user', 'content_type',
                    'change_message', 'is_addition', 'is_change', 'is_deletion')
    list_filter = ['action_time', 'user', 'content_type']
    ordering = ('-action_time',)
    # We don't want people changing this historical record:

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        # returning false causes table to not show up in admin page :-(
        # I guess we have to allow changing for now
        return True

    def has_delete_permission(self, request, obj=None):
        return False


class CaseFileadmin(admin.ModelAdmin):
    """Create an admin view of the history/log table"""
    list_display = ('case', 'file', 'descrpiton')
    search_fields = ['case__Application_number', 'file', 'descrpiton']
    show_change_link = True


class orgchildeadmin(admin.ModelAdmin):
    """Create an admin view of the cost and support """
    list_display = ('support', 'support1', 'cost')
    search_fields = ['support__Application_number', 'support1', 'cost']
    list_filter = ['support1', ]
    show_change_link = True
    # sum function in list display

    def get_changelist(self, request, **kwargs):
        return TotalAveragesChangeList


class org_description_admin(admin.ModelAdmin):
    """Create an admin view of the cost and support """
    list_display = ('suppo', 'suppo_description')
    search_fields = ['suppo', 'suppo_description']
    list_filter = ['suppo', ]
    show_change_link = True
# inline admin class for violations


class Violation_admin(admin.ModelAdmin):
    # Create the violation list
    list_display = ('violation', 'violation_type', 'date_of_violation',)


admin.site.register(Checking, CheckingAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(LogEntry, LogAdmin)
admin.site.register(CaseFile, CaseFileadmin)
admin.site.register(SupportOrgchild, orgchildeadmin)
admin.site.register(Support_descrption, org_description_admin)
admin.site.register(Violation, Violation_admin)
