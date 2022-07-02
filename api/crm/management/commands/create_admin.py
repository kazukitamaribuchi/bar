from django.contrib.auth.management.commands import createsuperuser
from ...models import mUser
import logging
import os

logging.basicConfig(
    level = logging.DEBUG,
    format = '''%(levelname)s %(asctime)s %(pathname)s:%(funcName)s:%(lineno)s
    %(message)s''')

logger = logging.getLogger(__name__)

class Command(createsuperuser.Command):
    help = 'Create a Superuser'

    def handle(self, *args, **options):
        options.setdefault('interactive', False)
        username = 'admin'
        email = 'admin@gmail.com'
        password = 'admin'
        database = options.get('database')

        try:
            user_data = {
                'username': username,
                'email': email,
                'password': password,
            }

            exists = self.UserModel._default_manager.db_manager(database).filter(username=username).exists()
            if not exists:
                self.UserModel._default_manager.db_manager(database).create_superuser(**user_data)

        except Exception as e:
            logger.error(e)
