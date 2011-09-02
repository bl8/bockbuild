class MonoPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'mono', '2.10.5',
			sources = [
				'http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.bz2',
				'patches/mono-runtime-relocation.patch'
			],
			configure_flags = [
				'--with-jit=yes',
				'--with-ikvm=no',
				'--with-mcs-docs=no',
				'--with-moonlight=no',
				'--enable-quiet-build'
			]
		)

		# Mono (in libgc) likes to fail to build randomly
		self.make = 'for i in 1 2 3 4 5 6 7 8 9 10; do make && break; done'

#	def prep (self):
#		Package.prep (self)
#		self.sh ('patch -p1 < "%{sources[1]}"')

	def install (self):
		Package.install (self)
		if Package.profile.name == 'darwin':
			self.sh ('sed -ie "s/libcairo.so.2/libcairo.2.dylib/" "%{prefix}/etc/mono/config"')

MonoPackage ()
