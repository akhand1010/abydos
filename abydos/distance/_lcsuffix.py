# -*- coding: utf-8 -*-

# Copyright 2018 by Christopher C. Little.
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

"""abydos.distance._lcsuffix.

Longest common suffix
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from os.path import commonprefix

from ._lcprefix import LCPrefix

__all__ = ['LCSuffix']


class LCSuffix(LCPrefix):
    """Longest common suffix.

    .. versionadded:: 0.4.0
    """

    def lcsuffix(self, strings):
        """Return the longest common suffix of a list of strings.

        Longest common suffix (LCSuffix).

        Parameters
        ----------
        strings : list of strings
            Strings for comparison

        Returns
        -------
        str
            The longest common suffix

        Examples
        --------
        >>> sfx = LCSuffix()
        >>> sfx.lcsuffix('cat', 'hat')
        'at'
        >>> sfx.lcsuffix('Niall', 'Neil')
        'N'
        >>> sfx.lcsuffix('aluminum', 'Catalan')
        'al'
        >>> sfx.lcsuffix('ATCG', 'TAGC')
        'A'

        .. versionadded:: 0.4.0

        """
        strings = [s[::-1] for s in strings]
        return commonprefix(strings)[::-1]

    def dist_abs(self, src, tar, *args):
        """Return the length of the longest common suffix of the strings.

        Parameters
        ----------
        src : str
            Source string for comparison
        tar : str
            Target string for comparison
        *args : strs
            Additional strings for comparison

        Raises
        ------
        ValueError
            All arguments must be of type str

        Returns
        -------
        int
            The length of the longest common suffix

        Examples
        --------
        >>> sfx = LCSuffix()
        >>> sfx.dist_abs('cat', 'hat')
        0
        >>> sfx.dist_abs('Niall', 'Neil')
        1
        >>> sfx.dist_abs('aluminum', 'Catalan')
        0
        >>> sfx.dist_abs('ATCG', 'TAGC')
        0

        .. versionadded:: 0.4.0

        """
        strings = [src, tar]
        for arg in args:
            if isinstance(arg, str):
                strings.append(arg)
            else:
                raise ValueError('All arguments must be of type str')

        return len(self.lcsuffix(strings))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
