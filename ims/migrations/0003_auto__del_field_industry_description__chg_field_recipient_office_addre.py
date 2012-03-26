# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'DevelopmentPartner', fields ['acronym']
        db.delete_unique('development_partner', ['acronym'])

        # Removing unique constraint on 'Recipient', fields ['acronym']
        db.delete_unique('recipient', ['acronym'])

        # Deleting field 'Industry.description'
        db.delete_column('industry', 'description')

        # Changing field 'Recipient.office_address'
        db.alter_column('recipient', 'office_address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Recipient.year_founded'
        db.alter_column('recipient', 'year_founded', self.gf('django.db.models.fields.SmallIntegerField')(max_length=4, null=True))

        # Changing field 'Recipient.telephone'
        db.alter_column('recipient', 'telephone', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=14, null=True))

        # Changing field 'Recipient.legal_status'
        db.alter_column('recipient', 'legal_status', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Recipient.development_policy'
        db.alter_column('recipient', 'development_policy', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'Recipient.contact_person'
        db.alter_column('recipient', 'contact_person', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Recipient.email'
        db.alter_column('recipient', 'email', self.gf('django.db.models.fields.EmailField')(max_length=45, null=True))

        # Changing field 'DevelopmentPartner.development_policy'
        db.alter_column('development_partner', 'development_policy', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))


    def backwards(self, orm):
        
        # Adding field 'Industry.description'
        db.add_column('industry', 'description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Changing field 'Recipient.office_address'
        db.alter_column('recipient', 'office_address', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Adding unique constraint on 'Recipient', fields ['acronym']
        db.create_unique('recipient', ['acronym'])

        # Changing field 'Recipient.year_founded'
        db.alter_column('recipient', 'year_founded', self.gf('django.db.models.fields.SmallIntegerField')(default=2012, max_length=4))

        # Changing field 'Recipient.telephone'
        db.alter_column('recipient', 'telephone', self.gf('django.db.models.fields.PositiveIntegerField')(default='', max_length=14))

        # Changing field 'Recipient.legal_status'
        db.alter_column('recipient', 'legal_status', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'Recipient.development_policy'
        db.alter_column('recipient', 'development_policy', self.gf('django.db.models.fields.CharField')(default='', max_length=500))

        # Changing field 'Recipient.contact_person'
        db.alter_column('recipient', 'contact_person', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Recipient.email'
        db.alter_column('recipient', 'email', self.gf('django.db.models.fields.EmailField')(default='', max_length=45))

        # Adding unique constraint on 'DevelopmentPartner', fields ['acronym']
        db.create_unique('development_partner', ['acronym'])

        # Changing field 'DevelopmentPartner.development_policy'
        db.alter_column('development_partner', 'development_policy', self.gf('django.db.models.fields.CharField')(default='', max_length=500))


    models = {
        'ims.developmentpartner': {
            'Meta': {'object_name': 'DevelopmentPartner', 'db_table': "'development_partner'"},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'development_policy': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '60', 'null': 'True'})
        },
        'ims.industry': {
            'Meta': {'ordering': "['name']", 'object_name': 'Industry', 'db_table': "'industry'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        'ims.project': {
            'Meta': {'unique_together': "(('industry', 'name'),)", 'object_name': 'Project', 'db_table': "'project'"},
            'collaborators': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ims.Industry']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ims.DevelopmentPartner']"}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ims.Recipient']"}),
            'sector': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'})
        },
        'ims.projectdetail': {
            'Meta': {'ordering': "['-commencement_year']", 'object_name': 'ProjectDetail', 'db_table': "'project_detail'"},
            'challenges': ('django.db.models.fields.TextField', [], {}),
            'commencement_year': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True'}),
            'coverage_areas': ('django.db.models.fields.TextField', [], {}),
            'current_status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'duration': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True'}),
            'goals': ('django.db.models.fields.TextField', [], {}),
            'implementation_level': ('django.db.models.fields.TextField', [], {}),
            'key_implementing_stakeholders': ('django.db.models.fields.TextField', [], {}),
            'objectives': ('django.db.models.fields.TextField', [], {}),
            'outcomes': ('django.db.models.fields.TextField', [], {}),
            'pm_structure': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['ims.Project']", 'unique': 'True', 'primary_key': 'True'}),
            'sources_of_funding': ('django.db.models.fields.TextField', [], {}),
            'target_beneficiaries': ('django.db.models.fields.TextField', [], {}),
            'total_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2', 'db_index': 'True'})
        },
        'ims.recipient': {
            'Meta': {'ordering': "['-year_founded']", 'object_name': 'Recipient', 'db_table': "'recipient'"},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'development_policy': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '45', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legal_status': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'office_address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'telephone': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '14', 'null': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '60', 'null': 'True'}),
            'year_founded': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '4', 'null': 'True'})
        }
    }

    complete_apps = ['ims']
