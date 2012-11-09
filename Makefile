all: maketar rpmbuild

rpmbuild:
	rpmbuild --define "_topdir `pwd`" -ba SPECS/guard-puppy.spec

maketar:
	tar -czf SOURCES/guard-puppy.tar.gz guard-puppy/
