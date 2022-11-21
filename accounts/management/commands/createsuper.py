from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):

    help = "This command creates superuser"

    def handle(self, *args, **options):
        try:
            User.objects.get(username="masterAdmin")
            self.stdout.write(self.style.SUCCESS("Superuser Exists"))
        except User.DoesNotExist:
            User.objects.create_superuser("masterAdmin", "", "1q2w3e4r!!")
            self.stdout.write(self.style.SUCCESS("Superuser Created"))