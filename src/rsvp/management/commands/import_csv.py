from django.core.management.base import BaseCommand, CommandError
import csv
from rsvp.models import RSVP, Person


class Command(BaseCommand):
    args = '<guests.csv [allow_double]>'
    help = ("Takes csv with field 'Name' and creates groups with each group "
            "being a comma seprated list of names.")

    def make_party(self, line):
        people = line['Name'].split(',')
        family_name = people[0]
        guests = 1 if len(people) == 1 else 0
        double = RSVP.objects.filter(family_name=family_name).exists()
        if self.allow_double or not double:
            group = RSVP.objects.create(family_name=family_name,
                                        additonal_allowed=guests)
            self.stdout.write("Group '%s' has been added" % str(group))
            for person in people:
                double = Person.objects.filter(name=person).exists()
                if self.allow_double or not double:
                    person = Person.objects.create(name=person, group=group)
                    self.stdout.write("\tPerson '%s' added" % str(person))
                else:
                    self.stdout.write("\tPerson '%s' exists!" % str(person))
        else:
            self.stdout.write("\tGroup '%s' exists!" % str(family_name))

    def handle(self, *args, **options):
        try:
            self.allow_double = True if args[1] in ('True', 'true') else False
        except IndexError:
            self.allow_double = False
            pass
        except ValueError:
            if args[1] == ' ':
                raise CommandError('second argument must be a bool')
            else:
                pass
        try:
            with open(args[0], 'r') as file:
                self.stdout.write('File open')
                reader = csv.DictReader(file)
                count = 0
                for line in reader:
                    self.make_party(line)
                    count += 1
        except FileNotFoundError:
            raise CommandError('Can not access the file')
        except IndexError:
            raise CommandError('No file given')
        except KeyboardInterrupt:
            raise CommandError('Canceled!')
        else:
            self.stdout.write("Done.")
