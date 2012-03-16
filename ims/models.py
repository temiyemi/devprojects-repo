from django.db import models
from utils import hash_password

USER_LEVELS = (
    (-1, 'blocked'),
    ( 0, 'unactivated'),
    ( 1, 'normal'),
    ( 2, 'staff'),
    ( 3, 'admin')
)

SECTORS = (
    ('private','Private'),
    ('public','Public'),
    ('both','Private & Public')
)

INSTITUTIONS = (
    ('recipient','Recipient'),
    ('partner','Partner'),
    ('none','None')
)

class Industry(models.Model):
    name = models.CharField(max_length=45, unique=True)
    description = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'industry'
        ordering = ['name']

class Organization(models.Model):
    name = models.CharField(max_length=200, unique=True)
    acronym = models.CharField(max_length=20, null=True, unique=True)
    development_policy = models.CharField(max_length=500)
    sector = models.CharField(max_length=20, choices=SECTORS, db_index=True)
    industry = models.CharField(max_length=20)
    website = models.URLField(max_length=60, null=True)

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        abstract = True

class DevelopmentPartner(Organization):
    class Meta:
        db_table = 'development_partner'

class Recipient(Organization):
    year_founded = models.SmallIntegerField(max_length=4)
    legal_status = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=60)
    office_address = models.CharField(max_length=200)
    email = models.EmailField(max_length=45)
    telephone = models.PositiveIntegerField(max_length=14)

    class Meta:
        db_table = 'recipient'
        ordering = ['-year_founded']

class Project(models.Model):
    name = models.CharField(max_length=200)
    partner = models.ForeignKey(DevelopmentPartner)
    recipient = models.ForeignKey(Recipient)
    industry = models.ForeignKey(Industry, db_index=True)
    sector = models.CharField(max_length=20, choices=SECTORS, db_index=True)
    collaborators = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return '(%s) %s' % (self.projectdetail.commencement_year, self.name)

    class Meta:
        db_table = 'project'
        unique_together = ('industry','name')

class ProjectDetail(models.Model):
    project = models.OneToOneField(Project, primary_key=True)
    commencement_year = models.SmallIntegerField(db_index=True)
    duration = models.PositiveSmallIntegerField(db_index=True)
    objectives = models.TextField()
    implementation_level = models.TextField()
    pm_structure = models.TextField()
    total_cost = models.DecimalField(decimal_places=2, max_digits=9, db_index=True)
    sources_of_funding = models.TextField()
    target_beneficiaries = models.TextField()
    coverage_areas = models.TextField()
    key_implementing_stakeholders = models.TextField()
    current_status = models.CharField(max_length=100)
    goals = models.TextField()
    outcomes = models.TextField()
    challenges = models.TextField()

    class Meta:
        db_table = 'project_detail'
        ordering = ['-commencement_year']

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password_hash = models.CharField(max_length=56)
    email = models.EmailField(max_length=45, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    level = models.SmallIntegerField(default=0, choices=USER_LEVELS)
    institution = models.PositiveIntegerField(default=0, null=True)
    institution_type = models.CharField(max_length=30, choices=INSTITUTIONS, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid_password(self, password):
        return hash_password(password) == self.password_hash

    class Meta:
        db_table = 'user'