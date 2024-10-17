%define name edje_editor
%define version 0.3.2
%define svn	20090808
%define release %mkrel 4

Summary:	Visual editor for edje file
Name:		%name
Version:	%version
Release:	%release
License: 	BSD
Group: 		Graphical desktop/Enlightenment
Source:		%{name}-%{version}.tar.bz2
URL:		https://www.enlightenment.org/
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	edje-devel >= 0.9.9.050, edje >= 0.9.9.050
BuildRequires: 	evas-devel >= 0.9.9.052
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
%_iconsdir/*.png
%{_datadir}/applications/*
