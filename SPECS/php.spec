%define _build_pkgcheck_set %{nil}
%define _build_pkgcheck_srpm %{nil}

%define _disable_lto 1

%define build_test 1
%{?_with_test: %{expand: %%global build_test 1}}
%{?_without_test: %{expand: %%global build_test 0}}

%define build_libmagic 0
%{?_with_libmagic: %{expand: %%global build_libmagic 1}}
%{?_without_libmagic: %{expand: %%global build_libmagic 0}}

%define php7_common_major 5
%define libname %mklibname php7_common %{php7_common_major}

%define __noautoreq '.*/bin/awk|.*/bin/gawk'

Summary:	The PHP7 scripting language
Name:		php
Version:	7.1.9
Release:	%mkrel 1
Source0:	http://ch1.php.net/distributions/php-%{version}.tar.xz
Group:		Development/PHP
License:	PHP License
URL:		http://www.php.net
Source2:	maxlifetime
Source3:	php.crond
Source4:	php-fpm.service
Source5:	php-fpm.sysconf
Source6:	php-fpm.logrotate
# S7 comes from ext/fileinfo/create_data_file.php but could be removed someday
Source7:	create_data_file.php
Source9:        php-fpm-tmpfiles.conf
Source10:	php.ini
Patch1:		php-shared.diff
Patch3:		php-libtool.diff
Patch4:		php-phpize.diff
Patch5:		php-phpbuilddir.diff
# http://www.outoforder.cc/projects/apache/mod_transform/
# http://www.outoforder.cc/projects/apache/mod_transform/patches/php7-apache2-filters.patch
Patch6:		php5-apache2-filters.diff
# remove libedit once and for all
Patch7:		php-no_libedit.diff
Patch8:		php-xmlrpc_epi.patch
Patch9:		php-xmlrpc_no_rpath.diff
Patch10:	php-5.5.7-detect-freetype-2.5.x.patch
Patch11:	php-5.3.8-bdb-5.2.diff
Patch12:	php-5.5.6-db-6.0.patch
Patch13:	php-7.0.1-clang-warnings.patch
#####################################################################
# Stolen from PLD
Patch20:	php-mail.diff
Patch21:	php-filter-shared.diff
Patch22:	php-dba-link.patch
Patch23:	php-zlib-for-getimagesize.patch
Patch26:	php-5.3.9RC2-mcrypt-libs.diff
# for kolab2
# P50 was rediffed from PLD (php-5.3.3-8.src.rpm) which merges the annotation and status-current patches
Patch27:	php-imap-annotation+status-current.diff
# P51 was taken from http://kolab.org/cgi-bin/viewcvs-kolab.cgi/server/php/patches/php-5.3.2/
Patch28:	php-imap-myrights.diff
Patch29:	php-5.3.x-fpm-0.6.5-shared.diff
Patch30:	php-5.3.x-fpm-0.6.5-mdv_conf.diff
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
Patch228:	php-5.3.0RC2-xmlrpc-epi_fix.diff

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

BuildRequires:	apache-devel >= 2.2.0
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

# stupid postgresql... stupid build system...
# this is needed due to the postgresql packaging and due to bugs like this:
# https://qa.mandriva.com/show_bug.cgi?id=52527
%define postgresql_version %(pg_config &>/dev/null && pg_config 2>/dev/null | grep "^VERSION" | awk '{ print $4 }' 2>/dev/null || echo 0)

%description
PHP7 is an HTML-embeddable scripting language. PHP7 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP7 is fairly simple. The
most common use of PHP7 coding is probably as a replacement for CGI scripts.

%package	cli
Summary:	PHP7 CLI interface
Group:		Development/Other
Requires:	%{libname} >= %{EVRD}
Requires:	php-ctype >= %{EVRD}
Requires:	php-filter >= %{EVRD}
Requires:	php-ftp >= %{EVRD}
Requires:	php-gettext >= %{EVRD}
Requires:	php-hash >= %{EVRD}
Requires:	php-ini >= %{version}
Requires:	php-json >= %{EVRD}
Requires:	php-openssl >= %{EVRD}
Requires:	php-posix >= %{EVRD}
Requires:	php-session >= %{EVRD}
# Suggests:	php-suhosin >= 0.9.33
Requires:	php-sysvsem >= %{EVRD}
Requires:	php-sysvshm >= %{EVRD}
Requires:	php-timezonedb >= 3:2009.10
Requires:	php-tokenizer >= %{EVRD}
Requires:	php-xmlreader >= %{EVRD}
Requires:	php-xmlwriter >= %{EVRD}
Requires:	php-zlib >= %{EVRD}
Requires:	php-xml >= %{EVRD}
Provides:	php = %{EVRD}
Provides:	/usr/bin/php

%description	cli
PHP7 is an HTML-embeddable scripting language. PHP7 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP7 is fairly simple. The
most common use of PHP7 coding is probably as a replacement for CGI scripts.

This package contains a command-line (CLI) version of php. You must also
install libphp7_common. If you need apache module support, you also need to
install the apache-mod_php package.

