# 6 kyu: https://www.codewars.com/kata/football-yellow-and-red-cards/train/python
import re

import pytest


def men_still_standing(cards):
    if len(cards) == 0:
        return 11, 11
    else:
        a_team = [0] * 11
        b_team = [0] * 11
        a_players_left, b_players_left = 11, 11
        card_extractor = re.compile(r'([AB])(\d+)([YR])')
        for card in cards:
            match = card_extractor.match(card)
            team, player, color = match.groups()
            if team == 'A':
                a_players_left = update_referee_notebook(a_players_left, a_team, int(player))
            else:
                b_players_left = update_referee_notebook(b_players_left, b_team, int(player))
        return a_players_left, b_players_left


def update_referee_notebook(players_left, team, player):
    index = player - 1
    team[index] = team[index] + 1
    if team[index] == 2:
        players_left -= 1
    return players_left


def test_no_cards_given():
    assert men_still_standing([]) == (11, 11)


@pytest.mark.parametrize('cards, expected_result', [(['A1Y', 'A1Y'], (10, 11)),
                                                    (['B1Y', 'B1Y'], (11, 10))])
def test_two_yellow_cards_for_same_player_in_same_team(cards, expected_result):
    assert men_still_standing(cards) == expected_result
