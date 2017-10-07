%define _disable_ld_no_undefined 1

%define mod_name mod_php
%define load_order 70

%define build_test 1

%{?_with_test: %{expand: %%global build_test 1}}
%{?_without_test: %{expand: %%global build_test 0}}

%define build_libmagic 0
%{?_with_libmagic: %{expand: %%global build_libmagic 1}}
%{?_without_libmagic: %{expand: %%global build_libmagic 0}}

%define php7_common_major 5
%define libname %mklibname php7_common %{php7_common_major}

# enforce versioned postgresql dependencies because of multiple version
# availability in the distribution
%define postgresql_version %(pg_config &>/dev/null && pg_config 2>/dev/null | grep "^VERSION" | awk '{ print $4 }' 2>/dev/null || echo 0)

Summary:	The PHP7 scripting language
Name:		php
Version:	7.1.10
Release:	%mkrel 1
Source0:	http://php.net/distributions/php-%{version}.tar.xz
Group:		Development/PHP
License:	PHP License
URL:		http://www.php.net
Source1:	php-test.ini
Source2:	maxlifetime
Source3:	php.crond
Source4:	php-fpm.service
Source5:	php-fpm.sysconf
Source6:	php-fpm.logrotate
# S7 comes from ext/fileinfo/create_data_file.php but could be removed someday
Source7:	create_data_file.php
Source9:	php-fpm-tmpfiles.conf
Patch1:		php-shared.diff
#update init to 7.1.9
Patch2:		php-7.1.9-mga_php.ini.diff
Patch3:		php-libtool.diff
Patch5:		php-phpbuilddir.diff
# http://www.outoforder.cc/projects/apache/mod_transform/
# http://www.outoforder.cc/projects/apache/mod_transform/patches/php5-apache2-filters.patch
Patch6:		php5-apache2-filters.diff
# remove libedit once and for all
Patch7:		php-no_libedit.diff
Patch8:		php-xmlrpc_epi.patch
Patch9:		php-xmlrpc_no_rpath.diff
Patch11:	php-7.0.3-libdb.diff
# submitted as https://github.com/php/php-src/pull/361
Patch12:	php-5.5.0-mysqlnd-unix-sock-addr.patch
Patch13:	php-7.0.1-clang-warnings.patch
#####################################################################
# Stolen from PLD
Patch21:	php-filter-shared.diff
Patch22:	php-dba-link.patch
Patch23:	php-zlib-for-getimagesize.patch
#(spuhler) taken from Mandriva
Patch26:	php-5.3.9RC2-mcrypt-libs.diff
# for kolab2
# P50 was rediffed from PLD (php-5.3.3-8.src.rpm) which merges the annotation and status-current patches
# Patch27:	php-imap-annotation+status-current.diff 
# P51 was taken from http://kolab.org/cgi-bin/viewcvs-kolab.cgi/server/php/patches/php-5.3.2/
# Patch28:	php-imap-myrights.diff
# was dropped by kolab2


Patch29:	php-5.3.x-fpm-0.6.5-shared.diff
Patch30:	php-5.3.x-fpm-0.6.5-mdv_conf.diff

#Stolen from remi - Functional changes
Patch48: php-7.1.9-openssl-load-config.patch
#####################################################################
# stolen from debian
Patch50:	php-session.save_path.diff
Patch51:	php-exif_nesting_level.diff
#####################################################################
# Stolen from fedora
Patch101:	php-cxx.diff
Patch102:	php-install.diff
Patch105:	php-umask.diff
# Fixes for extension modules
Patch113:	php-libc-client.diff
Patch114:	php-no_pam_in_c-client.diff
# Functional changes
Patch115:	php-dlopen.diff
# Fix bugs
Patch120:	php-tests-wddx.diff
Patch121:	php-bug43221.diff
Patch123:	php-bug43589.diff
Patch226:	php-no-fvisibility_hidden_fix.diff
Patch227:	php-5.3.0RC1-enchant_lib64_fix.diff
Patch229:	php-5.5.2-session.use_strict_mode.diff
#Stolen from remi
Patch230: php-7.0.0-includedir.patch
Patch300: php-7.0.10-datetests.patch


BuildRequires:	apache-devel >= 2.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	file
BuildRequires:	flex
BuildRequires:	lemon
BuildRequires:	libtool
BuildRequires:	openssl
BuildRequires:	re2c >= 0.13.4

BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libzip)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)

BuildRequires:	firebird-devel

BuildRequires:	aspell-devel
BuildRequires:	bzip2-devel
BuildRequires:	c-client-devel >= 2007
BuildRequires:	db-devel
BuildRequires:	elfutils-devel
BuildRequires:	freetds-devel >= 0.63
BuildRequires:	gdbm-devel
BuildRequires:	gd-devel >= 2.0.33
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
BuildRequires:	gpm-devel
BuildRequires:	icu-devel >= 49.0
BuildRequires:	jpeg-devel
BuildRequires:	openldap-devel
BuildRequires:	libmcrypt-devel
BuildRequires:	cyrus-sasl 
BuildRequires:	libtool-devel
BuildRequires:	mbfl-devel >= 1.2.0
BuildRequires:	mysql-devel >= 4.1.7
BuildRequires:	net-snmp-devel
BuildRequires:	net-snmp-mibs
BuildRequires:	onig-devel >= 5.9.2
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel
BuildRequires:	readline-devel
BuildRequires:	recode-devel
BuildRequires:	t1lib-devel
BuildRequires:	tidy-devel
BuildRequires:	unixODBC-devel >= 2.2.1
BuildRequires:	xmlrpc-epi-devel
%if %{build_libmagic}
BuildRequires:	magic-devel
%endif
Epoch: 3

%description
PHP7 is an HTML-embeddable scripting language. PHP7 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP7 is fairly simple. The
most common use of PHP7 coding is probably as a replacement for CGI scripts.

%package	ini
Summary:	INI files for PHP
Group:		Development/Other

%description ini
The php-ini package contains the ini file required for PHP.


%package -n apache-mod_php
Summary:	The PHP7 HTML-embedded scripting language for use with apache
Group:		System/Servers
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	apache >= 2.2
#TODO are theses really required ?
Requires:	php-ctype >= %{epoch}:%{version}
Requires:	php-filter >= %{epoch}:%{version}
Requires:	php-ftp >= %{epoch}:%{version}
Requires:	php-gettext >= %{epoch}:%{version}
Requires:	php-hash >= %{epoch}:%{version}
Requires:	php-ini >= %{version}
Requires:	php-json >= %{epoch}:%{version}
Requires:	php-openssl >= %{epoch}:%{version}
Requires:	php-pcre >= %{epoch}:%{version}
Requires:	php-posix >= %{epoch}:%{version}
Requires:	php-session >= %{epoch}:%{version}
Recommends:	php-suhosin >= 0.9.33
Requires:	php-sysvsem >= %{epoch}:%{version}
Requires:	php-sysvshm >= %{epoch}:%{version}
Requires:	php-tokenizer >= %{epoch}:%{version}
Requires:	php-xmlreader >= %{epoch}:%{version}
Requires:	php-xmlwriter >= %{epoch}:%{version}
Requires:	php-zlib >= %{epoch}:%{version}
Requires:	php-xml >= %{epoch}:%{version}
Requires:	php-timezonedb >= 3:2012.3
# php is not fully thread safe
# http://www.php.net/manual/en/faq.installation.php#faq.installation.apache2
# http://stackoverflow.com/questions/681081/is-php-thread-safe

Epoch:		%{epoch}

%description -n apache-mod_php
PHP7 is an HTML-embedded scripting language. PHP7 attempts to make it easy for
developers to write dynamically generated web pages. PHP7 also offers built-in
database integration for several commercial and non-commercial database
management systems, so writing a database-enabled web page with PHP7 is fairly
simple. The most common use of PHP coding is probably as a replacement for CGI
scripts. The %{name} module enables the apache web server to understand
and process the embedded PHP language in web pages.

This package contains PHP version 7. You'll also need to install the apache web
server.

%package	cli
Summary:	PHP7 CLI interface
Group:		Development/Other
URL:		http://www.php.net/cli
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	php-ctype >= %{epoch}:%{version}
Requires:	php-filter >= %{epoch}:%{version}
Requires:	php-ftp >= %{epoch}:%{version}
Requires:	php-gettext >= %{epoch}:%{version}
Requires:	php-hash >= %{epoch}:%{version}
Requires:	php-ini >= %{version}
Requires:	php-json >= %{epoch}:%{version}
Requires:	php-openssl >= %{epoch}:%{version}
Requires:	php-pcre >= %{epoch}:%{version}
Requires:	php-posix >= %{epoch}:%{version}
Requires:	php-session >= %{epoch}:%{version}
Recommends:	php-suhosin >= 0.9.33
Requires:	php-sysvsem >= %{epoch}:%{version}
Requires:	php-sysvshm >= %{epoch}:%{version}
Requires:	php-timezonedb >= 3:2012.3
Requires:	php-tokenizer >= %{epoch}:%{version}
Requires:	php-xmlreader >= %{epoch}:%{version}
Requires:	php-xmlwriter >= %{epoch}:%{version}
Requires:	php-zlib >= %{epoch}:%{version}
Requires:	php-xml >= %{epoch}:%{version}
Provides:	php = %{epoch}:%{version}
Provides:	/usr/bin/php

%description	cli
This package contains a command-line (CLI) version of php. You must also
install libphp7_common. If you need apache module support, you also need to
install the apache-mod_php package.

%package	cgi
Summary:	PHP7 CGI interface
Group:		Development/Other
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	php-ctype >= %{epoch}:%{version}
Requires:	php-filter >= %{epoch}:%{version}
Requires:	php-ftp >= %{epoch}:%{version}
Requires:	php-gettext >= %{epoch}:%{version}
Requires:	php-hash >= %{epoch}:%{version}
Requires:	php-ini >= %{version}
Requires:	php-json >= %{epoch}:%{version}
Requires:	php-openssl >= %{epoch}:%{version}
Requires:	php-pcre >= %{epoch}:%{version}
Requires:	php-posix >= %{epoch}:%{version}
Requires:	php-session >= %{epoch}:%{version}
Recommends:	php-suhosin >= 0.9.33
Requires:	php-sysvsem >= %{epoch}:%{version}
Requires:	php-sysvshm >= %{epoch}:%{version}
Requires:	php-timezonedb >= 3:2012.3
Requires:	php-tokenizer >= %{epoch}:%{version}
Requires:	php-xmlreader >= %{epoch}:%{version}
Requires:	php-xmlwriter >= %{epoch}:%{version}
Requires:	php-zlib >= %{epoch}:%{version}
Requires:	php-xml >= %{epoch}:%{version}
Provides:	php = %{epoch}:%{version}
Provides:	php-fcgi = %{epoch}:%{version}-%{release}
Obsoletes:	php-fcgi
# because of a added compat softlink
Conflicts:	php-fcgi < %{epoch}:%{version}-%{release}

%description	cgi
PHP7 is an HTML-embeddable scripting language. PHP7 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP7 is fairly simple. The
most common use of PHP7 coding is probably as a replacement for CGI scripts.

This package contains a standalone (CGI) version of php with FastCGI support.
You must also install libphp7_common. If you need apache module support, you
also need to install the apache-mod_php package.

%package -n	%{libname}
Summary:	Shared library for PHP7
Group:		Development/Other
Provides:	php-pcre = %{epoch}:%{version}
Provides:	php-simplexml = %{epoch}:%{version}

%description -n	%{libname}
This package provides the common files to run with different implementations of
PHP7. You need this package if you install the php standalone package or a
webserver with php support (ie: apache-mod_php).

%package	devel
Summary:	Development package for PHP7
Group:		Development/C
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	autoconf automake libtool
Requires:	bison
Requires:	byacc
Requires:	chrpath
Requires:	dos2unix
Requires:	flex
Requires:	libxml2-devel >= 2.6
Requires:	libxslt-devel >= 1.1.0
Requires:	openssl
Requires:	openssl-devel >= 0.9.7
Requires:	pam-devel
Requires:	pcre-devel >= 6.6
Requires:	re2c >= 0.9.11
Requires:	tcl

%description	devel
The php-devel package lets you compile dynamic extensions to PHP7. Included
here is the source for the php extensions. Instead of recompiling the whole php
binary to add support for, say, oracle, install this package and use the new
self-contained extensions support. For more information, read the file
SELF-CONTAINED-EXTENSIONS.

%package	openssl
Summary:	OpenSSL extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/openssl
Requires:	%{libname} >= %{epoch}:%{version}

%description	openssl
This is a dynamic shared object (DSO) for PHP that will add OpenSSL support.

%package	zlib
Summary:	Zlib extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/zlib
Requires:	%{libname} >= %{epoch}:%{version}

%description	zlib
This is a dynamic shared object (DSO) for PHP that will add zlib compression
support to PHP.

%package	doc
Summary:	Documentation for PHP
Group:		Development/PHP
BuildArch:	noarch

%description	doc
Documentation for php.

%package	bcmath
Summary:	The bcmath module for PHP
Group:		Development/PHP
URL:		http://www.php.net/bcmath
Requires:	%{libname} >= %{epoch}:%{version}

%description	bcmath
This is a dynamic shared object (DSO) for PHP that will add bc style precision
math functions support.

For arbitrary precision mathematics PHP offers the Binary Calculator which
supports numbers of any size and precision, represented as strings.

%package	bz2
Summary:	Bzip2 extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/bzip2
Requires:	%{libname} >= %{epoch}:%{version}

%description	bz2
This is a dynamic shared object (DSO) for PHP that will add bzip2 compression
support to PHP.

The bzip2 functions are used to transparently read and write bzip2 (.bz2)
compressed files.

%package	calendar
Summary:	Calendar extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/calendar
Requires:	%{libname} >= %{epoch}:%{version}

%description	calendar
This is a dynamic shared object (DSO) for PHP that will add calendar support.

The calendar extension presents a series of functions to simplify converting
between different calendar formats. The intermediary or standard it is based on
is the Julian Day Count. The Julian Day Count is a count of days starting from
January 1st, 4713 B.C. To convert between calendar systems, you must first
convert to Julian Day Count, then to the calendar system of your choice. Julian
Day Count is very different from the Julian Calendar! For more information on
Julian Day Count, visit http://www.hermetic.ch/cal_stud/jdn.htm. For more
information on calendar systems visit
http://www.boogle.com/info/cal-overview.html. Excerpts from this page are
included in these instructions, and are in quotes.

%package	ctype
Summary:	Ctype extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/ctype
Requires:	%{libname} >= %{epoch}:%{version}

%description	ctype
This is a dynamic shared object (DSO) for PHP that will add ctype support.

The functions provided by this extension check whether a character or string
falls into a certain character class according to the current locale (see also
setlocale()).

%package	curl
Summary:	Curl extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/curl
Requires:	%{libname} >= %{epoch}:%{version}

%description	curl
This is a dynamic shared object (DSO) for PHP that will add curl support.

