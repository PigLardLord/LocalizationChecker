import mmap
import os
import datetime


def getFilteredKeys(filename, keys: [str] = []):
    with open(filename) as fp:
        line = fp.readline()
        cnt = 1
        result = []
        while line:
            splittedLine = line.strip().split('"')
            if len(splittedLine) > 1:
                key = splittedLine[1]
                if key not in keys:
                    result.append(key)
            line = fp.readline()
            cnt += 1
    return result


def findUsedLocalizations(filename, key):
    hasValue = os.path.getsize(filename) > 0
    if hasValue:
        with open(filename, 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
            if s.find(key.encode()) != -1:
                return filename
    return None


def findInFolder(folder, key, extWhitelist, extBlacklist, folderWhitelist, folderBlacklist):
    resultArray = []

    for path, _, files in os.walk(folder):
        for fileName in files:
            ext = os.path.splitext(fileName)[1]
            isExtInWhitelist = checkWhitelist(ext, extWhitelist)
            isExtNotInBlacklist = checkBlacklist(ext, extBlacklist)

            isFolderInWhiteList = checkWhitelist(path, folderWhitelist)
            isFolderNotInBlacklist = checkBlacklist(path, folderBlacklist)

            if isExtInWhitelist and isFolderInWhiteList and isExtNotInBlacklist and isFolderNotInBlacklist:
                fullPath = os.path.join(path, fileName)
                result = findUsedLocalizations(fullPath, key)
                if result is not None:
                    resultArray.append(result)
    return resultArray


def checkBlacklist(element, blacklist):
    return True if blacklist is None else all(x not in element for x in blacklist)


def checkWhitelist(element, whitelist):
    return True if whitelist is None else any(x in element for x in whitelist)


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def check_for_keys(keys, projectPath, extWhitelist, extBlacklist, folderWhitelist, folderBlacklist):
    total = len(keys)

    outputFileName = "out/localizationLog {}.txt".format(datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S"))
    with open(outputFileName, 'a') as logFile:
        for i, key in enumerate(keys):

            print(" " * 200, end='\r')
            print('\nLooking for: ' + key)
            printProgressBar(i + 1, total, 'Progress:', 'Complete')
            results = findInFolder(projectPath, key, extWhitelist, extBlacklist, folderWhitelist, folderBlacklist)

            print("\033[F" + " " * 200)
            print(" " * 200, end='\r')
            if len(results) > 0:
                logFile.write("\nFound \"{}\" in:\n".format(key))
                print("Found \"{}\" in:".format(key))
                for result in results:
                    logFile.write("{}\n".format(result))
                    print(result)
            else:
                logFile.write("\nKey \"{}\" was not found! DELETE IT\n".format(key))
                print("Key \"{}\" was not found! DELETE IT".format(key))


def check(inputFile, projectPath, extWhitelist, extBlacklist, folderWhitelist, folderBlacklist):

    keys = getFilteredKeys(inputFile)
    check_for_keys(keys, projectPath, extWhitelist, extBlacklist, folderWhitelist, folderBlacklist)
