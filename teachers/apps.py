from django.apps import AppConfig as DjangoAppConfig

from datetime import datetime
from dateutil.tz import gettz

from edc_base.apps import AppConfig as BaseEdcBaseAppConfig


class AppConfig(DjangoAppConfig):
    name = 'Professional Teachers Registration'
    verbose_name = 'Professional Teachers Registration'


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Professional Teachers Registration'
    institution = 'Triallav Holdings'
    disclaimer = 'For Triallav Holdings & it\'s Customers use only.'