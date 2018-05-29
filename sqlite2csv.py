#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2018 Matteo Alessio Carrara <sw.matteoac@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sqlite3
import csv

class Exporter:
    def __init__(self, dbname, expdir=None):
        self._dbname = dbname
        self._expdir = expdir + "/" if expdir != None else "./"
        self._db = sqlite3.connect(self._dbname)
        self._c = self._db.cursor()

    def run(self, table, columns, fname=None):
        fname = table if fname == None else fname
        with open("%s/%s.csv" % (self._expdir, fname), "w") as of:
            self._c.execute("SELECT %s FROM %s" % (columns, table))
            cw = csv.writer(of)
            cw.writerow([x.strip() for x in columns.split(',')])
            cw.writerows(self._c.fetchall())