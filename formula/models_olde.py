import datetime
from django.db import models
from .validators import validate_file_extensison
from django import forms
from  django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _
#here is the model of suported orgs
class Support_descrption(models.Model):
    suppo=models.CharField(max_length=255,null=True,blank=True,verbose_name="اسم الجهة الداعمة ")
    suppo_description=models.CharField(max_length=255,null=True,blank=True,verbose_name="وصف حول الجهة ")
    def __str__(self):
            return self.suppo
#this is the application model from user 
class Registration(models.Model):
    """
    Modèle de l'inscription
    """
    gender_CHOICES = (
        ('0', 'Female'),
        ('1', 'Male'),
        ('2', 'prefer not to say'),
       
    )
    education_CHOICES = (
        ('0', 'مادون الثانوي '),
        ('1', 'الثانوي'),
        ('2', 'الجامعي'),
        ('3', 'ما بعد جامعي'),
             
    )
    city_CHOICES = (
        ('aleppo', 'Aleppo'),
        ('damascus', 'Damascus'),('daraa', 'Daraa'),('deir ez-Zor','Deir ez-Zor'),
        ('hama', 'Hama'),('al-Hasakah', 'Al-Hasakah'),('homs', 'Homs'),
        ('idlib', 'Idlib'),  ('latakia', 'Latakia'), ('quneitra', 'Quneitra'),
         ('raqqa', 'Raqqa'),('as-Suwayda', 'As-Suwayda'),('tartus', 'Tartus'),
        ('other', 'other'),

    )

    family_CHOICES = (
       ('متزوج','متزوج/ة'),
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
    procesc_CHOICES = (
         ('0', _('لم يتم البدء بالمعالجة')),
        ('1', _('الخطوة الاولى')),
        ('2', _('الخطوة الثانية')),
       ('3', _('الخطوة الثالثة')),
         ('4', _('تمت المعالجة')),
        ('5', _('تحميل ملفات مرفقة')),

    )
    app_CHOICES = (
        ('0', 'نعم'),
        ('1', 'لا'),

    )
    
    support_CHOICES = (
        ('0', 'مراسلون بلا حدود | RSF'),
        ('1', 'فري بريس أنليميتيد | FPU'),
        ('2', 'مؤسسة الإعلام النسوي الدولية | IWMF'),
        ('3', 'مؤسسة كاليتي | Kality Foundation'),
        ('4', 'لايف لاين | Lifeline'),


        
    )
    jobـCHOICES = (
        ('0', 'مراسل/ة '),
        ('1', 'محرر/ة '),
        ('2', 'مصور/ة '),
        ('3', 'مراسل/ة حربي/ة '),
        ('4', 'مراسل/ة عسكري/ة '), 
        ('5', 'كاتب/ة- مدير/ة المكتب الاعلامي '),
        ('6', ' رئيس/ة تحرير '),
        ('7',' معد/ة تقارير ' ),
        ('8',' سيناريست '),
        ('9',' مدير/ة قسم الإنتاج '),
        ('10','  منسق/ة إعلامي/ة  '),
        ('11',' مونيتير '),
        ('12','مخرج/ة  '),
        ('13','  منتج/ة - متحدث/ة إعلامي/ة'),
        ('14','  عامل/ة في المجال الإعلامي '),
        ('15',' ناشط/ة إعلامي/ة '),
        ('16','  مقدم/ة برامج- مذيع/ة '),
        ('17','فنان/ة تشكيلي/ة '),
        ('18','ممثل/ة '),
        ('19',' غير ذلك'),

    )
    
    #Information perso 
    Application_number= models.AutoField(primary_key=True,default=None,unique=True)
    Application_date = models.DateField(_("application_date "),null=True,auto_now_add=True)
    gender = models.CharField( _("الجنس"),max_length=30,choices=gender_CHOICES,null=True )
    first_name = models.CharField(_("الاسم الاول"), max_length=30 )
    last_name = models.CharField(_("الاسم الاخير"),max_length=255, null=True)
    medical_state_inf=models.CharField(max_length=255, blank=True,choices=app_CHOICES,default=1, null=True, verbose_name="هل لديك وضع صحي خاص ")
    medical_note_inf= models.CharField(max_length=255, blank=True, null=True, verbose_name="شرح مختصر لحالتك الصحية ")

    #birth information 
    birth_date = models.DateField(verbose_name="تاريخ الميلاد ")
    birth_place = models.CharField(max_length=255, verbose_name="مكان الولادة")
    country = CountryField(max_length=255, verbose_name=" الدولة")
    city = models.CharField(max_length=255,null=True,choices=city_CHOICES, verbose_name="المحافظة")
    region= models.CharField(max_length=255,null=True, verbose_name="المنطقة")
    #current adress 
    country_rec=CountryField(max_length=255,verbose_name='الدولة الحالية',default='some_value')
    current_city = models.CharField(max_length=255, verbose_name="المدينة الحالية?",default='')
    #Connection information 
    mail = models.EmailField(max_length=255, verbose_name="البريدالالكتروني")
    phone = models.CharField(max_length=255, blank=True, null=True,verbose_name="الهاتف ") 
    facebook=models.CharField(max_length=255, blank=True, null=True,verbose_name="حساب الفيسبوك") 
    #education and jobs 
    educatton_level=models.CharField(max_length=255, blank=True,choices=education_CHOICES, null=True, verbose_name=" التحصيل العلمي   ")  
    job= models.CharField(max_length=255, blank=True, null=True,choices=jobـCHOICES,verbose_name="المهنة ") 
    start_date=models.DateField(verbose_name='تاريخ بدء العمل',null= True)
    current_org_comp=models.CharField(max_length=255, blank=True, null=True,verbose_name="جهة العمل الحالية") 
    Previous_employers=models.CharField(max_length=255, blank=True, null=True,verbose_name="جهة العمل السابقة") 
    org_memeber =models.CharField(max_length=255, blank=True,default=1,choices=app_CHOICES, null=True,verbose_name="هل كنت عضوا في أحد المجمعات الصحفية")
    paid_job =models.CharField(max_length=255, blank=True, null=True,default=1,choices=app_CHOICES,verbose_name="هل عملت بإجر مسبقاُ")
    name_of_company_paid=models.CharField(max_length=255, blank=True, null=True,verbose_name="اذكر اسم الجهة او المنظمة ") 
    details=models.CharField(max_length=255, blank=True, null=True,verbose_name="يرجى ذكر التفاصيل ") 
    #violation information and details about it 
    violations=models.CharField(max_length=255, blank=True, default=1,null=True,choices=app_CHOICES,verbose_name=" هل سبق أن تعرضت لأي نوع من أنواع الانتهاكات؟")
    relation_with_org=models.CharField(max_length=255, blank=True,choices=app_CHOICES, null=True,verbose_name="هل لديك أي ارتباطات تنظيمية مع أي فصيل عسكري أو ديني أو تجمع سياسي أو ديني؟")
    summary_of_relations = models.TextField(blank=True, null=True, verbose_name="الرجاء الإجابة مع ذكر التفاصيل")
    articls_link_1= models.TextField(max_length=200,  blank=True, null=True,verbose_name="روابط إعلامية منشورة باسمك الصريح أو المستعار")
    summary_of_your_state = models.TextField(blank=True, null=True, verbose_name="اكتب ملخص عن حالتك")
    #ask_for helpe 
    type_of_dmande= models.CharField( max_length=30,verbose_name="طبيعة المساعدة المطلوبة" ,choices=demand_CHOICES,null=True,blank=True )
    resaon_for_help = models.TextField(blank=True, null=True, verbose_name="رجاء اكتب ملخص لسبب طلب المساعدة ")
    list_of_tools=models.TextField(max_length=255, blank=True, null=True,verbose_name="إن كان الدعم المطلوب متعلق بمستلزمات خاصة بالعمل، نرجو تزويدنا بقائمة الأسعار")
    last_job_salary=models.CharField(max_length=255, blank=True, null=True,verbose_name="يرجى ذكر آخر عمل تقاضيت منه أجر وقيمة الأجر")
    reason_stopping_job=models.CharField(max_length=255, blank=True, null=True,verbose_name="لماذا لا تستطيع أن تعمل بأجر في الوقت الحالي؟")
    # family state
    family_state= models.CharField( max_length=30, choices=family_CHOICES,null=True,default='عازب' ,verbose_name="الوضع العائلي")
    have_kids=models.CharField(max_length=255, blank=True,default=1,choices=app_CHOICES, null=True,verbose_name="هل لديك أولاد؟") 
    number_kids=models.CharField(max_length=255, blank=True, null=True,verbose_name="كم عدد أفراد العائلة") 
    summary_of_recsituation = models.TextField(blank=True, null=True, verbose_name="يرجى شرح الوضع الحالي")
    #other org to helpe
    other_org_demand=models.CharField(max_length=255, blank=True,choices=app_CHOICES, null=True,verbose_name="هل تقدمت بطلب مساعدة لأي منظمة سابقاً؟ ")
    name_org=models.CharField(max_length=255, blank=True, null=True,verbose_name="ما هي المنظمة أو المنظمات") 
    date_of_demand_org= models.DateField(blank=True, null=True,verbose_name="نرجو معرفة تاريخ تقديم الطلب ؟ ")
    tyoe_of_demand_other_org=models.CharField(max_length=255, blank=True, null=True,verbose_name="ما هي طبيعة الطلب؟")
    result_of_demand_other_org=models.CharField(max_length=255, blank=True, null=True,verbose_name="ما هي نتيجة الطلب؟")
    recmond_1=models.CharField(max_length=255, blank=True, null=True,verbose_name="مصدر1 للتثبت من عملك")
    phon_1= models.CharField(max_length=255, blank=True, null=True,verbose_name="رقم هاتف للمصدر الاول ")
    email_1=models.EmailField(max_length=255,  blank=True, null=True,verbose_name="بريد الكتروني للمصدر الاول")
    recmond_2=models.CharField(max_length=255, blank=True, null=True,verbose_name="مصدر 2 للتثبت من عملك")
    phon_2= models.CharField(max_length=255, blank=True, null=True,verbose_name="رقم هاتف للمصدر الثاني ")
    email_2=models.EmailField(max_length=255, blank=True, null=True,verbose_name="بريد الكتروني للمصدر الثاني")
    training_media =models.CharField(max_length=255, blank=True,choices=app_CHOICES,default=1, null=True,verbose_name="هل سبق أن شاركت بأي ورشات أو دورات لتطوير الخبرات الإعلامية أو الحقوقية؟") 
    details_traning_media=models.CharField(max_length=255, blank=True, null=True,verbose_name="يرجى ذكر التفاصيل ") 
    #user name and created by and state check 
    created_by = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    state_step=models.CharField( _("المعالجة"),max_length=30,blank=True,default=0, choices=procesc_CHOICES,null=True)
    support_org_state_1=models.ForeignKey(Support_descrption,null=True,default=1,blank=True,on_delete=models.CASCADE,verbose_name="الجهة المحولة" )
    def __str__(self):
            return u"%s" % (self.Application_number)
#evalutions model procesing steps
class Checking(models.Model):
    app_CHOICES = (
        ('0', 'نعم'),
        ('1', 'لا'),

    )
    
    recmond_CHOICES = (
        ('0', 'التنيجة ايجابية'),
        ('1', 'النتيجة سلبية'),

    )
    zerone_CHOICES = (
        ('0', '0'),
        ('1', '1'),

    )
    experinc_CHOICES = (
        ('0', 'أقل من عامين'),
        ('1', 'عامين إلى خمسة'),
        ('2', 'أكثر من خمسة '),
        
    )
    result_CHOICES = (
        ('0', 'مقبولة'),
        ('1', 'مرفوضة'),
        ('2', 'بحث عن مانحين'),
        
    )
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)
    date_of_updat=models.DateField(editable =False,null=True,blank=True,auto_now=True,verbose_name="تاريخ اخر تحديث ")
    tiitle_of_state = models.CharField(max_length=255, blank=True, null=True,verbose_name="عنوان الحالة")
    urg_mark= models.CharField(max_length=255, blank=True, null=True,verbose_name="درجة الطوارئ " )
    confirm_stat=models.CharField(max_length=255, blank=True, null=True,verbose_name="نوع الحالة " )
    verfication_method=models.CharField(max_length=255, blank=True, null=True,verbose_name="آلية التحقق ")
    total_of_note=models.CharField(max_length=255, blank=True,default=0, null=True,verbose_name=" مجموع النقاط")
    #first step 
    family_state_1= models.CharField( max_length=30,null=True,blank=True ,verbose_name="الوضع العائلي")
    medical_state=models.CharField( max_length=30,null=True ,blank=True,verbose_name="-الوضع الطبي ")
    medical_state_note=models.CharField( max_length=30,null=True ,blank=True,verbose_name="تقيم الوضع الصحي")
    educatton_level_1=models.CharField(max_length=255, blank=True, null=True, verbose_name="التحصيل العلمي")
    cruntly_adre=models.CharField( max_length=30,null=True ,blank=True,verbose_name="	تقيم خطورة مكان الإقامة الحالي  ")
    traning_partcipate=models.CharField( max_length=30,null=True ,blank=True,verbose_name="	المشاركة بورشات سابقة")
    member_in_journal=models.CharField( max_length=30,null=True,blank=True ,verbose_name="هل هو عضو في مجمع صحفي")
    hase_violants=models.CharField( max_length=30,null=True ,blank=True,default=1,verbose_name="تعرّض مُقدّم الطلب لأيّ انتهاكات ")
    is_related_with_media= models.CharField(max_length=255, blank=True,choices= app_CHOICES ,null=True, verbose_name="هل طلب الدعم مرتبط بالعمل الصحفي")  
    number_of_year_exprince=models.CharField(max_length=255, blank=True,null=True,choices=experinc_CHOICES, verbose_name= "عدد سنوات الخبرة في العمل")  
    note_of_year_experince=models.CharField(max_length=255, default=0,blank=True,null=True, verbose_name= "تقيم عدد سنوات الخبرة في العمل")
    note_paid_job=models.CharField(max_length=255, blank=True,null=True, verbose_name= "تقيم العمل بإجر")
    manitry_realtion=models.CharField(max_length=255, blank=True,null=True,choices=app_CHOICES, verbose_name= "هل لديه ارتباطات عسكرية")
    note_manitry_realtion=models.CharField(max_length=255, blank=True,null=True, verbose_name= "ملاحظة حول لارتباطات العسكرية")
    is_thier_info_correct=models.CharField(max_length=255,choices=app_CHOICES, blank=True,null=True, verbose_name= "هل قدم معلومات صحيحة ضمن طلب الدعم ")
    #second step 
    is_thier_heate_speech=models.CharField(max_length=255,choices=app_CHOICES, blank=True,null=True, verbose_name= "-	هل يُحرّض على العنف والكراهية؟ أو الإرهاب أو الطائفيّة؟ " )
    is_thier_heate_speech_note=models.CharField(max_length=255, blank=True,null=True, verbose_name= "شرح لتقيم التحريض " )
    type_heate_speech=models.CharField(max_length=255,choices=app_CHOICES, blank=True,null=True, verbose_name= "هل هو خطاب تميّزي على أساس العرق أو الدين أو أو النوع الجندري أو الطائفة أو القوميّة؟ " )
    note_type_heate_speech=models.CharField(max_length=255, blank=True,null=True, verbose_name= "هل هو خطاب تميّزي على أساس العرق أو الدين أو أو النوع الجندري أو الطائفة أو القوميّة؟ " )
    rspect_legal_coppyright=models.CharField(max_length=255,choices=app_CHOICES, blank=True,null=True, verbose_name= "-هل يُراعي الحق في الخصوصيّة والصور؟  " )
    note_rspect_legal_coppyright=models.CharField(max_length=255, blank=True,null=True, verbose_name= "شرح لمراعاة خصوصية الصور " )
    mark_rspect_legal_coppyright=models.CharField(max_length=255, blank=True,default=0,null=True, verbose_name= "-تقيم الحق في الخصوصيّة والصور؟" )
    rspect_coppyright=models.CharField(max_length=255,choices=app_CHOICES, blank=True,null=True, verbose_name= "هل يُراعي حقوق الملكية الفكرية؟ " )
    note_rspect_coppyright=models.CharField(max_length=255, blank=True,null=True, verbose_name= "شرح لاحترام حقوق النشر " )
    mark_rspect_coppyright=models.CharField(max_length=255, blank=True,null=True,default=0,verbose_name= " تقيم شرح لاحترام حقوق النشر  " )
    rspect_right_human=models.CharField(max_length=255,choices=app_CHOICES, blank=True,null=True, verbose_name= "هل يُراعي شرعة حقوق الإنسان؟  " )
    note_rspect_right_human=models.CharField(max_length=255, blank=True,null=True, verbose_name= "شرح لتقيم احترام حقوق الانسان " )
    mark_rspect_right_human=models.CharField(max_length=255, blank=True,null=True,default=0,verbose_name= "تقيم احترام حقوق الانسان " )
    prof_media=models.CharField(max_length=255,choices=zerone_CHOICES, blank=True,null=True, verbose_name= "المهنية في صياغة الاخبار" )
    #third step
    first_recmond_name=models.CharField(max_length=255, blank=True,null=True, verbose_name= "اسم المعرف الاول" )
    here_speech_1=models.CharField(max_length=255,choices=recmond_CHOICES, blank=True,null=True, verbose_name= "شهادة المعرف" )
    recmond_1att=models.CharField(max_length=255,blank=True,null=True,verbose_name='اثبات شهادة المعرف الأول')
    second_recmond_name=models.CharField(max_length=255, blank=True,null=True, verbose_name= "اسم المعرف الثاني" )
    here_speech_2=models.CharField(max_length=255,choices=recmond_CHOICES, blank=True,null=True, verbose_name= "شهادة المعرف" )
    recmond_2_att=models.CharField(max_length=255,blank=True,null=True,verbose_name="اثبات شهادة المعرف الثاني")
    #forth step
    check_responsabl_group_opnion=models.TextField(max_length=255,blank=True,null=True,verbose_name="تحقق مسؤول التواصل أو المتعاونين تسجيل المعلومات الواردة حول طالب الدعم ")
    date_of_verficaton=models.DateField(blank=True, null=True,verbose_name="تاريخ الانتهاء من التحقق ")
    result_of_verfication=models.CharField(max_length=255,choices=result_CHOICES, blank=True, null=True,verbose_name="نتيجة التحقق ")
    sumary_of_study=models.TextField(max_length=255,blank=True,null=True,verbose_name="ملاحظات إضافية تتضمن أية ملاحظات حول الحالة ")
    # def __str__(self):
    #     return self.registration
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.registration:
            self.date_of_updat = timezone.now()
        
        return super(Checking, self).save(*args, **kwargs)
