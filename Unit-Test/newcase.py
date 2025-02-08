from camelcase import CamelCase
c = CamelCase('little', 'another')
s = 'this is a another sentence, but this one is a little different'
print(c.hump(s))
# This is a another Sentence, But This One is a little Different