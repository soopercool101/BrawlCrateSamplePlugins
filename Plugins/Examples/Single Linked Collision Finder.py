__author__ = "soopercool101"
__version__ = "1.0.0"

from BrawlCrate.API import *
from BrawlLib.SSBB.ResourceNodes import *
from System.IO import *

# Get a stage folder
folder = BrawlAPI.OpenFolderDialog("Select a folder which contains stages")
if folder != "":
    list = ""
    # Open every file in the folder
    for file in Directory.GetFiles(folder):
        if BrawlAPI.OpenFileNoErrors(file):
            # Find all collision objects
            collObjs = BrawlAPI.NodeListOfType[CollisionObject]()
            found = False
            # Check each collision plane for any unknown flag
            for obj in collObjs:
                for plane in obj._planes:
                    if plane.LinkLeft == plane.LinkRight:
                        fName = Path.GetFileNameWithoutExtension(file)
                        # Add this file to the list if it isn't already there
                        if not found:
                            list += "" + fName + "\n"
                        found = True
                        # Write to the console where the single-linked collision is found
                        BrawlAPI.WriteToConsole(fName + "/" + obj.Parent.Name + "/" + obj.Name + " | " + str(plane.LinkLeft.Value))
            # Close the file
            BrawlAPI.ForceCloseFile()
    # List any files where the flags are found
    if list != "":
        BrawlAPI.ShowMessage("The following files contain single-linked collisions:\n\n" + list, "Found Single-Linked Collisions")
    else:
        BrawlAPI.ShowError("No single-linked collisions found", "Error")