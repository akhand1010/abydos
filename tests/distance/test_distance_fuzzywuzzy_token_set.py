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

"""abydos.tests.distance.test_distance_fuzzywuzzy_token_set.

This module contains unit tests for abydos.distance.FuzzyWuzzyTokenSet
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import FuzzyWuzzyTokenSet


class FuzzyWuzzyTokenSetTestCases(unittest.TestCase):
    """Test FuzzyWuzzyTokenSet functions.

    abydos.distance.FuzzyWuzzyTokenSet
    """

    cmp = FuzzyWuzzyTokenSet()

    def test_fuzzywuzzy_token_set_sim(self):
        """Test abydos.distance.FuzzyWuzzyTokenSet.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), 1.0)
        self.assertEqual(self.cmp.sim('a', ''), 1.0)
        self.assertEqual(self.cmp.sim('', 'a'), 1.0)
        self.assertEqual(self.cmp.sim('abc', ''), 1.0)
        self.assertEqual(self.cmp.sim('', 'abc'), 1.0)
        self.assertEqual(self.cmp.sim('abc', 'abc'), 1.0)
        self.assertEqual(self.cmp.sim('abcd', 'efgh'), 0.3333333333333333)

        self.assertAlmostEqual(self.cmp.sim('Nigel', 'Niall'), 0.6666666667)
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Nigel'), 0.6666666667)
        self.assertAlmostEqual(self.cmp.sim('Colin', 'Coiln'), 0.8333333333)
        self.assertAlmostEqual(self.cmp.sim('Coiln', 'Colin'), 0.8333333333)
        self.assertAlmostEqual(
            self.cmp.sim('ATCAACGAGT', 'AACGATTAG'), 0.6666666667
        )

    def test_fuzzywuzzy_token_set_dist(self):
        """Test abydos.distance.FuzzyWuzzyTokenSet.dist."""
        # Base cases
        self.assertEqual(self.cmp.dist('', ''), 0.0)
        self.assertEqual(self.cmp.dist('a', ''), 0.0)
        self.assertEqual(self.cmp.dist('', 'a'), 0.0)
        self.assertEqual(self.cmp.dist('abc', ''), 0.0)
        self.assertEqual(self.cmp.dist('', 'abc'), 0.0)
        self.assertEqual(self.cmp.dist('abc', 'abc'), 0.0)
        self.assertEqual(self.cmp.dist('abcd', 'efgh'), 0.6666666666666667)

        self.assertAlmostEqual(self.cmp.dist('Nigel', 'Niall'), 0.3333333333)
        self.assertAlmostEqual(self.cmp.dist('Niall', 'Nigel'), 0.3333333333)
        self.assertAlmostEqual(self.cmp.dist('Colin', 'Coiln'), 0.1666666667)
        self.assertAlmostEqual(self.cmp.dist('Coiln', 'Colin'), 0.1666666667)
        self.assertAlmostEqual(
            self.cmp.dist('ATCAACGAGT', 'AACGATTAG'), 0.3333333333
        )


if __name__ == '__main__':
    unittest.main()