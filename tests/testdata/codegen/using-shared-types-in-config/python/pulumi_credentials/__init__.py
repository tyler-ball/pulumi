# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .provider import *
from .user import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_credentials.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_credentials.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "credentials",
  "mod": "index",
  "fqn": "pulumi_credentials",
  "classes": {
   "credentials:index:User": "User"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "credentials",
  "token": "pulumi:providers:credentials",
  "fqn": "pulumi_credentials",
  "class": "Provider"
 }
]
"""
)