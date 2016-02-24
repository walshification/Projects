from sniffer.api import *

import termstyle


# customize the pass/fail colors
pass_fg_color = termstyle.green
pass_bg_color = termstyle.bg_default
fail_fg_color = termstyle.red
fail_bg_color = termstyle.bg_default


watch_paths = ['.']
clear = True


@file_validator
def py_files(filename):
    import os
    return (filename.endswith('.py') and
            not os.path.basename(filename).startswith('.'))


@runnable
def run_tests(*args):
    import os
    exit_code = os.system('env/bin/coverage run -m unittest discover ./tests')
    os.system('env/bin/coverage report -m')
    return exit_code == 0
