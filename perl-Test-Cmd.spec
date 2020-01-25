#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Cmd
Summary:	Test::Cmd - Perl module for portable testing of commands and scripts
#Summary(pl.UTF-8):	
Name:		perl-Test-Cmd
Version:	1.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	462ed981f09e02a5d9bdfb309425ede0
URL:		http://www.baldmt.com/Test-Cmd/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Test::Cmd module provides a low-level framework for portable
automated testing of executable commands and scripts (in any language,
not just Perl), especially commands and scripts that interact with the
file system.

The Test::Cmd module makes no assumptions about what constitutes
a successful or failed test.  Attempting to read a file that doesn't
exist, for example, may or may not be an error, depending on the
software being tested.

Consequently, no Test::Cmd methods (including the new() method)
exit, die or throw any other sorts of exceptions (but they all do
return useful error indications).  Exceptions or other error status
should be handled by a higher layer: a subclass of Test::Cmd, or
another testing framework such as the Test or Test::Simple Perl
modules, or by the test itself.

(That said, see the Test::Cmd::Common module if you want a similar
module that provides exception handling, either to use directly in
your own tests, or as an example of how to use Test::Cmd.)

In addition to running tests and evaluating conditions, the Test::Cmd
module manages and cleans up one or more temporary workspace
directories, and provides methods for creating files and directories
in those workspace directories from in-line data (that is,
here-documents), allowing tests to be completely self-contained. When
used in conjunction with another testing framework, the Test::Cmd
module can function as a fixture (common startup code for multiple
tests) for simple management of command execution and temporary
workspaces.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/Cmd
%{_mandir}/man3/*
