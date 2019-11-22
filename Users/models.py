from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class User(AbstractUser):
    USER_TYPE = [
        (1, 'موظف'),
        (2, 'أستاذ'),
        (3, 'طالب'),
        (4, 'Admin'),
    ]
    user_type = models.PositiveIntegerField(choices=USER_TYPE, default=3)
    temp_pass = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class RankType(models.Model):
    rank_type = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):
        return self.rank_type

    class Meta:
        ordering = ['-id']
        verbose_name = 'Rank Type'
        verbose_name_plural = 'Ranks Type'


class Rank(models.Model):
    rank_name = models.CharField(max_length=30, null=False, blank=False)
    rank_type = models.ForeignKey(RankType, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.rank_name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Rank'
        verbose_name_plural = 'Ranks'


class Ministry(models.Model):
    ministry_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.ministry_name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Ministry'
        verbose_name_plural = 'Ministries'


class Force(models.Model):
    force_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.force_name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Force'
        verbose_name_plural = 'Forces'


class Profile(models.Model):
    MARITAL_STATUS = [
        (1, 'أعزب'),
        (2, 'متزوج'),
    ]
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rank_type = models.ForeignKey(RankType, on_delete=models.DO_NOTHING)
    rank_name = models.ForeignKey(Rank, on_delete=models.DO_NOTHING)
    ministry_name = models.ForeignKey(Ministry, on_delete=models.DO_NOTHING, blank=True, null=True)
    force_name = models.ForeignKey(Force, on_delete=models.DO_NOTHING, blank=True, null=True)
    marital_status = models.PositiveSmallIntegerField(choices=MARITAL_STATUS, blank=False, null=False)
    military_id = models.PositiveIntegerField(blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    national_id = models.PositiveIntegerField(blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        name = '{0.first_name} {0.last_name}'
        return name.format(self)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Profile'
        verbose_name_plural = "Profiles"


class CourseHistory(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course_history = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.course_history

    class Meta:
        ordering = ['-id']
        verbose_name = 'Course History'
        verbose_name_plural = "Courses History"


class JobHistory(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    job_history = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.job_history

    class Meta:
        ordering = ['-id']
        verbose_name = 'Job History'
        verbose_name_plural = "Jobs History"
