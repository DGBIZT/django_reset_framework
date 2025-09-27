from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff: # Проверка что это менеджер
            return True
        return request.user == view.get_object().owner #  Проверка что это владелец
