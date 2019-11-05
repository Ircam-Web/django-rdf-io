from __future__ import unicode_literals

try:
   from django.core import signals
except:
    import signals


__version__ = (0, 1)

default_app_config = 'rdf_io.apps.RDFIOConfig'
