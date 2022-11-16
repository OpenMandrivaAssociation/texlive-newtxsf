Name:		texlive-newtxsf
Version:	59227
Release:	1
Summary:	Sans-math fonts for use with newtx
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/newtxsf
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newtxsf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newtxsf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a maths support that amounts to
modifications of the STIX sans serif Roman and Greek letters
with most symbols taken from newtxmath (which must of course be
installed and its map file enabled).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/newtxsf
%{_texmfdistdir}/fonts/vf/public/newtxsf
%{_texmfdistdir}/fonts/type1/public/newtxsf
%{_texmfdistdir}/fonts/tfm/public/newtxsf
%{_texmfdistdir}/fonts/map/dvips/newtxsf
%doc %{_texmfdistdir}/doc/fonts/newtxsf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
