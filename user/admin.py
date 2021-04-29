from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.fields import Field

from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
import re
from .models import Client


class ClientAdminResource(resources.ModelResource):
    username = Field(attribute='user__username')
    
    class Meta:
        model = Client
        skip_unchanged = True
        report_skipped = False
        client_field = ('id', 'username', 'first_name', 'last_name', 'email', 'active',
                        'phone', 'created_at', 'updated_at')
        fields = client_field
        order = client_field


class InputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        return [(1, '')]

    def choices(self, changelist):
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v) for k, v in changelist.get_filters_params().items() if k != self.parameter_name)
        yield all_choice

    def queryset(self, request, queryset):
        if not self.value():
            return queryset


class ClientEmailFilter(InputFilter):
    """
        Allow user to validate email through input field
    """
    parameter_name = 'email'
    title = _('client email')

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
            return queryset.filter(email__in=re.split(' |, |,| ,', self.value().rstrip()))


class ClientAdmin(ImportExportActionModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'active',
                    'phone', 'created_at', 'updated_at')
    list_filter = (ClientEmailFilter, 'active', ('created_at', DateTimeRangeFilter),
                  ('updated_at',DateTimeRangeFilter))
    search_fields = ('id', 'email')
    readonly_fields = ['active', ]

    resource_class = ClientAdminResource
    def export_admin_action(self, request, queryset):
        """
            Maximum number for export is 1000
        """
        qs = queryset[:1000]
        return super(ClientAdmin, self).export_admin_action(request, qs)

    export_admin_action.short_description = 'Export selected Client'


    def get_readonly_fields(self, request, obj=None):
        """
            Only superuser can change client to active
        """
        read_only_fields = ['active']
        if request.user.is_superuser or request.user.has_perm('user.can_active_client'):
            read_only_fields.remove('active')
            return read_only_fields
        return self.readonly_fields

admin.site.register(Client, ClientAdmin)