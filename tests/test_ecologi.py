import requests_mock
from ecologi import Ecologi

ecologi = Ecologi()


def test_me():
    with requests_mock.Mocker() as m:
        m.get(
            url='https://public.ecologi.com/users/owenvoke/impact',
            json={"trees": 1733, "carbonOffset": 41.05}
        )

        impact = ecologi.impact('owenvoke')

        assert type(impact) == dict
        assert impact.get('trees') == 1733
        assert impact.get('carbonOffset') == 41.05


def test_authenticated():
    with requests_mock.Mocker() as m:
        m.get(
            url='https://public.ecologi.com/users/owenvoke/impact',
            json={"trees": 1733, "carbonOffset": 41.05}
        )

        user_exists = ecologi.user_exists('owenvoke')

        assert type(user_exists) == bool
        assert user_exists is True


def test_not_authenticated():
    with requests_mock.Mocker() as m:
        m.get(
            url='https://public.ecologi.com/users/non-existant-user/impact',
            status_code=404,
            json={"responseCode": "Not Found Exception"}
        )

        me = ecologi.user_exists('non-existant-user')

        assert type(me) == bool
        assert me is False
