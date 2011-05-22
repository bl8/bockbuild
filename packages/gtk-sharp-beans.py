class GtkSharpBeansPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'gtk-sharp-beans', 'master')
		self.commit = '270c098e625be97b5e055af0887c2a4d7b855fb6'
		self.source_dir_name = 'mono-gtk-sharp-beans-%s' % self.commit[:7]
		self.configure = './autogen.sh --prefix="%{prefix}"'
		self.sources = [
			'http://github.com/mono/gtk-sharp-beans/tarball/%{commit}'
		]

GtkSharpBeansPackage ()
