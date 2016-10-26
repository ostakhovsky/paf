import datetime
import os
from datetime import date


def make_sure_path_exists(log_path):
    try:
        os.makedirs(log_path)
    except OSError as e:    
        print e 
             
def get_timestamp():
    return datetime.datetime.now().strftime('%Y_%m_%d_%H:%M_%S')

def getLog(log_dir='logs'):
    log_path = os.path.join(os.getcwd(), log_dir)
    log_name = 'testrun_' + get_timestamp() + '.log'
    make_sure_path_exists(log_path)
    try:
        log_file = open(os.path.join(log_path, log_name), 'a')
        return log_file
    except IOError as e:
        print e
        return -1


def qaprint(log_file_handler, log_entry):
    if  log_file_handler != -1:
        new_line = log_entry + ' ' + get_timestamp() + '\n'
        log_file_handler.write(new_line)
        print new_line
    else:
        print("Could not write to log")
        
def close_log(log_file):
    log_file.close()