%package	dbg
Summary:	Debugging version of the PHP7 CLI interface
Group:		Development/Other
Requires:	%{libname} >= %{EVRD}
Requires:	php-ctype >= %{EVRD}
Requires:	php-filter >= %{EVRD}
Requires:	php-ftp >= %{EVRD}
Requires:	php-gettext >= %{EVRD}
Requires:	php-hash >= %{EVRD}
Requires:	php-ini >= %{version}
Requires:	php-json >= %{EVRD}
Requires:	php-openssl >= %{EVRD}
Requires:	php-posix >= %{EVRD}
Requires:	php-session >= %{EVRD}
# Suggests:	php-suhosin >= 0.9.33
Requires:	php-sysvsem >= %{EVRD}
Requires:	php-sysvshm >= %{EVRD}
Requires:	php-timezonedb >= 3:2009.10
Requires:	php-tokenizer >= %{EVRD}
Requires:	php-xmlreader >= %{EVRD}
Requires:	php-xmlwriter >= %{EVRD}
Requires:	php-zlib >= %{EVRD}
Requires:	php-xml >= %{EVRD}
Provides:	php = %{EVRD}

%description	dbg
PHP7 is an HTML-embeddable scripting language. PHP7 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP7 is fairly simple. The
most common use of PHP7 coding is probably as a replacement for CGI scripts.

This package contains a debugging version of php. You must also
install libphp7_common. If you need apache module support, you also need to
install the apache-mod_php package.

%package	cgi
Summary:	PHP7 CGI interface
Group:		Development/Other
Requires:	%{libname} >= %{EVRD}
Requires:	php-ctype >= %{EVRD}
Requires:	php-filter >= %{EVRD}
Requires:	php-ftp >= %{EVRD}
Requires:	php-gettext >= %{EVRD}
Requires:	php-hash >= %{EVRD}
Requires:	php-ini >= %{version}
Requires:	php-json >= %{EVRD}
Requires:	php-openssl >= %{EVRD}
Requires:	php-posix >= %{EVRD}
Requires:	php-session >= %{EVRD}
# Suggests:	php-suhosin >= 0.9.33
Requires:	php-sysvsem >= %{EVRD}
Requires:	php-sysvshm >= %{EVRD}
Requires:	php-timezonedb >= 3:2009.10
Requires:	php-tokenizer >= %{EVRD}
Requires:	php-xmlreader >= %{EVRD}
Requires:	php-xmlwriter >= %{EVRD}
Requires:	php-zlib >= %{EVRD}
Requires:	php-xml >= %{EVRD}
Provides:	php = %{EVRD}
Provides:	php-fcgi = %{EVRD}
Obsoletes:	php-fcgi
# because of a added compat softlink
Conflicts:	php-fcgi < %{EVRD}

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
Provides:	php-pcre = %{EVRD}
Provides:	php-simplexml = %{EVRD}
Requires:	systemd-units
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description -n	%{libname}
This package provides the common files to run with different implementations of
PHP7. You need this package if you install the php standalone package or a
webserver with php support (ie: apache-mod_php).

%package	devel
Summary:	Development package for PHP7
Group:		Development/C
Requires:	%{libname} >= %{EVRD}
Requires:	autoconf automake libtool
Requires:	bison
Requires:	byacc
Requires:	chrpath
Requires:	dos2unix
Requires:	flex
Requires:	openssl
Requires:	re2c >= 0.9.11
Requires:	tcl
Requires:	pam-devel
Requires:	pkgconfig(libpcre)
Requires:	pkgconfig(libxml-2.0)
Requires:	pkgconfig(libxslt)
Requires:	pkgconfig(openssl)


%description	devel
The php-devel package lets you compile dynamic extensions to PHP7. Included
here is the source for the php extensions. Instead of recompiling the whole php
binary to add support for, say, oracle, install this package and use the new
self-contained extensions support. For more information, read the file
SELF-CONTAINED-EXTENSIONS.

%package	openssl
Summary:	OpenSSL extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	openssl
This is a dynamic shared object (DSO) for PHP that will add OpenSSL support.

%package	zlib
Summary:	Zlib extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	zlib
This is a dynamic shared object (DSO) for PHP that will add zlib compression
support to PHP.

%package	doc
Summary:	Documentation for PHP
Group:		Development/PHP

%description	doc
Documentation for php.

%package	bcmath
Summary:	The bcmath module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	bcmath
This is a dynamic shared object (DSO) for PHP that will add bc style precision
math functions support.

For arbitrary precision mathematics PHP offers the Binary Calculator which
supports numbers of any size and precision, represented as strings.

%package	bz2
Summary:	Bzip2 extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	bz2
This is a dynamic shared object (DSO) for PHP that will add bzip2 compression
support to PHP.

The bzip2 functions are used to transparently read and write bzip2 (.bz2)
compressed files.

%package	calendar
Summary:	Calendar extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

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
Requires:	%{libname} >= %{EVRD}

%description	ctype
This is a dynamic shared object (DSO) for PHP that will add ctype support.

The functions provided by this extension check whether a character or string
falls into a certain character class according to the current locale (see also
setlocale()).

%package	curl
Summary:	Curl extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

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
Requires:	%{libname} >= %{EVRD}

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
Requires:	%{libname} >= %{EVRD}

