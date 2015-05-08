#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
############################
THIS TRANSFORMS ACRIS DATA INTO NETWORKX DATA
############################
"""

import sqlite3
conn = sqlite3.connect('db/real-property.db?mode=ro')
c = conn.cursor()

for row in c.execute("SELECT * FROM real_property_masters LIMIT 10"):
	print row

