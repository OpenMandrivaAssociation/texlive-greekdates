Name:		texlive-greekdates
Version:	1.0
Release:	1
Summary:	Provides ancient Greek day and month names, dates, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/greekdates
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greekdates.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greekdates.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greekdates.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides easy access to ancient Greek names of days
and months of various regions of Greece. In case the historical
information about a region is not complete, we use the Athenian
name of the month. Moreover commands and options are provided,
in order to completely switch to the "ancient way", commands
such as \today.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
