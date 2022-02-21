class FileFormats:
    DragFunc = 'Drag function (*.drg;*.snr;*.ardrg)'


class FileParse(object):
    def __init__(self):
        pass

    def open_format(self, fileFormat, fileName):
        if fileFormat == FileFormats.DragFunc:
            return self.open_df(fileName)

    def save_format(self, fileFormat, fileNeme, data, comment):
        if fileFormat == FileFormats.DragFunc:
            return self.save_df(fileNeme, data, comment)

    @staticmethod
    def open_df(fileName):
        try:
            with open(fileName, 'r') as f:
                lines = f.readlines()
            splited = [i.replace('\n', '').split('\t') for i in lines if '\t' in i]
            if not splited:
                splited = [i.replace('\n', '').split(' ') for i in lines if ' ' in i]
                splited = [i for i in splited if len(i) == 2]
            data = [(float(cd), float(v)) for v, cd in splited]
            data.sort(reverse=False)
            comment = lines[0]
            return data, comment
        except Exception('Wrong file data') as err:
            print(err)
            return None

    @staticmethod
    def save_df(fileName, data, comment):
        try:
            ret = []
            ret.append(comment)
            for (cd, v) in data:
                ret.append(f'{str(v)}\t{str(cd)}')
            ret = '\n'.join(ret)

            with open(fileName, 'w') as f:
                f.write(ret)
            return True
        except Exception as err:
            print(err)
        return False


if __name__ == '__main__':
    fp = FileParse()
    fp.open_format(
        FileFormats.DragFunc,
        r"C:\Users\Sergey\Documents\ArcherBC\Recent\323-lapua n559 11,7g (180gr) naturalis_radar.drg"
    )
