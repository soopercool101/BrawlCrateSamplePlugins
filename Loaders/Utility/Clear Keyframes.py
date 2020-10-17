from BrawlCrate.API import *
from BrawlCrate.NodeWrappers import CHR0Wrapper, CHR0EntryWrapper
from BrawlLib.SSBB.ResourceNodes import *
from BrawlLib.Wii.Animations import *
from System.Windows.Forms import ToolStripMenuItem

def clear_translation(sender, event_args):
    if isinstance(BrawlAPI.SelectedNode, CHR0Node):
        for node in BrawlAPI.SelectedNode.Children:
            clear_node_translation(node)
    else:
        clear_node_translation(BrawlAPI.SelectedNode)
    BrawlAPI.RefreshPreview()

def clear_node_translation(node):
    for x in range(0, node.FrameCount):
        node.RemoveKeyframeOnlyTrans(x)

def clear_scale(sender, event_args):
    if isinstance(BrawlAPI.SelectedNode, CHR0Node):
        for node in BrawlAPI.SelectedNode.Children:
            clear_node_scale(node)
    else:
        clear_node_scale(BrawlAPI.SelectedNode)
    BrawlAPI.RefreshPreview()

def clear_node_scale(node):
    for x in range(0, node.FrameCount):
        node.RemoveKeyframeOnlyScale(x)

def clear_rotation(sender, event_args):
    if isinstance(BrawlAPI.SelectedNode, CHR0Node):
        for node in BrawlAPI.SelectedNode.Children:
            clear_node_rotation(node)
    else:
        clear_node_rotation(BrawlAPI.SelectedNode)
    BrawlAPI.RefreshPreview()

def clear_node_rotation(node):
    for x in range(0, node.FrameCount):
        node.RemoveKeyframeOnlyRot(x)

BrawlAPI.AddContextMenuItem(CHR0Wrapper, None, 'Clears translation keyframes for all entries', None, ToolStripMenuItem('Clear Translation', None, clear_translation))
BrawlAPI.AddContextMenuItem(CHR0Wrapper, None, 'Clears rotation keyframes for all entries', None, ToolStripMenuItem('Clear Rotation', None, clear_rotation))
BrawlAPI.AddContextMenuItem(CHR0Wrapper, None, 'Clears scale keyframes for all entries', None, ToolStripMenuItem('Clear Scale', None, clear_scale))
BrawlAPI.AddContextMenuItem(CHR0EntryWrapper, None, 'Clears translation keyframes', None, ToolStripMenuItem('Clear Translation', None, clear_translation))
BrawlAPI.AddContextMenuItem(CHR0EntryWrapper, None, 'Clears rotation keyframes', None, ToolStripMenuItem('Clear Rotation', None, clear_rotation))
BrawlAPI.AddContextMenuItem(CHR0EntryWrapper, None, 'Clears scale keyframes', None, ToolStripMenuItem('Clear Scale', None, clear_scale))