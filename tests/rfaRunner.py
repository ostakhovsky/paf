'''
Created on Oct 19, 2016
@author: sashaalexander
@author: team X
'''
from rfaUtils import getLog, qaPrint, getLocalEnv, getTestCases
import sys
# process command line arguments
if len(sys.argv) < 2:
    sys.exit('Usage: rfaRunner.py --testrun=<testRunId>')

testName = sys.argv[0].split('/')[-1].replace('.py', '')

for i in range(1, len(sys.argv)):
    arg = sys.argv[i].split('=')
    if arg[0].lower() == '--testrun':
        trid = int(arg[1])
# read properties
localProperties = getLocalEnv('local.properties')
# read test cases
test_cases = getTestCases(trid)
# get the log file handle
log = getLog(testName, localProperties['log_dir'])

# exit if log creation failed
if log == -1:
    sys.exit("Unable to create log file")

message = "It is working, right?"

# call qaPrint to print a message with timestamp and write it to the log file
qaPrint(log, message)
qaPrint(log, "Me like what me see")

# close the log file if it open
if not log.closed:
    log.close()
