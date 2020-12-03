__author__ = "soopercool101"
__version__ = "1.0.0"

from BrawlCrate.API import *
from BrawlLib.SSBB.ResourceNodes import *
from BrawlCrate.NodeWrappers import PluginWrapper
from System.Windows.Forms import ToolStripMenuItem
import struct

# Wrapper for UVs
class UVWrapper(PluginWrapper):
    # This function returns a new instance of the class.
    # Necessary in order to properly call necessary functions
    def GetInstance(self):
        return UVWrapper()

def shiftUV_handler(sender, event_args):
    scaleX = BrawlAPI.UserFloatInput("X-Scale", "X Scale multiplier to apply to the UVs (Applied first)", 1.0)
    scaleY = BrawlAPI.UserFloatInput("Y-Scale", "Y Scale multiplier to apply to the UVs (Applied first)", 1.0)
    transX = BrawlAPI.UserFloatInput("X-Translation", "X Translation offset to apply to the UVs (Applied second)", 0.0)
    transY = BrawlAPI.UserFloatInput("Y-Translation", "Y Translation offset to apply to the UVs (Applied second)", 0.0)
    shiftUV(scaleX, scaleY, transX, transY)

def shiftUV(scaleX, scaleY, transX, transY):
    i = 0
    for vec2 in BrawlAPI.SelectedNode.Points:
        vec2.X = vec2.X * scaleX
        vec2.X = vec2.X + transX
        vec2.Y = vec2.Y * scaleY
        vec2.Y = vec2.Y + transY
        BrawlAPI.SelectedNode.Points[i] = vec2
        i += 1
    BrawlAPI.SelectedNode.Points = BrawlAPI.SelectedNode.Points
    BrawlAPI.SelectedNode.SignalPropertyChange()

# Create an instance of our wrapper class and add it to the API wrapper cache
wrapper = UVWrapper()
BrawlAPI.AddWrapper[MDL0UVNode](wrapper)
# Add a context menu item to our new wrapper
BrawlAPI.AddContextMenuItem(UVWrapper, ToolStripMenuItem("Shift UVs", None, shiftUV_handler))
