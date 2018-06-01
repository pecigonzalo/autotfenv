import glob
import subprocess
import sys

import hcl


def findTerraformVersion():
    for file in glob.glob("./*.tf"):
        with open(file, 'r') as tfile:
            try:
                obj = hcl.load(tfile)
            except ValueError:
                return

            terraform = obj.get('terraform')
            if terraform:
                version = findVersion(terraform)
                if version:
                    return version


def findVersion(terraform):
    return terraform.get('required_version')


def findRunningVersion():
    cmd = subprocess.run(['terraform', 'version'], stdout=subprocess.PIPE)
    version = cmd.stdout.splitlines()[0].split()[1][1:].decode('utf-8')
    return version


def switchToVersion(version):
    cmd = subprocess.run(['tfenv', 'use', version], stdout=subprocess.PIPE)
    cmd.check_returncode()


def main():
    required_version = findTerraformVersion()
    if required_version:
        required_version = required_version.split(',')[0].split(' ')[1]
    else:
        return

    running_version = findRunningVersion()

    if required_version and running_version != required_version:
        print("Required: " + required_version)
        print("Runing: " + running_version)
        response = input("Switch to required version? (y/N) ")
        if response == 'y':
            switchToVersion(required_version)


sys.exit(main())
