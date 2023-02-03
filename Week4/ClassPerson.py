#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 09:25:07 2023

@author: nunoa
"""


class Person:
    '''A class person with name, address and contry'''

    def __init__(self, full_name: str, addr: str, country: str):
        self.name = full_name
        self.addr = addr
        self.country = country

    def first_name(self):
        names = self.name.split(" ")
        return names[0]

    def last_name(self):
        names = self.name.split(" ")
        return names[-1]

    def who_am_i(self):
        fn = self.first_name()
        ln = self.last_name()
        a = self.addr
        c = self.country
        str = f"I am {ln}, {fn} {ln}. I live in {a}. I am from {c}"
        return str


def test_Person():
    pJB = Person("James Bond", "London, UK", "UK")
    pRH = Person("Robin Hood", "Nottingham, UK", "UK")
    pLM = Person("Lethiwe Mwendwa", "Nottingham, UK", "Keyna")
    pTM = Person("Thomas Frewer", "Nottingham, UK", "UK")
    pNA = Person("Nuno Rodrigues Amalio", "Nottingham, UK", "Portugal")
    pJE = Person("Jonathan Alexander East", "Nottingham, UK", "UK")
    pTN = Person("Taboka Ndlovu", "Nottingham, UK", "Zimbabwe")
    people = [pJB, pRH, pLM, pTM, pNA, pJE, pTN]

    print("My 'Person' objects are:")
    for p in people:
        print(p.who_am_i())
