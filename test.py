from metaspace import Namespace


class X(Namespace):
    def func():
        return 123

import X as foo
from X import func
assert func() == 123
assert foo.func() == 123
