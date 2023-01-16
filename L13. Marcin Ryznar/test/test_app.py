from app import extract_sentiment
from app import text_contain_word
from app import hello
import pytest
from app import quicksort
from timeit import timeit
import random


def test_hello():
    got = hello("Marcin")
    want = "Hello Marcin"

    assert got == want



testdata1 = ["I think today will be a great day"]

@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0

testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output



listpos = [i for i in range(500)]
listlos = random.sample(range(0, 500), 500)
listrow = 500*[1]

def test_quicksort():  
    t1_quick = timeit("quicksort(listpos)", number=1000, globals=globals())/1000
    t2_quick = timeit("quicksort(listlos)", number=1000, globals=globals())/1000
    t3_quick = timeit("quicksort(listrow)", number=1000, globals=globals())/1000
    return t1_quick, t2_quick, t3_quick



