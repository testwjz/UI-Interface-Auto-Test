import os

from config.readConfig import ReadConfig, dirpath


def get_case_data():
    params = []
    for i in __get_listfile():
        params.extend(__get_datalist(i))
    return params


def __get_datalist(fileName):
    readconfig = ReadConfig(os.path.join(dirpath, "interface", fileName))
    datalist = [(readconfig.get('DATA', 'Data' + str(i)), readconfig.get('ASSERT', 'assert' + str(i)),
                 readconfig.get('HTTP', 'url'), readconfig.get('HTTP', 'header')) for i in
                range(1, (1 + int(readconfig.get('HTTP', 'dataNum'))))]
    return datalist


def __get_listfile():
    path = os.listdir(os.path.join(dirpath, "interface"))
    listfile = [i for i in path if '.ini' in i]
    return listfile
