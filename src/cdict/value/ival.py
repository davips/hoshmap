#  Copyright (c) 2021. Davi Pereira dos Santos
#  This file is part of the cdict project.
#  Please respect the license - more about this in the section (*) below.
#
#  cdict is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  cdict is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with cdict.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is illegal and it is unethical regarding the effort and
#  time spent here.
#
from functools import cached_property
from typing import Any

from hosh import Hosh


class iVal:
    value: Any
    hosh: Hosh
    result: Any

    def evaluate(self):
        _ = self.value

    @cached_property
    def id(self):
        return self.hosh.id

    @staticmethod
    def handle_id(id):
        """
        >>> iVal.handle_id("sduityv76453rjhgv7utfgsdfkhsdfsdfgi7tgsg").id
        'sduityv76453rjhgv7utfgsdfkhsdfsdfgi7tgsg'
        >>> from hosh import Hosh
        >>> iVal.handle_id(Hosh.fromid("sduityv76453rjhgv7utfgsdfkhsdfsdfgi7tgsg")).id
        'sduityv76453rjhgv7utfgsdfkhsdfsdfgi7tgsg'
        """
        if isinstance(id, str):
            return Hosh.fromid(id)
        elif isinstance(id, Hosh):
            return id
        else:  # pragma: no cover
            raise Exception(f"Wrong id type: {type(id)}")

    def __mul__(self, other):
        return self.hosh * (other if isinstance(other, Hosh) else other.hosh)