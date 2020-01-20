__author__ = "soopercool101"
__version__ = "1.0.0"

from BrawlCrate.API import BrawlAPI
from BrawlLib.SSBB.ResourceNodes import *
from BrawlCrate.UI import MainForm
from System.IO import *
import re

# Main function
# Ask for the fighter directory
folder = BrawlAPI.OpenFolderDialog("Open Fighter Folder")
if folder:
    # Save setting of whether or not fighter PACs get decompressed. But disable it for now.
    setting = MainForm.Instance.AutoDecompressFighterPAC
    MainForm.Instance.AutoDecompressFighterPAC = False
    # Get fighter subfolders
    fighterDir = Directory.CreateDirectory(folder).GetDirectories()
    for subfolder in fighterDir:
        name = subfolder.Name.lower()
        # Ignore transforming characters
        if not name == "kirby" or name == "koopa" or name == "gkoopa" or name == "zelda" or name == "sheik" or name == "wario" or name == "warioman" or name == "poketrainer":
            for file in subfolder.GetFiles():
                # Get ##, Dark, Fake, Spy, and Alt costumes that aren't Etc/Final/Results/Entry files
                if re.search(r"(?<![Ee][Tt][Cc])(?<![Ff][Ii][Nn][Aa][Ll])(?<![Rr][Ee][Ss][Uu][Ll][Tt])(?<![Ee][Nn][Tt][Rr][Yy])(\d\d|[Ss][Pp][Yy]|[Dd][Aa][Rr][Kk]|[Ff][Aa][Kk][Ee]|[Aa][Ll][Tt]\w).[Pp][Aa][Cc]$", file.Name) is not None:
                    # Open the file
                    BrawlAPI.OpenFile(file.FullName)
                    if isinstance(BrawlAPI.RootNode, ARCNode):
                        # Compress as ExtendedLZ77 if it isn't already
                        if not BrawlAPI.RootNode.Compression == "ExtendedLZ77":
                            BrawlAPI.RootNode.Compression = "ExtendedLZ77"
                            BrawlAPI.SaveFile()
                    # Close the file without displaying messages
                    BrawlAPI.ForceCloseFile()
    # Ask if you'd like to turn off the auto-compress fighter PAC option (Assumedly you would if using this)
    if setting:
        if not BrawlAPI.ShowYesNoPrompt("BrawlCrate is currently set to decompress PAC files by default. Would you like to change this behavior?", "Update Settings"):
            MainForm.Instance.AutoDecompressFighterPAC = setting