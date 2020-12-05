Summary:	Measure complexity of C source
Summary(pl.UTF-8):	Mierzenie złożoności kodu źródłowego w C
Name:		complexity
Version:	1.13
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	http://ftp.gnu.org/gnu/complexity/%{name}-%{version}.tar.xz
# Source0-md5:	93aa255c784e68edfd64d96f705ad3f3
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/complexity/
BuildRequires:	autogen-devel >= 5.18.16
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo >= 4.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Complexity is a tool designed for analyzing the complexity of C
program functions. It is very similar to the McCabe scoring, but
addresses several issues not considered in that scoring scheme.

%description -l pl.UTF-8
Complexity to narzędzie zaprojektowane do analizy złożoności funkcji w
języku C. Jest bardzo podobne do punktacji McCabe, ale bierze pod
uwagę kilka aspektów nie uwzględnianych w tym schemacie.

%prep
%setup -q
%patch0 -p1

%build
cd src
# need to regenerate [opts.c, opts.h] to build with autogen < 5.18.17
autogen opts.def
cd ..
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/complexity
%attr(755,root,root) %{_bindir}/cx-vs-mc
%{_infodir}/complexity.info*
%{_mandir}/man1/complexity.1*
