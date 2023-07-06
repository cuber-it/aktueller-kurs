import table_documents_simple_pydoc as table
import table_documented_sphinx as tableX


class Reader:
    pass

class Writer:
    pass


t = table.Tabelle()
t2 = tableX.Tabelle()

t.load(Reader())
t.dump(Writer())

t.row_count()