#model to add attach documents
class CaseFile(models.Model):
    case = models.ForeignKey(Registration, on_delete=models.CASCADE) # When a Case is deleted, upload models are also deleted
    file = models.FileField(upload_to='documents/', null = True, blank = True)
    descrpiton=models.CharField(max_length=255,null=True,verbose_name="وصف الملف المرفق ")
    def __unicode__(self):
        return self.case
class SupportOrg(models.Model):
    support_CHOICES = (
        ('0', 'مراسلون بلا حدود | RSF'),
        ('1', 'فري بريس أنليميتيد | FPU'),
        ('2', 'مؤسسة الإعلام النسوي الدولية | IWMF'),
        ('3', 'مؤسسة كاليتي | Kality Foundation'),
        ('4', 'لايف لاين | Lifeline'),


        
    )
    result_of_org_CHOICES = (
        ('0', 'مقبول'),
        ('1', 'مرفوض'),
       
        
    )
    support=models.OneToOneField(Registration, on_delete=models.CASCADE)
    date_of_response= models.DateField(verbose_name="تاريخ الإحالة ",blank=True)
    result_of_org=models.CharField(max_length=255,null=True,choices=result_of_org_CHOICES,default=False,verbose_name="النتيجة")
    date_of_result= models.DateField(verbose_name="تاريخ الإحالة ",blank=True)    
