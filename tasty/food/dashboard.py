"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'wine_price_crawler.dashboard.CustomIndexDashboard'
"""
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard
from jet.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # # append a group for "Administration" & "Applications"
        # self.children.append(modules.Group(
        #     _('Group: Administration & Applications'),
        #     column=1,
        #     collapsible=True,
        #     children = [
        #         modules.AppList(
        #             _('Administration'),
        #             column=1,
        #             collapsible=False,
        #             models=('django.contrib.*',),
        #         ),
        #         modules.AppList(
        #             _('Applications'),
        #             column=1,
        #             css_classes=('collapse closed',),
        #             exclude=('django.contrib.*',),
        #         )
        #     ]
        # ))

        # self.children.append(modules.ModelList(
        #     _('Administration'),
        #     column=1,
        #     collapsible=False,
        # ))
        #
        # self.children.append(modules.LinkList(
        #     _('Crawling Triggers'),
        #     column=2,
        #     children=[
        #         {
        #             'title': _('Crawl Wine Searcher'),
        #             'url': reverse('spider_control', kwargs={'spider_name': 'wine_searcher_api'}),
        #             'external': False,
        #         },
        #     ]
        # ))
