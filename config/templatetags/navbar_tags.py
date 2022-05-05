from django import template
from config.models import AboutUs, SiteSetting

register = template.Library()


@register.inclusion_tag('navbar_partial.html')
def navbar():
    about = True
    site = True
    aboutus_count = AboutUs.objects.count()
    site_setting = SiteSetting.objects.count()
    if aboutus_count > 0:
        about = False
    if site_setting > 0:
        site = False
    return {'about': about, 'site_setting': site}
