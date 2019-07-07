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
            team, player, card_color = match.groups()
            if team == 'A':
                a_players_left = update_referee_notebook(a_players_left, a_team, int(player), card_color)
            else:
                b_players_left = update_referee_notebook(b_players_left, b_team, int(player), card_color)
            if a_players_left == 6 or b_players_left == 6:
                return a_players_left, b_players_left

        return a_players_left, b_players_left


def update_referee_notebook(players_left, team, player, card_color):
    index = player - 1
    if team[index] >= 2:  # ignore red card if player is already out
        return players_left
    team[index] = team[index] + (1 if card_color == 'Y' else 2)
    if team[index] >= 2:
        players_left -= 1
    return players_left


def test_no_cards_given():
    assert men_still_standing([]) == (11, 11)


@pytest.mark.parametrize('cards, expected_result', [(['A1Y', 'A1Y'], (10, 11)),
                                                    (['B1Y', 'B1Y'], (11, 10))])
def test_two_yellow_cards_for_same_player_in_same_team(cards, expected_result):
    assert men_still_standing(cards) == expected_result


@pytest.mark.parametrize('cards, expected_result', [(['A1Y', 'A1R'], (10, 11)),
                                                    (['B1Y', 'B1R'], (11, 10))])
def test_yellow_then_red_for_same_player_is_red(cards, expected_result):
    assert men_still_standing(cards) == expected_result


@pytest.mark.parametrize('cards, expected_result', [(['A1R', 'A1R', 'A1R'], (10, 11)),
                                                    (['B1R', 'B1R', 'B1R'], (11, 10))])
def test_more_than_one_red_for_same_player_is_ignored(cards, expected_result):
    assert men_still_standing(cards) == expected_result


@pytest.mark.parametrize('cards, expected_result', [(['A11R'], (10, 11)),
                                                    (['B11R'], (11, 10)),
                                                    (['A11R', 'B11R'], (10, 10))])
def test_red_cards_only(cards, expected_result):
    assert men_still_standing(cards) == expected_result


@pytest.mark.parametrize('cards, expected_result', [(['A11R', 'A10R', 'A9R', 'A8R', 'A7R', 'A6R', 'A5R'], (6, 11)),
                                                    (['B11R', 'B10R', 'B9R', 'B8R', 'B7R', 'B6R', 'B5R'], (11, 6))])
def test_red_cards_are_capped_to_six(cards, expected_result):
    assert men_still_standing(cards) == expected_result
