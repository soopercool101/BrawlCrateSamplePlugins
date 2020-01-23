__author__ = "soopercool101 and Sammi Husky"
__version__ = "2.0.0"

from BrawlCrate.API import *
from BrawlLib.SSBB.ResourceNodes import *
from BrawlCrate.NodeWrappers import PluginWrapper
from System.Windows.Forms import ToolStripMenuItem
import struct

# Font node parser. All plugin node parsers must be derived from ResourceNode (or a derivative therein) and the PluginResourceParser interface
class RFNTNode(ARCEntryNode, PluginResourceParser):
    # Set our resource type (Dictates nodewrapper and icon)
    def get_ResourceFileType(self):
        return ResourceType.NoEditFolder

    # Gets a formatted name for the object, matching other ArcEntryNodes
    def get_Name(self):
        return "NW4R Font [" + str(self.FileIndex) + "]"

    # Called by super class to check if this loader matches the data
    def TryParse(self, stream):
        # Get the 4-byte tag at the beginning of the node. Many nodetypes in Brawl use this type of identifier
        src = file(stream)
        src.seek(0,0)
        tag = ""
        tag = tag.join(struct.unpack('>4s', src.read(4)))

        # If the tag matches, return an instance of our class
        if tag == "RFNT": #RFNT
            return RFNTNode()
        # Otherwise, return null as a fail state
        return None

    # Called for each instance of a new node, in order to set it up properly. This is where data beyond the tag should be read and stored
    def OnInitialize(self):
        # On initialize returns true if it has children, false if it does not
        return False

# Wrapper for font files
class RFNTWrapper(PluginWrapper):
    # This function returns a new instance of the class.
    # Necessary in order to properly call necessary functions
    def GetInstance(self):
        return RFNTWrapper()

# Basic test function that is called by the context menu
def doSomething_handler(sender, event_args):
    BrawlAPI.ShowMessage("This is a test function","Title")

# Create an instance of our node class and add it to the API loader cache
node = RFNTNode()
BrawlAPI.AddResourceParser(node)
# Create an instance of our wrapper class and add it to the API wrapper cache
wrapper = RFNTWrapper()
BrawlAPI.AddWrapper[RFNTNode](wrapper)
# Add a context menu item to our new wrapper
BrawlAPI.AddContextMenuItem(RFNTWrapper, ToolStripMenuItem("Do Something", None, doSomething_handler))
