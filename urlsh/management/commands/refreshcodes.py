from django.core.management.base import BaseCommand, CommandError
from urlsh.models import Url


class Command(BaseCommand):
    help = 'Refreshes all Url shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return Url.objects.refresh_shortcodes(items=options['items'])
