from .core.objects.apiobjects import MainTable
from .core.objects import Row, banned_columns
from .core.exceptions.messages import LoadingMsg as msg
from .load_utils import _new
            

def new(columns=None, cls=Row):
    return _new(columns=columns, cls=cls)




