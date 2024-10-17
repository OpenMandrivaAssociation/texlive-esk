Name:		texlive-esk
Version:	18115
Release:	2
Summary:	Package to encapsulate Sketch files in LaTeX sources
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/esk
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esk.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esk.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The ESK package allows to encapsulate Sketch files in LaTeX
sources. This is very useful for keeping illustrations in sync
with the text. It also frees the user from inventing
descriptive names for new files that fit into the confines of
file system conventions. Sketch is a 3D scene description
language by Eugene K. Ressler and can generate TikZ and
PSTricks code. ESK behaves in a similar fashion to EMP (which
encapsulates Metapost files), and was in fact developed from
it.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/esk/esk.sty
%doc %{_texmfdistdir}/doc/latex/esk/COPYING
%doc %{_texmfdistdir}/doc/latex/esk/README
%doc %{_texmfdistdir}/doc/latex/esk/esk.pdf
%doc %{_texmfdistdir}/doc/latex/esk/eskman.pdf
#- source
%doc %{_texmfdistdir}/source/latex/esk/Makefile
%doc %{_texmfdistdir}/source/latex/esk/esk.drv
%doc %{_texmfdistdir}/source/latex/esk/esk.dtx
%doc %{_texmfdistdir}/source/latex/esk/esk.ins
%doc %{_texmfdistdir}/source/latex/esk/eskman.drv

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
