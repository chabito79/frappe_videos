# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "videos"
app_title = "Videos de Ayuda"
app_publisher = "C0D1G0 B1NAR10"
app_description = "Aplicacion de Videos de Ayuda para el sistema de Punto de Venta"
app_icon = "octicon octicon-device-camera-video"
app_color = "#ff5858"
app_email = "admin@codigo-binario.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/videos/css/videos.css"
# app_include_js = "/assets/videos/js/videos.js"

# include js, css files in header of web template
# web_include_css = "/assets/videos/css/videos.css"
# web_include_js = "/assets/videos/js/videos.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "videos.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "videos.install.before_install"
# after_install = "videos.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "videos.notifications.get_notification_config"

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
# 		"videos.tasks.all"
# 	],
# 	"daily": [
# 		"videos.tasks.daily"
# 	],
# 	"hourly": [
# 		"videos.tasks.hourly"
# 	],
# 	"weekly": [
# 		"videos.tasks.weekly"
# 	]
# 	"monthly": [
# 		"videos.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "videos.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "videos.event.get_events"
# }

