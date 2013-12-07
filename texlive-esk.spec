# revision 18115
# category Package
# catalog-ctan /macros/latex/contrib/esk
# catalog-date 2010-05-11 12:36:30 +0200
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-esk
Version:	1.0
Release:	3
Summary:	Package to encapsulate Sketch files in LaTeX sources
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/esk
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esk.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esk.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 751577
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718366
- texlive-esk
- texlive-esk
- texlive-esk
- texlive-esk

