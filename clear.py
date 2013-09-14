#!/usr/bin/python
# -*- coding: utf-8 -*-

from lib import eueuser

if __name__ == '__main__':
    from lib import euemongo
    m = euemongo.mongo(host="localhost", port=27017, database="eue")
    m.connect()
    u = eueuser.user(m, "users")
    print u.delete("david.guenault@gmail.com")
    print m.disconnect()
