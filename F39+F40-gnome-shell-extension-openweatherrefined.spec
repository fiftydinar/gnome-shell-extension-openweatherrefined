%global extension   openweatherrefined
%global uuid        openweather-extension@penguin-teal.github.io
%global gettext     gnome-shell-extension-%{extension}
%global version     133
%global commit      59a1490afd8cdfe97ef4e8fd6932cc2d77138456

Name:           gnome-shell-extension-%{extension}
Version:        %{version}
Release:        1%{?dist}
Summary:        Display weather information for any location on Earth in the GNOME Shell
License:        GPLv3
URL:            https://github.com/penguin-teal/gnome-openweather
Source0:        %{url}/archive/%{commit}/gnome-openweather-%{commit}.tar.gz
BuildArch:      noarch
BuildRequires:  gettext
Requires:       gnome-shell >= 45, gnome-shell < 47

%description
Display weather information for any location on Earth in the GNOME Shell

%prep
%autosetup -n gnome-openweather-%{commit}

%install
# install main extension files
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
cp -r src/* %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
cp -r media %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
cp -r metadata.json %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

# install locale files
pushd po
for po in *.po; do
    install -d -m 0755 %{buildroot}%{_datadir}/locale/${po%.po}/LC_MESSAGES
    msgfmt -o %{buildroot}%{_datadir}/locale/${po%.po}/LC_MESSAGES/%{gettext}.mo $po
done
popd
%find_lang %{gettext}

%files -f %{gettext}.lang
%doc README.md
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
* Sat Apr 06 2024 Fifty Dinar <srbaizoki4@tuta.io> - 133-1
- note: Changelog also includes unofficial release v132-2 & v132-3 changelogs
- improvement: Hide "Gusts" in pop-up if unavailable (instead of showing "?")
- improvement: Colon after "Gusts" in pop-up 

* Fri Apr 05 2024 Fifty Dinar <srbaizoki4@tuta.io> - 132-3
- note: This is an unofficial release supplied by the packager to include some fixes to the previous release
- bugfix: Failure to change pressure unit to kPa
- bugfix: Feels like... stats are not showing in side of pop-up 

* Wed Apr 03 2024 Fifty Dinar <srbaizoki4@tuta.io> - 132-2
- note: This is an unofficial release supplied by the packager to include some fixes for Fedora 39 users
- bugfix: Revert to add_factor for Gnome 45 to fix some regressions
- bugfix: Crash on first-run Geoclue fail
- bugfix: -0 temperature display

* Sat Mar 30 2024 Fifty Dinar <srbaizoki4@tuta.io> - 132-1
- improvement: Gnome 46 support (while maintaining Gnome 45 support)
- improvement: "Use Extension API Key" now is flipped and reads "Use Custom API Key" for clarity
- improvement: Revert wind direction to use letters instead of arrows by default
- improvement: Improve Czech translations (thanks lev741)
- improvement: Improve Dutch translations (thanks Heimen Stoffels)

* Fri Mar 29 2024 Fifty Dinar <srbaizoki4@tuta.io> - 131-2
- packaging: Make sure that this version of extension doesn't install on Gnome 46/Fedora 40

* Sun Mar 10 2024 Fifty Dinar <srbaizoki4@tuta.io> - 131-1
- improvement: Notice on how to search up new locations in "Edit Location" menu
- improvement: No more space between humidity value and "%"
- bugfix: Fix extension not initializing sometimes
- bugfix: Fix migrations only happening on first extension download
