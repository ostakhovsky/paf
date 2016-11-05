'''
Created on Oct 19, 2016

@author: sashaalexander
@author: team 9
'''
from datetime import datetime
import os
import sys


def getLog(testName, logDir):
    """
    Creates logDir directory, if it doesn't exist,
    creates or opens a log file in 'logs' directory.
    """
    # assign a current working directory + '/logs' to log_dir variable (platform independent)
    log_dir = os.path.join(os.getcwd(), logDir)
    # or --> script directory: log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    # or --> user directory: log_dir = os.path.join(os.path.expanduser("~"), "logs")

    try:
        # if logs directory(!) doesn't exist, create it
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
            # open log file with prefix and timestamp (platform independent) in Append mode
        log = open(os.path.join(log_dir, testName + "_" + getCurTime("%Y%m%d_%H-%M-%S") + ".log"), "a")
        return log
    except (OSError, IOError):
        # return -1 in case of exception
        return -1


def qaPrint(log, message):
    """
    Prints 'timestamp + message' to console and writes it to the log file
    """
    # current date and time as string + message. example: [Oct 25 01:52:33.000001] TC1 - Passed
    log_message = getCurTime("[%b %d %H:%M:%S.%f]") + " " + message
    # prints log_message
    print log_message
    # writes message to a log file
    log.write(log_message + "\n")


def getCurTime(date_time_format):
    """
    Returns current date_time as a string formatted according to date_time_format
    """
    date_time = datetime.now().strftime(date_time_format)
    return date_time


def getLocalEnv(propertiesFileName):
    try:
        properties = open(propertiesFileName, "r")
        props = {}
        for line in properties:
            line = line.strip()
            if "=" not in line: continue
            if line.startswith("#"): continue
            k, v = line.split("=", 1)
            props[k] = v
        return props
    except Exception as e:
        print e
        return -1


def getTestCases(testRunId):
    TEST_CASE_KEYS = ('tcid', 'rest_URL', 'HTTP_method', 'HTTP_RC_desired', 'param_list')
    testCases = {}
    try:
        testCasesFile = open(str(testRunId) + '.txt')
        for line in testCasesFile:
            tc = line.strip().split("|")
            for i in range(1, len(tc) - 1):
                if tc[0] not in testCases:
                    testCases[tc[0]] = {}
                testCases[tc[0]][TEST_CASE_KEYS[i]] = tc[i]
            testCases[tc[0]][TEST_CASE_KEYS[-1]] = tc[-1].split(',')
        return testCases
    except Exception as ex:
        print ex
        return -1


def usage():
    print ('[ERROR]Invalid parameters. Proper usage: rfaRunner.py --testrun=<testRunId>')


def closeLog(log):
    # close the log file if it open
    if not log.closed:
        qaPrint(log, 'Test suite ends')
        log.close()


def getArguments(args):
    arguments = {}
    if len(args) < 2:
        sys.exit(usage())
    try:
        arguments['testName'] = args[0].split('/')[-1].replace('.py', '')
        for i in range(1, len(args)):
            arg = args[i].split('=')
            if arg[0].lower() == '--testrun':
                arguments['trid'] = int(arg[1])
                if (arguments['trid'] not in range(1, 10001)):
                    usage()
                    sys.exit("[ERROR]Invalid parameter, value should be [0-10000]")
        return arguments
    except Exception:
        sys.exit(usage())


def logTestCases(test_cases,log):
    for key, value in test_cases.iteritems():
        qaPrint(log, '[INFO]Test case #' + key + str(value))


def validateProperties(properties):
    if properties == -1:
        sys.exit('[ERROR]Could not read properties')
    if 'log_dir'not in properties.keys():
        sys.exit("[ERROR]log_dir property is missing")

