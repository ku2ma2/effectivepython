"""
項目36: subprocessを使って子プロセスを管理する

Use subprocess to Manage Child Processes

- 

"""

import subprocess
import time


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc


if __name__ == "__main__":
    start = time.time()
    procs = []
    for _ in range(10):
        proc = run_sleep(0.1)
        procs.append(proc)

    for proc in procs:
        proc.communicate()
    end = time.time()
    print('Finish in %.3f seconds' % (end - start))
