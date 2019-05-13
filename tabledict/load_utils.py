from .core.objects import Row, banned_columns
from .core.objects.apiobjects import MainTable
from .core.exceptions.messages import LoadingMsg as msg

def fill_empty(n, lst):
    x = len(lst)
    for _ in lst:
        yield _
    yield from ("" for b in range(n - x))


def forbidden_columns(columns, msg=msg):
    for x in columns:
        if x in banned_columns:
            raise ValueError(
                msg.forbidden_column.format(x))


def _new(columns=None, cls=Row, custom_columns=False):
    # Empty Main Selection
    if isinstance(columns, str):
        columns = [columns]
    if columns:
        forbidden_columns(columns)
    if not columns:
        columns = tuple()
    if not isinstance(columns, tuple):
        columns = tuple(columns)
    return MainTable(keys=columns, cls=cls)

def figure_out_columns(columns):
    finalcolumns = []

    # We don't need to completely clean this up, just prevent unusable columns.
    # PSV will automatically handle collisions
    # We need to keep these as close as possible to the original
    empty_counter = 0
    for x in (x.strip() for x in columns):
        result = x
        if result in banned_columns:
            result = "psv_banned_columns_{}".format(x)
        if not result:
            result = "psv_empty_column_{}".format(empty_counter)
            empty_counter += 1
        finalcolumns.append(result)
    return finalcolumns
