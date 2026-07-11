%global tl_name greekdates
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Provides ancient Greek day and month names, dates, etc.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/greekdates
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/greekdates.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/greekdates.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/greekdates.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides easy access to ancient Greek names of days and
months of various regions of Greece. In case the historical information
about a region is not complete, we use the Athenian name of the month.
Moreover commands and options are provided, in order to completely
switch to the "ancient way", commands such as \today.

