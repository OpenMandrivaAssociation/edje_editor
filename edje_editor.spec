%define name edje_editor
%define version 0.3.2
%define svn	20090227
%define release %mkrel 2

Summary:	Visual editor for edje file
Name:		%name
Version:	%version
Release:	%release
License: 	BSD
Group: 		Graphical desktop/Enlightenment
Source:		%{name}-%{version}.tar.bz2
Source1:	%name.desktop
URL:		http://www.enlightenment.org/
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	edje-devel >= 0.9.9.050, edje >= 0.9.9.050
BuildRequires: 	evas-devel >= 0.9.9.050
Buildrequires:	ecore-devel >= 0.9.9.050
BuildRequires:	etk-devel >= 0.1.0.42
Requires: 	edje >= 0.9.9.050
BuildRequires:  imagemagick, flex
BuildRequires:  desktop-file-utils

%description
Edje_editor is a visual editor for edje file

%prep
%setup -q -n %name-%version

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
rm -f %buildroot
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cp -vf %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Graphics" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%name.desktop

mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}
install -m 644 data/images/e17.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 data/images/e17.png %buildroot%_iconsdir/%name.png
convert -resize 16x16 data/images/e17.png %buildroot%_miconsdir/%name.png

mkdir -p %buildroot%{_datadir}/pixmaps
cp data/images/e17.png %buildroot%{_datadir}/pixmaps/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post 
%{update_menus} 
%endif

%if %mdkversion < 200900
%postun 
%{clean_menus} 
%endif

%files
%defattr(-,root,root)
%doc  AUTHORS COPYING* README
%{_bindir}/%name
%{_datadir}/%name
%_liconsdir/*.png
%_iconsdir/*.png
%_miconsdir/*.png
%_datadir/pixmaps/*.png
%{_datadir}/applications/*

