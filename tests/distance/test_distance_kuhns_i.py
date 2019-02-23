# -*- coding: utf-8 -*-

# Copyright 2019 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.tests.distance.test_distance_kuhns_i.

This module contains unit tests for abydos.distance.KuhnsI
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import KuhnsI


class KuhnsITestCases(unittest.TestCase):
    """Test KuhnsI functions.

    abydos.distance.KuhnsI
    """

    cmp = KuhnsI()
    cmp_no_d = KuhnsI(alphabet=1)

    def test_kuhns_i_sim(self):
        """Test abydos.distance.KuhnsI.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), 0.0)
        self.assertEqual(self.cmp.sim('a', ''), -6.507705122865472e-06)
        self.assertEqual(self.cmp.sim('', 'a'), -6.507705122865472e-06)
        self.assertEqual(self.cmp.sim('abc', ''), -1.3015410245730944e-05)
        self.assertEqual(self.cmp.sim('', 'abc'), -1.3015410245730944e-05)
        self.assertEqual(self.cmp.sim('abc', 'abc'), 0.0101780508121616)
        self.assertEqual(self.cmp.sim('abcd', 'efgh'), -3.2538525614327364e-05)

        self.assertAlmostEqual(self.cmp.sim('Nigel', 'Niall'), 0.007614015)
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Nigel'), 0.007614015)
        self.assertAlmostEqual(self.cmp.sim('Colin', 'Coiln'), 0.007614015)
        self.assertAlmostEqual(self.cmp.sim('Coiln', 'Colin'), 0.007614015)
        self.assertAlmostEqual(
            self.cmp.sim('ATCAACGAGT', 'AACGATTAG'), 0.017788812
        )

        # Tests with alphabet=1 (no d factor)
        self.assertEqual(self.cmp_no_d.sim('', ''), 0.0)
        self.assertEqual(self.cmp_no_d.sim('a', ''), -1.0)
        self.assertEqual(self.cmp_no_d.sim('', 'a'), -1.0)
        self.assertEqual(self.cmp_no_d.sim('abc', ''), -0.5)
        self.assertEqual(self.cmp_no_d.sim('', 'abc'), -0.5)
        self.assertEqual(self.cmp_no_d.sim('abc', 'abc'), 1.0)
        self.assertEqual(self.cmp_no_d.sim('abcd', 'efgh'), -0.2)

        self.assertAlmostEqual(
            self.cmp_no_d.sim('Nigel', 'Niall'), 0.3703703704
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim('Niall', 'Nigel'), 0.3703703704
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim('Colin', 'Coiln'), 0.3703703704
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim('Coiln', 'Colin'), 0.3703703704
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG'), 0.7857142857
        )

    def test_kuhns_i_dist(self):
        """Test abydos.distance.KuhnsI.dist."""
        # Base cases
        self.assertEqual(self.cmp.dist('', ''), 1.0)
        self.assertEqual(self.cmp.dist('a', ''), 1.0000065077051228)
        self.assertEqual(self.cmp.dist('', 'a'), 1.0000065077051228)
        self.assertEqual(self.cmp.dist('abc', ''), 1.0000130154102458)
        self.assertEqual(self.cmp.dist('', 'abc'), 1.0000130154102458)
        self.assertEqual(self.cmp.dist('abc', 'abc'), 0.9898219491878384)
        self.assertEqual(self.cmp.dist('abcd', 'efgh'), 1.0000325385256144)

        self.assertAlmostEqual(self.cmp.dist('Nigel', 'Niall'), 0.992385985)
        self.assertAlmostEqual(self.cmp.dist('Niall', 'Nigel'), 0.992385985)
        self.assertAlmostEqual(self.cmp.dist('Colin', 'Coiln'), 0.992385985)
        self.assertAlmostEqual(self.cmp.dist('Coiln', 'Colin'), 0.992385985)
        self.assertAlmostEqual(
            self.cmp.dist('ATCAACGAGT', 'AACGATTAG'), 0.982211188
        )

        # Tests with alphabet=1 (no d factor)
        self.assertEqual(self.cmp_no_d.dist('', ''), 1.0)
        self.assertEqual(self.cmp_no_d.dist('a', ''), 2.0)
        self.assertEqual(self.cmp_no_d.dist('', 'a'), 2.0)
        self.assertEqual(self.cmp_no_d.dist('abc', ''), 1.5)
        self.assertEqual(self.cmp_no_d.dist('', 'abc'), 1.5)
        self.assertEqual(self.cmp_no_d.dist('abc', 'abc'), 0.0)
        self.assertEqual(self.cmp_no_d.dist('abcd', 'efgh'), 1.2)

        self.assertAlmostEqual(
            self.cmp_no_d.dist('Nigel', 'Niall'), 0.6296296296
        )
        self.assertAlmostEqual(
            self.cmp_no_d.dist('Niall', 'Nigel'), 0.6296296296
        )
        self.assertAlmostEqual(
            self.cmp_no_d.dist('Colin', 'Coiln'), 0.6296296296
        )
        self.assertAlmostEqual(
            self.cmp_no_d.dist('Coiln', 'Colin'), 0.6296296296
        )
        self.assertAlmostEqual(
            self.cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG'), 0.2142857143
        )


if __name__ == '__main__':
    unittest.main()