from models import *
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from chartit import DataPool, PivotDataPool, Chart, PivotChart
#from django.core.urlresolvers import reverse
#from django.template import RequestContext

def charts():
   pass

#view:index | url: index_url
@require_http_methods(["GET"])
def index(request):
    return render_to_response('ims/index.html', { 'nav':'index', 'charts':charts() })

#view:projects | url projects_url
@require_http_methods(["GET"])
def projects(request):
    projects = Project.objects.select_related().all()
    return render_to_response('ims/projects.html', { 'projects': projects, 'nav':'projects' })

#view:project, &:project_id | url project_url
@require_http_methods(["GET"])
def project(request, id):
    project = Project.objects.select_related(depth=1).get(pk=id)
    return render_to_response('ims/project_detail.html', {'project':project, 'nav':'projects' })

#view:partners | url partners_url
@require_http_methods(["GET"])
def partners(request):
    partners = DevelopmentPartner.objects.select_related(depth=2).all()
    return render_to_response('ims/partners.html', { 'partners': partners, 'nav':'partners' })

#view:partner &:partner_id | url partner_url
@require_http_methods(["GET"])
def partner(request, id):
    partner = DevelopmentPartner.objects.select_related(depth=2).get(pk=id)
    return render_to_response('ims/partner_detail.html', {'partner':partner, 'nav':'partners'})

#view:recipients | url recipients_url
@require_http_methods(["GET"])
def recipients(request):
    recipients = Recipient.objects.select_related(depth=2).all()
    return render_to_response('ims/recipients.html',{ 'recipients': recipients, 'nav':'recipients' })

#view:recipient &:recipient_id | url recipient_url
@require_http_methods(["GET"])
def recipient(request, id):
    recipient = Recipient.objects.select_related(depth=2).get(pk=id)
    return render_to_response('ims/recipient_detail.html', { 'recipient':recipient, 'nav':'recipients' })