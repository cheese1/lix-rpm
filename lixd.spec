%global debug_package %{nil}
%global forgeurl https://github.com/SimonN/LixD/

Name:           lix
Version:        0.10.7
Release:        0.1%{?dist}
Summary:        A single and multiplaer puzzle game inspired by Lemmings
Group:          Games and Entertainment
# CC0-1.0 for exerything, expect "Bitstream Vera and Public Domain" for dejavu-sans fonts and CC-BY-4.0 for Rubix's music
License:        CC0-1.0 AND (Bitstream Vera and Public Domain) AND CC-BY-4.0
URL:            https://www.lixgame.com/
# Add -i -v for detailed information
%forgemeta
Source:         %{forgesource}
# TODO: Add music source
BuildRequires:  ldc dub
BuildRequires:  pkgconf-pkg-config
BuildRequires:   enet-devel
BuildRequires:  allegro5-devel allegro5-addon-acodec-devel allegro5-addon-audio-devel allegro5-addon-image-devel allegro5-addon-ttf-devel

# Deps:
# pobrać tagi z gita dla projektów (binarki ze zmianą katalogu z dub-repo są ok, ale tagi są bardziej wiarygodne
# lix-dub-deps-local-X.Y-DATE
# dub add-path dub-deps-local
# dub build --nodeps  --cache=local ...
# dub remove-path ...
# dub clean-caches - ?

%description
Lix is a puzzle game inspired by Lemmings. Lix is free and open source.
Assign skills to guide the lix through over 700 singleplayer puzzles.
Design your own levels with the included editor.
Attack and defend in real-time multiplayer for 2 to 8 players: Who can save the most lix?

%prep
%setup -q -n LixD-%{version}

%build
export DFLAGS="%{_d_optflags}"
dub build -f -b releaseXDG

%install
install -Dm 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
#TODO: can system fonts be used?
cp -ar data/ images/ levels/ %{buildroot}%{_datadir}/%{name}
install -Dm 0644 doc/lix.6 %{buildroot}%{_mandir}/man6/lix.6
#TODO: Needs to be duplicated?
install -Dm 0644 data/images/lix_logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -Dm 0644 data/images/lix_logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.lixgame.Lix.svg
install -Dm 0644 data/desktop/com.lixgame.Lix.metainfo.xml %{buildroot}%{_datadir}/metainfo/com.lixgame.Lix-metainfo.xml
install -Dm 0644 data/desktop/com.lixgame.Lix.desktop %{buildroot}%{_datadir}/applications/com.lixgame.Lix.desktop
# TODO: Separate package for music
#cp -ar music/%{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%doc README.md doc/cmdargs.txt doc/history.txt doc/levmaint.txt doc/thanks.txt
%license doc/copying.txt
%{_bindir}/lix
%{_datadir}/lix
%{_datadir}/icons/hicolor/scalable/apps/lix.svg
%{_datadir}/icons/hicolor/scalable/apps/com.lixgame.Lix.svg
%{_datadir}/applications/com.lixgame.Lix.desktop
%{_datadir}/metainfo/com.lixgame.Lix-metainfo.xml
%{_mandir}/man6/lix.6*

%changelog
* Sat Mar 25 2023 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> 0.10.7-0.1
- initial package