PHP supports libcurl, a library created by Daniel Stenberg, that allows you to
connect and communicate to many different types of servers with many different
types of protocols. libcurl currently supports the http, https, ftp, gopher,
telnet, dict, file, and ldap protocols. libcurl also supports HTTPS
certificates, HTTP POST, HTTP PUT, FTP uploading (this can also be done with
PHP's ftp extension), HTTP form based upload, proxies, cookies, and
user+password authentication.

%package	dba
Summary:	DBA extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/dba
Requires:	%{libname} >= %{epoch}:%{version}

%description	dba
This is a dynamic shared object (DSO) for PHP that will add flat-file databases
(DBA) support.

These functions build the foundation for accessing Berkeley DB style databases.

This is a general abstraction layer for several file-based databases. As such,
functionality is limited to a common subset of features supported by modern
databases such as Sleepycat Software's DB2. (This is not to be confused with
IBM's DB2 software, which is supported through the ODBC functions.)

%package	dom
Summary:	Dom extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/dom
Requires:	%{libname} >= %{epoch}:%{version}

%description	dom
This is a dynamic shared object (DSO) for PHP that will add dom support.

The DOM extension is the replacement for the DOM XML extension from PHP 4. The
extension still contains many old functions, but they should no longer be used.
In particular, functions that are not object-oriented should be avoided.

The extension allows you to operate on an XML document with the DOM API.

%package	enchant
Summary:	Libenchant binder, support near all spelling tools
Group:		Development/PHP
URL:		http://www.php.net/
Requires:	%{libname} >= %{epoch}:%{version}

%description	enchant
Enchant is a binder for libenchant. Libenchant provides a common API for many
spell libraries:

 - aspell/pspell (intended to replace ispell)
 - hspell (hebrew)
 - ispell 
 - hunspell (OpenOffice project, mozilla)
 - uspell (primarily Yiddish, Hebrew, and Eastern European languages)
   A plugin system allows to add custom spell support.
   see www.abisource.com/enchant/

%package	exif
Summary:	EXIF extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/exif
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	php-mbstring >= %{epoch}:%{version}

%description	exif
This is a dynamic shared object (DSO) for PHP that will add EXIF tags support
in image files.

With the exif extension you are able to work with image meta data. For example,
you may use exif functions to read meta data of pictures taken from digital
cameras by working with information stored in the headers of the JPEG and TIFF
images.

%package	fileinfo
Summary:	Fileinfo extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/fileinfo
Requires:	%{libname} >= %{epoch}:%{version}

%description	fileinfo
This extension allows retrieval of information regarding vast majority of file.
This information may include dimensions, quality, length etc...

Additionally it can also be used to retrieve the mime type for a particular
file and for text files proper language encoding.

%package	filter
Summary:	Extension for safely dealing with input parameters
Group:		Development/PHP
URL:		http://www.php.net/filter
Requires:	%{libname} >= %{epoch}:%{version}

%description	filter
The Input Filter extension is meant to address this issue by implementing a set
of filters and mechanisms that users can use to safely access their input data.

%package	ftp
Summary:	FTP extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/ftp
Requires:	%{libname} >= %{epoch}:%{version}

%description	ftp
This is a dynamic shared object (DSO) for PHP that will add FTP support.

The functions in this extension implement client access to file servers
speaking the File Transfer Protocol (FTP) as defined in
http://www.faqs.org/rfcs/rfc959. This extension is meant for detailed access to
an FTP server providing a wide range of control to the executing script. If you
only wish to read from or write to a file on an FTP server, consider using the
ftp:// wrapper  with the filesystem functions  which provide a simpler and more
intuitive interface.

%package	gd
Summary:	GD extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/gd
Requires:	%{libname} >= %{epoch}:%{version}
Provides:	php-gd-bundled = %{epoch}:%{version}
Obsoletes:	php-gd-bundled

%description	gd
This is a dynamic shared object (DSO) for PHP that will add GD support,
allowing you to create and manipulate images with PHP using the gd library.

PHP is not limited to creating just HTML output. It can also be used to create
and manipulate image files in a variety of different image formats, including
gif, png, jpg, wbmp, and xpm. Even more convenient, PHP can output image
streams directly to a browser. You will need to compile PHP with the GD library
of image functions for this to work. GD and PHP may also require other
libraries, depending on which image formats you want to work with.

You can use the image functions in PHP to get the size of JPEG, GIF, PNG, SWF,
TIFF and JPEG2000 images.

%package	gettext
Summary:	Gettext extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/gettext
Requires:	%{libname} >= %{epoch}:%{version}

%description	gettext
This is a dynamic shared object (DSO) for PHP that will add gettext support.

The gettext functions implement an NLS (Native Language Support) API which can
be used to internationalize your PHP applications. Please see the gettext
documentation for your system for a thorough explanation of these functions or
view the docs at http://www.gnu.org/software/gettext/manual/gettext.html.

%package	gmp
Summary:	Gmp extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/gmp
Requires:	%{libname} >= %{epoch}:%{version}

%description	gmp
This is a dynamic shared object (DSO) for PHP that will add arbitrary length
number support using the GNU MP library.

%package	hash
Summary:	HASH Message Digest Framework
Group:		Development/PHP
URL:		http://www.php.net/hash
Requires:	%{libname} >= %{epoch}:%{version}

%description	hash
Native implementations of common message digest algorithms using a generic
factory method.

Message Digest (hash) engine. Allows direct or incremental processing of
arbitrary length messages using a variety of hashing algorithms.

%package	iconv
Summary:	Iconv extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/iconv
Requires:	%{libname} >= %{epoch}:%{version}

%description	iconv
This is a dynamic shared object (DSO) for PHP that will add iconv support.

This module contains an interface to iconv character set conversion facility.
With this module, you can turn a string represented by a local character set
into the one represented by another character set, which may be the Unicode
character set. Supported character sets depend on the iconv implementation of
your system. Note that the iconv function on some systems may not work as you
expect. In such case, it'd be a good idea to install the GNU libiconv library.
It will most likely end up with more consistent results.

%package	imap
Summary:	IMAP extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/iamp
Requires:	%{libname} >= %{epoch}:%{version}

%description	imap
This is a dynamic shared object (DSO) for PHP that will add IMAP support.

These functions are not limited to the IMAP protocol, despite their name. The
underlying c-client library also supports NNTP, POP3 and local mailbox access
methods.

%package	interbase
Summary:	Interbase/Firebird database module for PHP
Group:		Development/PHP
URL:		http://www.php.net/ibase
Requires:	%{libname} >= %{epoch}:%{version}
Obsoletes:	php-firebird
Provides:	php-firebird = %{epoch}:%{version}

%description	interbase
This is a dynamic shared object (DSO) for PHP that will add Firebird
database support.

%package	intl
Summary:	Internationalization extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/intl
Requires:	%{libname} >= %{epoch}:%{version}

%description	intl
This is a dynamic shared object (DSO) for PHP that will add
Internationalization support.

Internationalization extension implements ICU library functionality in PHP.

%package	json
Summary:	JavaScript Object Notation
Group:		Development/PHP
URL:		http://www.php.net/json
Requires:	%{libname} >= %{epoch}:%{version}

%description	json
Support for JSON (JavaScript Object Notation) serialization.

%package	ldap
Summary:	LDAP extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/ldap
Requires:	%{libname} >= %{epoch}:%{version}

%description	ldap
This is a dynamic shared object (DSO) for PHP that will add LDAP support.

LDAP is the Lightweight Directory Access Protocol, and is a protocol used to
access "Directory Servers". The Directory is a special kind of database that
holds information in a tree structure.

The concept is similar to your hard disk directory structure, except that in
this context, the root directory is "The world" and the first level
subdirectories are "countries". Lower levels of the directory structure contain
entries for companies, organisations or places, while yet lower still we find
directory entries for people, and perhaps equipment or documents.

%package	mbstring
Summary:	MBstring extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/mbstring
Requires:	%{libname} >= %{epoch}:%{version}

%description	mbstring
This is a dynamic shared object (DSO) for PHP that will add multibyte string
support.

mbstring provides multibyte specific string functions that help you deal with
multibyte encodings in PHP. In addition to that, mbstring handles character
encoding conversion between the possible encoding pairs. mbstring is designed
to handle Unicode-based encodings such as UTF-8 and UCS-2 and many single-byte
encodings for convenience.

%package	mcrypt
Summary:	Mcrypt extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/mcrypt
Requires:	%{libname} >= %{epoch}:%{version}

%description	mcrypt
This is a dynamic shared object (DSO) for PHP that will add mcrypt support.

This is an interface to the mcrypt library, which supports a wide variety of
block algorithms such as DES, TripleDES, Blowfish (default), 3-WAY, SAFER-SK64,
SAFER-SK128, TWOFISH, TEA, RC3 and GOST in CBC, OFB, CFB and ECB cipher modes.
Additionally, it supports RC6 and IDEA which are considered "non-free".

%package	mysqli
Summary:	MySQL database module for PHP
Group:		Development/PHP
URL:		http://www.php.net/mysqli
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	%{name}-mysqlnd = %{epoch}:%{version}

%description	mysqli
This is a dynamic shared object (DSO) for PHP that will add MySQL database
support.

The mysqli extension allows you to access the functionality provided by MySQL
4.1 and above. It is an improved version of the older PHP MySQL driver,
offering various benefits. The developers of the PHP programming language
recommend using MySQLi when dealing with MySQL server versions 4.1.3 and newer
(takes advantage of new functionality)

More information about the MySQL Database server can be found at
http://www.mysql.com/

Documentation for MySQL can be found at http://dev.mysql.com/doc/.

Documentation for MySQLi can be found at http://www.php.net/manual/en/mysqli.overview.php.

%package	mysqlnd
Summary:	MySQL native database module for PHP
Group:		Development/PHP
URL:		http://www.php.net/mysqlnd
Requires:	%{libname} >= %{epoch}:%{version}

%description	mysqlnd
This is a dynamic shared object (DSO) for PHP that will add MySQL native
database support.

These functions allow you to access MySQL database servers. More information
about MySQL can be found at http://www.mysql.com/.

Documentation for MySQL can be found at http://dev.mysql.com/doc/.

%package	odbc
Summary:	ODBC extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/odbc
Requires:	%{libname} >= %{epoch}:%{version}

%description	odbc
This is a dynamic shared object (DSO) for PHP that will add ODBC support.

In addition to normal ODBC support, the Unified ODBC functions in PHP allow you
to access several databases that have borrowed the semantics of the ODBC API to
implement their own API. Instead of maintaining multiple database drivers that
were all nearly identical, these drivers have been unified into a single set of
ODBC functions.

%package	opcache
Summary:	Zend OPcache for PHP
Group:		Development/PHP
URL:		http://www.php.net/opcache
Requires:	%{libname} >= %{epoch}:%{version}
Conflicts:	php-xcache

%description	opcache
This is a dynamic shared object (DSO) for PHP that will add OPcache support.

The Zend OPcache provides faster PHP execution through opcode caching and
optimization. It improves PHP performance by storing precompiled script
bytecode in the shared memory. This eliminates the stages of reading code from
the disk and compiling it on future access. In addition, it applies a few
bytecode optimization patterns that make code execution faster.

%package	pcntl
Summary:	Process Control extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/pcntl
Requires:	%{libname} >= %{epoch}:%{version}

%description	pcntl
This is a dynamic shared object (DSO) for PHP that will add process spawning
and control support. It supports functions like fork(), waitpid(), signal()
etc.

Process Control support in PHP implements the Unix style of process creation,
program execution, signal handling and process termination. Process Control
should not be enabled within a webserver environment and unexpected results may
happen if any Process Control functions are used within a webserver
environment.

%package	pdo
Summary:	PHP Data Objects Interface
Group:		Development/PHP
URL:		http://www.php.net/pdo
Requires:	%{libname} >= %{epoch}:%{version}

%description	pdo
PDO provides a uniform data access interface, sporting advanced features such
as prepared statements and bound parameters. PDO drivers are dynamically
loadable and may be developed independently from the core, but still accessed
using the same API.

Read the documentation at http://www.php.net/pdo for more information.

%package	pdo_dblib
Summary:	Sybase Interface driver for PDO
Group:		Development/PHP
URL:		http://www.php.net/pdo_dblib
Requires:       freetds >= 0.63
Requires:	php-pdo >= %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}

%description	pdo_dblib
PDO_DBLIB is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to Microsoft SQL Server and Sybase databases through the
FreeTDS libary.

%package	pdo_firebird
Summary:	Firebird/InterBase driver for PDO
Group:		Development/PHP
URL:		http://www.php.net/pdo_firebird
Requires:	php-pdo >= %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}

%description	pdo_firebird
PDO_Firebird is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to Firebird databases.

%package	pdo_mysql
Summary:	MySQL Interface driver for PDO
Group:		Development/PHP
URL:		http://www.php.net/pdo_mysql
Requires:	php-pdo >= %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	%{name}-mysqlnd = %{epoch}:%{version}

%description	pdo_mysql
PDO_MYSQL is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to MySQL 3.x, 4.x and 5.x databases.
 
PDO_MYSQL will take advantage of native prepared statement support present in
MySQL 4.1 and higher. If you're using an older version of the mysql client
libraries, PDO will emulate them for you.

Please note that this build does NOT support compression protocol because it
is built with MySQL Native Driver (mysqlnd).

%package	pdo_odbc
Summary:	ODBC v3 Interface driver for PDO
Group:		Development/PHP
URL:		http://www.php.net/pdo_odbc
Requires:	php-pdo >= %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}

%description	pdo_odbc
PDO_ODBC is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to databases through ODBC drivers or through the IBM DB2
Call Level Interface (DB2 CLI) library. PDO_ODBC currently supports three
different "flavours" of database drivers:
 
 o ibm-db2  - Supports access to IBM DB2 Universal Database, Cloudscape, and
              Apache Derby servers through the free DB2 client. ibm-db2 is not
	      supported in Mageia.

 o unixODBC - Supports access to database servers through the unixODBC driver
              manager and the database's own ODBC drivers.

 o generic  - Offers a compile option for ODBC driver managers that are not
              explicitly supported by PDO_ODBC.

%package	pdo_pgsql
Summary:	PostgreSQL interface driver for PDO
Group:		Development/PHP
URL:		http://www.php.net/pdo_pgsql
Requires:	php-pdo >= %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	postgresql-libs >= %{postgresql_version}

%description	pdo_pgsql
PDO_PGSQL is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to PostgreSQL databases.

%package	pdo_sqlite
Summary:	SQLite v3 Interface driver for PDO
Group:		Development/PHP
URL:		http://www.php.net/pdo_sqlite
Requires:	php-pdo >= %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}

%description	pdo_sqlite
PDO_SQLITE is a driver that implements the PHP Data Objects (PDO) interface to
enable access to SQLite 3 databases.

This extension provides an SQLite v3 driver for PDO. SQLite V3 is NOT
compatible with the bundled SQLite 2 in PHP 5, but is a significant step
forwards, featuring complete utf-8 support, native support for blobs, native
support for prepared statements with bound parameters and improved concurrency.

%package	pgsql
Summary:	PostgreSQL database module for PHP
Group:		Development/PHP
URL:		http://www.php.net/pgsql
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	postgresql-libs >= %{postgresql_version}

%description	pgsql
This is a dynamic shared object (DSO) for PHP that will add PostgreSQL database
support.

PostgreSQL database is Open Source product and available without cost.
Postgres, developed originally in the UC Berkeley Computer Science Department,
pioneered many of the object-relational concepts now becoming available in some
commercial databases. It provides SQL92/SQL99 language support, transactions,
referential integrity, stored procedures and type extensibility. PostgreSQL is
an open source descendant of this original Berkeley code.

%package	phar
Summary:	Allows running of complete applications out of .phar files
Group:		Development/PHP
URL:		http://www.php.net/phar
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	php-bz2
Requires:	php-hash

%description	phar
This is the extension version of PEAR's PHP_Archive package. Support for
zlib, bz2 and crc32 is achieved without any dependency other than the external
zlib or bz2 extension.

.phar files can be read using the phar stream, or with the Phar class. If the
SPL extension is available, a Phar object can be used as an array to iterate
over a phar's contents or to read files directly from the phar.

Phar archives can be created using the streams API or with the Phar class, if
the phar.readonly ini variable is set to false.

Full support for MD5 and SHA1 signatures is possible. Signatures can be
required if the ini variable phar.require_hash is set to true. When PECL
extension hash is avaiable then SHA-256 and SHA-512 signatures are supported as
well.

%package	posix
Summary:	POSIX extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/posix
Requires:	%{libname} >= %{epoch}:%{version}

%description	posix
This is a dynamic shared object (DSO) for PHP that will add POSIX functions
support to PHP.

This module contains an interface to those functions defined in the IEEE 1003.1
(POSIX.1) standards document which are not accessible through other means.
POSIX.1 for example defined the open(), read(), write() and close() functions,
too, which traditionally have been part of PHP 3 for a long time. Some more
system specific functions have not been available before, though, and this
module tries to remedy this by providing easy access to these functions.

%package	pspell
Summary:	Pspell extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}

%description	pspell
This is a dynamic shared object (DSO) for PHP that will add pspell support to
PHP.

These functions allow you to check the spelling of a word and offer
suggestions.

%package	readline
Summary:	Readline extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/readline
Requires:	%{libname} >= %{epoch}:%{version}

%description	readline
This PHP module adds support for readline functions (only for cli and cgi
SAPIs).

The readline() functions implement an interface to the GNU Readline library.
These are functions that provide editable command lines. An example being the
way Bash allows you to use the arrow keys to insert characters or scroll
through command history. Because of the interactive nature of this library, it
will be of little use for writing Web applications, but may be useful when
writing scripts used from a command line.

%package	recode
Summary:	Recode extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/recode
Requires:	%{libname} >= %{epoch}:%{version}

%description	recode
This is a dynamic shared object (DSO) for PHP that will add recode support
using the recode library.

This module contains an interface to the GNU Recode library. The GNU Recode
library converts files between various coded character sets and surface
encodings. When this cannot be achieved exactly, it may get rid of the
offending characters or fall back on approximations. The library recognises or
produces nearly 150 different character sets and is able to convert files
between almost any pair. Most RFC 1345 character sets are supported.

%package	session
Summary:	Session extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/session
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	webserver-base

%description	session
This is a dynamic shared object (DSO) for PHP that will add session support.

Session support in PHP consists of a way to preserve certain data across
subsequent accesses. This enables you to build more customized applications and
increase the appeal of your web site.

A visitor accessing your web site is assigned a unique id, the so-called
session id. This is either stored in a cookie on the user side or is propagated
in the URL.

%package	shmop
Summary:	Shared Memory Operations extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/shmop
Requires:	%{libname} >= %{epoch}:%{version}

%description	shmop
This is a dynamic shared object (DSO) for PHP that will add Shared Memory
Operations support.

Shmop is an easy to use set of functions that allows PHP to read, write, create
and delete Unix shared memory segments.

%package	snmp
Summary:	NET-SNMP extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/snmp
Requires:	net-snmp-mibs
Requires:	%{libname} >= %{epoch}:%{version}

%description	snmp
This is a dynamic shared object (DSO) for PHP that will add SNMP support using
the NET-SNMP libraries.

In order to use the SNMP functions you need to install the NET-SNMP package.

%package	soap
Summary:	Soap extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/soap
Requires:	%{libname} >= %{epoch}:%{version}

%description	soap
This is a dynamic shared object (DSO) for PHP that will add soap support.

The SOAP extension can be used to write SOAP Servers and Clients. It supports
subsets of SOAP 1.1, SOAP 1.2 and WSDL 1.1 specifications.

%package	sockets
Summary:	Sockets extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/sockets
Requires:	%{libname} >= %{epoch}:%{version}

%description	sockets
This is a dynamic shared object (DSO) for PHP that will add sockets support.

The socket extension implements a low-level interface to the socket
communication functions based on the popular BSD sockets, providing the
possibility to act as a socket server as well as a client.

%package	sqlite3
Summary:	SQLite database bindings for PHP
Group:		Development/PHP
URL:		http://www.php.net/sqlite3
Requires:	php-pdo >= %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}
Conflicts:	php-sqlite

%description	sqlite3
This is an extension for the SQLite Embeddable SQL Database Engine. SQLite is a
C library that implements an embeddable SQL database engine. Programs that link
with the SQLite library can have SQL database access without running a separate
RDBMS process.

SQLite is not a client library used to connect to a big database server. SQLite
is the server. The SQLite library reads and writes directly to and from the
database files on disk.

%package	sysvmsg
Summary:	SysV msg extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/sem
Requires:	%{libname} >= %{epoch}:%{version}

%description	sysvmsg
This is a dynamic shared object (DSO) for PHP that will add SysV message queues
support.

%package	sysvsem
Summary:	SysV sem extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/sem
Requires:	%{libname} >= %{epoch}:%{version}

%description	sysvsem
This is a dynamic shared object (DSO) for PHP that will add SysV semaphores
support.

%package	sysvshm
Summary:	SysV shm extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/sem
Requires:	%{libname} >= %{epoch}:%{version}

%description	sysvshm
This is a dynamic shared object (DSO) for PHP that will add SysV Shared Memory
support.

%package	tidy
Summary:	Tidy HTML Repairing and Parsing for PHP
Group:		Development/PHP
URL:		http://www.php.net/tidy
Requires:	%{libname} >= %{epoch}:%{version}

%description	tidy
Tidy is a binding for the Tidy HTML clean and repair utility which allows you
to not only clean and otherwise manipluate HTML documents, but also traverse
the document tree using the Zend Engine 2 OO semantics.

%package	tokenizer
Summary:	Tokenizer extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/tokenizer
Requires:	%{libname} >= %{epoch}:%{version}

%description	tokenizer
This is a dynamic shared object (DSO) for PHP that will add Tokenizer support.

The tokenizer functions provide an interface to the PHP tokenizer embedded in
the Zend Engine. Using these functions you may write your own PHP source
analyzing or modification tools without having to deal with the language
specification at the lexical level.

%package	xml
Summary:	XML extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/xml
Requires:	%{libname} >= %{epoch}:%{version}

%description	xml
This is a dynamic shared object (DSO) for PHP that will add XML support. This
extension lets you create XML parsers and then define handlers for different
XML events.

%package	xmlreader
Summary:	Xmlreader extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/xmlreader
Requires:	php-dom
Requires:	%{libname} >= %{epoch}:%{version}

%description	xmlreader
XMLReader represents a reader that provides non-cached, forward-only access to
XML data. It is based upon the xmlTextReader api from libxml

%package	xmlrpc
Summary:	Xmlrpc extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/xmlrpc
Requires:	%{libname} >= %{epoch}:%{version}

%description	xmlrpc
This is a dynamic shared object (DSO) for PHP that will add XMLRPC support.

These functions can be used to write XML-RPC servers and clients. You can find
more information about XML-RPC at http://www.xmlrpc.com/, and more
documentation on this extension and its functions at
http://xmlrpc-epi.sourceforge.net/.

%package	xmlwriter
Summary:	Provides fast, non-cached, forward-only means to write XML data
Group:		Development/PHP
URL:		http://www.php.net/xmlwriter
Requires:	%{libname} >= %{epoch}:%{version}

%description	xmlwriter
This extension wraps the libxml xmlWriter API. Represents a writer that
provides a non-cached, forward-only means of generating streams or files
containing XML data.

%package	xsl
Summary:	Xsl extension module for PHP
Group:		Development/PHP
URL:		http://www.php.net/xsl
Requires:	%{libname} >= %{epoch}:%{version}

%description	xsl
This is a dynamic shared object (DSO) for PHP that will add xsl support.

The XSL extension implements the XSL standard, performing XSLT transformations
using the libxslt library