class SupportOrgchild(models.Model):
    support=models.ForeignKey(Registration,on_delete=models.CASCADE)
    support1=models.ForeignKey(Support_descrption,null=True,blank=True,on_delete=models.CASCADE ,verbose_name="الجهة الداعمة ")
    cost=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name="التكلفة مقدرة باليورو" )
#model to add violation to the registration form or application
class Violation(models.Model):
    violation_CHOICES = (
        ('0', ' اعتقال'),
        ('1', 'اختطاف'),
        ('2', 'منع من العمل'),
         ('3', 'مصادرة معدات'),
         ('4', 'اعتداء بالضرب'),
           ('5', 'اصابة'),
             ('6', 'تهديد'),
          ('7', 'ابتزاز'),
       ('8', 'غير ذلك'),

    )
    violation = models.ForeignKey(Registration, on_delete=models.CASCADE)
    violation_type=models.CharField(max_length=200,choices=violation_CHOICES,null=True,verbose_name='نوع الانتهاك')
    date_of_violation= models.DateField(verbose_name="تاريخ الانتهاك ",blank=True)
class docs(models.Model):
    docs= models.ForeignKey(
        Registration,
        verbose_name='docs', on_delete=models.CASCADE
    )
    doc= models.FileField(
        upload_to='documents/', verbose_name='ملف'
    )
    class Meta:
            verbose_name = ' ملفات'
