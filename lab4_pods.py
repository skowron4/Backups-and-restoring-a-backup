import subprocess
import os

def do_in_cmd(command):
    if subprocess.call(command) != 0:
        print('command not executed')
        return True
    print('command executed')
    return False

def return_path_to_backup():
    return os.path.join(os.environ.get('BACKUPS_DIR') or os.path.expandvars('%USERPROFILE%\.backups'))

def return_path_to_file_history(backup_dir):
    return f"{backup_dir}/history.json"