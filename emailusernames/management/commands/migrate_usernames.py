from django.core.management.base import BaseCommand, CommandError

from emailusernames.utils import migrate_usernames


class Command(BaseCommand):
	"""
	Migrate all existing users using the 'migrate_usernames' function as Command 
	so that migrations will be applied programmatically, no need of call it in a script or whatever
	"""

	def handle(self):
		"""
		The migrate_usernames callback
		"""
		try:
			migrate_usernames()
		except Exception, e:
			raise CommandError(e.message)
