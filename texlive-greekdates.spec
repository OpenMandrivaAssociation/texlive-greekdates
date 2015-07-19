# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/greekdates
# catalog-date 2008-08-21 09:38:31 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-greekdates
Version:	1.0
Release:	10
Summary:	Provides ancient Greek day and month names, dates, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/greekdates
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greekdates.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greekdates.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greekdates.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752430
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718580
- texlive-greekdates
- texlive-greekdates
- texlive-greekdates
- texlive-greekdates

