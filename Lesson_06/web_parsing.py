from urllib.parse import urlparse


def parse_parameters(query: str) -> dict:
    """
    This function can parse parameters passed by the user.
    Accepts an url with or without parameters as input, returns a
    dictionary with parameters or empty.
    :param query: Some URL
    :return: Dictionary with parameters or empty.
    """
    html = urlparse(query)
    param_parse = html.query
    if param_parse:
        params = dict(i.split('=') for i in param_parse.split('&'))
    else:
        params = dict(param_parse)

    return params


def parse_cookies(query: str) -> dict:
    """
    This function can parse cookies passed by the user.
    Accepts a cookies as input, returns a dictionary with parameters or empty.
    :param query: Some cookies
    :return: Dictionary with parameters or empty.
    """
    params = {}
    for item in query.split(';'):
        params.update(i.split('=', 1) for i in item.split())
    print(params)

    return params


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('https://www.python.org?') == {}
    assert parse_parameters(
        'https://docs.python.org/3?name=ferret&color=purple') == {
               'name': 'ferret', 'color': 'purple'}
    assert parse_parameters(
        'https://www.python.org/doc/?name=ferret') == {
               'name': 'ferret'}
    assert parse_parameters(
        'https://www.python.org/doc/?name=ferret&color=purple&login=admin') == {
               'name': 'ferret', 'color': 'purple', 'login': 'admin'}
    assert parse_parameters(
        'https://www.python.org/doc/?one=1&2=two') == {
               'one': '1', '2': 'two'}

    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
    assert parse_cookies('__utma=32101439.917134183.1636909172.1636909172.'
                         '1636909172.1; __utmz=32101439.1636909172.1.1.utmcsr='
                         'duckduckgo.com|utmccn=(referral)|utmcmd=referral|'
                         'utmcct=/') == \
           {'__utma': '32101439.917134183.1636909172.1636909172.1636909172.1',
            '__utmz': '32101439.1636909172.1.1.utmcsr=duckduckgo.com|utmccn='
                      '(referral)|utmcmd=referral|utmcct=/'}
    assert parse_cookies('__utma=32101439.917134183.1636909172.1637010818.'
                         '1637015905.3; __utmz=32101439.1636909172.1.1.utmcsr='
                         'duckduckgo.com|utmccn=(referral)|utmcmd=referral|'
                         'utmcct=/; __utmc=32101439;'
                         '__utmb=32101439.2.10.1637015905; __utmt=1') == \
           {'__utma': '32101439.917134183.1636909172.1637010818.1637015905.3',
            '__utmz': '32101439.1636909172.1.1.utmcsr=duckduckgo.com|utmccn='
                      '(referral)|utmcmd=referral|utmcct=/',
            '__utmc': '32101439', '__utmb': '32101439.2.10.1637015905',
            '__utmt': '1'}
    assert parse_cookies('_gcl_au=1.1.1269769116.1636900111;'
                         'PHPSESSID=mvrknprt8eu3p3dts0r5ab6rh2') == \
           {'_gcl_au': '1.1.1269769116.1636900111',
            'PHPSESSID': 'mvrknprt8eu3p3dts0r5ab6rh2'}
