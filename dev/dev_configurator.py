# A place for me to sort out the details of this current refactor.
# I want to be able to construct all needed objects from a config file,
# as well as save out modified objects to that config file.

# This will turn into a test of the configurator... Not really looking to 
# perform the calibration. Just load everything, then save everything out, 
# to a different file and make sure stuff is the same.



# initialize
# provided with a path, load toml or create a default toml.

# check if config has cameras....needed for session to determine if it should find them


# SIDE NOTE HERE: session.find_cameras could just be a standalone helper function.
# might as well hold it in config for the time being...


# load cameras



# load streams *from cameras* (these do not require loading from config)



# load charuco


# save cameras



# load charuco



# save charuco


# load camera array (composed of  camera data objects for calibration/triangulation)









