Package ('udev', '170',
	sources = [ 'http://www.kernel.org/pub/linux/utils/kernel/hotplug/%{name}-%{version}.tar.bz2' ],
	configure_flags = [
		'--disable-hwdb',
		'--disable-introspection',
		'--disable-udev_acl'
	]
)
