from models import *
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.core.urlresolvers import reverse
#from datetime import date, timedelta
#from django.template import RequestContext

#view:index
@require_http_methods(["GET"])
def index(request):
    return render_to_response('ims/index.html', {'nav':'index'})

#view:projects
@require_http_methods(["GET"])
def projects(request):
    projects = Project.objects.all()
    return render_to_response('ims/projects.html', { 'projects': projects, 'nav':'projects' })

#view:projects_by_sector
@require_http_methods(["GET"])
def projects_by_sector(request, sector):
    projects = get_list_or_404(Project, sector=sector)
    return render_to_response('ims/projects.html', { 'projects': projects, 'nav':'projects' })

#view:project, :project_id
@require_http_methods(["GET"])
def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render_to_response('ims/project_detail.html', {'project':project, 'nav':'projects' })

#view:partners
@require_http_methods(["GET"])
def partners(request):
    partners = DevelopmentPartner.objects.all()
    return render_to_response('ims/partners.html', { 'partners': partners, 'nav':'partners' })

#view:partner :partner_id
@require_http_methods(["GET"])
def partner(request, id):
    partner = get_object_or_404(DevelopmentPartner, pk=id)
    #partner_projects = partner.project_set.all()
    return render_to_response('ims/partner_detail.html', {'partner':partner, 'nav':'partners'})

#view:recipients
@require_http_methods(["GET"])
def recipients(request):
    recipients = Recipient.objects.all()
    return render_to_response('ims/recipients.html',{ 'recipients': recipients, 'nav':'recipients' })

#view:recipient :recipient_id
@require_http_methods(["GET"])
def recipient(request, id):
    recipient = get_object_or_404(Recipient, pk=id)
    #recipient_projects = recipient.project_set.all()
    return render_to_response('ims/recipient_detail.html', { 'recipient':recipient, 'nav':'recipients' })