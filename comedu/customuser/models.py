from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self,student_id, position, username, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """

        if not student_id:
            raise ValueError('Users must have an student id')

        if not email:
            raise ValueError('Users must have an email address')

        if not student_id:
            raise ValueError('Users must have an student id')

        user = self.model(
            username = username,
            position=position,
            student_id=student_id,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,student_id, position, username, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            student_id=student_id,
            position=position,
            username=username,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    username = models.CharField(verbose_name="name", max_length=20)

    student_id = models.IntegerField(
        verbose_name="student_id(학번)",
        unique=True,
        )

    date_of_birth = models.DateField()

    position = models.CharField(
        max_length=10,
        verbose_name="직책(교수, 학생)",
        choices=(('pro', '교수'),('stu', '학생'))
        )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['date_of_birth', 'email', 'username' , 'position']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
