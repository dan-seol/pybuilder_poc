#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
#use_plugin("python.unittest")
use_plugin("pypi:pybuilder_pytest")
use_plugin("pypi:pybuilder_pytest_coverage")
use_plugin("python.flake8")
use_plugin("python.distutils")


name = "pybuilder_poc"
default_task = ["clean", "analyze", "verify", "package", "publish"]


@init
def set_properties(project):
    project.set_property('flake8_break_build', True)
