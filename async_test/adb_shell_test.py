import subprocess

adb_path = r"D:\adbCmd\platform-tools\adb.exe"
def run():
    result = subprocess.run(["adb","shell","su -c 'stop mculog && echo -e \"log.set.loglevel.current 0\ncar.set.temp.config $id $value\" > /dev/ttyHS4'"],
                            capture_output=True, text=True, check=True)
    # if result.stderr:
    #     print(result.stderr)
    print(result.stdout)

run()