import sys


class DataBase:

    def __init__(self):
        self.data_base = {}
        self.transactions = []

    def set_value(self, variable_name, value):
        self.__update_transaction(variable_name)
        self.data_base[variable_name] = value

    def get(self, variable_name):
        return self.data_base[variable_name] if variable_name in self.data_base else None

    def unset(self, variable_name):
        self.__update_transaction(variable_name)
        self.set_value(variable_name, None)

    def counts(self, value):
        return list(self.data_base.values()).count(value)

    def begin(self):
        self.transactions.append({})

    def rollback(self):
        if self.transactions:
            last_transcation = self.transactions.pop()
            for variable_name, value in last_transcation.items():
                self.data_base[variable_name] = value

    def commit(self):
        self.transactions = []

    def __update_transaction(self, variable_name):
        if self.transactions and not variable_name in self.transactions[-1]:
            self.transactions[-1][variable_name] = self.get(variable_name)


def run():
    db = DataBase()

    while True:

        try:
            query = input().strip()
        except EOFError:
            return
        if query == '':
            return
        command = query.split(' ')
        if command[0] == 'END':
            return
        try:
            if command[0] == 'SET':
                db.set_value(command[1], command[2])
            elif command[0] == 'UNSET':
                db.unset(command[1])
            elif command[0] == 'GET':
                result = db.get(command[1])
                print(result) if result else 'NULL'
            elif command[0] == 'COUNTS':
                print(db.counts(command[1]))
            elif command[0] == 'BEGIN':
                db.begin()
            elif command[0] == 'ROLLBACK':
                db.rollback()
            elif command[0] == 'COMMIT':
                db.commit()
        except:
            pass


if __name__ == '__main__':
    run()
