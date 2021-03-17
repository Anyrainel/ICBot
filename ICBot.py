import json
import os
import shutil
import shlex
import webbrowser
import subprocess
from pathlib import Path
from datetime import datetime


def logtime():
    return datetime.now().strftime(r'%Y%m%d%H%M%S')


def run(command, name):
    print(">>> [%s]" % name, command)
    ret = subprocess.call(shlex.split(command))
    print(">>> [%s] finished with return code" % name, ret)


def main(setting):
    rootdir = Path(__file__).parent.absolute()
    airtest = os.path.join(
        setting['AirtestIDEDirectory'], 'AirtestIDE', 'AirtestIDE.exe')
    device = setting['DeviceAdbUrl']
    params = '&&'.join([
        'cap_method=JAVACAP',
        'ori_method=MINICAPORI',
        'touch_method=MINITOUCH',
    ])
    logdir = os.path.join(rootdir, setting['LogReportDirectory'], logtime())
    main = os.path.join(rootdir, 'main.air')

    if setting['CleanUpLogBeforeRun']:
        shutil.rmtree(logdir)
    os.makedirs(logdir, exist_ok=True)

    run_command = '"%s" runner "%s" ' % (airtest, main)
    run_command += ' --device "%s?%s" ' % (device, params)
    run_command += ' --log "%s" ' % (logdir)
    run(run_command, 'Runner')

    if setting['ShowLogReportAfterRun']:
        loghtml = os.path.join(logdir, 'log.html')
        report_command = '"%s" reporter "%s" ' % (airtest, main)
        report_command += ' --log_root "%s" ' % logdir
        report_command += ' --outfile "%s" ' % loghtml
        run(report_command, 'Reporter')
        if os.path.isfile(loghtml):
            webbrowser.open(loghtml, new=2)
        else:
            print(">>> Cannot find log HTML, runner or reporter has errors.")
    return


if __name__ == '__main__':
    if not os.path.isfile('settings.json'):
        raise Exception('Settings are missing. Copy settings.default.json to settings.json and adjust.')
    with open('settings.json', 'r') as txt:
        builder = ""
        # Naively remove comments to avoid depending on other lib
        for linestr in txt.readlines():
            line = linestr.strip()
            if not line.startswith('//'):
                builder += line
        setting = json.loads(builder)
    main(setting)
