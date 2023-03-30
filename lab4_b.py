import json
import os
import shutil
import sys
from lab4_pods import do_in_cmd, return_path_to_backup, return_path_to_file_history

def restore():
    dir_path = sys.argv[1] if len(sys.argv) > 0 else os.getcwd()

    backup_dir = return_path_to_backup()

    history_file = return_path_to_file_history(backup_dir)
    backup_dates = []

    with open(history_file, 'r') as file:
        for line in file:
            backup_dates.append(json.loads(line))

    is_running = True
    backup_file = ""

    while is_running:
        for i, data in enumerate(backup_dates):
            print(f"{i + 1}. data: {data['data']}; path: {data['path']}; dir name: {data['dir name']}")
        print()
        try:
            backup_num = int(input("Enter the number of the backup to restore: "))
            if backup_num > len(backup_dates) or backup_num < 0:
                print("You selected non-existent record")
                print()
            else:
                is_running = False
                backup_file = backup_dates[backup_num - 1]['path']
        except ValueError:
            print("You didn't provide a number")
            print()

    command = f'powershell.exe Expand-Archive -Path {os.path.join(backup_file)} -DestinationPath {os.path.dirname(dir_path)}'

    shutil.rmtree(dir_path)

    if do_in_cmd(command):
        return

if __name__ == "__main__":
    restore()