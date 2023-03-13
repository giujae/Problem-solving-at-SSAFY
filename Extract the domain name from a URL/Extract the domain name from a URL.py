def domain_name(url):
    lst = list(url.split('/'))
    result = list((''.join(lst)).split('.'))
    for i in range(len(result)):
        if 'www' in result[i]:
            return result[1]
        else:
            if 'https' in result[i]:
                return result[i][6:]
            elif 'http' in result[i]:
                return result[i][5:]
            else:
                return result[i]