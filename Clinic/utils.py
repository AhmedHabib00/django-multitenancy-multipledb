from django.db import connection


def hostname_from_request(request):
    """
    Take the request, remove the port and return bare url.
    """
    return request.get_host().split(':')[0].lower()


def tenant_db_from_request(request):
    """
    call other two functions, compare host url and dictionary and return db name for tenant
    """
    host_name = hostname_from_request(request)
    tenant_map = get_tenants_map()
    return tenant_map.get(host_name)


def get_tenants_map():
    """
    return a dictionary of tenant urls and db names
    """
    return {
        'clinic1.localhost': 'db2',
        'clinic2.localhost': 'db3',
    }
