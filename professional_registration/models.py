from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin

from django_crypto_fields.fields import IdentityField


class TeacherMember(SiteModelMixin, BaseUuidModel):
    
    teacher_id = models.CharField(
        verbose_name="Registration ID",
        max_length=200,)
    
    first_name = models.CharField(
        verbose_name="First Name",
        max_length=200,)
    
    middle_name = models.CharField(
        verbose_name="Middle Name",
        max_length=200)
    
    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=200)

    gender = models.CharField(
        verbose_name="Gender",
        max_length=200,
        choices=(('male', 'Male'), ('female', 'Female')))

    email = models.EmailField()

    dob = models.DateTimeField("Date of Birth")

    nationality = models.CharField(
        verbose_name="Nationality",
        max_length=200)

    omang = IdentityField(
        verbose_name="Omang/Passport No")

    current_address = models.CharField(
        verbose_name="Current Address",
        max_length=200)

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.teacher_id}, {self.first_name} {self.last_name}'


class Education(SiteModelMixin, BaseUuidModel):

    teacher_id = models.CharField(
        verbose_name="Registration ID",
        max_length=200,)

    qualification = models.CharField(
        verbose_name="Qualification",
        max_length=200,)
    
    exprence = models.CharField(
        verbose_name="Teaching Experience",
        max_length=200)
    
    teacher_type = models.CharField(
        verbose_name="Teacher Type",
        max_length=200,
        choices=(('specialized', 'Specialized'), ('general', 'General')))

    specialization = models.CharField(
        verbose_name="Specilization",
        max_length=200,
        choices=(('math', 'Maths'), ('chemistry', 'Chemistry'), ('english', 'Engilish')))


    education_level = models.CharField(
        verbose_name="Education Level",
        max_length=200,
        choices=(('primary', 'Primary'), ('junior', 'Junior'), ('senior', 'Senior'), ('university', 'University')))

    history = HistoricalRecords()

    def __str__(self):
        return self.teacher_id


class WorkExperience(SiteModelMixin, BaseUuidModel):

    teacher_id = models.CharField(
        verbose_name="Registration ID",
        max_length=200,)

    employment_declaration = models.CharField(
        verbose_name="Are you currently practicing?",
        max_length=200,)
    
    practicing_school = models.CharField(
        verbose_name="Practicing School",
        max_length=200)
    
    prev_practice = models.CharField(
        verbose_name="Do you have a previous practice?",
        max_length=200,
        choices=(('yes', 'Yes'), ('no', 'No')))

    prev_practice_name = models.CharField(
        verbose_name="Previous practice name",
        max_length=200,)

    criminal = models.CharField(
        verbose_name="Have you ever been charged or indicted in Botswana or any country with a criminal offence which you have not been tried i court?",
        max_length=200,
        choices=(('yes', 'Yes'), ('no', 'No')))

    criminal_explain = models.TextField(
        verbose_name="If yes above, explain")

    relation_record = models.FileField(
            verbose_name="Employee relations record",
            upload_to ='uploads/% Y/% m/% d/')

    service_training = models.FileField(
            verbose_name="Service training",
            upload_to ='uploads/% Y/% m/% d/')

    security_clearance = models.FileField(
            verbose_name="Security Clearance",
            upload_to ='uploads/% Y/% m/% d/')

    history = HistoricalRecords()

    def __str__(self):
        return self.teacher_id


class License(SiteModelMixin, BaseUuidModel):

    teacher_id = models.CharField(
        verbose_name="Registration ID",
        max_length=200,)

    license_number = models.CharField(
        verbose_name="License Number",
        max_length=200,)

    type = models.CharField(
        verbose_name="License Type?",
        max_length=200,
        choices=(('permenent', 'Permenent'), ('temporary', 'Temporary'), ('student', 'Student')))
    
    issue_date = models.DateTimeField("Issue date")

    validity = models.DateTimeField("Validity period")
    
    status = models.CharField(
        verbose_name="License status",
        max_length=200,
        choices=(('active', 'Active'), ('deactive', 'Deactive'), ('terminated', 'Terminated'), ('expired', 'Expired')))

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.teacher_id}, {self.license_number}'


class Payment(SiteModelMixin, BaseUuidModel):

    teacher_id = models.CharField(
        verbose_name="Registration ID",
        max_length=200,)

    payment_type = models.CharField(
        verbose_name="Payment Type",
        max_length=200,
        choices=(('registration', 'Registration'), ('license', 'License Application')))

    amount = models.DecimalField(
        verbose_name="Amount paid",
        max_digits=10, decimal_places=2)
    
    pay_date = models.DateTimeField("Date of payment")

    payment_status = models.CharField(
        verbose_name="Payment status",
        max_length=200,
        choices=(('successful', 'Successful'), ('failed', 'Failed'), ('pending', 'Pending')))

    history = HistoricalRecords()

    def __str__(self):
        return self.teacher_id