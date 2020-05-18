from django.contrib import admin
from django.contrib import messages
from .models import CasosPorCidadePiaui, UpdateData
from django.utils.module_loading import import_string
from core import apps


admin.site.register(CasosPorCidadePiaui)


@admin.register(UpdateData)
class UpdateDataAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'file_name', 'active',)
    search_fields = ('name', 'active',)
    actions = ['update_selected']

    def update_selected(self, request, queryset):
        for model in queryset:
            name = model.file_name
            feedback, message = messages.INFO, f'Successfully updated with file {model.file_name}.'

            package = f'{apps.CoreConfig.name}.scraps'
            try:
                module = f'{package}.{name}.main'
                function = import_string(module)
                function()
            except ImportError:
                feedback = messages.ERROR
                message = f'Create file `{name}.py` on folder scrap.'

            messages.add_message(request, feedback, message)
