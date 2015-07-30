# -*- coding: utf-8 -*-

# Most of the code is taken from:
# http://stackoverflow.com/questions/191359/how-to-convert-a-file-to-utf-8-in-python

import os
import codecs

def binary_converter(   srcFileName, 
                        dstFileName=None, 
                        srcEncoding='cp1251', 
                        dstEncoding='utf-8',
                        BLOCKSIZE = 1048576
                    ):
    srcEqualsDst = False
    if not dstFileName:
        srcEqualsDst = True
        dstFileName = '%s.tmp' % srcFileName

    print "Converting '%s'..." % srcFileName
    with codecs.open(srcFileName, 'r', srcEncoding) as sourceFile:
        with codecs.open (dstFileName, 'w', dstEncoding) as targetFile:
            while 1:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)

    if srcEqualsDst:
        os.remove(srcFileName)
        os.rename(dstFileName, srcFileName)
