# Generated by Django 4.0.4 on 2022-05-04 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hater_app', '0002_follower_hater_following_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_body', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tag', models.CharField(max_length=50)),
                ('user', models.OneToOneField(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='criticism',
            name='hate_id',
        ),
        migrations.RemoveField(
            model_name='criticism',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='dislike',
            name='criticism_id',
        ),
        migrations.RemoveField(
            model_name='dislike',
            name='hate_id',
        ),
        migrations.RemoveField(
            model_name='dislike',
            name='hater_id',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='hater_being_followed_id',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='hater_following_id',
        ),
        migrations.AddField(
            model_name='dislike',
            name='criticism',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='hater_app.criticism'),
        ),
        migrations.AlterField(
            model_name='criticism',
            name='c_body',
            field=models.CharField(max_length=140),
        ),
        migrations.DeleteModel(
            name='Hate',
        ),
        migrations.AddField(
            model_name='hates',
            name='haters',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hater_app.user_profile'),
        ),
        migrations.AddField(
            model_name='criticism',
            name='haters',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='hater_app.user_profile'),
        ),
        migrations.AddField(
            model_name='criticism',
            name='hates',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='hater_app.hates'),
        ),
        migrations.AddField(
            model_name='dislike',
            name='hate',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='hater_app.hates'),
        ),
        migrations.AddField(
            model_name='dislike',
            name='haters',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hater_app.user_profile'),
        ),
        migrations.AddField(
            model_name='follower',
            name='hater_being_followed',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='followed', to='hater_app.user_profile'),
        ),
        migrations.AddField(
            model_name='follower',
            name='hater_following',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='following', to='hater_app.user_profile'),
        ),
    ]