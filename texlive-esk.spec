%global tl_name esk
%global tl_revision 18115

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Package to encapsulate Sketch files in LaTeX sources
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/esk
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esk.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esk.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The ESK package allows to encapsulate Sketch files in LaTeX sources.
This is very useful for keeping illustrations in sync with the text. It
also frees the user from inventing descriptive names for new files that
fit into the confines of file system conventions. Sketch is a 3D scene
description language by Eugene K. Ressler and can generate TikZ and
PSTricks code. ESK behaves in a similar fashion to EMP (which
encapsulates MetaPost files), and was in fact developed from it.