%package	wddx
Summary:	WDDX serialization functions
Group:		Development/PHP
URL:		http://www.php.net/wddx
Requires:	php-xml
Requires:	%{libname} >= %{epoch}:%{version}

%description	wddx
This is a dynamic shared object (DSO) that adds wddx support to PHP. 

These functions are intended for work with WDDX (http://www.openwddx.org/)

%package	zip
Summary:	A zip management extension for PHP
Group:		Development/PHP
URL:		http://www.php.net/zip

%description	zip
This is a dynamic shared object (DSO) for PHP that will add zip support to
create and read zip files using the libzip library.

%package	fpm
Summary:	PHP7 FastCGI Process Manager
Group:		Development/Other
Requires(post): systemd >= %{systemd_required_version}
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	php-ctype >= %{epoch}:%{version}
Requires:	php-filter >= %{epoch}:%{version}
Requires:	php-ftp >= %{epoch}:%{version}
Requires:	php-gettext >= %{epoch}:%{version}
Requires:	php-hash >= %{epoch}:%{version}
Requires:	php-ini >= %{version}
Requires:	php-json >= %{epoch}:%{version}
Requires:	php-openssl >= %{epoch}:%{version}
Requires:	php-pcre >= %{epoch}:%{version}
Requires:	php-posix >= %{epoch}:%{version}
Requires:	php-session >= %{epoch}:%{version}
Recommends:	php-suhosin >= 0.9.33
Requires:	php-sysvsem >= %{epoch}:%{version}
Requires:	php-sysvshm >= %{epoch}:%{version}
Requires:	php-timezonedb >= 3:2012.3
Requires:	php-tokenizer >= %{epoch}:%{version}
Requires:	php-xmlreader >= %{epoch}:%{version}
Requires:	php-xmlwriter >= %{epoch}:%{version}
Requires:	php-zlib >= %{epoch}:%{version}
Requires:	php-xml >= %{epoch}:%{version}
Requires:	webserver-base
Provides:	php = %{epoch}:%{version}

%description	fpm
PHP7 is an HTML-embeddable scripting language. PHP7 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP7 is fairly simple. The
most common use of PHP7 coding is probably as a replacement for CGI scripts.

This package contains the FastCGI Process Manager. You must also install
libphp7_common.

%package -n	phpdbg
Summary:	The interactive PHP debugger
Group:		Development/Other
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	php >= %{epoch}:%{version}

%description -n	phpdbg
PHP7 is an HTML-embeddable scripting language. PHP7 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP7 is fairly simple. The
most common use of PHP7 coding is probably as a replacement for CGI scripts.

This package contains the The interactive PHP debugger. You must also install
libphp7_common.

Implemented as a SAPI module, phpdbg can excert complete control over the
environment without impacting the functionality or performance of your code.

phpdbg aims to be a lightweight, powerful, easy to use debugging platform for
PHP5.4+

%prep

%setup -q

%if %{build_libmagic}
if ! [ -f %{_datadir}/misc/magic.mgc ]; then
    echo "ERROR: the %{_datadir}/misc/magic.mgc file is needed"
    exit 1
fi
%endif

# the ".droplet" suffix is here to nuke the backups later..., we don't want those in php-devel


%patch1 -p1 -b .shared.droplet
%patch2 -p1 -b .mga_php.ini.droplet
%patch3 -p1 -b .libtool.droplet
%patch5 -p1 -b .phpbuilddir.droplet
%patch6 -p1 -b .apache2-filters.droplet
%patch7 -p1 -b .no_libedit.droplet
%patch8 -p1 -b .xmlrpc_epi_header
%patch9 -p1 -b .xmlrpc_no_rpath.droplet
%patch11 -p1 -b .libdb.droplet
%patch12 -p1 -b .mysqlnd-unix-sock-addr.droplet
%patch13 -p1 -b .clangwarn~.droplet

#####################################################################
# Stolen from PLD
%patch21 -p0 -b .filter-shared.droplet
%patch22 -p1 -b .dba-link.droplet
%patch23 -p1 -b .zlib-for-getimagesize.droplet
%patch26 -p0 -b .mcrypt-libs.droplet

# fpm stuff
%patch29 -p1 -b .shared-fpm.droplet
%patch30 -p1 -b .fpmmdv.droplet

#Stolen from remi - Functional changes
%patch48 -p1 -b .loadconf.droplet
#####################################################################
# stolen from debian
%patch50 -p1 -b .session.save_path.droplet
%patch51 -p0 -b .exif_nesting_level.droplet

#####################################################################
# Stolen from fedora
%patch101 -p1 -b .cxx.droplet
%patch102 -p1 -b .install.droplet
%patch105 -p1 -b .umask.droplet
%patch113 -p1 -b .libc-client-php.droplet
%patch114 -p0 -b .no_pam_in_c-client.droplet
%patch115 -p1 -b .dlopen.droplet

# upstream fixes
%patch120 -p1 -b .tests-wddx.droplet
%patch121 -p1 -b .bug43221.droplet
%patch123 -p1 -b .bug43589.droplet
%patch226 -p1 -b .no-fvisibility_hidden.droplet
%patch227 -p0 -b .enchant_lib64_fix.droplet
%patch229 -p1 -b .session.use_strict_mode.droplet

#Stolen from remi - Build fixes
%patch230 -p1 -b .includedir.droplet
%patch300 -p1 -b .datetests.droplet

cp %{SOURCE1} php-test.ini
cp %{SOURCE4} php-fpm.service
cp %{SOURCE5} php-fpm.sysconf
cp %{SOURCE6} php-fpm.logrotate
cp %{SOURCE7} create_data_file.php



# nuke bogus checks becuase i fixed this years ago in our recode package
rm -f ext/recode/config9.m4

# Change perms otherwise rpm would get fooled while finding requires
find -name "*.inc" | xargs chmod 644
find -name "*.php*" | xargs chmod 644
find -name "*README*" | xargs chmod 644


# php7_module -> php_module to ease upgrades
find -type f |xargs sed -i -e 's,php7_module,php_module,g'
sed -i -e 's,APLOG_USE_MODULE(php7,APLOG_USE_MODULE(php,g' sapi/apache2handler/*

mkdir -p php-devel/extensions
mkdir -p php-devel/sapi

# Install test files in php-devel
cp -a tests php-devel

cp -dpR ext/* php-devel/extensions/
rm -f php-devel/extensions/informix/stub.c
rm -f php-devel/extensions/standard/.deps
rm -f php-devel/extensions/skeleton/EXPERIMENTAL

# SAPI
cp -dpR sapi/* php-devel/sapi/ 
rm -f php-devel/sapi/thttpd/stub.c
rm -f php-devel/sapi/cgi/php.sym
rm -f php-devel/sapi/fastcgi/php.sym
rm -f php-devel/sapi/pi3web/php.sym

# cleanup
find php-devel -name "*.droplet" | xargs rm -f

# don't ship MS Windows source
rm -rf php-devel/extensions/com_dotnet

# https://bugs.php.net/63362 - Not needed but installed headers.
# Drop some Windows specific headers to avoid installation,
# before build to ensure they are really not needed.
rm -f TSRM/tsrm_win32.h \
      TSRM/tsrm_config.w32.h \
      Zend/zend_config.w32.h \
      ext/mysqlnd/config-win.h \
      ext/standard/winver.h \
      main/win32_internal_function_disabled.h \
      main/win95nt.h

# likewise with these:
find php-devel -name "*.dsp" | xargs rm -f
find php-devel -name "*.mak" | xargs rm -f
find php-devel -name "*.w32" | xargs rm

# make sure using system libs
rm -rf ext/pcre/pcrelib
rm -rf ext/pdo_sqlite/sqlite
rm -rf ext/xmlrpc/libxmlrpc

%build
%serverbuild

# it does not work with -fPIE and someone added that to the serverbuild macro...
CFLAGS=`echo $CFLAGS|sed -e 's|-fPIE||g'`
CXXFLAGS=`echo $CXXFLAGS|sed -e 's|-fPIE||g'`

#export CFLAGS="`echo ${CFLAGS} | sed s/O2/O0/` -fPIC -L%{_libdir} -fno-strict-aliasing"
export CFLAGS="${CFLAGS} -fPIC -L%{_libdir} -fno-strict-aliasing"
export CXXFLAGS="${CFLAGS}"
export RPM_OPT_FLAGS="${CFLAGS}"

cat > php-devel/buildext <<EOF
#!/bin/bash
gcc -Wall -fPIC -shared $CFLAGS \\
    -I. \`%{_bindir}/php-config --includes\` \\
    -I%{_includedir}/libxml2 \\
    -I%{_includedir}/freetype \\
    -I%{_includedir}/openssl \\
    -I%{_usrsrc}/php-devel/ext \\
    -I%{_includedir}/\$1 \\
    \$4 \$2 -o \$1.so \$3 -lc
EOF

chmod 755 php-devel/buildext

#export PHP_AUTOCONF=autoconf-2.13
rm -f configure
rm -rf autom4te.cache
./buildconf --force

# Do this patch with a perl hack...
perl -pi -e "s|'\\\$install_libdir'|'%{_libdir}'|" ltmain.sh

export oldstyleextdir=yes
export EXTENSION_DIR="%{_libdir}/php/extensions"
export PROG_SENDMAIL="%{_sbindir}/sendmail"
export GD_SHARED_LIBADD="$GD_SHARED_LIBADD -lm"
SAFE_LDFLAGS=`echo %{ldflags}|sed -e 's|-Wl,--no-undefined||g'`
export LDFLAGS="$SAFE_LDFLAGS"

# never use "--disable-rpath", it does the opposite

# Configure php7
for i in fpm cgi cli apxs; do
./configure \
    `[ $i = fpm ] && echo --disable-cli --enable-fpm --with-libxml-dir=%{_prefix} --with-fpm-user=apache --with-fpm-group=apache --with-fpm-systemd` \
    `[ $i = cgi ] && echo --disable-cli` \
    `[ $i = cli ] && echo --disable-cgi --enable-cli` \
    `[ $i = apxs ] && echo --with-apxs2=%{_httpd_apxs}` \
    --build=%{_build} \
    --prefix=%{_prefix} \
    --exec-prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --sysconfdir=%{_sysconfdir} \
    --datadir=%{_datadir} \
    --includedir=%{_includedir} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libexecdir} \
    --localstatedir=/var/lib \
    --mandir=%{_mandir} \
    --enable-shared=yes \
    --enable-static=no \
    --with-libdir=%{_lib} \
    --with-config-file-path=%{_sysconfdir} \
    --with-config-file-scan-dir=%{_sysconfdir}/php.d \
    --disable-debug  \
    --enable-inline-optimization \
    --with-pcre-regex=%{_prefix} \
    --with-freetype-dir=%{_prefix} --with-zlib=%{_prefix} \
    --with-png-dir=%{_prefix} \
    --with-pdo-odbc=unixODBC \
    --with-zlib=shared,%{_prefix} --with-zlib-dir=%{_prefix} \
    --with-openssl=shared,%{_prefix} \
    --enable-libxml=%{_prefix} --with-libxml-dir=%{_prefix} \
    --without-pear \
    --enable-bcmath=shared \
    --with-bz2=shared,%{_prefix} \
    --enable-calendar=shared \
    --enable-ctype=shared \
    --with-curl=shared,%{_prefix} \
    --enable-dba=shared --with-gdbm --with-db4 --with-cdb  \
    --enable-dom=shared,%{_prefix} --with-libxml-dir=%{_prefix} \
    --with-enchant=shared,%{_prefix} \
    --enable-exif=shared \
    --enable-fileinfo=shared \
    --enable-filter=shared --with-pcre-dir=%{_prefix} \
    --enable-intl=shared --with-icu-dir=%{_prefix} \
    --enable-json=shared \
    --with-openssl-dir=%{_prefix} --enable-ftp=shared \
    --with-gd=shared,%{_prefix} --with-jpeg-dir=%{_prefix} --with-png-dir=%{_prefix} --with-zlib-dir=%{_prefix} --with-xpm-dir=%{_prefix}/X11R6 --with-freetype-dir=%{_prefix} --enable-gd-native-ttf \
    --with-gettext=shared,%{_prefix} \
    --with-gmp=shared,%{_prefix} \
    --enable-hash=shared,%{_prefix} \
    --with-iconv=shared \
    --with-imap=shared,%{_prefix} --with-imap-ssl=%{_prefix} \
    --with-ldap=shared,%{_prefix} --with-ldap-sasl=%{_prefix} \
    --enable-mbstring=shared,%{_prefix} --enable-mbregex --with-libmbfl=%{_prefix} --with-onig=%{_prefix} \
    --with-mcrypt=shared,%{_prefix} \
    --with-mysql-sock=/var/lib/mysql/mysql.sock --with-zlib-dir=%{_prefix} \
    --with-mysqli=shared,%{_bindir}/mysql_config \
    --enable-mysqlnd=shared,%{_prefix} \
    --with-unixODBC=shared,%{_prefix} \
    --enable-opcache=shared \
    --enable-pcntl=shared \
    --enable-pdo=shared,%{_prefix} --with-pdo-dblib=shared,%{_prefix} --with-pdo-mysql=shared,%{_prefix} --with-pdo-odbc=shared,unixODBC,%{_prefix} --with-pdo-pgsql=shared,%{_prefix} --with-pdo-sqlite=shared,%{_prefix} \
    --with-pgsql=shared,%{_prefix} \
    --enable-phar=shared \
    --enable-posix=shared \
    --with-pspell=shared,%{_prefix} \
    --with-readline=shared,%{_prefix} \
    --with-recode=shared,%{_prefix} \
    --enable-session=shared,%{_prefix} \
    --enable-shmop=shared,%{_prefix} \
    --enable-simplexml \
    --with-snmp=shared,%{_prefix} \
    --enable-soap=shared,%{_prefix} --with-libxml-dir=%{_prefix} \
    --enable-sockets=shared,%{_prefix} \
    --with-sqlite3=shared,%{_prefix} \
    --enable-sysvmsg=shared,%{_prefix} \
    --enable-sysvsem=shared,%{_prefix} \
    --enable-sysvshm=shared,%{_prefix} \
    --with-tidy=shared,%{_prefix} \
    --enable-tokenizer=shared,%{_prefix} \
    --enable-xml=shared,%{_prefix} --with-libxml-dir=%{_prefix} \
    --enable-xmlreader=shared,%{_prefix} \
    --with-xmlrpc=shared,%{_prefix} \
    --enable-xmlwriter=shared,%{_prefix} \
    --with-xsl=shared,%{_prefix} \
    --enable-wddx=shared --with-libxml-dir=%{_prefix} \
    --enable-zip=shared --with-libzip=%{_prefix} \
    --with-interbase=shared,%{_libdir}/firebird --with-pdo-firebird=shared,%{_libdir}/firebird \
    --enable-phpdbg

cp -f Makefile Makefile.$i

# left for debugging purposes
cp -f main/php_config.h php_config.h.$i

# when all else failed...
perl -pi -e "s|-prefer-non-pic -static||g" Makefile.$i

done

# remove all confusion...
perl -pi -e "s|^#define CONFIGURE_COMMAND .*|#define CONFIGURE_COMMAND \"This is irrelevant, look inside the %{_docdir}/php-doc/configure_command file. urpmi is your friend, use it to install extensions not shown below.\"|g" main/build-defs.h
cp config.nice configure_command; chmod 644 configure_command

%make PHPDBG_EXTRA_LIBS="-lreadline"

%if %{build_libmagic}
# keep in sync with latest system magic, the next best thing when system libmagic can't be used...
sapi/cli/php create_data_file.php %{_datadir}/misc/magic.mgc > ext/fileinfo/data_file.c
rm -rf ext/fileinfo/.libs ext/fileinfo/*.lo ext/fileinfo/*.la modules/fileinfo.so modules/fileinfo.la
cp -p ext/fileinfo/data_file.c php-devel/extensions/fileinfo/data_file.c
%make
%endif

# make php-cgi
cp -af php_config.h.cgi main/php_config.h
make -f Makefile.cgi sapi/cgi/php-cgi
cp -af php_config.h.apxs main/php_config.h

# make php-fpm
cp -af php_config.h.fpm main/php_config.h
make -f Makefile.fpm sapi/fpm/php-fpm
cp -af php_config.h.apxs main/php_config.h

# make apache-mod_php
mkdir mod_php
cd mod_php
cp -dpR ../php-devel/sapi/apache2handler/* .
cp ../main/internal_functions.c .
cp ../ext/date/lib/timelib_config.h .
mv mod_php7.c mod_php.c
find . -type f |xargs dos2unix
apxs \
	`apr-1-config --link-ld --libs` \
	`xml2-config --cflags` \
	-I. -I.. -I../main -I../Zend -I../TSRM \
	-L../libs -lphp7_common \
	-c mod_php.c sapi_apache2.c apache_config.c \
	php_functions.c internal_functions.c

%install

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}/php.d
install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_usrsrc}/php-devel
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_sysconfdir}/cron.d
install -d %{buildroot}/var/lib/php
install -d %{buildroot}%{_datadir}/php

make -f Makefile.apxs install \
	INSTALL_ROOT=%{buildroot} \
	INSTALL_IT="\$(LIBTOOL) --mode=install install libphp7_common.la %{buildroot}%{_libdir}/"

# borked autopoo
rm -f %{buildroot}%{_bindir}/php %{buildroot}%{_bindir}/php-cgi %{buildroot}%{_bindir}/phpdbg
./libtool --silent --mode=install install sapi/cli/php %{buildroot}%{_bindir}/php
./libtool --silent --mode=install install sapi/cgi/php-cgi %{buildroot}%{_bindir}/php-cgi
./libtool --silent --mode=install install sapi/phpdbg/phpdbg %{buildroot}%{_bindir}/phpdbg

# compat php-fcgi symink
ln -s php-cgi %{buildroot}%{_bindir}/php-fcgi

cp -dpR php-devel/* %{buildroot}%{_usrsrc}/php-devel/
install -m0644 run-tests*.php %{buildroot}%{_usrsrc}/php-devel/
install -m0644 main/internal_functions.c %{buildroot}%{_usrsrc}/php-devel/

install -m0644 sapi/cli/php.1 %{buildroot}%{_mandir}/man1/
install -m0644 scripts/man1/phpize.1 %{buildroot}%{_mandir}/man1/
install -m0644 scripts/man1/php-config.1 %{buildroot}%{_mandir}/man1/

# fpm
install -d %{buildroot}%{_unitdir}
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -d %{buildroot}%{_sysconfdir}/php-fpm.d
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man8
install -d %{buildroot}/var/lib/php-fpm
install -d %{buildroot}/var/log/php-fpm
install -D -p -m 0644 %{SOURCE9} %{buildroot}%{_tmpfilesdir}/php-fpm.conf
# a small bug here...
echo "; place your config here" > %{buildroot}%{_sysconfdir}/php-fpm.d/default.conf

./libtool --silent --mode=install install sapi/fpm/php-fpm %{buildroot}%{_sbindir}/php-fpm
install -m0644 sapi/fpm/php-fpm.8 %{buildroot}%{_mandir}/man8/
install -m0644 sapi/fpm/php-fpm.conf %{buildroot}%{_sysconfdir}/
install -m0644 php-fpm.service %{buildroot}%{_unitdir}/php-fpm.service
install -m0644 php-fpm.sysconf %{buildroot}%{_sysconfdir}/sysconfig/php-fpm
install -m0644 php-fpm.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/php-fpm

# adjust a bit
perl -pi -e "s|^pid.*|pid = /run/php-fpm/php-fpm.pid|g" %{buildroot}%{_sysconfdir}/php-fpm.conf

ln -snf extensions %{buildroot}%{_usrsrc}/php-devel/ext

# extensions
echo "extension = openssl.so"		> %{buildroot}%{_sysconfdir}/php.d/21_openssl.ini
echo "extension = zlib.so"		> %{buildroot}%{_sysconfdir}/php.d/21_zlib.ini
echo "extension = bcmath.so"		> %{buildroot}%{_sysconfdir}/php.d/66_bcmath.ini
echo "extension = bz2.so"		> %{buildroot}%{_sysconfdir}/php.d/10_bz2.ini
echo "extension = calendar.so"		> %{buildroot}%{_sysconfdir}/php.d/11_calendar.ini
echo "extension = ctype.so"		> %{buildroot}%{_sysconfdir}/php.d/12_ctype.ini
echo "extension = curl.so"		> %{buildroot}%{_sysconfdir}/php.d/13_curl.ini
echo "extension = dba.so"		> %{buildroot}%{_sysconfdir}/php.d/14_dba.ini
echo "extension = dom.so"		> %{buildroot}%{_sysconfdir}/php.d/18_dom.ini
echo "extension = exif.so"		> %{buildroot}%{_sysconfdir}/php.d/19_exif.ini
echo "extension = filter.so"		> %{buildroot}%{_sysconfdir}/php.d/81_filter.ini
echo "extension = ftp.so"		> %{buildroot}%{_sysconfdir}/php.d/22_ftp.ini
echo "extension = gd.so"		> %{buildroot}%{_sysconfdir}/php.d/23_gd.ini
echo "extension = gettext.so"		> %{buildroot}%{_sysconfdir}/php.d/24_gettext.ini
echo "extension = gmp.so"		> %{buildroot}%{_sysconfdir}/php.d/25_gmp.ini
echo "extension = hash.so"		> %{buildroot}%{_sysconfdir}/php.d/54_hash.ini
echo "extension = iconv.so"		> %{buildroot}%{_sysconfdir}/php.d/26_iconv.ini
echo "extension = imap.so"		> %{buildroot}%{_sysconfdir}/php.d/27_imap.ini
echo "extension = intl.so"		> %{buildroot}%{_sysconfdir}/php.d/27_intl.ini
echo "extension = ldap.so"		> %{buildroot}%{_sysconfdir}/php.d/28_ldap.ini
echo "extension = mbstring.so"		> %{buildroot}%{_sysconfdir}/php.d/29_mbstring.ini
echo "extension = mcrypt.so"		> %{buildroot}%{_sysconfdir}/php.d/30_mcrypt.ini
echo "extension = fileinfo.so"		> %{buildroot}%{_sysconfdir}/php.d/32_fileinfo.ini
echo "extension = mysqlnd.so"           > %{buildroot}%{_sysconfdir}/php.d/33_mysqlnd.ini
echo "extension = mysqli.so"		> %{buildroot}%{_sysconfdir}/php.d/37_mysqli.ini
echo "extension = enchant.so"		> %{buildroot}%{_sysconfdir}/php.d/38_enchant.ini
echo "extension = odbc.so"		> %{buildroot}%{_sysconfdir}/php.d/39_odbc.ini
echo "extension = pcntl.so"		> %{buildroot}%{_sysconfdir}/php.d/40_pcntl.ini
echo "extension = interbase.so"		> %{buildroot}%{_sysconfdir}/php.d/42_interbase.ini
echo "extension = pdo.so"		> %{buildroot}%{_sysconfdir}/php.d/70_pdo.ini
echo "extension = pdo_dblib.so"		> %{buildroot}%{_sysconfdir}/php.d/71_pdo_dblib.ini
echo "extension = pdo_mysql.so"		> %{buildroot}%{_sysconfdir}/php.d/73_pdo_mysql.ini
echo "extension = pdo_odbc.so"		> %{buildroot}%{_sysconfdir}/php.d/75_pdo_odbc.ini
echo "extension = pdo_pgsql.so"		> %{buildroot}%{_sysconfdir}/php.d/76_pdo_pgsql.ini
echo "extension = pdo_sqlite.so"	> %{buildroot}%{_sysconfdir}/php.d/77_pdo_sqlite.ini
echo "extension = pdo_firebird.so"	> %{buildroot}%{_sysconfdir}/php.d/78_pdo_firebird.ini
echo "extension = pgsql.so"		> %{buildroot}%{_sysconfdir}/php.d/42_pgsql.ini
echo "extension = posix.so"		> %{buildroot}%{_sysconfdir}/php.d/43_posix.ini
echo "extension = pspell.so"		> %{buildroot}%{_sysconfdir}/php.d/44_pspell.ini
echo "extension = readline.so"		> %{buildroot}%{_sysconfdir}/php.d/45_readline.ini
echo "extension = recode.so"		> %{buildroot}%{_sysconfdir}/php.d/46_recode.ini
echo "extension = session.so"		> %{buildroot}%{_sysconfdir}/php.d/47_session.ini
echo "session.gc_maxlifetime = 1440"	>> %{buildroot}%{_sysconfdir}/php.d/47_session.ini
echo "extension = shmop.so"		> %{buildroot}%{_sysconfdir}/php.d/48_shmop.ini
echo "extension = snmp.so"		> %{buildroot}%{_sysconfdir}/php.d/50_snmp.ini
echo "extension = soap.so"		> %{buildroot}%{_sysconfdir}/php.d/51_soap.ini
echo "extension = sockets.so"		> %{buildroot}%{_sysconfdir}/php.d/52_sockets.ini
echo "extension = sqlite3.so"		> %{buildroot}%{_sysconfdir}/php.d/78_sqlite3.ini
echo "extension = sysvmsg.so"		> %{buildroot}%{_sysconfdir}/php.d/56_sysvmsg.ini
echo "extension = sysvsem.so"		> %{buildroot}%{_sysconfdir}/php.d/57_sysvsem.ini
echo "extension = sysvshm.so"		> %{buildroot}%{_sysconfdir}/php.d/58_sysvshm.ini
echo "extension = tidy.so"		> %{buildroot}%{_sysconfdir}/php.d/59_tidy.ini
echo "extension = tokenizer.so"		> %{buildroot}%{_sysconfdir}/php.d/60_tokenizer.ini
echo "extension = xml.so"		> %{buildroot}%{_sysconfdir}/php.d/62_xml.ini
echo "extension = xmlreader.so"		> %{buildroot}%{_sysconfdir}/php.d/63_xmlreader.ini
echo "extension = xmlrpc.so"		> %{buildroot}%{_sysconfdir}/php.d/62_xmlrpc.ini
echo "extension = xmlwriter.so"		> %{buildroot}%{_sysconfdir}/php.d/64_xmlwriter.ini
echo "extension = xsl.so"		> %{buildroot}%{_sysconfdir}/php.d/63_xsl.ini
echo "extension = wddx.so"		> %{buildroot}%{_sysconfdir}/php.d/63_wddx.ini
echo "extension = json.so"		> %{buildroot}%{_sysconfdir}/php.d/82_json.ini
echo "extension = zip.so"		> %{buildroot}%{_sysconfdir}/php.d/83_zip.ini
echo "extension = phar.so"		> %{buildroot}%{_sysconfdir}/php.d/84_phar.ini
cat > %{buildroot}%{_sysconfdir}/php.d/99_opcache.ini <<"EOF"
zend_extension = opcache.so
opcache.memory_consumption=128
opcache.interned_strings_buffer=8
opcache.max_accelerated_files=4000
opcache.revalidate_freq=60
opcache.fast_shutdown=1
opcache.enable_cli=1
EOF

install -m0755 %{SOURCE2} %{buildroot}%{_libdir}/php/maxlifetime
install -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/cron.d/php
install -m0644 php.ini-production %{buildroot}%{_sysconfdir}/php.ini
install -m0644 php.ini-production %{buildroot}%{_sysconfdir}/php-cgi-fcgi.ini

# mod_php
install -d %{buildroot}%{_sysconfdir}/httpd/conf/modules.d
install -d %{buildroot}%{_libdir}/httpd/modules
install -m 755 mod_php/.libs/*.so %{buildroot}%{_httpd_moddir}
#install -m0755 .libs/libphp7.so %{buildroot}%{_httpd_moddir}/%{mod_name}.so

cat > %{buildroot}%{_httpd_modconfdir}/%{load_order}_%{mod_name}.conf <<EOF
LoadModule php_module modules/%{mod_name}.so

AddType application/x-httpd-php .php
AddType application/x-httpd-php .phtml
AddType application/x-httpd-php-source .phps

DirectoryIndex index.php index.phtml
EOF

# lib64 hack
perl -pi -e "s|/usr/lib|%{_libdir}|" \
    %{buildroot}%{_sysconfdir}/cron.d/php \
    %{buildroot}%{_sysconfdir}/php.ini \
    %{buildroot}%{_sysconfdir}/php-cgi-fcgi.ini \
    php.ini-production \
    php.ini-development

# install doc manually in %{_docdir}/php, rather than %{_docdir}/php-doc
install -d -m 755 %{buildroot}%{_docdir}/php
install -m 644 \
    CREDITS INSTALL LICENSE NEWS \
    php.ini-production php.ini-development \
    README.EXT_SKEL \
    README.input_filter README.PARAMETER_PARSING_API README.STREAMS \
    %{buildroot}%{_docdir}/php

# fix docs
cp Zend/LICENSE Zend/ZEND_LICENSE
cp README.SELF-CONTAINED-EXTENSIONS SELF-CONTAINED-EXTENSIONS
cp ext/openssl/README README.openssl
cp ext/spl/README README.spl
cp ext/libxml/CREDITS CREDITS.libxml
cp ext/zlib/CREDITS CREDITS.zlib

# cgi docs
cp sapi/cgi/CREDITS CREDITS.cgi
cp sapi/cgi/README.FastCGI README.fcgi

# cli docs
cp sapi/cli/CREDITS CREDITS.cli
cp sapi/cli/README README.cli
cp sapi/cli/TODO TODO.cli

# phar fixes
if [ -L %{buildroot}%{_bindir}/phar ]; then
    rm -f %{buildroot}%{_bindir}/phar
    mv %{buildroot}%{_bindir}/phar.phar %{buildroot}%{_bindir}/phar
fi

# house cleaning
rm -f %{buildroot}%{_bindir}/pear
rm -f %{buildroot}%{_libdir}/*.*a

# don't pack useless stuff
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/bcmath
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/bz2
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/calendar
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/ctype
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/curl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/dba
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/dom
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/enchant
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/ereg
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/exif
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/fileinfo
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/filter
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/ftp
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/gettext
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/gmp
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/hash
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/iconv
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/imap
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/intl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/json
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/ldap
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/libxml
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mbstring
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mcrypt
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mysql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mysqli
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mysqlnd
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/odbc
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/openssl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pcntl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pcre
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_dblib
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_mysql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_odbc
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_pgsql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_sqlite
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pgsql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/phar
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/posix
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pspell
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/readline
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/recode
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/shmop
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/snmp
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/soap
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sockets
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/spl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sqlite
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sqlite3
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/standard
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sysvmsg
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sysvsem
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sysvshm
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/tidy
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/tokenizer
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/wddx
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xml
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xmlreader
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xmlrpc
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xmlwriter
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xsl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/zip
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/zlib

# php-devel.i586: E: zero-length /usr/src/php-devel/extensions/pdo_firebird/EXPERIMENTAL
find %{buildroot}%{_usrsrc}/php-devel -type f -size 0 -exec rm -f {} \;

%multiarch_includes %{buildroot}%{_includedir}/php/main/build-defs.h

%multiarch_includes %{buildroot}%{_includedir}/php/main/php_config.h

%if %{build_test}
# do a make test
export NO_INTERACTION=1
export PHPRC="."
export REPORT_EXIT_STATUS=2
export MALLOC_CHECK_=2
export SKIP_ONLINE_TESTS=1
export TEST_PHP_DETAILED=0
export TEST_PHP_ERROR_STYLE=EMACS
export TEST_PHP_LOG_FORMAT=LEODC
export PHP_INI_SCAN_DIR=/dev/null

# FAILING TESTS:
# unknown errors with ext/date/tests/oo_002.phpt probably because of php-5.2.5-systzdata.patch
# http://bugs.php.net/bug.php?id=22414 (claimed to be fixed in 2003, but seems not)
# unknown errors with ext/standard/tests/general_functions/phpinfo.phpt
# unknown errors with ext/standard/tests/strings/setlocale_*
disable_tests="ext/date/tests/oo_002.phpt \
ext/standard/tests/file/bug22414.phpt \
ext/standard/tests/general_functions/phpinfo.phpt \
ext/standard/tests/strings/setlocale_basic1.phpt \
ext/standard/tests/strings/setlocale_basic2.phpt \
ext/standard/tests/strings/setlocale_basic3.phpt \
ext/standard/tests/strings/setlocale_variation1.phpt \
ext/standard/tests/strings/setlocale_variation3.phpt \
ext/standard/tests/strings/setlocale_variation4.phpt \
ext/standard/tests/strings/setlocale_variation5.phpt"

[[ -n "$disable_tests" ]] && \
for f in $disable_tests; do
  [[ -f "$f" ]] && mv $f $f.disabled
done

cat >php-test.ini <<EOF
[PHP]
extension_dir="`pwd`/modules"
EOF
for i in modules/*.so; do
	B="`basename $i`"
	case "$B" in
	opcache.so)
		echo zend_extension=$B >>php-test.ini
		;;
	wddx.so|xsl.so)
		# Unresolved symbols, need fixing
		;;
#	ctype.so|dom.so|openssl.so|zlib.so|ftp.so|gettext.so|posix.so|session.so|hash.so|sysvsem.so|sysvshm.so|tokenizer.so|xml.so|xmlreader.so|xmlwriter.so|filter.so|json.so)
		# Apparently loaded by default without a need to mention them in the ini file
#		;;
	*)
		echo extension=$B >>php-test.ini
		;;
	esac
done
cat >>php-test.ini <<EOF
open_basedir="`pwd`"
safe_mode=0
output_buffering=0
output_handler=0
magic_quotes_runtime=0
memory_limit=1G

[Session]
session.save_path="`pwd`"
EOF

TEST_PHP_EXECUTABLE=sapi/cli/php sapi/cli/php -n -c ./php-test.ini run-tests.php
%endif

%post fpm
%_tmpfilescreate php-fpm
%_post_service php-fpm

%preun fpm
%_preun_service php-fpm

# rpm filetrigger to reload httpd when installing/removing php extensions
%transfiletriggerin --  %{_libdir}/php/extensions/
systemctl reload-or-try-restart httpd.service || :

%files doc
%doc CREDITS INSTALL LICENSE NEWS Zend/ZEND_LICENSE 
%doc php.ini-production php.ini-development
%doc README.openssl README.spl CREDITS.libxml CREDITS.zlib
%doc README.EXT_SKEL README.input_filter
%doc README.PARAMETER_PARSING_API README.STREAMS

%files ini
%{_docdir}/php
%config(noreplace) %{_sysconfdir}/php.ini
%config(noreplace) %{_sysconfdir}/php-cgi-fcgi.ini
%dir %{_sysconfdir}/php.d
%dir %{_libdir}/php
%dir %{_datadir}/php
%dir %{_libdir}/php/extensions

%files -n apache-mod_php
%config(noreplace) %{_httpd_modconfdir}/*.conf
%{_httpd_moddir}/mod_php.so

%files -n %{libname}
%{_libdir}/libphp7_common.so.%{php7_common_major}*

%files cli
%doc CREDITS.cli README.cli TODO.cli
%{_bindir}/php
%{_mandir}/man1/php.1*

%files cgi
%doc CREDITS.cgi README.fcgi
%{_bindir}/php-cgi
%{_bindir}/php-fcgi
%{_mandir}/man1/php-cgi.1*

%files devel
%doc SELF-CONTAINED-EXTENSIONS CODING_STANDARDS README.* EXTENSIONS
%doc Zend/ZEND_* README.TESTING*
%{_bindir}/php-config
%{_bindir}/phpize
%{_libdir}/libphp7_common.so
%{_libdir}/php/build
%{_usrsrc}/php-devel
%{multiarch_includedir}/php/main/build-defs.h
%{multiarch_includedir}/php/main/php_config.h
%{_includedir}/php
%{_mandir}/man1/php-config.1*
%{_mandir}/man1/phpize.1*

%files openssl
%config(noreplace) %{_sysconfdir}/php.d/21_openssl.ini
%{_libdir}/php/extensions/openssl.so

%files zlib
%config(noreplace) %{_sysconfdir}/php.d/21_zlib.ini
%{_libdir}/php/extensions/zlib.so

%files bcmath
%config(noreplace) %{_sysconfdir}/php.d/66_bcmath.ini
%{_libdir}/php/extensions/bcmath.so

%files bz2
%config(noreplace) %{_sysconfdir}/php.d/10_bz2.ini
%{_libdir}/php/extensions/bz2.so

%files calendar
%config(noreplace) %{_sysconfdir}/php.d/11_calendar.ini
%{_libdir}/php/extensions/calendar.so

%files ctype
%config(noreplace) %{_sysconfdir}/php.d/12_ctype.ini
%{_libdir}/php/extensions/ctype.so

%files curl
%config(noreplace) %{_sysconfdir}/php.d/13_curl.ini
%{_libdir}/php/extensions/curl.so

%files dba
%config(noreplace) %{_sysconfdir}/php.d/14_dba.ini
%{_libdir}/php/extensions/dba.so

%files dom
%config(noreplace) %{_sysconfdir}/php.d/18_dom.ini
%{_libdir}/php/extensions/dom.so

%files enchant
%config(noreplace) %{_sysconfdir}/php.d/38_enchant.ini
%{_libdir}/php/extensions/enchant.so

%files exif
%config(noreplace) %{_sysconfdir}/php.d/19_exif.ini
%{_libdir}/php/extensions/exif.so

%files fileinfo
%config(noreplace) %{_sysconfdir}/php.d/32_fileinfo.ini
%{_libdir}/php/extensions/fileinfo.so

%files filter
%config(noreplace) %{_sysconfdir}/php.d/81_filter.ini
%{_libdir}/php/extensions/filter.so

%files ftp
%config(noreplace) %{_sysconfdir}/php.d/22_ftp.ini
%{_libdir}/php/extensions/ftp.so

%files gd
%config(noreplace) %{_sysconfdir}/php.d/23_gd.ini
%{_libdir}/php/extensions/gd.so

%files gettext
%config(noreplace) %{_sysconfdir}/php.d/24_gettext.ini
%{_libdir}/php/extensions/gettext.so

%files gmp
%config(noreplace) %{_sysconfdir}/php.d/25_gmp.ini
%{_libdir}/php/extensions/gmp.so

%files hash
%config(noreplace) %{_sysconfdir}/php.d/54_hash.ini
%{_libdir}/php/extensions/hash.so

%files iconv
%config(noreplace) %{_sysconfdir}/php.d/26_iconv.ini
%{_libdir}/php/extensions/iconv.so

%files imap
%config(noreplace) %{_sysconfdir}/php.d/27_imap.ini
%{_libdir}/php/extensions/imap.so

%files interbase
%config(noreplace) %{_sysconfdir}/php.d/42_interbase.ini
%{_libdir}/php/extensions/interbase.so

%files intl
%config(noreplace) %{_sysconfdir}/php.d/27_intl.ini
%{_libdir}/php/extensions/intl.so

%files json
%config(noreplace) %{_sysconfdir}/php.d/82_json.ini
%{_libdir}/php/extensions/json.so

%files ldap
%config(noreplace) %{_sysconfdir}/php.d/28_ldap.ini
%{_libdir}/php/extensions/ldap.so

%files mbstring
%config(noreplace) %{_sysconfdir}/php.d/29_mbstring.ini
%{_libdir}/php/extensions/mbstring.so

%files mcrypt
%config(noreplace) %{_sysconfdir}/php.d/30_mcrypt.ini
%{_libdir}/php/extensions/mcrypt.so

%files mysqli
%config(noreplace) %{_sysconfdir}/php.d/37_mysqli.ini
%{_libdir}/php/extensions/mysqli.so

%files mysqlnd
%config(noreplace) %{_sysconfdir}/php.d/33_mysqlnd.ini
%{_libdir}/php/extensions/mysqlnd.so

%files odbc
%config(noreplace) %{_sysconfdir}/php.d/39_odbc.ini
%{_libdir}/php/extensions/odbc.so

%files opcache
%config(noreplace) %{_sysconfdir}/php.d/99_opcache.ini
%{_libdir}/php/extensions/opcache.so

%files pcntl
%config(noreplace) %{_sysconfdir}/php.d/40_pcntl.ini
%{_libdir}/php/extensions/pcntl.so

%files pdo
%config(noreplace) %{_sysconfdir}/php.d/70_pdo.ini
%{_libdir}/php/extensions/pdo.so

%files pdo_dblib
%config(noreplace) %{_sysconfdir}/php.d/71_pdo_dblib.ini
%{_libdir}/php/extensions/pdo_dblib.so

%files pdo_firebird
%config(noreplace) %{_sysconfdir}/php.d/78_pdo_firebird.ini
%{_libdir}/php/extensions/pdo_firebird.so

%files pdo_mysql
%config(noreplace) %{_sysconfdir}/php.d/73_pdo_mysql.ini
%{_libdir}/php/extensions/pdo_mysql.so

%files pdo_odbc
%config(noreplace) %{_sysconfdir}/php.d/75_pdo_odbc.ini
%{_libdir}/php/extensions/pdo_odbc.so

%files pdo_pgsql
%config(noreplace) %{_sysconfdir}/php.d/76_pdo_pgsql.ini
%{_libdir}/php/extensions/pdo_pgsql.so

%files pdo_sqlite
%config(noreplace) %{_sysconfdir}/php.d/77_pdo_sqlite.ini
%{_libdir}/php/extensions/pdo_sqlite.so

%files pgsql
%config(noreplace) %{_sysconfdir}/php.d/42_pgsql.ini
%{_libdir}/php/extensions/pgsql.so

%files phar
%config(noreplace) %{_sysconfdir}/php.d/84_phar.ini
%{_libdir}/php/extensions/phar.so
%{_bindir}/phar
%{_mandir}/man1/phar.1*
%{_mandir}/man1/phar.phar.1*

%files pspell
 %config(noreplace) %{_sysconfdir}/php.d/44_pspell.ini
 %{_libdir}/php/extensions/pspell.so

%files posix
%config(noreplace) %{_sysconfdir}/php.d/43_posix.ini
%{_libdir}/php/extensions/posix.so

%files readline
%config(noreplace) %{_sysconfdir}/php.d/45_readline.ini
%{_libdir}/php/extensions/readline.so

%files recode
%config(noreplace) %{_sysconfdir}/php.d/46_recode.ini
%{_libdir}/php/extensions/recode.so

%files session
%config(noreplace) %{_sysconfdir}/php.d/47_session.ini
%config(noreplace) %{_sysconfdir}/cron.d/php
%{_libdir}/php/extensions/session.so
%{_libdir}/php/maxlifetime
%attr(01733,apache,apache) %dir /var/lib/php

%files shmop
%config(noreplace) %{_sysconfdir}/php.d/48_shmop.ini
%{_libdir}/php/extensions/shmop.so

%files snmp
%config(noreplace) %{_sysconfdir}/php.d/50_snmp.ini
%{_libdir}/php/extensions/snmp.so

%files soap
%config(noreplace) %{_sysconfdir}/php.d/51_soap.ini
%{_libdir}/php/extensions/soap.so

%files sockets
%config(noreplace) %{_sysconfdir}/php.d/52_sockets.ini
%{_libdir}/php/extensions/sockets.so

%files sqlite3
%config(noreplace) %{_sysconfdir}/php.d/78_sqlite3.ini
%{_libdir}/php/extensions/sqlite3.so

%files sysvmsg
%config(noreplace) %{_sysconfdir}/php.d/56_sysvmsg.ini
%{_libdir}/php/extensions/sysvmsg.so

%files sysvsem
%config(noreplace) %{_sysconfdir}/php.d/57_sysvsem.ini
%{_libdir}/php/extensions/sysvsem.so

%files sysvshm
%config(noreplace) %{_sysconfdir}/php.d/58_sysvshm.ini
%{_libdir}/php/extensions/sysvshm.so

%files tidy
%config(noreplace) %{_sysconfdir}/php.d/59_tidy.ini
%{_libdir}/php/extensions/tidy.so

%files tokenizer
%config(noreplace) %{_sysconfdir}/php.d/60_tokenizer.ini
%{_libdir}/php/extensions/tokenizer.so

%files xml
%config(noreplace) %{_sysconfdir}/php.d/62_xml.ini
%{_libdir}/php/extensions/xml.so

%files xmlreader
%config(noreplace) %{_sysconfdir}/php.d/63_xmlreader.ini
%{_libdir}/php/extensions/xmlreader.so

%files xmlrpc
%config(noreplace) %{_sysconfdir}/php.d/62_xmlrpc.ini
%{_libdir}/php/extensions/xmlrpc.so

%files xmlwriter
%config(noreplace) %{_sysconfdir}/php.d/64_xmlwriter.ini
%{_libdir}/php/extensions/xmlwriter.so

%files xsl
%config(noreplace) %{_sysconfdir}/php.d/63_xsl.ini
%{_libdir}/php/extensions/xsl.so

%files wddx
%config(noreplace) %{_sysconfdir}/php.d/63_wddx.ini
%{_libdir}/php/extensions/wddx.so

%files zip
%config(noreplace) %{_sysconfdir}/php.d/83_zip.ini
%{_libdir}/php/extensions/zip.so

%files fpm
%doc sapi/fpm/CREDITS sapi/fpm/LICENSE
%{_unitdir}/php-fpm.service
%config(noreplace) %{_sysconfdir}/php-fpm.conf
%config(noreplace) %{_sysconfdir}/sysconfig/php-fpm
%{_sysconfdir}/logrotate.d/php-fpm
%dir %{_sysconfdir}/php-fpm.d
%config(noreplace) %{_sysconfdir}/php-fpm.d/default.conf
%{_sbindir}/php-fpm
%{_mandir}/man8/php-fpm.8*
%attr(0711,apache,apache) %dir /var/lib/php-fpm
%attr(0711,apache,apache) %dir /var/log/php-fpm
%{_tmpfilesdir}/php-fpm.conf

%files -n phpdbg
%doc sapi/phpdbg/CREDITS sapi/phpdbg/Changelog.md sapi/phpdbg/README.md
%doc sapi/phpdbg/*.php
%{_bindir}/phpdbg
%{_mandir}/man1/phpdbg.1*

%changelog
* Sat Sep 30 2017 Tomás Flores <cognitus> - 7.1.10-1.mga6
+ Update to 7.1.10

* Fri Sep 22 2017 Tomás Flores <cognitus> 1.1.9-2.mga6
+ Remove patches from Openmandriva 
+ Add and update patches from Mageia
- 7.1.9

* Sat Sep 09 2017 Tomás Flores <cognitus> 1.1.9-1.mga6
+ Ported from Openmandriva
+ Update version
- 7.1.9

* Thu Jul 20 2017 luigiwalser <luigiwalser> 3:5.6.31-1.mga7
+ Revision: 1125477
- 5.6.31

* Wed Mar 15 2017 mrambo3501 <mrambo3501> 3:5.6.30-2.mga6
+ Revision: 1092770
- Rebuild for icu-58.2

* Thu Jan 26 2017 luigiwalser <luigiwalser> 3:5.6.30-1.mga6
+ Revision: 1083456
- 5.6.30

* Mon Dec 12 2016 luigiwalser <luigiwalser> 3:5.6.29-1.mga6
+ Revision: 1074332
- 5.6.29

* Fri Nov 11 2016 luigiwalser <luigiwalser> 3:5.6.28-1.mga6
+ Revision: 1066319
- 5.6.28

* Tue Oct 18 2016 luigiwalser <luigiwalser> 3:5.6.27-1.mga6
+ Revision: 1061547
- 5.6.27

* Fri Sep 16 2016 luigiwalser <luigiwalser> 3:5.6.26-1.mga6
+ Revision: 1053436
- 5.6.26

* Fri Aug 19 2016 luigiwalser <luigiwalser> 3:5.6.25-1.mga6
+ Revision: 1046976
- 5.6.25

* Thu Jul 21 2016 luigiwalser <luigiwalser> 3:5.6.24-1.mga6
+ Revision: 1043001
- 5.6.24

* Thu Jun 23 2016 luigiwalser <luigiwalser> 3:5.6.23-1.mga6
+ Revision: 1037370
- 5.6.23

* Thu May 26 2016 luigiwalser <luigiwalser> 3:5.6.22-1.mga6
+ Revision: 1018682
- 5.6.22

* Sat May 14 2016 shlomif <shlomif> 3:5.6.21-2.mga6
+ Revision: 1015258
- Rebuild for the new ICU (new major)

* Thu Apr 28 2016 luigiwalser <luigiwalser> 3:5.6.21-1.mga6
+ Revision: 1007229
- 5.6.21

* Tue Apr 12 2016 philippem <philippem> 3:5.6.20-2.mga6
+ Revision: 1000799
- change BR for Firebird (BR pkgconfig(fbclient)
- rebuild for Firebird 3

* Thu Mar 31 2016 luigiwalser <luigiwalser> 3:5.6.20-1.mga6
+ Revision: 997138
- 5.6.20

* Mon Mar 07 2016 luigiwalser <luigiwalser> 3:5.6.19-1.mga6
+ Revision: 987216
- 5.6.19

* Thu Mar 03 2016 umeabot <umeabot> 3:5.6.18-3.mga6
+ Revision: 983891
- Rebuild for openssl

* Sat Feb 27 2016 oden <oden> 3:5.6.18-2.mga6
+ Revision: 980045
- rebuild for new mariadb, postgresql, freetds.
- revert to jsonc-1.3.7 due to "- using system libjson-c is no more supported" (wtf?)
- rebuild
- jsonc-1.3.9 https://pecl.php.net/package-changelog.php?package=jsonc&release=1.3.9
- drop old cruft

* Thu Feb 04 2016 luigiwalser <luigiwalser> 3:5.6.18-1.mga6
+ Revision: 935911
- 5.6.18

* Tue Jan 19 2016 neoclust <neoclust> 3:5.6.17-2.mga6
+ Revision: 925882
- Rebuild now that all php7 has been removed from the BS
- Revert to php 5.6.17

  + oden <oden>
    - mention the event mpm

* Thu Jan 14 2016 oden <oden> 3:7.0.2-4.mga6
+ Revision: 922990
- make it easy to use php-fpm + apache-mod_proxy

* Fri Jan 08 2016 oden <oden> 3:7.0.2-3.mga6
+ Revision: 920603
- 7.0.2

* Fri Jan 01 2016 luigiwalser <luigiwalser> 3:7.0.2-2.mga6
+ Revision: 917914
- rebuild for icu

* Sat Dec 26 2015 oden <oden> 3:7.0.2-1.mga6
+ Revision: 915097
- 7.0.2RC1
- rediff patches are remove some

* Sun Dec 06 2015 tv <tv> 3:7.0.0-1.mga6
+ Revision: 908548
- new release

* Fri Nov 27 2015 tv <tv> 3:7.0.0-0.0.RC8.1.mga6
+ Revision: 906457
- 7.0 RC8

* Sat Nov 14 2015 oden <oden> 3:7.0.0-0.0.RC7.1.mga6
+ Revision: 903120
- rebuilt against latest libzip
- drop kolab patches due to http://lists.kolab.org/pipermail/devel/2014-July/015094.html

* Thu Nov 12 2015 tv <tv> 3:7.0.0-0.0.RC7.0.mga6
+ Revision: 902957
- 7.0 RC7
- use a macro for RC

* Thu Oct 29 2015 tv <tv> 3:7.0.0-0.0.RC6.0.mga6
+ Revision: 896492
- 7.0.0RC6
- fix download URL

* Mon Oct 26 2015 oden <oden> 3:7.0.0-0.0.RC5.2.mga6
+ Revision: 895585
- php-mysql is gone, forgot to fix that.

* Thu Oct 22 2015 oden <oden> 3:7.0.0-0.0.RC5.1.mga6
+ Revision: 894259
- yihaa!

* Thu Oct 01 2015 luigiwalser <luigiwalser> 3:5.6.14-1.mga6
+ Revision: 885553
- 5.6.14

* Sun Sep 06 2015 tv <tv> 3:5.6.13-2.mga6
+ Revision: 873154
- switch to new upstream file trigger syntax

* Fri Sep 04 2015 luigiwalser <luigiwalser> 3:5.6.13-1.mga6
+ Revision: 872773
- 5.6.13

* Fri Aug 07 2015 luigiwalser <luigiwalser> 3:5.6.12-1.mga6
+ Revision: 861573
- 5.6.12
- rediff patch 2

* Sat Jul 25 2015 cjw <cjw> 3:5.6.11-2.mga6
+ Revision: 857356
- rebuild for icu 55

* Sun Jul 12 2015 luigiwalser <luigiwalser> 3:5.6.11-1.mga6
+ Revision: 853354
- 5.6.11

* Sat Jun 27 2015 cjw <cjw> 3:5.6.10-2.mga6
+ Revision: 846271
- rebuild for libvpx 1.4

* Sat Jun 13 2015 luigiwalser <luigiwalser> 3:5.6.10-1.mga5
+ Revision: 823053
- 5.6.10

* Fri May 15 2015 luigiwalser <luigiwalser> 3:5.6.9-1.mga5
+ Revision: 822101
- 5.6.9
- remove opcache conflicts with eaccelerator (gone) and apcu (invalid) (mga#15743)

* Fri Apr 17 2015 luigiwalser <luigiwalser> 3:5.6.8-1.mga5
+ Revision: 820363
- 5.6.8
- remove CVE-2015-135[12] patches which were upstreamed

* Fri Mar 20 2015 luigiwalser <luigiwalser> 3:5.6.7-1.mga5
+ Revision: 819002
- 5.6.7
- remove upstream patch for php#68942
- remove CVE-2015-2305 patch (fixed upstream)
- add patch from dragonflybsd via debian to fix CVE-2015-2305

* Fri Feb 27 2015 luigiwalser <luigiwalser> 3:5.6.6-3.mga5
+ Revision: 817157
- add upstream patch to fix secondary issue in php#68942

* Fri Feb 20 2015 oden <oden> 3:5.6.6-2.mga5
+ Revision: 816036
- jsonc-1.3.7 (http://pecl.php.net/package-changelog.php?package=jsonc&release=1.3.7)

* Thu Feb 19 2015 luigiwalser <luigiwalser> 3:5.6.6-1.mga5
+ Revision: 815958
- rediff upstream patches to fix CVE-2015-1351 and CVE-2015-1352
- 5.6.6

* Mon Feb 16 2015 oden <oden> 3:5.6.5-2.mga5
+ Revision: 815162
- rebuilt for libgd-2.1.1

* Fri Jan 23 2015 luigiwalser <luigiwalser> 3:5.6.5-1.mga5
+ Revision: 812010
- 5.6.5

* Thu Dec 18 2014 luigiwalser <luigiwalser> 3:5.6.4-1.mga5
+ Revision: 804059
- 5.6.4
- rediff patches 2 and 30
- remove upstreamed patches 230-233

* Tue Nov 25 2014 cjw <cjw> 3:5.6.3-4.mga5
+ Revision: 799271
- fix postgresql-libs dependency version for postgresql release candidate releases

* Tue Nov 25 2014 cjw <cjw> 3:5.6.3-3.mga5
+ Revision: 799133
- rebuild against postgresql9.4

* Wed Nov 19 2014 luigiwalser <luigiwalser> 3:5.6.3-2.mga5
+ Revision: 797847
- add upstream bugfixes via fedora related to php-fpm and ipv6

* Thu Nov 13 2014 luigiwalser <luigiwalser> 3:5.6.3-1.mga5
+ Revision: 796883
- 5.6.3
- remove CVE-2014-3710 patch (fixed upstream in 5.6.3)

* Fri Oct 31 2014 luigiwalser <luigiwalser> 3:5.6.2-2.mga5
+ Revision: 795034
- add upstream patch to fix CVE-2014-3710

* Sat Oct 18 2014 oden <oden> 3:5.6.2-1.mga5
+ Revision: 783749
- 5.6.2 (fixes CVE-2014-3668, CVE-2014-3669, CVE-2014-3670)

* Wed Oct 15 2014 umeabot <umeabot> 3:5.6.0-3.mga5
+ Revision: 739071
- Second Mageia 5 Mass Rebuild

* Fri Sep 26 2014 tv <tv> 3:5.6.0-2.mga5
+ Revision: 725161
- rebuild for bogus file deps
- use %%global for req/prov exclude
- autoconvert to new prov/req excludes
- s/uggests:/Recommends:/

* Wed Sep 03 2014 oden <oden> 3:5.6.0-1.mga5
+ Revision: 671508
- 5.6.0

* Fri Aug 15 2014 oden <oden> 3:5.6.0-0.1.RC4.1.mga5
+ Revision: 662684
- 5.6.0RC4

* Mon Aug 04 2014 oden <oden> 3:5.6.0-0.1.RC3.2.mga5
+ Revision: 659540
- jsonc-1.3.6

* Thu Jul 31 2014 oden <oden> 3:5.6.0-0.1.RC3.1.mga5
+ Revision: 658494
- 5.6.0RC3

* Tue Jul 08 2014 oden <oden> 3:5.6.0-0.1.RC2.1.mga5
+ Revision: 650729
- added phpdbg.1
- 5.6.0RC2

* Sun Jun 29 2014 oden <oden> 3:5.6.0-0.1.RC1.1.mga5
+ Revision: 641146
- heh...
- 5.6.0RC1

* Tue Jun 10 2014 oden <oden> 3:5.6.0-0.0.beta4.1.mga5
+ Revision: 635355
- 5.6.0beta4

* Fri May 16 2014 oden <oden> 3:5.6.0-0.0.beta3.1.mga5
+ Revision: 623003
- 5.6.0beta3

* Wed May 07 2014 oden <oden> 3:5.6.0-0.0.beta2.1.mga5
+ Revision: 621002
- P23: rediff
- P1: rediff
- 5.6.0beta2

* Fri Apr 18 2014 oden <oden> 3:5.6.0-0.0.beta1.1.mga5
+ Revision: 616244
- php-5.6.0beta1
- jsonc-1.3.5
- P0: rediff
- P1: rediff, bump soname to match the release and fix linkage.
- P2: rediff
- P25: drop upstream implemented patch
- add the bundled phpdbg as a subpackage (look here: http://phpdbg.com)

* Fri Apr 04 2014 luigiwalser <luigiwalser> 3:5.5.11-1.mga5
+ Revision: 611737
- 5.5.11

* Wed Mar 12 2014 oden <oden> 3:5.5.10-1.mga5
+ Revision: 602619
- 5.5.10
- jsonc-1.3.4

* Wed Feb 26 2014 oden <oden> 3:5.5.9-3.mga5
+ Revision: 597276
- jsonc-1.3.4

* Wed Feb 19 2014 oden <oden> 3:5.5.9-2.mga5
+ Revision: 594798
- P230: security fix for CVE-2014-1943 (upstream)

* Wed Feb 12 2014 oden <oden> 3:5.5.9-1.mga5
+ Revision: 589735
- 5.5.9
- rediffed a lot of patches

* Tue Jan 14 2014 luigiwalser <luigiwalser> 3:5.5.8-2.mga4
+ Revision: 566586
- do not reload httpd when it is not running in filetriggers

* Tue Jan 14 2014 oden <oden> 3:5.5.8-1.mga4
+ Revision: 566544
- 5.5.8
- rediff the external libzip patch
- jsonc-1.3.3

* Fri Dec 13 2013 luigiwalser <luigiwalser> 3:5.5.7-1.mga4
+ Revision: 556537
- 5.5.7

* Fri Nov 22 2013 oden <oden> 3:5.5.6-1.mga4
+ Revision: 552282
- rediff some patches
- 5.5.6

* Tue Oct 22 2013 oden <oden> 3:5.5.5-1.mga4
+ Revision: 545808
- 5.5.5 (http://www.php.net/ChangeLog-5.php#5.5.5)

* Mon Oct 21 2013 umeabot <umeabot> 3:5.5.4-3.mga4
+ Revision: 537673
- Mageia 4 Mass Rebuild

* Fri Sep 27 2013 fwang <fwang> 3:5.5.4-2.mga4
+ Revision: 487500
- rebuild for icu 52

* Fri Sep 20 2013 fwang <fwang> 3:5.5.4-1.mga4
+ Revision: 481811
- 5.5.4 final

* Tue Sep 10 2013 fwang <fwang> 3:5.5.4-0.0.RC1.3.mga4
+ Revision: 477030
- rebuild for new postgresql

* Mon Sep 09 2013 oden <oden> 3:5.5.4-0.0.RC1.2.mga4
+ Revision: 476668
- jsonc-1.3.2

* Fri Sep 06 2013 oden <oden> 3:5.5.4-0.0.RC1.1.mga4
+ Revision: 475425
- 5.5.4RC1
- rediffed some patches

* Tue Aug 27 2013 luigiwalser <luigiwalser> 3:5.5.3-2.mga4
+ Revision: 472083
- rebuild for cyrus-sasl

  + fwang <fwang>
    - add descriptive url

* Fri Aug 23 2013 fwang <fwang> 3:5.5.3-1.mga4
+ Revision: 470029
- new version 5.5.3

  + oden <oden>
    - fix #8538 (There is an undocumented hard-coded limit of 24 minutes on PHP session lifetime)
    - fix #10331 (php-sqlite3 does not obsolete php-sqlite)
    - 5.5.2
    - rediff some patches

* Mon Jul 22 2013 oden <oden> 3:5.5.1-1.mga4
+ Revision: 457143
- 5.5.1
- P50: rediff
- fix the php-test.ini file according to needed loading sequence
- fix the loading of opcache
- keep all the sources in php-devel for easier post-testing

* Fri Jun 28 2013 oden <oden> 3:5.5.0-5.mga4
+ Revision: 447732
- add back the deprecated php-mysql package (fixes #10628)

* Mon Jun 24 2013 blino <blino> 3:5.5.0-4.mga4
+ Revision: 446070
- buildrequire mysql-devel for mysql_config

* Sun Jun 23 2013 blino <blino> 3:5.5.0-3.mga4
+ Revision: 446060
- mysqlnd: detect mysql unix socket path with mysql_config (this fixes mysqli and pdo_mysql)

* Sun Jun 23 2013 blino <blino> 3:5.5.0-2.mga4
+ Revision: 445794
- specify back mysql socket path at configure (to fix mysqli)

* Fri Jun 21 2013 oden <oden> 3:5.5.0-1.mga4
+ Revision: 445354
- 5.5.0
- P11 & P25: newer rediffed patches from fedora
- P30: rediff
- the mysql extension is deprecated, so might as well remove it now...

* Thu Jun 13 2013 oden <oden> 3:5.5.0-0.0.RC3.4.mga4
+ Revision: 442540
- bump release
- fix the php-fpm.service file (Remi Collet)
- add some conflicts for the php-opcache sub package

* Thu Jun 13 2013 oden <oden> 3:5.5.0-0.0.RC3.3.mga4
+ Revision: 442476
- use /run/php-fpm
- add systemd to php-fpm (Remi Collet)

* Thu Jun 13 2013 oden <oden> 3:5.5.0-0.0.RC3.2.mga4
+ Revision: 442375
- S10: use json from pecl due to licensing issues

  + fwang <fwang>
    - deprecate mysql extension

* Sun Jun 09 2013 oden <oden> 3:5.5.0-0.0.RC3.1.mga4
+ Revision: 441224
- 5.5.0RC3
- bye, bye logos and the eastern egg crap (drop P302+P303)
- P2: patch and use the php.ini-production file because the shipped php.ini file is several years old...
- P20: rediff
- say hello to opcache

* Sun Jun 09 2013 oden <oden> 3:5.4.16-1.mga4
+ Revision: 441117
- 5.4.16 (fixes CVE-2013-2110)
- rediffed P25

* Mon Jun 03 2013 fwang <fwang> 3:5.4.15-3.mga4
+ Revision: 435546
- rebuild for new libpng

* Tue May 28 2013 oden <oden> 3:5.4.15-2.mga4
+ Revision: 429242
- use ext/gd from php-5.5.0RC2 for now

* Sun May 26 2013 oden <oden> 3:5.4.15-1.mga4
+ Revision: 428167
- 5.4.15
- rediffed P25
- use the new libgd 2.1.x that should render the php-gd-bundled package obsolete

* Sun May 26 2013 fwang <fwang> 3:5.4.13-4.mga4
+ Revision: 427995
- rebuild for new icu

* Fri Apr 26 2013 fwang <fwang> 3:5.4.13-3.mga3
+ Revision: 411308
- fix systemd unit file so that it can start correctly (bug#9844)

* Sun Mar 24 2013 colin <colin> 3:5.4.13-2.mga3
+ Revision: 404859
- Add systemd requires and general post/pre fixes (mga#9302)

* Fri Mar 15 2013 oden <oden> 3:5.4.13-1.mga3
+ Revision: 403244
- 5.4.13 (fixes CVE-2013-1635, CVE-2013-1643)

* Tue Mar 05 2013 oden <oden> 3:5.4.12-2.mga3
+ Revision: 401489
- P303: added a new mageia logo by R?\195?\169mi Verschelde

* Fri Feb 22 2013 oden <oden> 3:5.4.12-1.mga3
+ Revision: 399881
- 5.4.12

* Thu Jan 31 2013 luigiwalser <luigiwalser> 3:5.4.11-2.mga3
+ Revision: 393831
- rebuild for icu

* Mon Jan 21 2013 oden <oden> 3:5.4.11-1.mga3
+ Revision: 390585
- 5.4.11 (http://php.net/ChangeLog-5.php#5.4.11)

* Thu Jan 17 2013 colin <colin> 3:5.4.10-5.mga3
+ Revision: 388944
- Use tmpfiles for php-fpm runtime dir creation

* Wed Jan 09 2013 spuhler <spuhler> 3:5.4.10-4.mga3
+ Revision: 343541
- reversed threadsafe build

* Sat Jan 05 2013 spuhler <spuhler> 3:5.4.10-3.mga3
+ Revision: 339336
- built threadsafe

* Wed Dec 26 2012 oden <oden> 3:5.4.10-2.mga3
+ Revision: 335433
- make it backportable

* Fri Dec 21 2012 fwang <fwang> 3:5.4.10-1.mga3
+ Revision: 333629
- new version 5.4.10

* Sat Dec 01 2012 fwang <fwang> 3:5.4.9-3.mga3
+ Revision: 323654
- rebuild for new pcre

* Sat Nov 24 2012 oden <oden> 3:5.4.9-2.mga3
+ Revision: 321559
- maybe better configure line now...
- rebuild
- remove pok crap
- merge firebird (interbase) into this package

* Sat Nov 24 2012 fwang <fwang> 3:5.4.9-1.mga3
+ Revision: 321476
- new version 5.4.9

  + oden <oden>
    - whoops. didn't realize php-5.4 only has sqlite3 support.
    - fix #8164 (php-sqlite3 obsoletes php-sqlite)

* Fri Nov 09 2012 fwang <fwang> 3:5.4.8-9.mga3
+ Revision: 316669
- rebuild for updated icu

* Tue Nov 06 2012 fwang <fwang> 3:5.4.8-8.mga3
+ Revision: 314746
- rebuild for new icu

* Thu Oct 25 2012 fwang <fwang> 3:5.4.8-7.mga3
+ Revision: 309900
- recognize more recent jpeg version
- update description

  + luigiwalser <luigiwalser>
    - use macros for php-fpm service
    - php-fpm requires webserver-base for apache user
    - php-cli provides /usr/bin/php (mga#6534)

* Tue Oct 23 2012 fwang <fwang> 3:5.4.8-6.mga3
+ Revision: 309398
- prepare to build pdo_mysql-bundled
- note for mysqlnd

* Fri Oct 19 2012 fwang <fwang> 3:5.4.8-5.mga3
+ Revision: 308312
- force load mysqlnd before mysql exts

* Fri Oct 19 2012 fwang <fwang> 3:5.4.8-4.mga3
+ Revision: 308152
- specify ldflags
- enable vpx support

* Fri Oct 19 2012 fwang <fwang> 3:5.4.8-3.mga3
+ Revision: 308147
- all mysql exts are now using mysqlnd now

* Fri Oct 19 2012 fwang <fwang> 3:5.4.8-2.mga3
+ Revision: 308140
- build with mysqlnd per default upstream

* Fri Oct 19 2012 fwang <fwang> 3:5.4.8-1.mga3
+ Revision: 308062
- new version 5.4.8

* Wed Oct 17 2012 obgr_seneca <obgr_seneca> 3:5.4.7-2.mga3
+ Revision: 307677
- Add requires for webserver-base in php-session

* Mon Sep 17 2012 fwang <fwang> 3:5.4.7-1.mga3
+ Revision: 294677
- new version 5.4.7

* Wed Sep 12 2012 oden <oden> 3:5.4.6-1.mga3
+ Revision: 292568
- remove libphp5.so from file lists as well
- 5.4.6
- make mod_php the more correct way

  + spuhler <spuhler>
    - upgrade to 5.4.6

* Tue Jul 31 2012 fwang <fwang> 3:5.4.5-2.mga3
+ Revision: 276425
- force echo 0 for iurt
- force echo 0 for iurt
- rebuild for db-5.3

  + guillomovitch <guillomovitch>
    - no need to redefine configure commands to explain packaging granularity (especially when giving wrong path to document file)
    - sanitize build flags usage
    - use %%{_unitdir} macro
    - drop useless dependencies
    - cleanup postgresql dependencies computing, and use a better problem description
    - drop fedora-supposed patches non existing in fedora
    - drop useless references to bugzilla in package description
    - drop unused macros
    - use apache-provided rpm macros
    - clean up files list
    - useless buildtime check, we have dependencies for this

* Wed Jul 25 2012 spuhler <spuhler> 3:5.4.5-1.mga3
+ Revision: 274185
- upgrade to 5.4.5
- upgrade to 5.4.5

* Mon Jul 23 2012 blino <blino> 3:5.4.4-8.mga3
+ Revision: 273674
- install module in standard apache location (and not include double libphp5_common.so there)

* Sun Jul 22 2012 spuhler <spuhler> 3:5.4.4-7.mga3
+ Revision: 273511
- took out those old coments Conflicts:	apache-mpm-worker >= %%{apache_version}
  and apache-mpm-event >= %%{apache_version}

* Sun Jul 22 2012 cjw <cjw> 3:5.4.4-6.mga3
+ Revision: 273458
- apache-mod_php: fix apache configuration location
- apache-mod_php: (build-)depends on apache >= 2.4.2-1

* Sun Jul 22 2012 blino <blino> 3:5.4.4-5.mga3
+ Revision: 273433
- fix apxs path (now in bindir)
- require apache instead of obsolete apache-mpm and comment old apache conflicts

  + spuhler <spuhler>
    - Rebuild for Apache-2.4

* Sun Jul 15 2012 spuhler <spuhler> 3:5.4.4-3.mga3
+ Revision: 270903
+ rebuild (emptylog)

* Sun Jul 15 2012 spuhler <spuhler> 3:5.4.4-2.mga3
+ Revision: 270900
+ rebuild (emptylog)

* Sun Jul 15 2012 spuhler <spuhler> 3:5.4.4-1.mga3
+ Revision: 270874
- upgrade to 5.4.4

* Sun Jul 15 2012 spuhler <spuhler> 3:5.4.3-1.mga3
+ Revision: 270816
- Ugrade to version5.4.3
  Spec file based on MDV (Oden)
  php-ini and apache-mod_php split off

* Fri Jun 15 2012 luigiwalser <luigiwalser> 3:5.3.14-1.mga3
+ Revision: 260870
- 5.3.14 (fixes CVE-2012-2143)

* Mon Jun 11 2012 luigiwalser <luigiwalser> 3:5.3.13-4.mga3
+ Revision: 259856
- additional patch from upstream via debian for similar issue in phar code

* Wed Jun 06 2012 luigiwalser <luigiwalser> 3:5.3.13-3.mga3
+ Revision: 256297
- fix CVE-2012-2386 (php bug 61065)

* Wed May 30 2012 fwang <fwang> 3:5.3.13-2.mga3
+ Revision: 249670
- rebuild for new icu

* Thu May 10 2012 luigiwalser <luigiwalser> 3:5.3.13-1.mga2
+ Revision: 235135
- 5.3.13 (fixes CVE-2012-2335 and CVE-2012-2336)

* Sat May 05 2012 luigiwalser <luigiwalser> 3:5.3.12-2.mga2
+ Revision: 234742
- fix CVE-2012-2311

* Fri May 04 2012 fwang <fwang> 3:5.3.12-1.mga2
+ Revision: 234690
- new version 4.3.12 (fixing CVE-2012-1823)

  + luigiwalser <luigiwalser>
    - 5.3.11 (partial sync with mdv)

* Tue Apr 24 2012 luigiwalser <luigiwalser> 3:5.3.10-8.mga2
+ Revision: 233143
- fix CVE-2012-1172 (php bug 55500)

* Mon Apr 02 2012 pterjan <pterjan> 3:5.3.10-7.mga2
+ Revision: 227746
- Fix enable-libxml parameter to really enable it

  + luigiwalser <luigiwalser>
    - let webserver-base package add apache user

* Mon Mar 19 2012 luigiwalser <luigiwalser> 3:5.3.10-6.mga2
+ Revision: 224021
- use arch independent libdir to find modules (thanks Funda Wang)

* Mon Mar 19 2012 luigiwalser <luigiwalser> 3:5.3.10-5.mga2
+ Revision: 223999
- use filetriggers to reload httpd on php extension installation

* Fri Mar 16 2012 spuhler <spuhler> 3:5.3.10-4.mga2
+ Revision: 223575
- removed Patch20: php-mail.diff as it leaks mail info, Bug # 4571

* Thu Mar 01 2012 spuhler <spuhler> 3:5.3.10-3.mga2
+ Revision: 216448
- added Obsoletes: php-pspel
- removed pspell

* Thu Feb 09 2012 spuhler <spuhler> 3:5.3.10-2.mga2
+ Revision: 206599
- changed pm.max_children from 5 to 35

  + fwang <fwang>
    - new version 5.3.10

* Thu Jan 19 2012 guillomovitch <guillomovitch> 3:5.3.9-4.mga2
+ Revision: 198248
- include php-ini package
- merge it with doc subpackage

* Thu Jan 19 2012 spuhler <spuhler> 3:5.3.9-3.mga2
+ Revision: 198028
- activated the test
  updated corrected mageia logo ptach

  + fwang <fwang>
    - fix wording of logo patch

* Tue Jan 17 2012 fwang <fwang> 3:5.3.9-2.mga2
+ Revision: 197193
- fix html mismatch tags

* Tue Jan 17 2012 spuhler <spuhler> 3:5.3.9-1.mga2
+ Revision: 197188
- added BuildRequires: autoconf2.1
- upgrade to 5.3.9

* Tue Jan 03 2012 guillomovitch <guillomovitch> 3:5.3.9-0.RC4.1.mga2
+ Revision: 189937
- generate mod_php directly from this package
- sync common fedora patches, and apply suhosin patch last
- drop fedora patches not in fedora anymore
- switch to fedora build system, using a different directory for each SAPI
- don't run configure for cli, it is never built
- stop messing with configure command value on phpinfo page
- drop redundant configure options
- new RC version
- drop redondant build dependencies
- handle php-dev files in %%install only, to avoid multiple copies
- trim descriptions, no need to mention dependencies managed by rpm
- spec cleanup
- turn hard dependency on suhosin to as soft dependency, as it is not mandatory

  + fwang <fwang>
    - chagne mandriva into mageia, disable image for now

* Tue Dec 20 2011 spuhler <spuhler> 3:5.3.9-0.RC3.1.mga2
+ Revision: 184708
- upgrade to 5.4RC3
  synched with Mandriva

* Thu Dec 08 2011 fwang <fwang> 3:5.3.8-4.mga2
+ Revision: 178854
- rebuild for new odbc

* Mon Dec 05 2011 fwang <fwang> 3:5.3.8-3.mga2
+ Revision: 176942
- rebuild for new gdbm

  + guillomovitch <guillomovitch>
    - spec cleanup

* Tue Sep 13 2011 fwang <fwang> 3:5.3.8-2.mga2
+ Revision: 142812
- rebuild for new libpng
- new version 5.3.8 ( sync with mandriva )

  + guillomovitch <guillomovitch>
    - rebuild for latest net-snmp
    - turn hard dependency on suhosin to a soft dependency, as it is a perfectly optional component

* Mon Jun 20 2011 fwang <fwang> 3:5.3.6-3.mga2
+ Revision: 110372
- rebuild for new icu

* Thu May 19 2011 dmorgan <dmorgan> 3:5.3.6-2.mga1
+ Revision: 99741
- Fix perl detection

  + pterjan <pterjan>
    - Add upstream fix for CVE-2011-1148

* Sun Apr 17 2011 pterjan <pterjan> 3:5.3.6-1.mga1
+ Revision: 87304
- Update to 5.3.6
  - Fixes CVE-2011-1153, CVE-2011-1092, CVE-2011-0708, CVE-2011-0421
  - Sync with Mandriva

* Fri Mar 25 2011 dmorgan <dmorgan> 3:5.3.5-3.mga1
+ Revision: 77249
- Lemon is not provided anymore by sqlite3
  Comment it on the spec file to see if the php module still build without it
  or if we need to remove this module.
- Rebuild against new mysql

  + misc <misc>
    - Rebuild to remove Mandriva logo
    - add some comments about patches
    - do not show mandriva logo on phpinfo()
    - s/Mandriva/Mageia/. We should use a macro for that.

* Thu Jan 13 2011 dmorgan <dmorgan> 3:5.3.5-0.mga1
+ Revision: 16674
- Remove mdv macros
- Fix mageia bugzilla url

  + spuhler <spuhler>
    -BuildRoot:	%%{_tmppath}/%%{name}-%%{version}-%%{release}-buildroot
     -report bugs here: http://qa.mandriva.com/ so that the official maintainer of
    -this Mandriva package can help you. More information regarding the
      +report bugs to the official maintainer of
      +this Mageia package. More information regarding the
    - imported package php


* Fri Jan 07 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.5-0mdv2011.0
+ Revision: 629668
- 5.3.5 (fixes CVE-2010-4645)
- compile with ordinary %%optflags
- rediffed the suhosin and autopoo patches

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.4-6mdv2011.0
+ Revision: 627853
- suhosin-patch-5.3.4-0.9.10 (no changes)

  + Funda Wang <fwang@mandriva.org>
    - tighten BR

* Sun Jan 02 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.4-5mdv2011.0
+ Revision: 627657
- don't force the usage of automake1.7
- make it build with autoconf-2.5+ (fedora)

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.4-4mdv2011.0
+ Revision: 627003
- rebuilt against mysql-5.5.8 libs, again

* Mon Dec 27 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.4-3mdv2011.0
+ Revision: 625424
- rebuilt against mysql-5.5.8 libs

* Thu Dec 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.4-2mdv2011.0
+ Revision: 622268
- rebuild

* Wed Dec 15 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.4-1mdv2011.0
+ Revision: 622181
- 5.3.4
- added post 5.3.4 fixes:
- P229: fix upstream bug 53517
- P230: fix upstream bug 53541

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.4-0.0.RC2.1mdv2011.0
+ Revision: 606170
- 5.3.4RC2

* Tue Nov 23 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.4-0.0.RC1.2mdv2011.0
+ Revision: 599908
- rebuild

* Mon Nov 22 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.4-0.0.RC1.1mdv2011.0
+ Revision: 599693
- 5.3.4RC1 (fixes at least CVE-2010-2950,3436,3709,3710,3870,4150.
  note: CVE-2010-2950 was fixed silently by the suhoson patch)
- dropped upstream patches that fixed various security issues
- revived the kolab2 patches
- rediffed the suhosin patch (P301)

* Wed Nov 17 2010 Colin Guthrie <cguthrie@mandriva.org> 3:5.3.3-9mdv2011.0
+ Revision: 598363
- Apply upstream fix for php#50027. (Garbage Collection bug)

  + Oden Eriksson <oeriksson@mandriva.com>
    - P232: security fix for CVE-2010-3870 (upstream)
    - fix deps

* Sun Oct 31 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.3-7mdv2011.0
+ Revision: 590876
- P229: security fix for CVE-2010-3436 (upstream)
- P230: security fix for CVE-2010-3709 (upstream)
- P231: security fix for CVE-2010-3710 (upstream)

* Tue Oct 12 2010 Funda Wang <fwang@mandriva.org> 3:5.3.3-6mdv2011.0
+ Revision: 585012
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - better description for mysqli

* Fri Sep 24 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.3-4mdv2011.0
+ Revision: 580886
- provide the more up to date and bundled phar code

* Tue Aug 24 2010 Funda Wang <fwang@mandriva.org> 3:5.3.3-3mdv2011.0
+ Revision: 572559
- drop extra space in Makefile.global

* Tue Jul 27 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.3-2mdv2011.0
+ Revision: 561821
- suhosin-patch-5.3.3-0.9.10
- 5.3.3

* Fri Jul 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.3-0.0.RC3.1mdv2011.0
+ Revision: 554270
- 5.3.3RC3

* Mon Jul 12 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.3-0.0.RC2.1mdv2011.0
+ Revision: 551241
- 5.3.3RC2

* Mon Jun 14 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-11mdv2010.1
+ Revision: 547986
- new fpm svn snap

* Thu Jun 10 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-10mdv2010.1
+ Revision: 547830
- additional php-fpm config fixes

* Wed Jun 09 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-9mdv2010.1
+ Revision: 547360
- rediffed two of the fpm patches (whoops!)
- new fpm svn snap from HEAD

* Sat May 08 2010 Ahmad Samir <ahmadsamir@mandriva.org> 3:5.3.2-8mdv2010.1
+ Revision: 544056
- resubmit for missing packages

* Wed Apr 28 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-7mdv2010.1
+ Revision: 540059
- new fpm svn snap

* Thu Apr 08 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-6mdv2010.1
+ Revision: 532888
- new fpm snap (r297689)

* Tue Apr 06 2010 Funda Wang <fwang@mandriva.org> 3:5.3.2-5mdv2010.1
+ Revision: 531922
- rebuild for new openssl

* Sat Mar 27 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-4mdv2010.1
+ Revision: 527906
- P229: security fix for CVE-2010-0397 (svn)

* Sun Mar 21 2010 Funda Wang <fwang@mandriva.org> 3:5.3.2-3mdv2010.1
+ Revision: 526079
- rebuild for new icu

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-2mdv2010.1
+ Revision: 514498
- suhosin-patch-5.3.2-0.9.9.1

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-1mdv2010.1
+ Revision: 514488
- 5.3.2
- rebuilt against openssl-0.9.8m

* Wed Feb 24 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-0.0.RC3.1mdv2010.1
+ Revision: 510636
- 5.3.2RC3
- drop the gmp-5.0.0 patch as it's fixed upstream

* Wed Feb 17 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-0.0.RC2.2mdv2010.1
+ Revision: 507036
- rebuild

* Fri Feb 12 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-0.0.RC2.1mdv2010.1
+ Revision: 504807
- 5.3.2RC2
- rediffed P301 (suhosin)
- new fpm snapshot (S7)

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 3:5.3.2-0.0.RC1.5mdv2010.1
+ Revision: 503521
- add patch build with gmp 5.0.0
- rebuild fo new gmp

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Fri Jan 15 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-0.0.RC1.3mdv2010.1
+ Revision: 491845
- new fpm svn snapshot

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-0.0.RC1.2mdv2010.1
+ Revision: 488692
- added libjpegv v8 support

  + Funda Wang <fwang@mandriva.org>
    - recognize libjpegv7 in gd ext

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.2-0.0.RC1.1mdv2010.1
+ Revision: 485152
- 5.3.2RC1
- rediffed some patches
- dropped one patch added upstream

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-6mdv2010.1
+ Revision: 484979
- really link against bdb 4.8

* Fri Jan 01 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-5mdv2010.1
+ Revision: 484761
- rebuilt against bdb 4.8

* Mon Dec 28 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-4mdv2010.1
+ Revision: 483128
- use a svn snap of fpm instead of maintaining a patch

* Sun Dec 20 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-3mdv2010.1
+ Revision: 480472
- added fpm from upstream

  + Funda Wang <fwang@mandriva.org>
    - fix configure_command dir

* Mon Nov 30 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-2mdv2010.1
+ Revision: 471745
- suhosin-patch-5.3.1-0.9.8

* Fri Nov 20 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-1mdv2010.1
+ Revision: 467633
- 5.3.1

* Fri Nov 13 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC4.1mdv2010.1
+ Revision: 465708
- 5.3.1RC4

* Mon Nov 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC3.2mdv2010.1
+ Revision: 463584
- fix #54993 (With latest php-5.3.xx, it not needed build separated binary for FastCGI SAPI support)

* Fri Nov 06 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC3.1mdv2010.1
+ Revision: 461144
- 5.3.1RC3
- fix #55063 (Calling utf8_encode or utf8_decode functions stalls PHP)

* Wed Oct 21 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC2.1mdv2010.0
+ Revision: 458554
- dropped P229,P230,P231,P232 as these was implemented in 5.3.1RC2
- rediffed the suhosin patch (P301)

* Tue Oct 20 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC1.5mdv2010.0
+ Revision: 458451
- P230: security fix for a open_basedir bypass vulnerability (svn)
- P231: security fix for a safe_mode bypass vulnerability (svn)
- P232: security fix for CVE-2009-3546.diff (svn)
- P233: upstream fix for php bug 49224

* Thu Oct 15 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC1.4mdv2010.0
+ Revision: 457717
- rebuilt against new net-snmp libs

* Tue Sep 29 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC1.3mdv2010.0
+ Revision: 450934
- fix build
- re-add the suhosin patch (0.9.8)

* Sun Sep 27 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC1.2mdv2010.0
+ Revision: 449829
- P229: security fix for CVE-2009-3291

* Sat Sep 05 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.1-0.0.RC1.1mdv2010.0
+ Revision: 432063
- fix the libedit patch
- 5.3.1RC1
- rediffed one patch, dropped a redundant patch
- rebuilt against libtiff-3.9.1 and libpng-1.2.39
- previous changes cleaned out work arounds for old'ish problems...
- cleanups (#1)
- cleanups (#1)

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - use autoconf 2.13 for regenerating configure, upstream still use the old autotools set

* Wed Aug 19 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-7mdv2010.0
+ Revision: 417998
- re-add requires on php-suhosin

* Mon Aug 17 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-6mdv2010.0
+ Revision: 417285
- rebuilt against libjpeg v7 (php-gd)

* Thu Jul 30 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-5mdv2010.0
+ Revision: 404813
- fix the postgresql version macro, thanks anssi!
- don't require the php-suhosin package for now as it's broken
- fix deps (helio)
- try to solve problems with "undefined symbol : lo_import_with_oid"
  due to postgresql packaging mess

  + Helio Chissini de Castro <helio@mandriva.com>
    - Removed duplicated buildrequires
    - Removed pg_config for version release. Buildrequires aren't installed in createsrpm time, so pg_config was never present during srpm creation.
      Since mandriva rpm already provides an automatic depends for libpq, there's no need to push explicit depends on php-pgsql nahd php-pdo_pgsql.

* Wed Jul 29 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-3mdv2010.0
+ Revision: 403839
- rebuilt to avoid adding deps in 200+ other spec files...
- revert nuked deps

* Fri Jul 24 2009 Helio Chissini de Castro <helio@mandriva.com> 3:5.3.0-2mdv2010.0
+ Revision: 399144
- Small cleanup in php package
- Fixed xmlrpc_epi compilation putting proper header ( Patch16 ).
- Normalize epochs. Every subpackage had a different epoch and the cascading
  caracteristic of rpm are affecting the subsequent subpackages. Now all
  packages follow the uniq epoch set.
- Add unixODBC as main odbc for pdo.
- removed invalid ( non existent ) options in configure:
  --with-flatfile, --with-inifile, --enable-spl, --enable-track-vars
  --enable-trans-sid, --enable-memory-limit, --with-versioning
- php now uses system regex to avoid define conflicts
- devel package is now requiring only proper libs

* Fri Jul 17 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-1mdv2010.0
+ Revision: 396804
- rediffed one fuzzy patch
- drop the suhosin patch as it's seems dead

* Tue Jul 14 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.3mdv2010.0
+ Revision: 395957
- nuke the systzdata patch and reintroduce the php-timezonedb package

* Thu Jul 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.2mdv2010.0
+ Revision: 393921
- P106: new(er) systzdata patch from fedora

* Wed Jul 01 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.1mdv2010.0
+ Revision: 391195
- 5.3.0 (final)
- rediffed one patch

* Fri Jun 19 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.0.RC4.1mdv2010.0
+ Revision: 387295
- fix build (#1)
- 5.3.0RC4

* Fri Jun 12 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.0.RC3.1mdv2010.0
+ Revision: 385542
- 5.3.0RC3
- rediffed one patch
- fix deps

* Fri Jun 12 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.0.RC2.4mdv2010.0
+ Revision: 385425
- rebuild

* Thu Jun 11 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.0.RC2.3mdv2010.0
+ Revision: 385287
- fix linkage (xmlrpc-epi)

* Fri May 29 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.0.RC2.2mdv2010.0
+ Revision: 381106
- temporary disable the suhosin patch (and 2 others in sequence)

* Wed May 13 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.3.0-0.0.RC2.1mdv2010.0
+ Revision: 375295
- 5.3.0RC2 (first draft)
- rediffed a lot of patches
- dropped a lot of redundant patches
- merged a lot of private changes into the cooker package
- the following extensions is gone or moved to pecl:
  - mhash (replaced by internal code)
  - mime_magic (replaced by fileinfo)
  - ming
  - ncurses
  - sqlite (replaced by sqlite3)
  - dbase
  - sybase (replaced by sybase_ct)
- the following extensions is new or moved from pecl:
  - enchant
  - fileinfo (uses bundled libmagic (for now))
  - intl
  - sqlite3
  - sybase_ct

* Thu Mar 26 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-6mdv2009.1
+ Revision: 361334
- added two more upstream patches

* Tue Mar 17 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-5mdv2009.1
+ Revision: 356848
- merge external php-zip into this package as this code is newer
- added a bunch of upstream fixes (P230 - P240)

* Fri Mar 13 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-4mdv2009.1
+ Revision: 354600
- the fix for #43486 broke the wddx extension. the fix isn't needed anymore

* Mon Mar 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-3mdv2009.1
+ Revision: 353306
- suhosin-patch-5.2.9-0.9.7

* Sun Mar 08 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-2mdv2009.1
+ Revision: 352897
- backported changes from 5.3 to link against the system oniguruma library (-lonig)

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-1mdv2009.1
+ Revision: 346351
- 5.2.9

* Wed Feb 25 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-0.0.RC3.2mdv2009.1
+ Revision: 344879
- rebuilt against new readline

* Thu Feb 19 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-0.0.RC3.1mdv2009.1
+ Revision: 342988
- 5.2.9RC3

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-0.0.RC2.2mdv2009.1
+ Revision: 342247
- fix libtool mess (thanks fedora)

* Sat Feb 14 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-0.0.RC2.1mdv2009.1
+ Revision: 340240
- 5.2.9RC2

* Mon Feb 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.9-0.0.RC1.1mdv2009.1
+ Revision: 338903
- 5.2.9RC1
- rediff some patches
- drop upstream implemented patches
- fix #26274, #45864, and probably many others by using -O0 for compiler
  optimization. either the bug is in php and/or in gcc 4.3.2. the
  dispute goes on... i rather just make it work for now...

* Thu Jan 29 2009 Funda Wang <fwang@mandriva.org> 3:5.2.8-7mdv2009.1
+ Revision: 335080
- rebuild for new libtool

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix security issue ( CAN-2008-5498 )(Bug #46909)

* Wed Jan 14 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.8-6mdv2009.1
+ Revision: 329447
- relink rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.8-5mdv2009.1
+ Revision: 321721
- rebuild

* Tue Dec 16 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.8-4mdv2009.1
+ Revision: 314881
- added P11 to fix build with -Werror=format-security

* Mon Dec 15 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.8-3mdv2009.1
+ Revision: 314591
- rebuilt against db4.7

* Fri Dec 12 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.8-2mdv2009.1
+ Revision: 313611
- rediff some patches to meet the nofuzz criteria

* Tue Dec 09 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.8-1mdv2009.1
+ Revision: 312064
- 5.2.8
- drop the magic_quotes_gpc_fix patch (the only change in 5.2.8, heh...)

* Mon Dec 08 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-2mdv2009.1
+ Revision: 311794
- fix reason why 5.2.7 was pulled (P230)
- use lowercase mysql-devel

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-1mdv2009.1
+ Revision: 310189
- 5.2.7
- suhosin-patch-5.2.7-0.9.6.3

* Sat Nov 29 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-0.0.RC5.1mdv2009.1
+ Revision: 308022
- 5.2.7RC5 (fixes CVE-2008-3658, CVE-2008-3659)
- 5.2.7RC2 (fixes CVE-2008-2829)
- 5.2.7RC1 (fixes CVE-2008-2665, CVE-2008-2666, CVE-2008-3660)

* Fri Nov 21 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-0.0.RC4.1mdv2009.1
+ Revision: 305416
- 5.2.7RC4

* Thu Nov 20 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-0.0.RC3.2mdv2009.1
+ Revision: 305278
- fix #45864 (gcc over-optimization causes segv's in some x86_64 apps.)

* Fri Nov 07 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-0.0.RC3.1mdv2009.1
+ Revision: 300656
- 5.2.7RC3

* Sat Oct 25 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-0.0.RC2.1mdv2009.1
+ Revision: 297258
- 5.2.7RC2
- drop P230, another fix for CVE-2008-2829 is implemented

* Wed Oct 15 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.7-0.0.RC1.1mdv2009.1
+ Revision: 293842
- 5.2.7RC1
- drop obsolete patches; P16,P122,P226,P227,P231,P232
- fix deps
- drop all those buildconflicts thanks to the new PHP_INI_SCAN_DIR env

* Thu Sep 25 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-18mdv2009.0
+ Revision: 288082
- bump release
- fix #44202 (Php-cli should PreRequires update-alternatives)
- fix #44206 (undefined symbol: SWFDisplayItem_get_x)

* Thu Sep 11 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-17mdv2009.0
+ Revision: 283721
- rediffed the kolab2 patches and added one more (P52)

* Sat Sep 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-16mdv2009.0
+ Revision: 281822
- fix #43486 (XML parsing ignores encoded elements in character data (e.g. &gt; &lt; etc.))

* Tue Sep 02 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-15mdv2009.0
+ Revision: 278891
- rebuild

* Mon Aug 25 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-14mdv2009.0
+ Revision: 275761
- enable t1lib in php-gd
- rebuilt against new ming libs

* Fri Aug 22 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-13mdv2009.0
+ Revision: 275133
- rebuilt mbstring against external shared libmbfl libs

* Tue Aug 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-12mdv2009.0
+ Revision: 263959
- new P106

* Tue Jul 29 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-11mdv2009.0
+ Revision: 252143
- hardcode %%{_localstatedir}

* Sun Jul 27 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-10mdv2009.0
+ Revision: 250655
- bump release
- added P232 (fixed upstream bug 44712)
- added P231 (fixes CVE-2008-2665, CVE-2008-2666)
- added P230 (fixes CVE-2008-2829)

* Mon Jul 14 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-9mdv2009.0
+ Revision: 235415
- rebuild

* Thu Jul 10 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-8mdv2009.0
+ Revision: 233358
- fix deps and linkage with c-client

* Mon Jun 23 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-7mdv2009.0
+ Revision: 228147
- rebuilt due to PayloadIsLzma problems

* Sun Jun 22 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-6mdv2009.0
+ Revision: 227920
- merged sybase support

* Mon Jun 16 2008 Anssi Hannula <anssi@mandriva.org> 3:5.2.6-5mdv2009.0
+ Revision: 219517
- build with main freetds; it has equal functionality now
  (php-freetds_mssql.diff renamed to php-freetds.diff with renaming
   hunks removed)

* Mon Jun 16 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-4mdv2009.0
+ Revision: 219348
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Fri May 16 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-3mdv2009.0
+ Revision: 208087
- bump release
- fix the freetds_mssql stuff
- rebuild

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.6-1mdv2009.0
+ Revision: 200057
- 5.2.6
- drop numerous upstream patches
- suhosin-patch-5.2.6-0.9.6.2

* Sat Apr 19 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-14mdv2009.0
+ Revision: 195829
- fix #40229 by dropping P195 (Prepared statements and bound values in PHP PDO MySQL don't work)
- added autoconf-2.62 fixes (spec file hacks + P218)
- added patches from upstream:
 - P219 - bug44594
 - P220 - bug44603
 - P221 - bug44613
 - P222 - bug44663
 - P223 - fixes possible stack buffer overflow in FastCGI SAPI
 - P224 - bug32979
 - P225 - bug44591
 - P226 - bug44650
 - P227 - bug44667
 - P228 - fixes weird behavior in CGI parameter parsing
 - P229 - bug44673
- drop P195 (bug44200) was unessesary
- added a more complete fix for bug44189

* Tue Apr 01 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-13mdv2008.1
+ Revision: 191385
- bump release
- added more upstream fixes
- added even more patches...
- added a whole bunch of upstream patches, bug number
  designated its file name
- added P151 to fix upstream bug 42177
- added P150 to fix upstream bug 43559
- added P149 to fix upstream bug 44046 (better patch)
- added P149 to fix upstream bug 44046
- added P148 to fix upstream bug 43505
- added P147 to fix upstream bug 42850
- added P146 to fix upstream bug 43495
- added P145 to fix upstream bug 43482
- added P144 to fix upstream bug 43386
- added P143 to fix upstream bug 43373
- added P142 from upstream that adds missing Reflection API metadata for DOM classes
- added P141 to fix upstream bug 43364
- added P140 to plug an suspected sec hole
- added P139 to fix upstream bug 43092
- added P138 to fix upstream bug 43994
- added P137 to fix upstream bug 43301
- added P136 to fix upstream bugs 43808,43527,43003,42190,41599
- added P135 to fix upstream bug 43293
- added P134 to fix upstream bug 43276
- added P133 to fix upstream bug 43248
- added P132 to fix upstream bug 37076
- added P131 to fix upstream bug 43221
- added P130 to fix upstream bug 43216
- added P129 to fix upstream bug 43201
- added P128 to fix upstream bug 43182
- added P127 that fixes upstream bug 43128
- added P126 to fix upstream bug 43105
- added P125 to fix upstream bug 44191
- added P124 to fix upstream bug 42945
- added P123 to fix upstream bug 42838
- added P122 to fix upstream bug 42779
- added P119 to fix upstream mysql fixes
- added P120 to fix upstream mysqli fixes
- added P118 that fixes upstream bug 42369
- use the complete fix for upstream bug 42272 (new patch)
- added P117 to fix upstream bug 42272
- added P116 that fixes numerous upstream bugs for OCI8
- P211 fixes CVE-2008-1384
- added P211 - fix integer overflow in length calculation

* Fri Feb 29 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-12mdv2008.1
+ Revision: 176686
- fix CVE-2008-0599

* Tue Feb 12 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-11mdv2008.1
+ Revision: 166131
- fix some of the rpmlint errors
- add reference to upstream #42604 for the huge list of buildconflicts

* Fri Feb 01 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-10mdv2008.1
+ Revision: 161203
- fix deps
- attempt to make the test suite working again
- drop redundant patches

* Fri Feb 01 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-9mdv2008.1
+ Revision: 161123
- rebuild

  + Pixel <pixel@mandriva.com>
    - nicer fix for "Buggy float to string conversion" on ix86 (#37171)

* Thu Jan 31 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-8mdv2008.1
+ Revision: 160816
- use another approach using -fno-tree-vrp on 32bit machines after recieving info from peroyvind

* Thu Jan 31 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-7mdv2008.1
+ Revision: 160697
- fix deps
- added P106 from fc9 that makes php use system time zone info

* Wed Jan 30 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-6mdv2008.1
+ Revision: 160467
- fix #37171 (PHP : Buggy float to string conversion (ex "0.0:" instead of "0.1"))

* Wed Jan 23 2008 Thierry Vignaud <tv@mandriva.org> 3:5.2.5-5mdv2008.1
+ Revision: 157266
- rebuild with fixed %%serverbuild macro

* Fri Dec 21 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-4mdv2008.1
+ Revision: 136515
- rebuilt against new build deps
- make it possible to link against db-4.6

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Mon Nov 12 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-3mdv2008.1
+ Revision: 108219
- suhosin-patch-5.2.5-0.9.6.2

* Mon Nov 12 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-2mdv2008.1
+ Revision: 108177
- don't use %%post, %%postun for the debug and devel subpackages (whoops!)

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-1mdv2008.1
+ Revision: 107529
- 5.2.5
- restart apache if needed

* Fri Nov 02 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-0.RC2.3mdv2008.1
+ Revision: 105413
- bump release
- ship some needed code in the devel package (take #2)

* Fri Nov 02 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-0.RC2.2mdv2008.1
+ Revision: 105295
- ship some needed code in the devel package

* Fri Nov 02 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.5-0.RC2.1mdv2008.1
+ Revision: 105236
- 5.2.5RC2
- rediffed P300
- don't pack useless stuff (gained approx. 7mb)

* Fri Sep 14 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.4-2mdv2008.0
+ Revision: 85585
- suhosin-patch-5.2.4-0.9.6.2

* Sat Sep 01 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.4-1mdv2008.0
+ Revision: 77387
- 5.2.4 (check http://www.php.net/releases/5_2_4.php)
- dropped obsolete/implemented patches; P4,P19,P31,P103,P111
- rediffed patches; P1,P7,P8,P20
- rediffed the suhosin patch (P301)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-10mdv2008.0
+ Revision: 64294
- rebuild

* Wed Aug 08 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-9mdv2008.0
+ Revision: 60315
- require the latest php-suhosin version
- use the bundled php-json code instead
- rebuilt against latest net-snmp-libs

* Sat Jun 23 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-8mdv2008.0
+ Revision: 43407
- use the new %%serverbuild macro

* Wed Jun 20 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-7mdv2008.0
+ Revision: 41861
- rediffed a lot of patches
- don't use curlwrappers
- fix deps
- use new P20 from pld, it also obsoletes P29

* Fri Jun 15 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-6mdv2008.0
+ Revision: 40071
- don't lie in the php-gd description, fixes #31410

* Wed Jun 13 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-5mdv2008.0
+ Revision: 38671
- fix naming of the ini files

* Tue Jun 12 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-4mdv2008.0
+ Revision: 38190
- bump release
- forgot to ship the source :)
- use distro conditional -fstack-protector
- major spec file rework, most bundled extensions are from now on build from this package
- added some patches that fixes different build problems
- use distro conditional -fstack-protector

* Sun Jun 03 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-2mdv2008.0
+ Revision: 34809
- suhosin-patch-5.2.3-0.9.6.2

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-1mdv2008.0
+ Revision: 33674
- 5.2.3 (fixes CVE-2007-1887 (improved), CVE-2007-1900, CVE-2007-2756, CVE-2007-2872)
- rediffed P25

* Sat May 26 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.2-2mdv2008.0
+ Revision: 31529
- updated the kolab2 patches (P11,P12)

* Mon May 07 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.2-1mdv2008.0
+ Revision: 24053
- 5.2.2
- suhosin-patch-5.2.2-0.9.6.2

* Tue May 01 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.2-0.RC2.0mdv2008.0
+ Revision: 19991
- 5.2.2RC2
- suhosin-patch-5.2.2rc2
- drop upstream patches; P106,P200,P210,P211,P,P212,P213,P214,P215

* Thu Apr 19 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.1-5mdv2008.0
+ Revision: 14941
- bump release

* Thu Apr 19 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.1-4mdv2008.0
+ Revision: 14938
- P211: security fix for CVE-2007-1001
- P212: security fix for CVE-2007-1285
- P213: security fix for CVE-2007-1583
- P214: security fix for CVE-2007-1718
- P215: security fix for CVE-2007-1454


* Fri Mar 09 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2.1-4mdv2007.1
+ Revision: 139553
- add the new php-timezonedb package as a dep to solve future presumptive problems

* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.1-3mdv2007.1
+ Revision: 134256
- fix deps

* Sun Mar 04 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.1-2mdv2007.1
+ Revision: 132333
- sync with fc (5.2.1-3)

* Fri Feb 09 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.1-1mdv2007.1
+ Revision: 118391
- use the gzip tar ball

* Wed Feb 07 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.1-0mdv2007.1
+ Revision: 117335
- 5.2.1
- suhosin-patch-5.2.1-0.9.6.2
- rediffed and dropped upstream patches

* Wed Feb 07 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-15mdv2007.1
+ Revision: 117063
- fix CVE-2007-0455

* Wed Dec 13 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-14mdv2007.1
+ Revision: 96376
- fix deps

* Fri Nov 24 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-13mdv2007.1
+ Revision: 87040
- fix build, sometimes it builds and sometimes not...
- rebuild
- added support for curl-7.16.0 (P209)

* Wed Nov 15 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-10mdv2007.1
+ Revision: 84539
- silly rabbit..., can't use "with" need to use "enable"

* Tue Nov 14 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-9mdv2007.1
+ Revision: 84165
- rebuild
- rebuild
- rebuild
- rebuild
- fix deps
- the pcre extension has to be compiled in statically
- broke out php-openssl and php-zlib into sub packages
- fix the long standing rpath issue

* Sun Nov 12 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-4mdv2007.0
+ Revision: 83488
- rebuild
- suhosin patch 0.9.6.2
- revert to the predictable automake version

* Thu Nov 09 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-2mdv2007.1
+ Revision: 79246
- suhosin patch 0.9.6.1

* Tue Nov 07 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-1mdv2007.0
+ Revision: 77319
- 5.2.0 (Major feature enhancements)
- suhosin-patch-5.2.0-0.9.6
- spec file cleansing
- rediffed patches; P1,P7,P23
- dropped obsolete/upstream patches; P22,P24,P26,P33,P209
- added P113 to make the php-imap build cleaner
- drop obsolete virtual provides
- use automake1.9 where needed instead of automake1.7
- use the bundled libtool
- require latest php-suhosin-0.9.10
- require php-filter and php-json (from pecl) to mimic a default php build
- fix better build after peeking at PLD again...

* Thu Nov 02 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.6-5mdv2007.1
+ Revision: 75149
- added fixes (P209) for latest imap c-client 2006 (andreas)

* Tue Oct 31 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.6-4mdv2007.1
+ Revision: 74298
- rebuild
- remove the "subrel" macro (duh!)

* Tue Oct 31 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.6-3.1mdv2007.1
+ Revision: 74289
- suhosin patch 0.9.6
- nuked the hardened-patch
- added the suhosin patch 0.9.5 and apply it per default (P300)
- rediffed patches; P7,P23
- P300 seems to address CVE-2006-4812, so no patching is needed
- force dependancy on the upcoming php-suhosin extension
- Import php

* Mon Aug 28 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.6-1
- 5.1.6 (Major security fixes)
- hardening-patch-5.1.5-0.4.14 (rediffed)
- deactivate upstream php-5.1.4-security-fix-5.patch (P203)

* Fri Aug 18 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-7mdv2007.0
- hardening-patch-5.1.4-0.4.14

* Thu Jul 27 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-6mdv2007.0
- hardening-patch-5.1.4-0.4.12
- drop the broken out patches P204,P205,P206,P207,P208 and use the full
  php-5.1.4-security-fix-5.patch (P203). those patches originates from
  that one. P203 fixes CVE-2006-2563,CVE-2006-2660,CVE-2006-1990,
  CVE-2006-3011 and some other security fixes. please read Changelog.secfix

* Wed Jul 19 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-5mdv2007.0
- P204: security fix for CVE-2006-2563
- P205: security fix for CVE-2006-2660
- P206: security fix - complete fix for CVE-2006-1990 on 64bit
- P207: security fix for CVE-2006-3011
- P208: check for open_basedir and safe_mode restrictions on imap_open
- P209: high characters fix for wddx
- rediffed the hardening-patch (P301)

* Tue Jun 06 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-4mdv2007.0
- rebuilt due to package loss

* Tue Jun 06 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-3mdv2007.0
- new tarball (contains the pear/install-pear-nozlib.phar file)
- hardening-patch-5.1.4-0.4.11
- added P203 (fixes open_basedir/safe_mode bypass via the realpath() cache)
- added S5 to keep a record of the licensing issues with the hardening-patch

* Sat May 06 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-2mdk
- added P30,P31,P32 from debian

* Sat May 06 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-1mdk
- 5.1.4
- hardening-patch-5.1.4-0.4.9

* Thu May 04 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.3-1mdk
- 5.1.3 (fixes CVE-2006-1490)
- rediffed P1,P7,P14

* Thu Apr 27 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-8mdk
- rebuild

* Wed Apr 26 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-7mdk
- added P29 to be able to track spam zombies

* Tue Apr 04 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-6mdk
- added P202 to fix CVE-2006-1490

* Wed Mar 22 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-5mdk
- fix deps

* Thu Feb 02 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-4mdk
- new group (Development/PHP) and iurt rebuild

* Mon Jan 30 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-3mdk
- added P24 from PLD (thanks!) to finally fix a nasty behaviour
  that loaded php.ini from current dir
- added P25,P26,P28,P28 from PLD

* Tue Jan 17 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-2mdk
- fix deps after reading how a default install works

* Sun Jan 15 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-1mdk
- 5.1.2
- rediffed P4,P8
- added P14 because some extensions stopped building
- added P15 do drop libedit in php-readline, it refused to build otherewise
- fix deps

* Mon Dec 26 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.1-4mdk
- added P13 (enables mod_php to manually add apache output filters)

* Sun Dec 18 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.1-3mdk
- added the Mandriva logo (P23) in phpinfo(); (after looking at pld)

* Tue Nov 29 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.1-2mdk
- hardening-patch-5.1.1-0.4.8

* Mon Nov 28 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.1-1mdk
- 5.1.1
- drop the php-yp dep as it is in pecl now

* Sun Nov 27 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-2mdk
- hardening-patch-5.1.0-0.4.6

* Fri Nov 25 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-1mdk
- 5.1.0

* Wed Nov 23 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC6.1mdk
- 5.1.0RC6, includes fixes for CVE-2005-3054,CVE-2005-3319,CVE-2005-3353
  CVE-2005-3388,CVE-2005-3389,CVE-2005-3390,CVE-2005-3388
- drop upstream patches; P114
- added parts from the CVE-2005-3388 patch from updates (P202)

* Sun Nov 13 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC4.2mdk
- rebuilt against openssl-0.9.8a

* Thu Nov 03 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC4.1mdk
- 5.1.0RC4
- rediffed patches; P4, P9, P120
- drop obsolete patches; P5, P100
- hardening-patch-5.0.5-0.4.5

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC1.2mdk
- rebuilt to provide a -debug package too

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC1.1mdk
- 5.1.0RC1
- dropped upstream implemented and redundant patches
- rediffed P4,P8,P9,P10,P100,P101,P120,P121
- fix deps
- hardening-patch-5.0.5-0.4.3

* Wed Sep 07 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.5-1mdk
- 5.0.5 (Major security fixes and closes about 150+ bugs)
- rediffed P4,P8,P100,P120,P121
- dropped upstream implemented patches; P109,P110,P113 (P120 
  was partly applied)

* Wed Sep 07 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-9mdk
- hardening-patch-5.0.4-0.4.1

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-8mdk
- rule out pear auto deps

* Sat Jul 30 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-7mdk
- added work arounds for rpm bugs, "Requires(foo,bar)" don't work

* Tue Jul 12 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-6mdk
- hardening-patch-5.0.4-0.3.2
- reworked the --with/--without magic

* Thu Jul 07 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-5mdk
- added rediffed P11 and P12 from the openpkg kolab2 packages

* Sun Jun 05 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-4mdk
- fix deps (typo)

* Sun Jun 05 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-3mdk
- fix deps

* Sat Jun 04 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-2mdk
- rebuild

* Fri May 27 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-1mdk
- rename the package (php5/php)
- sync with fedora
- use better anti ^M stripper
- use new rpm-4.4.x pre,post magic
- reworked the test suite run, many tests fails. some are fixed
  in cvs, and some are not and simply fails.

* Sun Apr 17 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-1mdk
- 5.0.4
- rediff P4,P6,P8,P9.P100
- drop P59,P60,P60 as they are implemented upstream

* Sun Mar 20 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-8mdk
- use the %%mkrel macro

* Thu Feb 17 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-7mdk
- it wasn't possible to build it --with hardened, fixed

* Wed Feb 16 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-6mdk
- fix description
- strip away annoying ^M, better approach

* Sat Feb 12 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-5mdk
- hardened-php-0.2.6 is disabled as it totally breaks commercial 
  applications like Zend(tm) stuff... :(
- added P57-P67 from fedora
- fix a *lot* of wrong-script-end-of-line-encoding rpmlint errors...

* Mon Jan 31 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-4mdk
- fix deps and conditional %%multiarch

* Fri Jan 14 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-3mdk
- hardened-php-0.2.6

* Thu Dec 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-2mdk
- fix deps for the devel package
- drop S5, it's in the NEWS file anyhow

* Thu Dec 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-1mdk
- 5.0.3
- new hardened-php-0.2.4 patch (P11)
- rediffed P4
- drop P55
- new P56

* Thu Dec 09 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.2-3mdk
- misc spec file fixes
- make and run the tests
- more lib64 fixes (P4,P55)

* Mon Nov 08 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.2-2mdk
- added P11 (from www.hardened-php.net)

* Sat Sep 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.2-1mdk
- 5.0.2

* Sun Aug 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.1-1mdk
- 5.0.1

* Mon Jul 19 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.0-1mdk
- 5.0.0
- used pld magic to make the shared lib and the php binaries
- rediffed and added some patches
- used parts from my private spec files
- get rid of the php-devel/PHP_BUILD file
- broke out ftp, yp, pcre, gettext, posix, ctype, sysvsem, sysvshm
- drop the "extensions hack", use another way in the info
- had to enable libxml in order to build some xml related modules

* Thu Jul 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.8-1mdk
- security fixes release (CAN-2004-0594, CAN-2004-0595)

* Tue Jul 13 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-5mdk
- remove redundant provides

* Sat Jun 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-4mdk
- sync with fedora (P57,P58) (4.3.7-3)

* Sat Jun 12 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-3mdk
- fix deps

* Thu Jun 10 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-2mdk
- added P11 (fixes one minor annoyance while running the tests)
- added P56 (fedora)

* Sat Jun 05 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-1mdk
- 4.3.7

* Thu May 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-5mdk
- fixed P8 and P10
- added P11 (fixes from 4.3.7RC1)
- updated S5

* Sat May 22 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-4mdk
- fix P5, i messed it up...
- nuke some patch -b droplets because it pollutes the php-devel package

* Sat May 22 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-3mdk
- rediffed P5, P21, P22
- added P23 - P29 from PLD, slightly adjusted

* Fri May 21 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-2mdk
- added P21 - P25 from fedora
- use the %%configure2_5x macro
- added P10 to make phpize work
- fix deps
- move scandir to /etc/php.d
- misc spec file fixes

* Wed May 05 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-1mdk
- rediffed P1 and P20
- drop P40, it's included

* Sun Mar 21 2004 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.3.4-4mdk
- fix PHP bug #25547
- fix bug22414.phpt