%description	dom
This is a dynamic shared object (DSO) for PHP that will add dom support.

The DOM extension is the replacement for the DOM XML extension from PHP 4. The
extension still contains many old functions, but they should no longer be used.
In particular, functions that are not object-oriented should be avoided.

The extension allows you to operate on an XML document with the DOM API.

%package	enchant
Summary:	Libenchant binder, support near all spelling tools
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	enchant
Enchant is a binder for libenchant. Libenchant provides a common API for many
spell libraries:

 - aspell/pspell (intended to replace ispell)
 - hspell (hebrew)
 - ispell 
 - myspell (OpenOffice project, mozilla)
 - uspell (primarily Yiddish, Hebrew, and Eastern European languages)
   A plugin system allows to add custom spell support.
   see www.abisource.com/enchant/

%package	exif
Summary:	EXIF extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}
Requires:	php-mbstring >= %{EVRD}

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
Requires:	%{libname} >= %{EVRD}

%description	fileinfo
This extension allows retrieval of information regarding vast majority of file.
This information may include dimensions, quality, length etc...

Additionally it can also be used to retrieve the mime type for a particular
file and for text files proper language encoding.

%package	filter
Summary:	Extension for safely dealing with input parameters
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	filter
The Input Filter extension is meant to address this issue by implementing a set
of filters and mechanisms that users can use to safely access their input data.

%package	ftp
Summary:	FTP extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

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
Requires:	%{libname} >= %{EVRD}

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
Requires:	%{libname} >= %{EVRD}

%description	gettext
This is a dynamic shared object (DSO) for PHP that will add gettext support.

The gettext functions implement an NLS (Native Language Support) API which can
be used to internationalize your PHP applications. Please see the gettext
documentation for your system for a thorough explanation of these functions or
view the docs at http://www.gnu.org/software/gettext/manual/gettext.html.

%package	gmp
Summary:	Gmp extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	gmp
This is a dynamic shared object (DSO) for PHP that will add arbitrary length
number support using the GNU MP library.

%package	hash
Summary:	HASH Message Digest Framework
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	hash
Native implementations of common message digest algorithms using a generic
factory method.

Message Digest (hash) engine. Allows direct or incremental processing of
arbitrary length messages using a variety of hashing algorithms.

%package	iconv
Summary:	Iconv extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

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
Requires:	%{libname} >= %{EVRD}

%description	imap
This is a dynamic shared object (DSO) for PHP that will add IMAP support.

These functions are not limited to the IMAP protocol, despite their name. The
underlying c-client library also supports NNTP, POP3 and local mailbox access
methods.

%package	intl
Summary:	Internationalization extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	intl
This is a dynamic shared object (DSO) for PHP that will add
Internationalization support.

Internationalization extension implements ICU library functionality in PHP.

%package	json
Summary:	JavaScript Object Notation
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	json
Support for JSON (JavaScript Object Notation) serialization.

%package	ldap
Summary:	LDAP extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

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
Requires:	%{libname} >= %{EVRD}
# To make it easier to find for e.g. Roundcube requesting php-multibyte
Provides:	%{name}-multibyte = %{EVRD}

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
Requires:	%{libname} >= %{EVRD}

%description	mcrypt
This is a dynamic shared object (DSO) for PHP that will add mcrypt support.

This is an interface to the mcrypt library, which supports a wide variety of
block algorithms such as DES, TripleDES, Blowfish (default), 3-WAY, SAFER-SK64,
SAFER-SK128, TWOFISH, TEA, RC3 and GOST in CBC, OFB, CFB and ECB cipher modes.
Additionally, it supports RC6 and IDEA which are considered "non-free".

%package	mysqli
Summary:	MySQL database module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}
Obsoletes:	%{name}-mysql < %{EVRD}

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
Requires:	%{libname} >= %{EVRD}

%description	mysqlnd
This is a dynamic shared object (DSO) for PHP that will add MySQL native
database support.

These functions allow you to access MySQL database servers. More information
about MySQL can be found at http://www.mysql.com/.

Documentation for MySQL can be found at http://dev.mysql.com/doc/.

%package	odbc
Summary:	ODBC extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	odbc
This is a dynamic shared object (DSO) for PHP that will add ODBC support.

In addition to normal ODBC support, the Unified ODBC functions in PHP allow you
to access several databases that have borrowed the semantics of the ODBC API to
implement their own API. Instead of maintaining multiple database drivers that
were all nearly identical, these drivers have been unified into a single set of
ODBC functions.

%package	opcache
Summary:	Opcode cache for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	opcache
Opcode cache for PHP

%package	pcntl
Summary:	Process Control extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

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
Requires:	%{libname} >= %{EVRD}

%description	pdo
PDO provides a uniform data access interface, sporting advanced features such
as prepared statements and bound parameters. PDO drivers are dynamically
loadable and may be developed independently from the core, but still accessed
using the same API.

Read the documentation at http://www.php.net/pdo for more information.

%package	pdo_dblib
Summary:	Sybase Interface driver for PDO
Group:		Development/PHP
Requires:       freetds >= 0.63
Requires:	php-pdo >= %{EVRD}
Requires:	%{libname} >= %{EVRD}

