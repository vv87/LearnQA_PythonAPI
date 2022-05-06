import pytest

header1 = "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 " \
          "(KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"

expected1 = {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}
# AR:'platform': 'Mobile', 'browser': 'No', 'device': 'Unknown'

header2 = "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) " \
          "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"

expected2 = {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}
# Wrong AR: 'platform': 'Mobile', 'browser': 'No', 'device': 'iOS'

header3 = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

expected3 = {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}
# Wrong AR: 'platform': 'Unknown', 'browser': 'Unknown', 'device': 'Unknown'

header4 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
          "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"

expected4 = {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}
# AR: 'platform': 'Web', 'browser': 'Chrome', 'device': 'No'

header5 = "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) " \
          "Version/13.0.3 Mobile/15E148 Safari/604.1"

expected5 = {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
# Wrong AR: 'platform': 'Mobile', 'browser': 'No', 'device': 'Unknown'


@pytest.mark.parametrize('header, expected', [(header1, expected1),
                                              (header2, expected2),
                                              (header3, expected3),
                                              (header4, expected4),
                                              (header5, expected5)])
def test_parametrize(header, expected):
    from requests import get
    url_user_agent_check = get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                        headers={"User-Agent": header}).json()

    expected_result = str(expected)[1:-1]
    assert expected_result in str(url_user_agent_check), f'{expected_result} is not in {url_user_agent_check}'
