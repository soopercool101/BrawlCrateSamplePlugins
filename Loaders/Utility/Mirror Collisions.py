__author__ = "soopercool101"
__version__ = "1.0.0"

from BrawlCrate.API import *
from BrawlCrate.NodeWrappers import CollisionWrapper
from BrawlCrate.UI import MainForm
from BrawlLib.Internal import Vector2
from BrawlLib.SSBB.ResourceNodes import *
from BrawlLib.SSBB.Types import CollisionPlaneType
from System.Windows.Forms import ToolStripMenuItem

# Function to ensure the context menu item is only active if it's the CSP ARC
def EnableCheck(sender, event_args):
    sender.Enabled = BrawlAPI.SelectedNode is not None

# Mirror along the x axis
def coll_flip_x(sender, event_args):
    for cObj in BrawlAPI.SelectedNode.Children:
        if cObj.LinkedBone is None:
            for link in cObj._points:
                link._rawValue = Vector2(0 - link._rawValue._x, link._rawValue._y)
            for plane in cObj._planes:
                rLedge = plane.IsRightLedge
                lLedge = plane.IsLeftLedge
                plane.SwapLinks()
                plane.IsRightLedge = lLedge
                plane.IsLeftLedge = rLedge
                if plane._type == CollisionPlaneType.RightWall:
                    plane._type = CollisionPlaneType.LeftWall
                elif plane._type == CollisionPlaneType.LeftWall:
                    plane._type = CollisionPlaneType.RightWall
    MainForm.Instance.resourceTree_SelectionChanged(None, None)

# Mirror along the y axis
def coll_flip_y(sender, event_args):
    for cObj in BrawlAPI.SelectedNode.Children:
        if cObj.LinkedBone is None:
            for link in cObj._points:
                link._rawValue = Vector2(link._rawValue._x, 0 - link._rawValue._y)
            for plane in cObj._planes:
                plane.SwapLinks()
                if plane._type == CollisionPlaneType.Floor:
                    plane._type = CollisionPlaneType.Ceiling
                    plane.IsFallThrough = false
                    plane.IsRightLedge = false
                    plane.IsLeftLedge = false
                elif plane._type == CollisionPlaneType.Ceiling:
                    plane._type = CollisionPlaneType.Floor
    MainForm.Instance.resourceTree_SelectionChanged(None, None)

# Add a button to our right click menu. In this case, adds buttons to the right click menu for any Collision Wrapper
#
# Arguments are (in order) as follows:
# Wrapper: Denotes which wrapper the context menu items will be added to
# Submenu: If not blank, adds to a submenu with this name
# Description: Creates a mouseover description for the item
# Conditional: When the wrapper's context menu is opened, this function is called. Allows enabling/disabling of plugin members based on specific conditions
# Items: One or more toolstripmenuitems that will be added
BrawlAPI.AddContextMenuItem(CollisionWrapper, 'Mirror', 'Flips Collision along the X-Axis', EnableCheck, ToolStripMenuItem('Mirror Unbound Collisions (X-Axis)', None, coll_flip_x))
BrawlAPI.AddContextMenuItem(CollisionWrapper, 'Mirror', 'Flips Collision along the Y-Axis', EnableCheck, ToolStripMenuItem('Mirror Unbound Collisions (Y-Axis)', None, coll_flip_y))
