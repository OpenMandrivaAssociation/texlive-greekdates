Name:		texlive-greekdates
Version:	15878
Release:	2
Summary:	Provides ancient Greek day and month names, dates, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/greekdates
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greekdates.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greekdates.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greekdates.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides easy access to ancient Greek names of days
and months of various regions of Greece. In case the historical
information about a region is not complete, we use the Athenian
name of the month. Moreover commands and options are provided,
in order to completely switch to the "ancient way", commands
such as \today.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/greekdates/greekdates.sty
%doc %{_texmfdistdir}/doc/latex/greekdates/README
%doc %{_texmfdistdir}/doc/latex/greekdates/greekdates.pdf
#- source
%doc %{_texmfdistdir}/source/latex/greekdates/greekdates.dtx
%doc %{_texmfdistdir}/source/latex/greekdates/greekdates.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
