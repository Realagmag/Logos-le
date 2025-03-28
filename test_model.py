from model import filter_children, draw_password, Word
from model import IncorrectWordLengthError
import pytest
from io import StringIO


def test_filter_children():
    list_to_filter = [5, 4.5, '7', 2, 3, '4', [3, 4, 5]]
    assert filter_children(list_to_filter, int) == [5, 2, 3]
    assert filter_children(list_to_filter, float) == [4.5]
    assert filter_children(list_to_filter, str) == ['7', '4']
    assert filter_children(list_to_filter, list) == [[3, 4, 5]]
    assert filter_children(list_to_filter, dict) == []


def test_draw_password():
    data = "place\ngrace\ncards\n"
    file_name = StringIO(data)
    password, all_words = draw_password(file_name)
    assert type(password) is Word
    assert len(all_words) == 3


def test_draw_password_not_5_letters_word():
    data = "place\ngrace\ncar"
    file_name = StringIO(data)
    with pytest.raises(IncorrectWordLengthError):
        draw_password(file_name)


def test_create_Word():
    word = Word('pałac')
    assert word.name == 'pałac'
    assert type(word) is Word


def test_compare_words():
    word1 = Word('flame')
    word2 = Word('grace')
    colors = word1.compare(word2)
    assert colors == ['grey', 'grey', 'green', 'grey', 'green']


def test_compare_words_addtional_yellows():
    word1 = Word('abcde')
    word2 = Word('dddaa')
    colors = word1.compare(word2)
    assert colors == ['#FFAE20', 'grey', 'grey', '#FFAE20', 'grey']


def test_compare_words_green_has_prio():
    word1 = Word('abcdd')
    word2 = Word('dddde')
    colors = word1.compare(word2)
    assert colors == ['#FFAE20', 'grey', 'grey', 'green', 'grey']
