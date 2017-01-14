from django.db import models


class GroupModel (models.Model):
    group_name = models.CharField(max_length=20, unique=True)  #музыкальная группа
    base_date = models.DateField()
    genre = models.CharField(max_length=255)


class MembershipModel (models.Model): #членство
    membership_num = models.IntegerField(unique=True)
    join_date = models.DateField()
    out_date = models.DateField()
    group = models.ForeignKey('GroupModel', null=True)


class MemberModel (models.Model):
    membership_num = models.ForeignKey('MembershipModel', null=True)
    member_name = models.CharField(max_length=20)
    member_surname = models.CharField(max_length=20)
    member_thirdname = models.CharField(max_length=20)
    member_bdate = models.DateField()

