# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'User'
        db.delete_table('user')

        # Deleting field 'Recipient.sector'
        db.delete_column('recipient', 'sector')

        # Deleting field 'Recipient.industry'
        db.delete_column('recipient', 'industry')

        # Deleting field 'DevelopmentPartner.sector'
        db.delete_column('development_partner', 'sector')

        # Deleting field 'DevelopmentPartner.industry'
        db.delete_column('development_partner', 'industry')


    def backwards(self, orm):
        
        # Adding model 'User'
        db.create_table('user', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('institution', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True)),
            ('password_hash', self.gf('django.db.models.fields.CharField')(max_length=56)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('level', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('institution_type', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=45, unique=True)),
        ))
        db.send_create_signal('ims', ['User'])

        # Adding field 'Recipient.sector'
        db.add_column('recipient', 'sector', self.gf('django.db.models.fields.CharField')(default=0, max_length=20, db_index=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Recipient.industry'
        raise RuntimeError("Cannot reverse this migration. 'Recipient.industry' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'DevelopmentPartner.sector'
        raise RuntimeError("Cannot reverse this migration. 'DevelopmentPartner.sector' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'DevelopmentPartner.industry'
        raise RuntimeError("Cannot reverse this migration. 'DevelopmentPartner.industry' and its values cannot be restored.")


    models = {
        'ims.developmentpartner': {
            'Meta': {'object_name': 'DevelopmentPartner', 'db_table': "'development_partner'"},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True', 'null': 'True'}),
            'development_policy': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '60', 'null': 'True'})
        },
        'ims.industry': {
            'Meta': {'ordering': "['name']", 'object_name': 'Industry', 'db_table': "'industry'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
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
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True', 'null': 'True'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'development_policy': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '45'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legal_status': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'office_address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telephone': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '14'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '60', 'null': 'True'}),
            'year_founded': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['ims']
