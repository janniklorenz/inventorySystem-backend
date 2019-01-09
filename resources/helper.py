

# Fetch a single entry from given table
# table: Table to use
# entryID: entry id to search
# schema: Schema to format
def generic_get_single(table, entryID, schema):
    entry = table.query.filter_by(id=entryID).first()
    return generic_single(entry, schema)

# Send a single entry from given entry
# entry: entry id to display
# schema: Schema to format
def generic_single(entry, schema):
    if entry is None:
        return {"message": "no entry with given id"}, 404
    entry = schema.dump(entry).data
    return entry, 200

# Fetch all entrys of given table
# entry: entrys to use
# schema: Schema to format
def generic_get_all(table, schema):
    entry = table.query.all()
    return generic_all(entry, schema)

def generic_all(entry, schema):
    entry = schema.dump(entry).data
    return entry, 200
