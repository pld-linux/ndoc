Summary:	API documentation generation tool for .NET
Summary(pl.UTF-8):	Narzędzie do generowania dokumentacji API dla .NET
Name:		ndoc
Version:	1.3.1
Release:	0.1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/ndoc/%{name}-devel-v%{version}.zip
# Source0-md5:	8950a53dd3c379e41781ba7f1834e948
Patch0:		%{name}-no-warnaserror.patch
URL:		http://ndoc.sourceforge.net/
BuildRequires:	mono-csharp >= 1.1.4.20050221svn
BuildRequires:	nant
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NDoc generates class libraries documentation from .NET assemblies and
the XML documentation files generated by the C# compiler. It also
works with VB.NET and Nemerle. NDoc uses add-on documenters to
generate documentation in several different formats, including
MSDN-online style web pages.

%description -l pl.UTF-8
NDoc generuje dokumentacje bibliotek klas z assemblies .NET oraz
plików XML generowanych przez kompilator C# nad podstawie źródeł.
Działa również z VB.NET oraz Nemerle. NDoc używa wtyczek do generacji
dokumentacji w różnych formatach m.in. strony HTML w formacie
MSDN-online.

%prep
%setup -q -c
%patch0 -p1

%build
nant -t:mono-1.0

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir}/mono/ndoc,%{_bindir}}
install bin/mono/1.0/*.{dll,exe} $RPM_BUILD_ROOT%{_libdir}/mono/ndoc

echo "#!/bin/sh" > $RPM_BUILD_ROOT%{_bindir}/NDocConsole
echo 'exec mono %{_libdir}/mono/ndoc/NDocConsole.exe "$@"' >> $RPM_BUILD_ROOT%{_bindir}/NDocConsole
ln -sf NDocConsole $RPM_BUILD_ROOT%{_bindir}/ndoc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc/sdk/* examples
%attr(755,root,root) %{_bindir}/*
%{_libdir}/mono/ndoc
