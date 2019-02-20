# Internal
# Python


class IDatabaseWrapper:

    def select(self, databaseTableName: str, primaryKey):
        raise NotImplementedError