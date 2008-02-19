from Form import *
from Table import *
from Module import *

class ModuleFile (Module, FormHelper):
    PROPERTIES = [
        'io_cache'
    ]

    def __init__ (self, cfg, prefix):
        Module.__init__ (self, 'file', cfg, prefix)
        FormHelper.__init__ (self, 'file', cfg)

    def _op_render (self):
        table = Table(2)
        self.AddTableCheckbox (table, "I/O cache", "%s!io_cache" % (self._prefix), True)
        return str(table)

    def _op_apply_changes (self, uri, post):
        self.ApplyChangesPrefix (self._prefix, ['io_cache'], post)

