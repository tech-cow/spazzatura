#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import *
from statistics import *
from collections import *

def roulette_wheel_bad():
    '''using choice()
    return:
        list: ['black', 'black', 'black', 'red', 'red', 'red']
        counter =  Counter({'black': 3, 'red': 3})
    '''
    population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
    l1 = [choice(population) for i in range(6)]
    c1 = Counter(l1)

    '''using choices() return: same as choice() but easier'''
    l2 = choices(population, k=6)
    c2 = Counter(l2)

def roulette_wheel_good():
    '''using choices() with weight'''
    c = Counter(choices(['red', 'black', 'green'], [18, 18, 2], k=6))
    print(c)


def deal_card():
    '''Deal 20 playing cards without replacement
        technique: counter, elements, sample, list.count
    '''
    deck = Counter(tens=16, low=36)
    deck = list(deck.elements()) #change element to a list of integer
    deal = sample(deck, 20) # randomly select 20 element from an array
    c = Counter(deal)

def bias_coin():
    '''5 or more heads from 7 spins of a biased coin
        technique: lambda, choies, list.count
    '''
    population = ['heads', 'tails']
    cumwgt = [0.60 , 1.00] #bias by 60%
    trial = lambda : choices(population, cumwgt, k=7).count('heads') >= 5
    n = 100000
    print(sum(trial() for i in range(n))/n)



if __name__ == '__main__':
    # roulette_wheel_good()
    # deal_card()
    bias_coin()
