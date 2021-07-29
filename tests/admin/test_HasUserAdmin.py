from django.contrib.auth import get_permission_codename
from django.contrib.auth.models import Permission
from django.urls import reverse

from complex_factories_sample.models import HasUserLimitedAccess


def test_HasUserAdmin(client, django_user_model):
    user_manager = django_user_model.objects.create(username='user_manager', is_staff=True)
    user_owner = django_user_model.objects.create(username='user_owner', is_staff=True)
    user_non_owner = django_user_model.objects.create(username='user_non_owner', is_staff=True)

    opts = HasUserLimitedAccess._meta
    see_all_permission = Permission.objects.get(
        codename=get_permission_codename('see_all', opts),
    )
    view_permission = Permission.objects.get(
        codename=get_permission_codename('view', opts),
    )
    user_manager.user_permissions.add(see_all_permission, view_permission)
    user_owner.user_permissions.add(view_permission)
    user_non_owner.user_permissions.add(view_permission)

    obj = HasUserLimitedAccess.objects.create(user=user_owner)
    admin_url_changelist = reverse(f'admin:{opts.app_label}_{opts.model_name}_changelist')
    admin_url_change = reverse(f'admin:{opts.app_label}_{opts.model_name}_change', args=[obj.id])

    client.force_login(user_manager)
    response = client.get(admin_url_changelist)
    assert response.status_code == 200
    response = client.get(admin_url_change)
    assert response.status_code == 200

    client.force_login(user_owner)
    response = client.get(admin_url_changelist)
    assert response.status_code == 200
    response = client.get(admin_url_change)
    assert response.status_code == 200

    client.force_login(user_non_owner)
    response = client.get(admin_url_changelist)
    assert response.status_code == 200
    response = client.get(admin_url_change)
    assert response.status_code == 302
