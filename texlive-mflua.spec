Name:		texlive-mflua
Version:	62774
Release:	1
Summary:	configuration and base files for MFLua
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mflua
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mflua.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
For information on this Lua-enabled Metafont, see, for example:
tug.org/TUGboat/tb32-2/tb101scarso.pdf.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/mflua
%{_texmfdistdir}/texmf-dist/metafont/mflua

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
