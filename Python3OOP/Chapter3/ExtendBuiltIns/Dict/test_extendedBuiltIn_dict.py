from LongNameDict import LongNameDict

longkeys = LongNameDict()
longkeys['hello'] = 1
longkeys['longest yet'] = 5
longkeys['hello2'] = 'world'

print(longkeys.longest_key())
