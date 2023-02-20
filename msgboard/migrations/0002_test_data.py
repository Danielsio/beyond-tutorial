from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('msgboard', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from msgboard.models import Message
        test_data = [
            ('Test User1', 'A simple test message'),
            ('Test User2', 'Another simple test message'),
        ]
        with transaction.atomic():
            for author, text in test_data:
                Message(author=author, text=text).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