%description	pdo_dblib
PDO_DBLIB is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to Microsoft SQL Server and Sybase databases through the
FreeTDS libary.

%package	pdo_mysql
Summary:	MySQL Interface driver for PDO
Group:		Development/PHP
Requires:	php-pdo >= %{EVRD}
Requires:	%{libname} >= %{EVRD}

%description	pdo_mysql
PDO_MYSQL is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to MySQL 3.x and 4.x databases.
 
PDO_MYSQL will take advantage of native prepared statement support present in
MySQL 4.1 and higher. If you're using an older version of the mysql client
libraries, PDO will emulate them for you.

%package	pdo_odbc
Summary:	ODBC v3 Interface driver for PDO
Group:		Development/PHP
Requires:	php-pdo >= %{EVRD}
Requires:	%{libname} >= %{EVRD}

%description	pdo_odbc
PDO_ODBC is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to databases through ODBC drivers or through the IBM DB2
Call Level Interface (DB2 CLI) library. PDO_ODBC currently supports three
different "flavours" of database drivers:
 
 o ibm-db2  - Supports access to IBM DB2 Universal Database, Cloudscape, and
              Apache Derby servers through the free DB2 client.

 o unixODBC - Supports access to database servers through the unixODBC driver
              manager and the database's own ODBC drivers.

 o generic  - Offers a compile option for ODBC driver managers that are not
              explicitly supported by PDO_ODBC.

%package	pdo_pgsql
Summary:	PostgreSQL interface driver for PDO
Group:		Development/PHP
Requires:	php-pdo >= %{EVRD}
Requires:	%{libname} >= %{EVRD}
Requires:	postgresql-libs >= %{postgresql_version}

%description	pdo_pgsql
PDO_PGSQL is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to PostgreSQL databases.

%package	pdo_sqlite
Summary:	SQLite v3 Interface driver for PDO
Group:		Development/PHP
Requires:	php-pdo >= %{EVRD}
Requires:	%{libname} >= %{EVRD}

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
Requires:	%{libname} >= %{EVRD}
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
Requires:	%{libname} >= %{EVRD}
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
Requires:	%{libname} >= %{EVRD}

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
Requires:	%{libname} >= %{EVRD}

%description	pspell
This is a dynamic shared object (DSO) for PHP that will add pspell support to
PHP.

These functions allow you to check the spelling of a word and offer
suggestions.

%package	readline
Summary:	Readline extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

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
Requires:	%{libname} >= %{EVRD}

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
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	%{libname} >= %{EVRD}

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
Requires:	%{libname} >= %{EVRD}

%description	shmop
This is a dynamic shared object (DSO) for PHP that will add Shared Memory
Operations support.

Shmop is an easy to use set of functions that allows PHP to read, write, create
and delete Unix shared memory segments.

%package	snmp
Summary:	NET-SNMP extension module for PHP
Group:		Development/PHP
Requires:	net-snmp-mibs
Requires:	%{libname} >= %{EVRD}

%description	snmp
This is a dynamic shared object (DSO) for PHP that will add SNMP support using
the NET-SNMP libraries.

In order to use the SNMP functions you need to install the NET-SNMP package.

%package	soap
Summary:	Soap extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	soap
This is a dynamic shared object (DSO) for PHP that will add soap support.

The SOAP extension can be used to write SOAP Servers and Clients. It supports
subsets of SOAP 1.1, SOAP 1.2 and WSDL 1.1 specifications.

%package	sockets
Summary:	Sockets extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	sockets
This is a dynamic shared object (DSO) for PHP that will add sockets support.

The socket extension implements a low-level interface to the socket
communication functions based on the popular BSD sockets, providing the
possibility to act as a socket server as well as a client.

%package	sqlite3
Summary:	SQLite database bindings for PHP
Group:		Development/PHP
Requires:	php-pdo >= %{EVRD}
Requires:	%{libname} >= %{EVRD}
Obsoletes:	%name-sqlite

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
Requires:	%{libname} >= %{EVRD}

%description	sysvmsg
This is a dynamic shared object (DSO) for PHP that will add SysV message queues
support.

%package	sysvsem
Summary:	SysV sem extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	sysvsem
This is a dynamic shared object (DSO) for PHP that will add SysV semaphores
support.

%package	sysvshm
Summary:	SysV shm extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	sysvshm
This is a dynamic shared object (DSO) for PHP that will add SysV Shared Memory
support.

%package	tidy
Summary:	Tidy HTML Repairing and Parsing for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	tidy
Tidy is a binding for the Tidy HTML clean and repair utility which allows you
to not only clean and otherwise manipluate HTML documents, but also traverse
the document tree using the Zend Engine 2 OO semantics.

%package	tokenizer
Summary:	Tokenizer extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	tokenizer
This is a dynamic shared object (DSO) for PHP that will add Tokenizer support.

The tokenizer functions provide an interface to the PHP tokenizer embedded in
the Zend Engine. Using these functions you may write your own PHP source
analyzing or modification tools without having to deal with the language
specification at the lexical level.

