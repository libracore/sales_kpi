# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sales_kpi"
app_title = "Sales KPI"
app_publisher = "libracore"
app_description = "Sales KPI Dashboard App for ERPNext"
app_icon = "fa fa-line-chart"
app_color = "gold"
app_email = "info@libracore.com"
app_license = "AGPL"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sales_kpi/css/sales_kpi.css"
# app_include_js = "/assets/sales_kpi/js/sales_kpi.js"

# include js, css files in header of web template
# web_include_css = "/assets/sales_kpi/css/sales_kpi.css"
# web_include_js = "/assets/sales_kpi/js/sales_kpi.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sales_kpi.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sales_kpi.install.before_install"
# after_install = "sales_kpi.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sales_kpi.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sales_kpi.tasks.all"
# 	],
# 	"daily": [
# 		"sales_kpi.tasks.daily"
# 	],
# 	"hourly": [
# 		"sales_kpi.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sales_kpi.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sales_kpi.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sales_kpi.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sales_kpi.event.get_events"
# }

