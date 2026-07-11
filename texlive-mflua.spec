%global tl_name mflua
%global tl_revision 78968

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	configuration and base files for MFLua
Group:		Publishing
URL:		https://www.ctan.org/pkg/mflua
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mflua.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mflua.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(luatex)
Requires:	texlive(metafont)
Requires:	texlive(mflua.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
For information on this Lua-enabled Metafont, see, for example:
tug.org/TUGboat/tb32-2/tb101scarso.pdf.

