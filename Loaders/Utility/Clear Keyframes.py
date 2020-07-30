from BrawlCrate.API import *
from BrawlCrate.NodeWrappers import CHR0EntryWrapper
from BrawlLib.SSBB.ResourceNodes import *
from BrawlLib.Wii.Animations import *
from System.Windows.Forms import ToolStripMenuItem

def clear_translation(sender, event_args):
    for x in range(0, BrawlAPI.SelectedNode.FrameCount):
        BrawlAPI.SelectedNode.RemoveKeyframeOnlyTrans(x)
    BrawlAPI.RefreshPreview()

def clear_scale(sender, event_args):
    for x in range(0, BrawlAPI.SelectedNode.FrameCount):
        BrawlAPI.SelectedNode.RemoveKeyframeOnlyScale(x)
    BrawlAPI.RefreshPreview()

def clear_rotation(sender, event_args):
    for x in range(0, BrawlAPI.SelectedNode.FrameCount):
        BrawlAPI.SelectedNode.RemoveKeyframeOnlyRot(x)
    BrawlAPI.RefreshPreview()

BrawlAPI.AddContextMenuItem(CHR0EntryWrapper, None, 'Clears Translation', None, ToolStripMenuItem('Clear Translation', None, clear_translation))
BrawlAPI.AddContextMenuItem(CHR0EntryWrapper, None, 'Clears Rotation', None, ToolStripMenuItem('Clear Rotation', None, clear_rotation))
BrawlAPI.AddContextMenuItem(CHR0EntryWrapper, None, 'Clears Scale', None, ToolStripMenuItem('Clear Scale', None, clear_scale))