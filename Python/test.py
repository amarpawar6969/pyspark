import hvac

client = hvac.Client(url='http://localhost:8200', token='hvs.e1ycTWZZThaOupvLZVvpCyyj')
secrets = client.secrets.kv.v2.read_secret_version(path='aws/')
print(secrets['data']['data'])
