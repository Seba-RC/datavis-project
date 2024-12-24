from django.db import models

# Create your models here.
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Dispositivo(models.Model):
    iddispositivo = models.IntegerField(db_column='idDispositivo', primary_key=True)  # Field name made lowercase. The composite primary key (idDispositivo, Usuario_idUsuario) found, that is not supported. The first column is selected.
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dispositivo'
        unique_together = (('iddispositivo', 'usuario_idusuario'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Pelicula(models.Model):
    idpelicula = models.AutoField(db_column='idPelicula', primary_key=True)  # Field name made lowercase. The composite primary key (idPelicula, idSubscripcion, idUsuario) found, that is not supported. The first column is selected.
    idsubscripcion = models.ForeignKey('Subscripcion', models.DO_NOTHING, db_column='idSubscripcion')
    idusuario = models.OneToOneField('Subscripcion', models.DO_NOTHING, db_column='idUsuario', to_field='idusuario', related_name='pelicula_idusuario_set')  # Field name made lowercase.
    nombrepelicula = models.CharField(db_column='nombrePelicula', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tipopelicula = models.CharField(db_column='tipoPelicula', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fechavista = models.DateField(db_column='fechaVista', blank=True, null=True)  # Field name made lowercase.
    fechaterminada = models.DateField(db_column='fechaTerminada', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pelicula'
        constraints = [
            models.UniqueConstraint(fields=['idpelicula', 'idsubscripcion', 'idusuario'], name='unique_pelicula_subscription_user'),
        ]


class Serie(models.Model):
    idserie = models.IntegerField(db_column='idSerie', primary_key=True)  # Field name made lowercase. The composite primary key (idSerie, idSubscripcion, idUsuario) found, that is not supported. The first column is selected.
    idsubscripcion = models.ForeignKey('Subscripcion', models.DO_NOTHING, db_column='idSubscripcion')  # Field name made lowercase.
    idusuario = models.OneToOneField('Subscripcion', models.DO_NOTHING, db_column='idUsuario', to_field='idusuario', related_name='serie_idusuario_set')  # Field name made lowercase.
    nombreserie = models.CharField(db_column='nombreSerie', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tiposerie = models.CharField(db_column='tipoSerie', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fechavista = models.DateField(db_column='fechaVista', blank=True, null=True)  # Field name made lowercase.
    fechaterminada = models.DateField(db_column='fechaTerminada', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serie'
        constraints = [
            models.UniqueConstraint(fields=['idserie', 'idsubscripcion', 'idusuario'], name='unique_serie_subscription_user'),
        ]



class Subscripcion(models.Model):
    idsubscripcion = models.IntegerField(db_column='idSubscripcion', primary_key=True)  # Field name made lowercase. The composite primary key (idSubscripcion, idUsuario) found, that is not supported. The first column is 
    idusuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='idusuario')  # Field name made lowercase.
    fechainicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechatermino = models.DateField(db_column='fechaTermino', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscripcion'
        constraints = [
            models.UniqueConstraint(fields=['idsubscripcion', 'idusuario'], name='unique_subscription_user'),
        ]


class Usuario(models.Model):
    idusuario = models.IntegerField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    idemail = models.CharField(db_column='idEmail', max_length=78)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    fechanacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    ciudad = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'usuario'


class Valoracionpelicula(models.Model):
    idpelicula = models.OneToOneField(Pelicula, models.DO_NOTHING, db_column='idPelicula', primary_key=True)  # Field name made lowercase.
    valoracionpelicula = models.DecimalField(db_column='valoracionPelicula', max_digits=10, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'valoracionpelicula'


class Valoracionserie(models.Model):
    idserie = models.OneToOneField(Serie, models.DO_NOTHING, db_column='idSerie', primary_key=True)  # Field name made lowercase.
    valoracionserie = models.DecimalField(db_column='valoracionSerie', max_digits=10, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'valoracionserie'
