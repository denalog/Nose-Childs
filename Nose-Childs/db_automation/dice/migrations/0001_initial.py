# Generated by Django 5.1.3 on 2024-11-29 03:24

from django.db import migrations, models

# 게임을 play 에서 나온 Dice number
#  E.g. Player A : 1,5 -> 6  (두 DiceNumber을 합친값)
#       Player B : 3,2 -> 5
# 결론 : Player A Win!
class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dice",
            fields=[
                ("number", models.IntegerField(primary_key=True, serialize=False)),
                #("number", models.IntegerField()),
            ],
            options={
                "db_table": "dice",
            },
        ),
    ]