%package	xml
Summary:	XML extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	xml
This is a dynamic shared object (DSO) for PHP that will add XML support. This
extension lets you create XML parsers and then define handlers for different
XML events.

%package	xmlreader
Summary:	Xmlreader extension module for PHP
Group:		Development/PHP
Requires:	php-dom
Requires:	%{libname} >= %{EVRD}

%description	xmlreader
XMLReader represents a reader that provides non-cached, forward-only access to
XML data. It is based upon the xmlTextReader api from libxml

%package	xmlrpc
Summary:	Xmlrpc extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	xmlrpc
This is a dynamic shared object (DSO) for PHP that will add XMLRPC support.

These functions can be used to write XML-RPC servers and clients. You can find
more information about XML-RPC at http://www.xmlrpc.com/, and more
documentation on this extension and its functions at
http://xmlrpc-epi.sourceforge.net/.

%package	xmlwriter
Summary:	Provides fast, non-cached, forward-only means to write XML data
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	xmlwriter
This extension wraps the libxml xmlWriter API. Represents a writer that
provides a non-cached, forward-only means of generating streams or files
containing XML data.

%package	xsl
Summary:	Xsl extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	xsl
This is a dynamic shared object (DSO) for PHP that will add xsl support.

The XSL extension implements the XSL standard, performing XSLT transformations
using the libxslt library

%package	wddx
Summary:	WDDX serialization functions
Group:		Development/PHP
Requires:	php-xml
Requires:	%{libname} >= %{EVRD}

%description	wddx
This is a dynamic shared object (DSO) that adds wddx support to PHP. 

