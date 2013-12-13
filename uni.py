DEFAULT_ENCODING = 'utf-8'

def decodestr(_str, encoding=DEFAULT_ENCODING):
    '''byte[] -> unicode'''
    assert isinstance(_str,str), 'arg not str'
    return _str.decode(encoding)

def encodeunicode(_uni,encoding=DEFAULT_ENCODING):
    '''unicode -> byte[]'''
    assert isinstance(_uni,unicode), 'arg not unicode'
    return _uni.encode(encoding)

if __name__ == '__main__':
    my_string = 'Hello World'
    print my_string
    print type(my_string)
    print len(my_string)

    my_unicode = u'Copyright (\u00A9)'
    print my_unicode
    print type(my_unicode)
    print len(my_unicode)

    my_unicode_encoded = my_unicode.encode('utf-8')
    print my_unicode_encoded
    print type(my_unicode_encoded)
    print len(my_unicode_encoded)

    my_unicode_encoded_decoded = my_unicode_encoded.decode('utf-8')
    print my_unicode_encoded_decoded
    print type(my_unicode_encoded_decoded)
    print len(my_unicode_encoded_decoded)

    try:
        my_unicode.encode('ascii')
    except UnicodeEncodeError,e:
        print e
    
    print my_unicode.encode('ascii','replace')
    print my_unicode.encode('ascii','xmlcharrefreplace')
    print my_unicode.encode('ascii','ignore')

    try:
        my_unicode_encoded.decode('ascii')
    except UnicodeDecodeError,e:
        print e

    import sys
    print sys.getdefaultencoding()
    my_result = u"Hello" + " World"
    print my_result,type(my_result)
    my_result2 = u'Hello' + " World".decode(sys.getdefaultencoding())
    print my_result2,type(my_result2)

    p1_u = u'Hello '
    p2_u = u' Copyright (\u00A9)'
    p2_s = p2_u.encode('utf-8')
    try:
        p1_u + p2_s #p1_u + p2_s.decode('ascii') #default
    except UnicodeDecodeError,e:
        print e
    #sys.setdefaultencoding('utf-8')
    #p3_u = p1_u + p2_s
    #print p3_u,type(p3_u)
