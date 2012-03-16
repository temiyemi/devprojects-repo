# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Industry'
        db.create_table('industry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal('ims', ['Industry'])

        # Adding model 'DevelopmentPartner'
        db.create_table('development_partner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True, null=True)),
            ('development_policy', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('sector', self.gf('django.db.models.fields.CharField')(max_length=20, db_index=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=60, null=True)),
        ))
        db.send_create_signal('ims', ['DevelopmentPartner'])

        # Adding model 'Recipient'
        db.create_table('recipient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True, null=True)),
            ('development_policy', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('sector', self.gf('django.db.models.fields.CharField')(max_length=20, db_index=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=60, null=True)),
            ('year_founded', self.gf('django.db.models.fields.SmallIntegerField')(max_length=4)),
            ('legal_status', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contact_person', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('office_address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=45)),
            ('telephone', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=14)),
        ))
        db.send_create_signal('ims', ['Recipient'])

        # Adding model 'Project'
        db.create_table('project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ims.DevelopmentPartner'])),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ims.Recipient'])),
            ('industry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ims.Industry'])),
            ('sector', self.gf('django.db.models.fields.CharField')(max_length=20, db_index=True)),
            ('collaborators', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal('ims', ['Project'])

        # Adding unique constraint on 'Project', fields ['industry', 'name']
        db.create_unique('project', ['industry_id', 'name'])

        # Adding model 'ProjectDetail'
        db.create_table('project_detail', (
            ('project', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ims.Project'], unique=True, primary_key=True)),
            ('commencement_year', self.gf('django.db.models.fields.SmallIntegerField')(db_index=True)),
            ('duration', self.gf('django.db.models.fields.PositiveSmallIntegerField')(db_index=True)),
            ('objectives', self.gf('django.db.models.fields.TextField')()),
            ('implementation_level', self.gf('django.db.models.fields.TextField')()),
            ('pm_structure', self.gf('django.db.models.fields.TextField')()),
            ('total_cost', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2, db_index=True)),
            ('sources_of_funding', self.gf('django.db.models.fields.TextField')()),
            ('target_beneficiaries', self.gf('django.db.models.fields.TextField')()),
            ('coverage_areas', self.gf('django.db.models.fields.TextField')()),
            ('key_implementing_stakeholders', self.gf('django.db.models.fields.TextField')()),
            ('current_status', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('goals', self.gf('django.db.models.fields.TextField')()),
            ('outcomes', self.gf('django.db.models.fields.TextField')()),
            ('challenges', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('ims', ['ProjectDetail'])

        # Adding model 'User'
        db.create_table('user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('password_hash', self.gf('django.db.models.fields.CharField')(max_length=56)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=45)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('level', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('institution', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True)),
            ('institution_type', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('ims', ['User'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Project', fields ['industry', 'name']
        db.delete_unique('project', ['industry_id', 'name'])

        # Deleting model 'Industry'
        db.delete_table('industry')

        # Deleting model 'DevelopmentPartner'
        db.delete_table('development_partner')

        # Deleting model 'Recipient'
        db.delete_table('recipient')

        # Deleting model 'Project'
        db.delete_table('project')

        # Deleting model 'ProjectDetail'
        db.delete_table('project_detail')

        # Deleting model 'User'
        db.delete_table('user')


    models = {
        'ims.developmentpartner': {
            'Meta': {'object_name': 'DevelopmentPartner', 'db_table': "'development_partner'"},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True', 'null': 'True'}),
            'development_policy': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'sector': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
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
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'legal_status': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'office_address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sector': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'telephone': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '14'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '60', 'null': 'True'}),
            'year_founded': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '4'})
        },
        'ims.user': {
            'Meta': {'object_name': 'User', 'db_table': "'user'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '45'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True'}),
            'institution_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'level': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'password_hash': ('django.db.models.fields.CharField', [], {'max_length': '56'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['ims']
