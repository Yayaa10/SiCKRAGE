#!/usr/bin/env python2

# Author: echel0n <echel0n@sickrage.ca>
# URL: https://sickrage.ca
#
# This file is part of SickRage.
#
# SickRage is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SickRage is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SickRage.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

import sys

import autoProcessTV

if len(sys.argv) < 2:
    print "No folder supplied - is this being called from SABnzbd?"
    sys.exit()
elif len(sys.argv) >= 8:
    autoProcessTV.processEpisode(sys.argv[1], sys.argv[2], sys.argv[7])
elif len(sys.argv) >= 3:
    autoProcessTV.processEpisode(sys.argv[1], sys.argv[2])
else:
    autoProcessTV.processEpisode(sys.argv[1])
