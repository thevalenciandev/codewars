import re

import pytest

number_matcher = re.compile(r'^(.*?)(\d*)$')


def increment_string(string):
    match = number_matcher.match(string)
    if match:
        prefix = match.group(1)
        number = match.group(2)
        return prefix + '1' if number == '' else prefix + str(int(number) + 1).zfill(len(number))


@pytest.mark.parametrize('string,expected', [('', '1'),
                                             ('foo', 'foo1')])
def test_no_number_appends_one(string, expected):
    assert increment_string(string) == expected


@pytest.mark.parametrize('string,expected', [('foo1', 'foo2'),
                                             ('foo9', 'foo10')])
def test_increment_number_if_exists(string, expected):
    assert increment_string(string) == expected


@pytest.mark.parametrize('string,expected', [('foobar00', 'foobar01'),
                                             ('foobar001', 'foobar002'),
                                             ('foobar099', 'foobar100')])
def test_increment_number_with_leading_zeros(string, expected):
    assert increment_string(string) == expected


@pytest.mark.parametrize('string,expected', [('1', '2')])
def test_only_number(string, expected):
    assert increment_string(string) == expected


def test_random():
    assert increment_string('326GH+s?1102l<Gu1A854207J,M$&c6060000010') == '326GH+s?1102l<Gu1A854207J,M$&c6060000011'
