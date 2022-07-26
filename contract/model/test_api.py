import xmlrpc.client

url = 'http://localhost:8069'
db = 'vconst'
username = 'admin'
password = '1'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version1 = common.version()
print(version1)

uid = common.authenticate(db, username, password, {})
print(uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# partner_id = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', False]]])
# print(partner_id)

# partner_record = models.execute_kw(db, uid, password, 'res.partner', 'read', [partner_id], {'fields': ['id', 'name']})
# print(partner_record)

# This line will first search in res_partner than read the data from the res_partner
abcd = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', False]]],
                         {'fields': ['id', 'name'], 'limit': 5})
# print(abcd)
for rec in abcd:
    print(rec)

new_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "Vatsal"}])
print(new_id)
