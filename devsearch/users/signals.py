from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

# @receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
        print(f"\033[36m█▓▒░ User created! \033[0m")
        print(f"\033[36m█▓▒░ Instance: {instance} \033[0m")
        print(f"\033[36m█▓▒░ CREATED: {created} \033[0m")

# @receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user  # instance here is a Profile. From Profile we get user
    user.delete()
    print(f"\033[35m█▓▒░ Deleting user... \033[0m")


post_save.connect(create_profile, sender=User)
post_delete.connect(delete_user, sender=Profile)
