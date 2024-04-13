from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


#  Custom User Manager karon login korar time a a default username die login kora lage, but ami email die login korbo tai custom user manager kortesi
class UserManager(BaseUserManager):
  def create_user(self, email, name, terms_and_conditions, password=None, password2=None):
      """
      Creates and saves a User with the given email, name, terms_and_conditions and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          terms_and_conditions=terms_and_conditions,
      )

      user.set_password(password)
      user.save(using=self._db)
      
      
      return user

  def create_superuser(self, email, name, terms_and_conditions, password=None):
      """
      Creates and saves a superuser with the given email, name, terms_and_conditions and password.
      """
      user = self.create_user(
          email,
          password=password,
          name=name,
          terms_and_conditions=terms_and_conditions,
      )
      user.is_admin = True
      user.save(using=self._db)
      
      
      return user
  
  
  
  
# default profile image set korar jonno
def default_profile_image():
    return "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"

# default banner image set korar jonno
def default_banner_image():
    return "https://pm1.aminoapps.com/6493/523caa97f0e93e86a127b572547a5eeaacae0e77_hq.jpg"

#  Custom User Model
class User(AbstractBaseUser):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  name = models.CharField(max_length=200, default="Name")
  profile_image = models.ImageField(upload_to='profile_images/', default=default_profile_image, null=True, blank=True)
  banner_image = models.ImageField(upload_to='banner_images/', default=default_banner_image, null=True, blank=True)
  terms_and_conditions = models.BooleanField()
  bio = models.CharField(max_length=255, null=True, blank=True, default="Write your bio")
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['name', 'terms_and_conditions']

  def __str__(self):
      return self.email

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      return self.is_admin








