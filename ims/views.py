from models import *
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
#from datetime import date, timedelta
#from django.template import RequestContext

#view:projects
def projects(request):
    projects = get_list_or_404(Project)
    return render_to_response('ims/projects.html', { 'projects': projects })

#view:projects_by_sector
def projects_by_sector(request, sector):
    projects = get_list_or_404(Project, sector=sector)
    return render_to_response('ims/projects.html', { 'projects': projects })

#view:project, :project_id
def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render_to_response('ims/project_detail.html', { 'project': project })

#view:partners
def partners(request):
    partners = get_list_or_404(DevelopmentPartner)
    return render_to_response('ims/partners.html', { 'partners': partners })

#view:partner :partner_id
def partner(request, id):
    partner = get_object_or_404(DevelopmentPartner, pk=id)
    partner_projects = partner.project_set.all()
    pass

#view:recipients
def recipients(request):
    recipients = get_list_or_404(Recipient)
    return render_to_response('ims/recipients.html',{ 'recipients': recipients })

#view:recipient :recipient_id
def recipient(request, id):
    recipient = get_object_or_404(Recipient, pk=id)
    recipient_projects = recipient.project_set.all()
    pass

#view:search

#view:index
def index(request):
    render_to_response('ims/index.html')