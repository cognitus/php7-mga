# php7.1-mga 

RPM Spec, patch and diff files for php 7.1.10 (28 Sep 2017) in Mageia 6


After install, the package [php-timezonedb](https://madb.mageia.org/package/show/name/php-timezonedb/application/0/arch/x86_64) needs rebuild with this version and probably [php-suhosin](https://madb.mageia.org/package/show/application/0/arch/x86_64/name/php-suhosin)


## QuickUsage

### Created rpmbuild structure in /~

```
 $ mkdir -p ~/rpmbuild/{BUILD,RPMS/i586,RPMS/x86_64,RPMS/noarch,SOURCES,SRPMS,SPECS,tmp}
```

### Install dependencies

For build rpm 

```
 # urpmi rpm-build rpmlint task-c++-devel task-c-devel
```

For compile php7 you needs all dependencies listed in .spec (BuildRequires)



### Put files in folders

Download and replace folders in

```
~/rpmbuild/
```

### Build

```
cd  ~/rpmbuild/SPECS
rpmbuild -ba php.spec
```
