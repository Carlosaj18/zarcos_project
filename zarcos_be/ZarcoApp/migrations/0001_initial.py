# Generated by Django 3.2.8 on 2021-10-06 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreCategoria', models.CharField(max_length=100, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreEvento', models.CharField(max_length=100, verbose_name='NombreEvento')),
                ('tipo', models.CharField(max_length=20, verbose_name='Tipo')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('duracion', models.IntegerField(default=0)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('descripcionSimple', models.CharField(max_length=256, verbose_name='DescripcionSimple')),
                ('descripcionCompleta', models.TextField()),
                ('imagen', models.ImageField(upload_to='')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('cupo_maximo', models.IntegerField(default=50)),
                ('is_active', models.BooleanField(default=True)),
                ('categoriaFK', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='evento', to='ZarcoApp.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ciudad', models.CharField(max_length=40, verbose_name='Ciudad')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('nombreLugar', models.CharField(max_length=100, verbose_name='Nombre_lugar')),
                ('complemento', models.CharField(max_length=256, verbose_name='Complemento')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('documento', models.CharField(max_length=15, unique=True, verbose_name='Documento')),
                ('nombres', models.CharField(max_length=30, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('telefono', models.CharField(max_length=15, verbose_name='Telefono')),
                ('imagen', models.ImageField(blank=True, max_length=200, null=True, upload_to='', verbose_name='Imagen de Perfil')),
                ('usuarioActivo', models.BooleanField(default=True)),
                ('usuarioAdministrador', models.BooleanField(default=False)),
                ('creacionUser', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('lugarFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lugarFK', to='ZarcoApp.lugar')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('numeroEntradas', models.IntegerField(default=1)),
                ('pagoTotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('fechaRegistro', models.DateTimeField(auto_now_add=True)),
                ('eventoFK', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='eventoFK', to='ZarcoApp.evento')),
                ('personaFK', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='personaFK', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='lugarFK',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='evento', to='ZarcoApp.lugar'),
        ),
    ]
