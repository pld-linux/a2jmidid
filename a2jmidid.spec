# not under active development, let's use latest code in GIT
%define commit 034d5db

Summary:	Daemon for exposing legacy ALSA sequencer applications in JACK MIDI system
Summary(pl.UTF-8):	Demon udostępniający tradycyjne aplikacje sekwencera ALSA w systemie MIDI JACK
Name:		a2jmidid
Version:	8
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://repo.or.cz/a2jmidid.git/snapshot/%{commit}.tar.gz
# Source0-md5:	df6b7cfb372fcafef532eefe08eab448
URL:		http://repo.or.cz/a2jmidid.git/
BuildRequires:	alsa-lib-devel
BuildRequires:	dbus-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A daemon for exposing legacy ALSA sequencer applications in JACK MIDI
system.

%description -l pl.UTF-8
Demon udostępniający tradycyjne aplikacje sekwencera ALSA w systemie
MIDI JACK.

%prep
%setup -qn %{name}-%{commit}

%build
CC="%{__cc}" \
CXX="%{__cxx}" \
CPP="%{__cpp}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LINKFLAGS="%{rpmldflags}" \
./waf configure \
	--prefix="%{_prefix}"

./waf build -vv

%install
rm -rf $RPM_BUILD_ROOT

./waf install --destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
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
