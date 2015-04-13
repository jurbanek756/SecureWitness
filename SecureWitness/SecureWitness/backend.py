from .models import CustomUser

class CustomBackend:

    def authenticate(self, username=None, password=None):
        try:
            user = CustomUser.objects.get(name=username)

            if password == user.password:
                return user
            else:
                return None


        except CustomUser.DoesNotExist:
            return None


    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
