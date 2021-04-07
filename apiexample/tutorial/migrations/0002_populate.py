from django.db import migrations
from django.utils import timezone

def populate_db(apps, schema_editor):
    Tutorial = apps.get_model('tutorial', 'Tutorial')

    newTutorial1 = Tutorial(title="One", description="Some description", published=True)
    newTutorial1.save()

    newTutorial2 = Tutorial(title="Two", description="Some description", published=False)
    newTutorial2.save()

    newTutorial3 = Tutorial(title="Three", description="Some description", published=True)
    newTutorial3.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial')
    ]

    operations = [
        migrations.RunPython(populate_db)
    ]
