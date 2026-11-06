
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home.html"


class AdminPanelView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "dashboard/admin_panel.html"

    def test_func(self):
        return self.request.user.is_staff
