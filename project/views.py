from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from fb_graph.handlers import FacebookGraphAPIHandler


class DemoView(LoginRequiredMixin, TemplateView):
    template_name = "demo.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        token = (
            self.request.user.socialaccount_set.get(provider="facebook")
            .socialtoken_set.first()
            .token
        )
        fb_graph = FacebookGraphAPIHandler(token)
        fb_graph.get_instagram_data()
        fb_graph.get_instagram_insights()
        fb_graph.get_instagram_medias()
        context["object1"] = fb_graph.instagram_data
        context["object2"] = fb_graph.instagram_insights
        context["object3"] = fb_graph.instagram_medias
        context["hashtags"] = [item[1:] for item in fb_graph.instagram_data["biography"].split(" ") if item.startswith("#")]
        for media in fb_graph.instagram_medias["data"]:
            if "caption" in media:
                context["hashtags"] += [item[1:] for item in media["caption"].split(" ") if item.startswith("#")]

        return context
