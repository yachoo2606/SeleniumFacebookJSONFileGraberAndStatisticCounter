import os
import zipfile
import MessengerCounter as mc


def main():
    jsonZips = {}

    for file in os.listdir(os.getcwd()):
        if "facebook" in file:
            found = False
            jsonNumbers = 0
            zip = zipfile.ZipFile(file)
            print(file)
            for name in zip.namelist():
                if "json" in name:
                    jsonNumbers += 1
                    print(f"\t{name}")
                    found = True
                    continue
            jsonZips[file] = jsonNumbers
            zip.close()
            if not found:
                os.remove(file)
    sortedFiles = sorted(jsonZips.items(), key=lambda x: x[1], reverse=True)

    print(sortedFiles[0])

    for file in os.listdir(os.getcwd()):
        if "facebook" in file:
            if file != sortedFiles[0][0]:
                os.remove(file)

    for file in os.listdir(os.getcwd()):
        if "facebook" in file:
            os.rename(file, "facebook.zip")

    mc.set_source('facebook.zip')
    mc.count(chars=True)
    data = mc.get_data()
    print(data)
    mc.statistics(*data)


if __name__ == '__main__':
    main()
