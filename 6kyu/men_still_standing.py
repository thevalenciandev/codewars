# 6 kyu: https://www.codewars.com/kata/football-yellow-and-red-cards/train/python
import re
import pytest


def men_still_standing(cards):
    if len(cards) == 0:
        return 11, 11
    else:
        a_team = [0] * 11
        b_team = [0] * 11
        a_players, b_players = 11, 11
        card_extractor = re.compile(r'([AB])(\d+)([YR])')
        for card in cards:
            match = card_extractor.match(card)
            team, player, color = match.groups()
            if team == 'A':
                index = int(player) - 1
                a_team[index] = a_team[index] + 1
                if a_team[index] == 2:
                    a_players -= 1
        return a_players, b_players


def test_no_cards_given():
    assert men_still_standing([]) == (11, 11)


@pytest.mark.parametrize('cards, expected_result', [(['A1Y', 'A1Y'], (10, 11))])
def test_two_yellow_cards_for_same_player_in_same_team(cards, expected_result):
    assert men_still_standing(cards) == expected_result
