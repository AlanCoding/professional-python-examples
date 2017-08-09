# Basics of what the builtin type() does

class A(object):

    def run(self):
        print 'a method that runs!'

class B(A):

    def skip(self):
        print 'skip method'


print 'calling classes'
A().run()
B().run()
B().skip()


def run(self):
    print 'run method defined in global namespace'

def skip(self):
    print 'skip method defined globally'

A = type('A', (object,), {
    'run': run
})

print ''
print 'same thing, but made with type()'

A().run()

B = type('B', (A,), {
    'skip': skip
})

B().run()
B().skip()
print ' B type ' + str(type(B))

print ''
print 'type of type ' + str(type(type))

