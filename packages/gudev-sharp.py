class GudevSharpPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'gudev-sharp', 'master')
		self.commit = '271ca29a44c0c5d660b0b724036e0fba32923c81'
		self.source_dir_name = 'mono-gudev-sharp-%s' % self.commit[:7]
		self.configure = './autogen.sh --prefix="%{prefix}"'
		self.sources = [
			'http://github.com/mono/gudev-sharp/tarball/%{commit}'
		]

GudevSharpPackage ()
