from MySQLdb import _mysql


class OldDBAdapter:
    DB_DATA = {'database': 'shotokai_db',
        'username' : 'shotokai_user',
        'password' : '8=TBy[*(0s2M',
        'prefix' : 'akds1_',
        'host' : 'shotokai.org',
        'port' : 3306,
    }

    def __init__(self):
        self.db = _mysql.connect(self.DB_DATA['host'], self.DB_DATA['username'], self.DB_DATA['password'], self.DB_DATA['database'], port=self.DB_DATA['port'])
        # works. Now need to do .query() then r = .store_result(), then r.fetch_row()
    
    def get_pages(self):
        self.db.query("SELECT bundle,body_value FROM {}node__body".format(self.DB_DATA['prefix']))
        r = self.db.store_result()
        return r


        

