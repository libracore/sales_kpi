from __future__ import unicode_literals
from frappe import _

def get_data():
    return[
        {
            "label": _("Sales"),
            "icon": "fa fa-line-chart",
            "items": [
                   {
                       "type": "page",
                       "name": "sales_dashboard",
                       "label": _("Sales Dashboard"),
                       "description": _("Sales Dashboard")
                   }
            ]
        }
    ]
