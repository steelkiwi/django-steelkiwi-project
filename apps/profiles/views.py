from django.views.generic import DetailView

from braces.views import LoginRequiredMixin

from .models import Profile


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.jhtml'

    def get_object(self, queryset=None):
        return self.model.objects.get(user_id=self.request.user.id)


profile_detail = ProfileDetailView.as_view()
