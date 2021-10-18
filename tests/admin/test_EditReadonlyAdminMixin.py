from django.urls import reverse

from complex_factories_sample.models import HasAutoCodeGenerateFunctionExample


def test_EditReadonlyAdminMixin(admin_client):
    opts = HasAutoCodeGenerateFunctionExample._meta
    admin_url_add = reverse(f'admin:{opts.app_label}_{opts.model_name}_add')

    name = "name"
    code = "name-code"
    response = admin_client.post(
        admin_url_add,
        {
            "name": name,
            "code": code,
        },
    )
    assert response.status_code == 302

    obj = HasAutoCodeGenerateFunctionExample.objects.get(name=name)
    assert obj.code == code

    admin_url_change = reverse(f'admin:{opts.app_label}_{opts.model_name}_change', args=[obj.id])
    response = admin_client.post(
        admin_url_change,
        {
            "name": name,
            "code": "New code",
        },
    )
    assert response.status_code == 302
    obj = HasAutoCodeGenerateFunctionExample.objects.get(name=name)
    assert obj.code == code  # check that the above request hasn't changed the code, confirming the code is readonly now
