# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Recipient.office_address'
        db.alter_column('recipient', 'office_address', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Recipient.development_policy'
        db.alter_column('recipient', 'development_policy', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DevelopmentPartner.development_policy'
        db.alter_column('development_partner', 'development_policy', self.gf('django.db.models.fields.TextField')(null=True))

        # Adding field 'ProjectDetail.collaborators'
        db.add_column('project_detail', 'collaborators', self.gf('django.db.models.fields.TextField')(null=True), keep_default=False)

        # Changing field 'ProjectDetail.key_implementing_stakeholders'
        db.alter_column('project_detail', 'key_implementing_stakeholders', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'ProjectDetail.target_beneficiaries'
        db.alter_column('project_detail', 'target_beneficiaries', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'ProjectDetail.coverage_areas'
        db.alter_column('project_detail', 'coverage_areas', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'ProjectDetail.challenges'
        db.alter_column('project_detail', 'challenges', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'ProjectDetail.sources_of_funding'
        db.alter_column('project_detail', 'sources_of_funding', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'ProjectDetail.goals'
        db.alter_column('project_detail', 'goals', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'ProjectDetail.outcomes'
        db.alter_column('project_detail', 'outcomes', self.gf('django.db.models.fields.TextField')(null=True))

        # Deleting field 'Project.collaborators'
        db.delete_column('project', 'collaborators')


    def backwards(self, orm):
        
        # Changing field 'Recipient.office_address'
        db.alter_column('recipient', 'office_address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Recipient.development_policy'
        db.alter_column('recipient', 'development_policy', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'DevelopmentPartner.development_policy'
        db.alter_column('development_partner', 'development_policy', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Deleting field 'ProjectDetail.collaborators'
        db.delete_column('project_detail', 'collaborators')

        # Changing field 'ProjectDetail.key_implementing_stakeholders'
        db.alter_column('project_detail', 'key_implementing_stakeholders', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'ProjectDetail.target_beneficiaries'
        db.alter_column('project_detail', 'target_beneficiaries', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'ProjectDetail.coverage_areas'
        db.alter_column('project_detail', 'coverage_areas', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'ProjectDetail.challenges'
        db.alter_column('project_detail', 'challenges', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'ProjectDetail.sources_of_funding'
        db.alter_column('project_detail', 'sources_of_funding', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'ProjectDetail.goals'
        db.alter_column('project_detail', 'goals', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'ProjectDetail.outcomes'
        db.alter_column('project_detail', 'outcomes', self.gf('django.db.models.fields.TextField')(default=''))

        # Adding field 'Project.collaborators'
        db.add_column('project', 'collaborators', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)


    models = {
        'ims.developmentpartner': {
            'Meta': {'object_name': 'DevelopmentPartner', 'db_table': "'development_partner'"},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'development_policy': ('django.db.models.fields.TextField', [], {'null': 'True'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ims.Industry']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ims.DevelopmentPartner']"}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ims.Recipient']"}),
            'sector': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'})
        },
        'ims.projectdetail': {
            'Meta': {'ordering': "['-commencement_year']", 'object_name': 'ProjectDetail', 'db_table': "'project_detail'"},
            'challenges': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'collaborators': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'commencement_year': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True'}),
            'coverage_areas': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'current_status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'duration': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True'}),
            'goals': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'implementation_level': ('django.db.models.fields.TextField', [], {}),
            'key_implementing_stakeholders': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'objectives': ('django.db.models.fields.TextField', [], {}),
            'outcomes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'pm_structure': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['ims.Project']", 'unique': 'True', 'primary_key': 'True'}),
            'sources_of_funding': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'target_beneficiaries': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'total_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2', 'db_index': 'True'})
        },
        'ims.recipient': {
            'Meta': {'ordering': "['-year_founded']", 'object_name': 'Recipient', 'db_table': "'recipient'"},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'development_policy': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '45', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legal_status': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'office_address': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'telephone': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '14', 'null': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '60', 'null': 'True'}),
            'year_founded': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '4', 'null': 'True'})
        }
    }

    complete_apps = ['ims']
