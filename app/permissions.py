from rest_framework.permissions import BasePermission

""" bu yerda faqat admin is_stuff bolsagina ruhsat berilsin
 degan logika qila olamdim!!!!! is_staff degan logika alohida ayoziladi """


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