These functions are intended for work with WDDX (http://www.openwddx.org/)

%package	zip
Summary:	A zip management extension for PHP
Group:		Development/PHP

%description	zip
This is a dynamic shared object (DSO) for PHP that will add zip support to
create and read zip files using the libzip library.

%package	fpm
Summary:	PHP7 FastCGI Process Manager
Group:		Development/Other
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	%{libname} >= %{EVRD}
Requires:	php-ctype >= %{EVRD}
Requires:	php-filter >= %{EVRD}
Requires:	php-ftp >= %{EVRD}
Requires:	php-gettext >= %{EVRD}
Requires:	php-hash >= %{EVRD}
Requires:	php-ini >= %{version}
Requires:	php-json >= %{EVRD}
Requires:	php-openssl >= %{EVRD}
Requires:	php-posix >= %{EVRD}
Requires:	php-session >= %{EVRD}
# Suggests:	php-suhosin >= 0.9.33
Requires:	php-sysvsem >= %{EVRD}
Requires:	php-sysvshm >= %{EVRD}
Requires:	php-timezonedb >= 3:2009.10
Requires:	php-tokenizer >= %{EVRD}
Requires:	php-xmlreader >= %{EVRD}
Requires:	php-xmlwriter >= %{EVRD}
Requires:	php-zlib >= %{EVRD}
Requires:	php-xml >= %{EVRD}
Provides:	php = %{EVRD}

%description	fpm
PHP7 is an HTML-embeddable scripting language. PHP7 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP7 is fairly simple. The
most common use of PHP7 coding is probably as a replacement for CGI scripts.

This package contains the FastCGI Process Manager. You must also install
libphp7_common.

%package -n	apache-mod_php
Summary:	The PHP HTML-embedded scripting language for use with apache
Group:		System/Servers
Requires(pre,postun):	rpm-helper
Requires:	%{libname} = %{EVRD}
Requires:	apache >= 2.4.0

Requires:	%{name}-ctype = %{EVRD}
Requires:	%{name}-filter = %{EVRD}
Requires:	%{name}-ftp = %{EVRD}
Requires:	%{name}-gettext = %{EVRD}
Requires:	%{name}-hash = %{EVRD}
Requires:	%{name}-ini >= %{version}
Requires:	%{name}-json = %{EVRD}
Requires:	%{name}-openssl = %{EVRD}
Requires:	%{name}-pcre = %{EVRD}
Requires:	%{name}-posix = %{EVRD}
Requires:	%{name}-session = %{EVRD}
Requires:	%{name}-sysvsem = %{EVRD}
Requires:	%{name}-tokenizer = %{EVRD}
Requires:	%{name}-xmlreader = %{EVRD}
Requires:	%{name}-xmlwriter = %{EVRD}
Requires:	%{name}-zlib = %{EVRD}
Requires:	%{name}-xml = %{EVRD}
Requires:	%{name}-timezonedb >= 3:2009.10
# Suggests:	%{name}-suhosin >= 0.9.29
Conflicts:	%{name}-suhosin < 0.9.29
Provides:	mod_php = %{EVRD}
BuildRequires:	dos2unix

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


%package -n	php-ini
Summary:	INI files for PHP
Group:		Development/Other

%description -n	php-ini
The php-ini package contains the ini file required for PHP.


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
%patch3 -p0 -b .libtool.droplet
%patch4 -p1 -b .phpize.droplet
%patch5 -p1 -b .phpbuilddir.droplet
%patch6 -p1 -b .apache2-filters.droplet
#patch7 -p1 -b .no_libedit.droplet
%patch8 -p1 -b .xmlrpc_epi_header
%patch9 -p0 -b .xmlrpc_no_rpath.droplet
#patch10 -p1 -b .ft252~
%patch11 -p1 -b .bdb-5.2.droplet
%patch12 -p1 -b .db60~
%patch13 -p1 -b .clangwarn~

#####################################################################
# Stolen from PLD
# FIXME needs porting
#patch20 -p1 -b .mail.droplet
%patch21 -p0 -b .filter-shared.droplet
%patch22 -p0 -b .dba-link.droplet
%patch23 -p1 -b .zlib-for-getimagesize.droplet
%patch26 -p0 -b .mcrypt-libs.droplet
# for kolab2
# FIXME needs porting
#patch27 -p1 -b .imap-annotation.droplet
#patch28 -p1 -b .imap-myrights.droplet
# fpm stuff
%patch29 -p1 -b .shared-fpm.droplet


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
%patch121 -p0 -b .bug43221.droplet
%patch123 -p0 -b .bug43589.droplet
%patch226 -p0 -b .no-fvisibility_hidden.droplet
%patch227 -p0 -b .enchant_lib64_fix.droplet
%patch228 -p0 -b .xmlrpc-epi_fix.droplet


cp %{SOURCE2} maxlifetime
cp %{SOURCE3} php.crond
cp %{SOURCE4} php-fpm.service
cp %{SOURCE5} php-fpm.sysconf
cp %{SOURCE6} php-fpm.logrotate
cp %{SOURCE7} create_data_file.php

# lib64 hack
perl -p -i -e "s|/usr/lib|%{_libdir}|" php.crond

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

# likewise with these:
find php-devel -name "*.dsp" | xargs rm -f
find php-devel -name "*.mak" | xargs rm -f
find php-devel -name "*.w32" | xargs rm

# maek sure using system libs
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
# FIXME switch to external gd (--with-gd=shared,%_prefix) once php bug #60108 is fixed
for i in fpm cgi cli apxs; do
./configure \
    `[ $i = fpm ] && echo --disable-cli --enable-fpm --with-libxml-dir=%{_prefix} --with-fpm-user=apache --with-fpm-group=apache` \
    `[ $i = cgi ] && echo --disable-cli` \
    `[ $i = cli ] && echo --disable-cgi --enable-cli` \
    `[ $i = apxs ] && echo --with-apxs2=%{_bindir}/apxs` \
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
    --with-gd=shared --with-jpeg-dir=%{_prefix} --with-png-dir=%{_prefix} --with-zlib-dir=%{_prefix} --with-xpm-dir=%{_prefix}/X11R6 --with-freetype-dir=%{_prefix} --enable-gd-native-ttf \
    --enable-gd-jis-conv \
    --with-gettext=shared,%{_prefix} \
    --with-gmp=shared,%{_prefix} \
    --enable-hash=shared,%{_prefix} \
    --with-iconv=shared \
    --with-imap=shared,%{_prefix} --with-imap-ssl=%{_prefix} \
    --with-ldap=shared,%{_prefix} --with-ldap-sasl=%{_prefix} \
    --enable-mbstring=shared,%{_prefix} --enable-mbregex --with-libmbfl=%{_prefix} --with-onig=%{_prefix} \
    --with-mcrypt=shared,%{_prefix} \
    --with-mysql-sock=/run/mysqld/mysql.sock --with-zlib-dir=%{_prefix} \
    --with-mysqli=shared,%{_bindir}/mysql_config \
    --enable-mysqlnd=shared,%{_prefix} \
    --with-unixODBC=shared,%{_prefix} \
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
    --enable-zip=shared --with-libzip=%{_prefix} || (cat config.log && exit 1)

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

make -f Makefile.apxs install \
	INSTALL_ROOT=%{buildroot} \
	INSTALL_IT="\$(LIBTOOL) --mode=install install libphp7_common.la %{buildroot}%{_libdir}/"

# borked autopoo
rm -f %{buildroot}%{_bindir}/php %{buildroot}%{_bindir}/php-cgi
./libtool --silent --mode=install install sapi/cli/php %{buildroot}%{_bindir}/php
./libtool --silent --mode=install install sapi/cgi/php-cgi %{buildroot}%{_bindir}/php-cgi

# compat php-fcgi symink
ln -s php-cgi %{buildroot}%{_bindir}/php-fcgi

cp -dpR php-devel/* %{buildroot}%{_usrsrc}/php-devel/
install -m0644 run-tests*.php %{buildroot}%{_usrsrc}/php-devel/
install -m0644 main/internal_functions.c %{buildroot}%{_usrsrc}/php-devel/

install -m0644 sapi/cli/php.1 %{buildroot}%{_mandir}/man1/
install -m0644 scripts/man1/phpize.1 %{buildroot}%{_mandir}/man1/
install -m0644 scripts/man1/php-config.1 %{buildroot}%{_mandir}/man1/

# fpm
install -d %{buildroot}/lib/systemd/system
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -d %{buildroot}%{_sysconfdir}/php-fpm.d
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man8
install -d %{buildroot}/var/lib/php-fpm
install -d %{buildroot}/var/log/php-fpm
install -d %{buildroot}/run/php-fpm
install -D -p -m 0644 %{SOURCE9} %{buildroot}%{_tmpfilesdir}/php-fpm.conf
# a small bug here...
echo "; place your config here" > %{buildroot}%{_sysconfdir}/php-fpm.d/default.conf

./libtool --silent --mode=install install sapi/fpm/php-fpm %{buildroot}%{_sbindir}/php-fpm
install -m0644 sapi/fpm/php-fpm.8 %{buildroot}%{_mandir}/man8/
install -m0644 sapi/fpm/php-fpm.conf %{buildroot}%{_sysconfdir}/
install -m0644 php-fpm.service %{buildroot}/lib/systemd/system/
install -m0644 php-fpm.sysconf %{buildroot}%{_sysconfdir}/sysconfig/php-fpm
install -m0644 php-fpm.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/php-fpm

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
echo "extension = mysqli.so"		> %{buildroot}%{_sysconfdir}/php.d/37_mysqli.ini
echo "extension = enchant.so"		> %{buildroot}%{_sysconfdir}/php.d/38_enchant.ini
echo "extension = odbc.so"		> %{buildroot}%{_sysconfdir}/php.d/39_odbc.ini
echo "extension = pcntl.so"		> %{buildroot}%{_sysconfdir}/php.d/40_pcntl.ini
echo "extension = pdo.so"		> %{buildroot}%{_sysconfdir}/php.d/70_pdo.ini
echo "extension = pdo_dblib.so"		> %{buildroot}%{_sysconfdir}/php.d/71_pdo_dblib.ini
echo "extension = pdo_mysql.so"		> %{buildroot}%{_sysconfdir}/php.d/73_pdo_mysql.ini
echo "extension = pdo_odbc.so"		> %{buildroot}%{_sysconfdir}/php.d/75_pdo_odbc.ini
echo "extension = pdo_pgsql.so"		> %{buildroot}%{_sysconfdir}/php.d/76_pdo_pgsql.ini
echo "extension = pdo_sqlite.so"	> %{buildroot}%{_sysconfdir}/php.d/77_pdo_sqlite.ini
echo "extension = mysqlnd.so"		> %{buildroot}%{_sysconfdir}/php.d/78_mysqlnd.ini
echo "extension = pgsql.so"		> %{buildroot}%{_sysconfdir}/php.d/42_pgsql.ini
echo "extension = posix.so"		> %{buildroot}%{_sysconfdir}/php.d/43_posix.ini
echo "extension = pspell.so"		> %{buildroot}%{_sysconfdir}/php.d/44_pspell.ini
echo "extension = readline.so"		> %{buildroot}%{_sysconfdir}/php.d/45_readline.ini
echo "extension = recode.so"		> %{buildroot}%{_sysconfdir}/php.d/46_recode.ini
echo "extension = session.so"		> %{buildroot}%{_sysconfdir}/php.d/47_session.ini
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
cat >%{buildroot}%{_sysconfdir}/php.d/85_opcache.ini <<"EOF"
zend_extension = %{_libdir}/php/extensions/opcache.so
opcache.memory_consumption=128
opcache.interned_strings_buffer=8
opcache.max_accelerated_files=4000
opcache.revalidate_freq=60
opcache.fast_shutdown=1
opcache.enable_cli=1
EOF

install -m0755 maxlifetime %{buildroot}%{_libdir}/php/maxlifetime
install -m0644 php.crond %{buildroot}%{_sysconfdir}/cron.d/php

# mod_php

install -d %{buildroot}%{_sysconfdir}/httpd/conf/modules.d
install -d %{buildroot}%{_libdir}/httpd/modules
install -m 755 mod_php/.libs/*.so %{buildroot}%{_libdir}/httpd/modules

cat > %{buildroot}%{_sysconfdir}/httpd/conf/modules.d/170_mod_php.conf << EOF
LoadModule php_module %{_libdir}/httpd/modules/mod_php.so

AddType application/x-httpd-php .php
AddType application/x-httpd-php .phtml
AddType application/x-httpd-php-source .phps

DirectoryIndex index.php index.phtml
EOF

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

# inis
install -d -m 755 %{buildroot}%{_sysconfdir}/php.d
install -d -m 755 %{buildroot}%{_libdir}/php/extensions
install -d -m 755 %{buildroot}%{_datadir}/php

sed -e 's,/usr/lib,%{_libdir},g' %{SOURCE10} >%{buildroot}%{_sysconfdir}/php.ini
cp %{buildroot}%{_sysconfdir}/php.ini %{buildroot}%{_sysconfdir}/php-cgi-fcgi.ini

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

%post bcmath
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun bcmath
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post bz2
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun bz2
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post calendar
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun calendar
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post cgi
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun cgi
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post cli
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun cli
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post ctype
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun ctype
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post curl
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun curl
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post dba
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun dba
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post devel
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun devel
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post doc
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun doc
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post dom
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun dom
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post enchant
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun enchant
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post exif
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun exif
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post fileinfo
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun fileinfo
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post filter
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun filter
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post ftp
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun ftp
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post gd
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun gd
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post gettext
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun gettext
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post gmp
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun gmp
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post hash
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun hash
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post iconv
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun iconv
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post imap
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun imap
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post intl
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun intl
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post json
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun json
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post ldap
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun ldap
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mbstring
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mbstring
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mcrypt
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mcrypt
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mysqli
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mysqli
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mysqlnd
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mysqlnd
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post odbc
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun odbc
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post openssl
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun openssl
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pcntl
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pcntl
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pdo
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pdo
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pdo_dblib
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pdo_dblib
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pdo_mysql
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pdo_mysql
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pdo_odbc
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pdo_odbc
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pdo_pgsql
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pdo_pgsql
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pdo_sqlite
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pdo_sqlite
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pgsql
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pgsql
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post phar
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun phar
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post posix
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun posix
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pspell
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pspell
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post readline
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun readline
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post recode
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun recode
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%pre session
%_pre_useradd apache /var/www /bin/sh

%post session
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun session
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post shmop
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun shmop
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post snmp
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun snmp
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post soap
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun soap
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post sockets
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun sockets
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post sqlite3
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun sqlite3
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post sysvmsg
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun sysvmsg
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post sysvsem
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun sysvsem
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post sysvshm
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun sysvshm
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post tidy
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun tidy
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post tokenizer
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun tokenizer
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post wddx
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun wddx
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post xml
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun xml
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post xmlreader
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun xmlreader
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post xmlrpc
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun xmlrpc
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post xmlwriter
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun xmlwriter
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post xsl
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun xsl
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post zip
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun zip
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post zlib
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun zlib
if [ "$1" = "0" ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post fpm
%tmpfiles_create php-fpm
%_post_service php-fpm
if [ $1 = 1 ]; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%pre fpm
%_preun_service php-fpm
%_pre_useradd apache /var/www /bin/sh

%preun fpm
if [ $1 = 0 ]; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable php-fpm.service >/dev/null 2>&1 || :
    /bin/systemctl stop php-fpm.service >/dev/null 2>&1 || :
fi

%postun fpm
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ]; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart php-fpm.service >/dev/null 2>&1 || :
fi
%_postun_userdel apache

%post -n apache-mod_php
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun -n apache-mod_php
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%files doc
%doc CREDITS INSTALL LICENSE NEWS Zend/ZEND_LICENSE 
%doc php.ini-production php.ini-development configure_command
%doc README.openssl README.spl CREDITS.libxml CREDITS.zlib
%doc README.EXT_SKEL README.input_filter
%doc README.PARAMETER_PARSING_API README.STREAMS

%files -n %{libname}
%{_libdir}/libphp7_common.so.%{php7_common_major}*

%files cli
%doc CREDITS.cli README.cli TODO.cli
%{_bindir}/php
%{_mandir}/man1/php.1*

%files dbg
%{_bindir}/phpdbg
%{_mandir}/man1/phpdbg.1*

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
 %config(noreplace) %{_sysconfdir}/php.d/78_mysqlnd.ini
 %{_libdir}/php/extensions/mysqlnd.so

%files odbc
 %config(noreplace) %{_sysconfdir}/php.d/39_odbc.ini
 %{_libdir}/php/extensions/odbc.so

%files opcache
 %config(noreplace) %{_sysconfdir}/php.d/85_opcache.ini
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

%files pdo_mysql
%config(noreplace)  %{_sysconfdir}/php.d/73_pdo_mysql.ini
 %{_libdir}/php/extensions/pdo_mysql.so

%files pdo_odbc
%config(noreplace)  %{_sysconfdir}/php.d/75_pdo_odbc.ini
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

%files posix
 %config(noreplace) %{_sysconfdir}/php.d/43_posix.ini
 %{_libdir}/php/extensions/posix.so

%files pspell
 %config(noreplace) %{_sysconfdir}/php.d/44_pspell.ini
 %{_libdir}/php/extensions/pspell.so

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
/lib/systemd/system/php-fpm.service
 %config(noreplace) %{_sysconfdir}/php-fpm.conf
 %config(noreplace) %{_sysconfdir}/sysconfig/php-fpm
 %{_sysconfdir}/logrotate.d/php-fpm
 %dir %{_sysconfdir}/php-fpm.d
 %config(noreplace) %{_sysconfdir}/php-fpm.d/default.conf
 %{_sbindir}/php-fpm
 %{_mandir}/man8/php-fpm.8*
%attr(0711,apache,apache) %dir /var/lib/php-fpm
%attr(0711,apache,apache) %dir /var/log/php-fpm
%attr(0711,apache,apache) %dir /run/php-fpm
%{_tmpfilesdir}/php-fpm.conf

%files -n apache-mod_php
 %config(noreplace) %{_sysconfdir}/httpd/conf/modules.d/*.conf
 %{_libdir}/httpd/modules/*.so

%files -n php-ini
%config(noreplace) %{_sysconfdir}/php.ini
%config(noreplace) %{_sysconfdir}/php-cgi-fcgi.ini
%dir %{_sysconfdir}/php.d
%dir %{_libdir}/php
%dir %{_libdir}/php/extensions
%dir %{_datadir}/php

%changelog
* Sat Sep 09 2017 Tomás Flores <cognitus> 1.1.9-1.mga6
+ Ported from Openmandriva
+ Update version
- 7.1.9
