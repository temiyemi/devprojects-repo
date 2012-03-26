from django.db import models
from datetime import datetime

YEARS = tuple([(x,x) for x in range(datetime.today().year, 1979, -1)])

SECTORS = (
    ('Private','Private'),
    ('Public','Public')
)

STATUS = (
    ('Abandoned','Abandoned'),
    ('Completed','Completed'),
    ('On-going','On-going')
)

class Industry(models.Model):
    name = models.CharField(max_length=45, unique=True)

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'industry'
        ordering = ['name']
        verbose_name_plural = 'Industries'

class Organization(models.Model):
    name = models.CharField(max_length=200, unique=True)
    acronym = models.CharField(max_length=20, null=True)
    development_policy = models.TextField(null=True)
    website = models.URLField(max_length=60, null=True)

    def __unicode__(self):
        return '%s' % self.name

    def investment(self):
        total = self.project_set.aggregate(costs=models.Sum('projectdetail__total_cost'))
        return total['costs']

    class Meta:
        abstract = True

class DevelopmentPartner(Organization):

    class Meta:
        db_table = 'development_partner'
        verbose_name = 'Development Partner'
        verbose_name_plural = 'Development Partners'

class Recipient(Organization):
    year_founded = models.SmallIntegerField(max_length=4, choices=YEARS, null=True)
    legal_status = models.CharField(max_length=200, null=True)
    contact_person = models.CharField(max_length=60, null=True)
    office_address = models.TextField(null=True)
    email = models.EmailField(max_length=45, null=True)
    telephone = models.PositiveIntegerField(max_length=14, null=True)

    class Meta:
        db_table = 'recipient'
        ordering = ['-year_founded']
        verbose_name = 'Recipient Institution'
        verbose_name_plural = 'Recipient Institutions'

class Project(models.Model):
    name = models.CharField(max_length=200)
    partner = models.ForeignKey(DevelopmentPartner, verbose_name='Development Partner')
    recipient = models.ForeignKey(Recipient, verbose_name='Recipient Institution')
    industry = models.ForeignKey(Industry, db_index=True, verbose_name='Field/Area')
    sector = models.CharField(max_length=20, choices=SECTORS, db_index=True)

    def __unicode__(self):
        return '(%s) %s' % (self.projectdetail.commencement_year, self.name)

    class Meta:
        db_table = 'project'
        unique_together = ('industry','name')
        verbose_name = 'Development Project'
        verbose_name_plural = 'Development Projects'
        ordering = ['-projectdetail__commencement_year']

class ProjectDetail(models.Model):
    project = models.OneToOneField(Project, primary_key=True)
    commencement_year = models.SmallIntegerField('Started in',db_index=True, choices=YEARS)
    duration = models.PositiveSmallIntegerField(db_index=True,
        help_text='Project duration in number of years'
    )
    total_cost = models.DecimalField(decimal_places=2, max_digits=16, db_index=True,
        help_text='Total cost in USD, $. Enter without commas'
    )
    current_status = models.CharField(max_length=100, choices=STATUS)
    objectives = models.TextField('Project Objectives')
    pm_structure = models.TextField('Project Management Structure')
    implementation_level = models.CharField(max_length=100, null=True)
    sources_of_funding = models.CharField('Funded by', max_length=100, null=True)
    target_beneficiaries = models.TextField('Beneficiaries', null=True)
    coverage_areas = models.TextField(null=True)
    key_implementing_stakeholders = models.TextField('Key Stakeholders', null=True)
    collaborators = models.TextField(null=True)
    goals = models.TextField('Project Goals', null=True)
    outcomes = models.TextField('Expected Outcomes', null=True)

    class Meta:
        db_table = 'project_detail'