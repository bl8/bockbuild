class BansheePackage (GnomePackage):
	def __init__ (self):
		GnomePackage.__init__ (self, 'banshee',
			version_major = '2.1',
			version_minor = '3')

#		self.configure = './autogen.sh --prefix=%{prefix}'

		self.configure_flags = [
			'--disable-docs',
			'--disable-boo',
			'--disable-youtube',
			'--disable-gnome'
		]

		self.configure_flags.extend ([
			'--disable-mtp',
			'--disable-daap',
			'--disable-appledevice'
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
		elif Package.profile.name == 'glick':
			self.configure_flags.extend ([
				'--with-vendor-build-id="banshee.fm Linux bundle"'
			])

BansheePackage ()
