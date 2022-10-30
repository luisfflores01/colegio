from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from modulos.persona.models import Profesor


class UsuarioManager(BaseUserManager):
    def _create_user(self, username, email, documento, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            documento=documento,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, documento, password=None, **extra_fields):
        """
        Funcion que se encarga de crear un usuario comun
        """
        return self._create_user(username, email, documento, password, False, False, **extra_fields)

    def create_superuser(self, username, email, documento, password=None, **extra_fields):
        """
        Funcion que se encarga de crear un super usuario administrador del sistema
        """
        return self._create_user(username, email, documento, password, True, True, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de Usuario', max_length=50, unique=True)
    email = models.EmailField('Correo Electronico', max_length=255, unique=True)
    # documento = models.CharField('Nro. Documento', max_length=15, unique=True)
    documento = models.ForeignKey(Profesor, related_name='+', on_delete=models.PROTECT)
    is_active = models.BooleanField('Esta Activo', default=True)
    is_staff = models.BooleanField('Personal Autorizado', default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    objects = UsuarioManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'documento', ]

    def __str__(self):
        return self.username
