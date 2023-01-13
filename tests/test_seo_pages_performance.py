from pages.pages_performance import *
from pytest_bdd import when


@when('I check SEO Pages Performance')
def get_seo_performance():
    seo_pages_performance()
    seo_pages_performance_mobile()


@when('I check SEO Pages Performance and send on slack')
def seo_performance_on_slack():
    seo_performance_slack()

