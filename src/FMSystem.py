import struct
import PyPDF2
def file_type(file_path):
    file_type = {
        '005374616e646172' : 'AIB', 'FFD8FF' : 'JPEG/JPG',
        '89504E47' : 'PNG', '47494638' : 'GIF',
        '49492A00' : 'TIFF', '424D' : 'BMP',
        '41433130': 'DWG', '38425053': 'PSD',
        '49492a': '50d 60d CR2', '7B5C727466': 'Rich Text Format (rtf)',
        '3C3F786D6C': 'XML', '68746D6C3E': 'HTML',
        '44656C69766572792D646174653A': 'Email', 'CFAD12FEC5FD746F': 'DBX',
        '2142444E': 'PST', 'D0CF11E0': 'XLS.OR.DOC',
        '5374616E64617264204A': 'MDB', 'FF575043': 'WPD',
        '252150532D41646F6265': 'EPS.OR.PSE', '255044462D312E': 'PDF',
        'AC9EBD8F': 'QDF', 'E3828596': 'PWL',
        '504B0304': 'ZIP', '52617221': 'RAR',
        '57415645': 'WAV', '41564920': 'AVI',
        '2E7261FD': 'RAM', '2E524D46': 'RM',
        '000001BA': 'MPG', '000001B3': 'MPG',
        '6D6F6F76': 'MOV', '3026B2758E66CF11': 'ASF',
        '4D546864': 'MID', '617364B0' : 'TXT'
    }
    def bytes2hex(bytes):
        hex_str = u""
        for i in range(len(bytes)):
            t = u"%x" % bytes[i]
            if len(t) % 2:
                hex_str += u"0"
            hex_str += t
        return hex_str.upper()

    with open(file_path, 'rb') as bin_file:
        hex_str = bytes2hex(struct.unpack_from("B" * 20, bin_file.read(20)))
        for type in file_type:
            if type in hex_str:
                return file_type[type]

def is_valid_pdf(file_path):
    res = True
    try:
        reader = PyPDF2.PdfFileReader(file_path)
        if reader.getNumPages() < 1:
            res = False
    except:
        res = False

    return res

