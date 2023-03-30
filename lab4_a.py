import os
import datetime
import sys
import json
from lab4_pods import do_in_cmd, return_path_to_backup, return_path_to_file_history

def backup():
    dir_path = sys.argv[1]

    backup_dir = return_path_to_backup()

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print('Backup dir created')

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    backup_name = f'{timestamp}-{os.path.basename(dir_path)}.zip'
    backup_path = os.path.join(backup_dir, backup_name)

    zip_command = f'powershell Compress-Archive -Path "{dir_path}" -DestinationPath "{backup_path}"'

    if do_in_cmd(zip_command):
        return

    history_file = return_path_to_file_history(backup_dir)
    backup_data = {'data':timestamp,'path':os.path.join(backup_dir, backup_name),'dir name':backup_name}

    with open(history_file, 'a', newline='') as file:
        json.dump(backup_data, file)
        file.write('\n')

if __name__ == '__main__':
    backup()
