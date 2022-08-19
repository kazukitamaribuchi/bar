import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from crm.models import mUser
from django.utils.safestring import mark_safe
import logging
import json

logger = logging.getLogger(__name__)

class HomeView(TemplateView):
    template_name = 'index.html'
