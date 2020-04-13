import argparse
from pyproject.checker import check

ap = argparse.ArgumentParser()
ap.add_argument('-p', '--project', required=True, help='Root folder of your Xcode project')
ap.add_argument('-i', '--input', required=True, help='Full path of ".strings" file containing keys you want to check')
ap.add_argument('-fw', '--folder_whitelist', required=False, nargs='+', type=str,
                help='Folder whitelist. i.e "-fw Classes Models ViewControllers"')
ap.add_argument('-fb', '--folder_blacklist', required=False, nargs='+', type=str,
                help='Folder blacklist. i.e "-fw Pods ExtLibs"')
ap.add_argument('-ew', '--extension_whitelist', required=False, nargs='+', type=str,
                help='Extension whitelist. i.e "-fw .swift .h .m"')
ap.add_argument('-eb', '--extension_blacklist', required=False, nargs='+', type=str,
                help='Extension blacklist. i.e "-fw .strings .slp"')
args = ap.parse_args()


def main(shellArgs):
    project = shellArgs.project
    inputFile = shellArgs.input
    fw = shellArgs.folder_whitelist
    fb = shellArgs.folder_blacklist
    ew = shellArgs.extension_whitelist
    eb = shellArgs.extension_blacklist

    check(inputFile, project, ew, eb, fw, fb)


if __name__ == "__main__":
    main(args)
