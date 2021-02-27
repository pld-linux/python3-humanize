#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Python 3 humanize utilities
Summary(pl.UTF-8):	Narzędzia Pythona 3 humanize
Name:		python3-humanize
Version:	2.0.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/humanize/
Source0:	https://files.pythonhosted.org/packages/source/h/humanize/humanize-%{version}.tar.gz
# Source0-md5:	65b289c0ec1a76a1d572aebc7cfed96f
URL:		https://pypi.org/project/humanize/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-freezegun
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This modest package contains various common humanization utilities,
like turning a number into a fuzzy human readable duration ('3 minutes
ago') or into a human readable size or throughput.

%description -l pl.UTF-8
Ten skromny pakiet zawiera różne narzędzia do ogólnej poprawy
interakcji z ludźmi - jak zamiana liczby na przybliżoną formę czytelną
dla człowieka ("3 minuty temu") albo czytelny dla człowieka rozmiar
czy przepustowość.

%prep
%setup -q -n humanize-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE README.md
%{py3_sitescriptdir}/humanize
%{py3_sitescriptdir}/humanize-%{version}-py*.egg-info
