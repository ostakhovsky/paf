'''
Created on Oct 19, 2016
@author: sashaalexander
@author: team 9
'''
from rfaUtils import getLog, qaPrint, getLocalEnv, getTestCases, closeLog, usage
import sys
from __builtin__ import str
# process command line arguments


if len(sys.argv) < 2:
    sys.exit(usage())

testName = sys.argv[0].split('/')[-1].replace('.py', '')

try:
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i].split('=')
        if arg[0].lower() == '--testrun':
            trid = int(arg[1])
except Exception:
    sys.exit(usage())

# read properties
localProperties = getLocalEnv('local.properties')

if localProperties == -1:
    sys.exit('[ERROR]Could not read properties')
# get the log file handle
if 'log_dir' in localProperties.keys():
    log = getLog(testName, localProperties['log_dir'])
else:
    sys.exit("[ERROR]log_dir property is missing")

# exit if log creation failed
if log == -1:
    sys.exit("[ERROR]Could not create log file")
qaPrint(log,"Test suite starts")
# read test cases
test_cases = getTestCases(trid)

if test_cases == -1:
    qaPrint(log, '[ERROR]Could not read test cases')
    closeLog(log)
    sys.exit()
else:
    qaPrint(log, 'Got test cases. Testrun id is ' + str(trid))
    for key,value in test_cases.iteritems():
        qaPrint(log,'Test case #'+ key  + str(value) )

closeLog(log)
