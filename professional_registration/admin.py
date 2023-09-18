from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from simple_history.admin import SimpleHistoryAdmin

from .model_admin import ModelAdminMixin
from .models import Education, TeacherMember, WorkExperience, License, Payment



class TeacherMemberAdmin(ModelAdminMixin, SimpleHistoryAdmin, admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('teacher_id',
                       'first_name',
                       'middle_name',
                       'last_name',
                       'gender',
                       'dob',
                       'email',
                       'nationality',
                       'omang',
                       'current_address',)},
         ),
        audit_fieldset_tuple
    )

    radio_fields = {'gender': admin.VERTICAL,}

admin.site.register(TeacherMember, TeacherMemberAdmin)


class EducationAdmin(ModelAdminMixin, SimpleHistoryAdmin, admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('teacher_id',
                       'qualification',
                       'exprence',
                       'teacher_type',
                       'specialization',
                       'education_level',)},
         ),
        audit_fieldset_tuple
    )

    radio_fields = {'teacher_type': admin.VERTICAL,}

admin.site.register(Education, EducationAdmin)


class WorkExperienceAdmin(ModelAdminMixin, SimpleHistoryAdmin, admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('teacher_id',
                       'employment_declaration',
                       'practicing_school',
                       'prev_practice',
                       'prev_practice_name',
                       'criminal',
                       'criminal_explain',
                       'relation_record',
                       'service_training',
                       'security_clearance')},
         ),
        audit_fieldset_tuple
    )

    radio_fields = {
        'prev_practice': admin.VERTICAL,
        'criminal': admin.VERTICAL,}

admin.site.register(WorkExperience, WorkExperienceAdmin)


class LicenseAdmin(ModelAdminMixin, SimpleHistoryAdmin, admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('teacher_id',
                       'license_number',
                       'type',
                       'issue_date',
                       'validity',
                       'status',)},
         ),
        audit_fieldset_tuple
    )

    radio_fields = {
        'type': admin.VERTICAL,
        'status': admin.VERTICAL,}

admin.site.register(License, LicenseAdmin)


class PaymentAdmin(ModelAdminMixin, SimpleHistoryAdmin, admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('teacher_id',
                       'payment_type',
                       'amount',
                       'pay_date',
                       'payment_status')},
         ),
        audit_fieldset_tuple
    )

    radio_fields = {
        'payment_type': admin.VERTICAL,
        'payment_status': admin.VERTICAL,}

admin.site.register(Payment, PaymentAdmin)