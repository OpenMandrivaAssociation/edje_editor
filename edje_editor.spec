%define name edje_editor
%define version 0.1.4
%define release %mkrel 1

Summary:	Edje_editor is an visual editor for edje file.
Name:		%name
Version:	%version
Release:	%release
License: 	BSD
Group: 		Graphical desktop/Enlightenment
Source:		ftp://ftp.enlightenment.org/pub/enlightenment/%{name}-%{version}.tar.bz2
Source1:	%name.desktop
URL:		http://www.enlightenment.org/
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires: 	evas-devel >= 0.9.9.038, engrave-devel >= 0.1.0, edje-devel >= 0.5.0.038
Buildrequires:	ecore-devel >= 0.9.9.038, etk-devel >= 0.1.0.003
Requires: 	evas >= 0.9.9.038, edje >= 0.5.0.038
BuildRequires:  ImageMagick, flex
BuildRequires:  desktop-file-utils

%description
Edje_editor is an visual editor for edje file.
This is a prealpha state, don't expect nothing.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_menudir}

cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):\
        needs="X11" \
        section="Multimedia/Graphics" \
        title="%name" \
        longtitle="%name " \
        command="%{_bindir}/%name -e x11" \
        icon="expedite.png" \
        startup_notify="true" \
        xdg="true"
EOF

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

%post 
%{update_menus} 

%postun 
%{clean_menus} 

%files
%defattr(-,root,root)
%doc  AUTHORS COPYING* README
%{_bindir}/%name
%{_datadir}/%name
%{_menudir}/*
%_liconsdir/*.png
%_iconsdir/*.png
%_miconsdir/*.png
%_datadir/pixmaps/*.png
%{_datadir}/applications/*

