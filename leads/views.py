from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse
from .models import Lead
from django.views import generic
from .forms import LeadModelForm, CustomUserCreationForm
from django.core.mail import send_mail

# Create your views here.
class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self) -> str:
        return reverse("login")

class HomePageView(generic.TemplateView):
    template_name = "home.html"

class LeadListView(generic.ListView):
    template_name = "lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(generic.DetailView):
    template_name = "lead_details.html"
    queryset = Lead.objects.all()
    context_object_name = 'lead'

class LeadCreateView(generic.CreateView):
    template_name = "lead_create.html"
    form_class = LeadModelForm

    def form_valid(self, form):
        send_mail(
            subject= "A lead has been created",
            message= "Pleas visit the site to view the created lead",
            from_email= "sanijacobs@proton.me",
            recipient_list= ["itopasani@gmail.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadUpdateView(generic.UpdateView):
    template_name = "lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")
    
class LeadDeleteView(generic.DeleteView):
    template_name = "lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")