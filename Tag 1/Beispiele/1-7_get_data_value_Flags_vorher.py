"""1-7 · vorher · get_data_value: eine Funktion, drei Schalter, ein Text-Sentinel

Quelle: test_parameters/abstract_test_config.py, AbstractDataDrivenTest.get_data_value
(Testframework des Teams). Abweichung: ``testData.fieldNames`` und ``testData.field`` durch
Zugriffe auf ein Dictionary ersetzt.

Welche Umwandlung stattfindet, entscheiden ``is_bool``, ``is_list`` und
``cast_type``. Sie schließen sich gegenseitig aus, das steht aber nirgends.
``"<none>"`` in der TSV-Datei bedeutet None.
"""


def get_data_value(record, column, def_val, is_bool=False, is_list=False, cast_type=None):
    ret = def_val
    if column in record:
        value = record[column].strip()
        if len(value) > 0:
            ret = value
            if ret == "<none>":
                ret = None
            elif is_list:
                ret = [e.strip() for e in ret.split(",")]
                ret = [None if e == "<none>" else e for e in ret]
            elif is_bool:
                # Allowing for entries true/false as well as t/f or v/x
                ret = (ret == "true" or ret == "t" or ret == "v")
            elif cast_type:
                ret = cast_type(ret)
    return ret


record = {"i_is_virtual": "True", "i_working_width": "12.5", "tags": "smoke, <none>", "tr_clothoid": ""}

# Aufrufe wie in read_implement_settings(); an der Aufrufstelle ist die Bedeutung
# der Positionsargumente nur mit Blick in die Signatur zu erkennen:
assert get_data_value(record, "i_working_width", None, cast_type=float) == 12.5
assert get_data_value(record, "tags", [], is_list=True) == ["smoke", None]
assert get_data_value(record, "tr_clothoid", 0, cast_type=int) == 0       # leer -> Vorgabe

# "True" mit großem T ergibt False, ohne Meldung:
assert get_data_value(record, "i_is_virtual", None, is_bool=True) is False

# Zwei Schalter zugleich: is_list gewinnt, cast_type wird still ignoriert:
assert get_data_value(record, "i_working_width", None, is_list=True, cast_type=float) == ["12.5"]

print("vorher: alle Beobachtungen bestätigt")
