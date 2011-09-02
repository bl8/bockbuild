Package ('mono-addins', '0.6.2',
	sources = [ 'http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.bz2' ],
	configure_flags = ['--disable-gui'],

	override_properties = { 'make': 'make' }
)
