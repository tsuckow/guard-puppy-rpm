rpmbuild:
	rpmbuild --define "_topdir `pwd`" -ba SPECS/guard-puppy.spec

all:
	tar -czf SOURCES/guard-puppy.tar.gz guard-puppy/
