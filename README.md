# php7.1-mga 


RPM Spec, patch and diff files for build php 7.1.11 (27 Oct 2017) in Mageia 6


After install, the package [php-timezonedb](https://madb.mageia.org/package/show/name/php-timezonedb/application/0/arch/x86_64) and all the php extension as [php-suhosin](https://madb.mageia.org/package/show/application/0/arch/x86_64/name/php-suhosin) ,
[php-redis](https://madb.mageia.org/package/show/application/0/arch/x86_64/name/php-sasl) , [php-sasl](https://madb.mageia.org/package/show/application/0/arch/x86_64/name/php-redis) needs rebuild with this version.


## QuickUsage


### Create rpmbuild structure in /~

```
 $ mkdir -p ~/rpmbuild/{BUILD,RPMS/i586,RPMS/x86_64,RPMS/noarch,SOURCES,SRPMS,SPECS,tmp}
```
create file [.rpmmacros](https://wiki.mageia.org/en/Packagers_RPM_tutorial#.rpmmacros_file_creation)


### Put files in folders

Download and replace in

```
~/rpmbuild/
```

### Install dependencies

For build rpm 

```
 # urpmi rpm-build rpmlint task-c++-devel task-c-devel
```

For compile php7 you needs all dependencies listed in .spec (BuildRequires) 

you can install all them with: (dnf rulez!)

```
 # dnf builddep php.spec
```

As note you need install lib64fbclient-devel or libfbclient-devel


### Build

Remember use with your own user

```
$ cd  ~/rpmbuild/SPECS
$ rpmbuild -ba php.spec
```
