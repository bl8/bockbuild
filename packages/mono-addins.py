Package ('mono-addins', '0.6.1',
	sources = [ 'http://ftp.novell.com/pub/mono/sources/%{name}/%{name}-%{version}.tar.bz2' ],
	configure_flags = ['--disable-gui'],

	override_properties = { 'make': 'make' }
)
