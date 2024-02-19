%global forgeurl https://github.com/SimonN/LixD/

Name:           lix
Version:        0.10.7
Release:        0.5%{?dist}
Summary:        A single and multiplaer puzzle game inspired by Lemmings
Group:          Games and Entertainment
# CC0-1.0 for everything, expect "Bitstream Vera and Public Domain" for dejavu-sans fonts
License:        CC0-1.0 AND (Bitstream Vera and Public Domain)
URL:            https://www.lixgame.com/
# Add -i -v for detailed information
%forgemeta
Source:         %{forgesource}
Source1:        lix-dub-deps-local-0.10-20230402.tar.xz
# TODO: Add explicit versioning - https://github.com/SimonN/LixD/issues/457
Source2:        https://www.lixgame.com/dow/lix-music.zip
BuildRequires:  ldc dub
BuildRequires:  pkgconf-pkg-config
BuildRequires:  enet-devel
BuildRequires:  allegro5-devel allegro5-addon-acodec-devel allegro5-addon-audio-devel allegro5-addon-image-devel allegro5-addon-ttf-devel
# dub uses git client to determine version of dependencies in local cache
BuildRequires:  git

Recommends:     lix-music = %{version}-%{release}

%description
Lix is a puzzle game inspired by Lemmings. Lix is free and open source.
Assign skills to guide the lix through over 700 singleplayer puzzles.
Design your own levels with the included editor.
Attack and defend in real-time multiplayer for 2 to 8 players: Who can save the most lix?


%package music
Summary: Music for Lix - a single and multiplaer puzzle game inspired by Lemmings
# CC0-1.0 for menulix.ogg and minim-mobius/, CC-BY-4.0 for rubix/
License: CC0-1.0 AND CC-BY-4.0

%description music
Music for Lix - a single and multiplaer puzzle game inspired by Lemmings.


%prep
%setup -q -n LixD-%{version}
tar xJf %{SOURCE1}
unzip %{SOURCE2}

%build
export DFLAGS="%{_d_optflags}"
export DUB_DEPS_LOCAL_PATH=$(pwd)/dub-deps-local
dub add-path "$DUB_DEPS_LOCAL_PATH"
# TODO: Run unit-tests?
dub build --nodeps  --cache=local -f -b releaseXDG
dub remove-path "$DUB_DEPS_LOCAL_PATH"
# Needed?
#dub clean-caches

%install
install -Dm 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
# TODO: can system font be used?
cp -ar data/ images/ levels/ %{buildroot}%{_datadir}/%{name}
cp -ar music/ %{buildroot}%{_datadir}/%{name}
install -Dm 0644 doc/lix.6 %{buildroot}%{_mandir}/man6/lix.6
install -Dm 0644 data/images/lix_logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.lixgame.Lix.svg
install -Dm 0644 data/desktop/com.lixgame.Lix.metainfo.xml %{buildroot}%{_datadir}/metainfo/com.lixgame.Lix-metainfo.xml
install -Dm 0644 data/desktop/com.lixgame.Lix.desktop %{buildroot}%{_datadir}/applications/com.lixgame.Lix.desktop

%files
%doc README.md doc/cmdargs.txt doc/history.txt doc/levmaint.txt doc/thanks.txt
%license doc/copying.txt
%{_bindir}/lix
%{_datadir}/lix/data
%{_datadir}/lix/images
%{_datadir}/lix/levels
%{_datadir}/icons/hicolor/scalable/apps/com.lixgame.Lix.svg
%{_datadir}/applications/com.lixgame.Lix.desktop
%{_datadir}/metainfo/com.lixgame.Lix-metainfo.xml
%{_mandir}/man6/lix.6*

%files music
%{_datadir}/lix/music

%changelog
* Sun Apr 02 2023 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> 0.10.7-0.5
- improve version rule for "Recommends"
- remove superfluous "clean" section (as suggested by linter)

* Sun Apr 02 2023 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> 0.10.7-0.4
- generate debuginfo packages

* Sun Apr 02 2023 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> 0.10.7-0.3
- recommended music subpackage
- remove duplicated svg icon (3,6MB)

* Sun Apr 02 2023 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> 0.10.7-0.2
- local (offline) dub dependencies

* Sat Mar 25 2023 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> 0.10.7-0.1
- initial package (loosely based on the SUSE version)

