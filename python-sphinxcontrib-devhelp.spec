%define	module	sphinxcontrib-devhelp

Summary:	Devhelp help file support for the Sphinx documentation generator
Name:		python-%{module}
Version:	2.0.0
Release:	1
Source0:	https://github.com/sphinx-doc/%{module}/archive/%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://sphinx-doc.org/
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
# Python 2 support dropped before 6.0
Obsoletes:	python2-%{module} < %{EVRD}
BuildSystem:	python

%description
Devhelp help file support for the Sphinx documentation generator

%prep
%autosetup -p1 -n %{module}-%{version}

%files
%{py_puresitedir}/sphinxcontrib*
