import sys
import maya.api.OpenMaya as om
import maya.cmds as cmds
import pyblish.api
import pyblish_maya


def maya_useNewAPI():  # noqa
    pass  # dummy method to tell Maya this plugin uses Maya Python API 2.0


def initializePlugin(plugin):
    pyblish.api.register_gui("pyblish_lite")
    pyblish_maya.setup()


def uninitializePlugin(plugin):
    pyblish.api.deregister_gui("pyblish_lite")
    pyblish_maya.teardown()
