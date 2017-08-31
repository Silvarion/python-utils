##############################
#
#   Silvarion's Python Utils - pythils
#
#   @author: Jesus Alejandro Sanchez Davila
#
#   This is a group of utility functions/procedures
#   that aim to help the developer simplify some common steps
#   inside their programs/scripts.
#
################


# Formatted printer for beautified logs and messages
def log (severity, msg):
    tag = severity.lower()
    import datetime
    ts = str(datetime.datetime.now()).split('.')[0]
    if  tag == 'debug' :
        tag = '[' + ts + '][DEBUG] '
    elif tag  == 'log' :
        tag = '[' + ts + ']LOG] '
    elif tag  == 'info' :
        tag = '[' + ts + '][INFO] '
    elif tag  == 'notice' :
        tag = '[' + ts + '][NOTICE] '
    elif tag  == 'warning' :
        tag = '[' + ts + '][WARNING] '
    elif tag  == 'error' :
        tag = '[' + ts + '][ERROR] '
    elif tag  == 'critical' :
        tag = '[' + ts + '][CRITICAL] '
    elif tag  == 'plain' :
        tag = ''

    print(tag + msg)
        
def readConfigFile (file_handle):
    # Return variable
    config = {}
    # Open the configuration file
    file_pointer= open(file_handle)
    # Create a list with each line
    contents = [line.rstrip('\n') for line in file_pointer]
    # Process each line separately
    for line in contents:
        key,value = line.split('=')
        config[key] = value
    return config

