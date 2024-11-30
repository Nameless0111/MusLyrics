from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.urls import path
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from .forms import UserPasswordChangeForm

class UserAdmin(BaseUserAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('password_change/<int:user_id>/', self.admin_site.admin_view(self.password_change_view), name='user_password_change'),
        ]
        return custom_urls + urls

    def password_change_view(self, request, user_id, form_url=''):
        user = User.objects.get(pk=user_id)
        if request.method == 'POST':
            form = UserPasswordChangeForm(user=user, data=request.POST)
            if form.is_valid():
                form.save()
                self.message_user(request, "Пароль успешно изменён.")
                return redirect('admin:auth_user_changelist')
        else:
            form = UserPasswordChangeForm(user=user)

        context = {
            'form': form,
            'user': user,
            'is_popup': False,
            'opts': self.model._meta,
        }
        return TemplateResponse(request, 'admin/auth/user/password_change.html', context)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)