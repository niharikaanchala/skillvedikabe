from django.contrib import admin

from .models import AboutHero, CtaSection, DemoSection, ValueItem, ValuesSection

admin.site.register(AboutHero)
admin.site.register(ValuesSection)
admin.site.register(ValueItem)
admin.site.register(CtaSection)
admin.site.register(DemoSection)
