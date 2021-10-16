from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .lugar                      import Lugar

class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        """
        Manager para crear el perfil de usuario
        Crea y guarda un user con el email y password dados.
        """
        if not username:
            raise ValueError('Es requerido que tener un usuario')
        
        user = self.model(
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password): # Comando en la terminal python manage.py createsuperuser
        """
        Manager para crear el perfil de usuario
        Crea y guarda un superuser con el email y password dados.
        """
        user = self.create_user(
            username  = username,
            password = password

        )

        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin, models.Model):

    def url_user(self, filename):
        ruta = "static/img/ima_evento/%s/%s"%(self.nombres, str(filename))
        return ruta
    
    id                    = models.BigAutoField(primary_key=True)
    username              = models.CharField('username', unique = True, max_length=100, blank=False, null=False)
    email                 = models.EmailField('Email', max_length = 100, unique=True)
    documento             = models.CharField('Documento', max_length=15, unique=True)
    nombres               = models.CharField('Nombres', max_length = 30, blank = False, null = False)
    apellidos             = models.CharField('Apellidos', max_length = 200, blank = False, null = False)
    telefono              = models.CharField('Telefono', max_length = 15)
    ciudad                = models.CharField('Ciudad', max_length=40, blank=False, null=False)
    direccion             = models.CharField('Direccion', max_length = 100, blank=False, null=False)    
    imagen                = models.ImageField('Imagen de Perfil', max_length=200, blank = True, null = True, upload_to=url_user) # pip install pillow && upload_to='perfil/'
    usuario_activo        = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    creacion_user         = models.DateTimeField(auto_now_add=True)
    password              = models.CharField('Password', max_length = 256)
        
    
    objects = UserManager() # se enlaza con la clase manager
    USERNAME_FIELD = 'username' # es el que va a usar para generar los tockens

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username'] # ordena alfabeticamente

    username              = models.CharField('username', unique = True, max_length=100, blank=False, null=False)
    email                 = models.EmailField('Email', max_length = 100, unique=True)
    documento             = models.CharField('Documento', max_length=15, unique=True)
    nombres               = models.CharField('Nombres', max_length = 30, blank = False, null = False)
    apellidos             = models.CharField('Apellidos', max_length = 200, blank = False, null = False)
    telefono              = models.CharField('Telefono', max_length = 15)
    imagen                = models.ImageField('Imagen de Perfil', max_length=200, blank = True, null = True) # pip install pillow && upload_to='perfil/'
    usuario_activo        = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    creacion_user         = models.DateTimeField(auto_now_add=True)
    password              = models.CharField('Password', max_length = 256)

    def __str__(self):
        return f'{self.nombres}, {self.apellidos}'

    def has_perm(self, perm, obj):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    @property
    def is_staff(self):
        return self.usuario_administrador