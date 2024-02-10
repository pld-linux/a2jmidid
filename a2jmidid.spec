Summary:	Daemon for exposing legacy ALSA sequencer applications in JACK MIDI system
Summary(pl.UTF-8):	Demon udostępniający tradycyjne aplikacje sekwencera ALSA w systemie MIDI JACK
Name:		a2jmidid
Version:	12
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.ladish.org/a2jmidid/%{name}-%{version}.tar.bz2
# Source0-md5:	8335cf6bdc52527fb9d5989e5cea18fe
URL:		https://a2jmidid.ladish.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	dbus-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A daemon for exposing legacy ALSA sequencer applications in JACK MIDI
system.

%description -l pl.UTF-8
Demon udostępniający tradycyjne aplikacje sekwencera ALSA w systemie
MIDI JACK.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python$,%{__python3},' a2j_control

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.rst NEWS.rst README
%attr(755,root,root) %{_bindir}/a2j
%attr(755,root,root) %{_bindir}/a2j_control
%attr(755,root,root) %{_bindir}/a2jmidi_bridge
%attr(755,root,root) %{_bindir}/a2jmidid
%attr(755,root,root) %{_bindir}/j2amidi_bridge
%{_datadir}/dbus-1/services/org.gna.home.a2jmidid.service
%{_mandir}/man1/a2j.1*
%{_mandir}/man1/a2j_control.1*
%{_mandir}/man1/a2jmidi_bridge.1*
%{_mandir}/man1/a2jmidid.1*
%{_mandir}/man1/j2amidi_bridge.1*
