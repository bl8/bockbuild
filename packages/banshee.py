class BansheePackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'banshee-1', '1.8.0')

		self.sources = [
			'http://download.banshee.fm/banshee/stable/%{version}/%{name}-%{version}.tar.bz2'
		]

		self.configure_flags = [
			'--disable-docs',
			'--disable-boo',
			'--disable-youtube',
			'--disable-gnome'
		]

		self.configure_flags.extend ([
			'--disable-mtp',
			'--disable-daap',
			'--disable-appledevice',
			'--disable-ipod'
		])

		if Package.profile.name == 'darwin':
			self.configure_flags.extend ([
				'--disable-youtube',
				'--disable-webkit',
				'--disable-mtp',
				'--disable-daap',
				'--disable-ipod',
				'--with-vendor-build-id="banshee.fm OSX 10.5+ i386/Intel"'
			])
#		elif Package.profile.name == 'linux':
#			self.configure_flags.extend ([
#				'--with-vendor-build-id="banshee.fm Linux i386"'
#			])

BansheePackage ()
