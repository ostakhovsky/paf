'''
Created on Oct 19, 2016
@author: sashaalexander
@author: team 9
'''
import sys
from __builtin__ import str

from rfaUtils import getLog, qaPrint, getLocalEnv, getTestCases, closeLog, getArguments, logTestCases, validateProperties

# process command line arguments
arguments = getArguments(sys.argv)

# read properties
localProperties = getLocalEnv('local.properties')
validateProperties(localProperties)

# get the log file handle
log = getLog(arguments['testName'], localProperties['log_dir'])

# exit if log creation failed
if log == -1:
    sys.exit("[ERROR]Could not create log file")
qaPrint(log,"[INFO]Test suite starts")

# read test cases
test_cases = getTestCases(arguments['trid'])

if test_cases == -1:
    qaPrint(log, '[ERROR]Could not read test cases')
    closeLog(log)
    sys.exit()
else:
    qaPrint(log, '[INFO]Got test cases. Testrun id is ' + str(arguments['trid']))
    logTestCases(test_cases,log)

closeLog(log)
