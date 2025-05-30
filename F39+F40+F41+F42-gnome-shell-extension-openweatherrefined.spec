%global extension   openweatherrefined
%global uuid        openweather-extension@penguin-teal.github.io
%global gettext     gnome-shell-extension-%{extension}
%global version     139

Name:           gnome-shell-extension-%{extension}
Version:        %{version}
Release:        2%{?dist}
Summary:        Display weather information for any location on Earth in the GNOME Shell
License:        GPLv3
URL:            https://github.com/penguin-teal/gnome-openweather
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  gettext
Requires:       gnome-shell >= 45, gnome-shell < 49

%description
Display weather information for any location on Earth in the GNOME Shell

%prep
%autosetup -n gnome-openweather-%{version}

%install
# install main extension files
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
cp -r src/* %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
cp -r media %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
# Modify metadata.json to support GNOME 48
sed -i 's/"47"/"47",\n    "48"/' metadata.json
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
* Mon Sep 23 2024 Fifty Dinar <srbaizoki4@tuta.io> - 139-2
- note: This is an unofficial release supplied by the packager to include support for GNOME 48
- improvement: Add GNOME 48 to metadata.json

* Mon Sep 23 2024 Fifty Dinar <srbaizoki4@tuta.io> - 139-1
- improvement: Add GNOME 47 to metadata.json

* Mon Jul 01 2024 Fifty Dinar <srbaizoki4@tuta.io> - 138-1
- improvement: Better French translations (thanks @Deuchnord)
- improvement: Better Russian translations (thanks @krotesk)
- improvement: Better Brazilian Portugese translations (thanks @Vinicius-Madeira)
- improvement: Better Turkish translations (thanks @furkansimsekli)
- improvement: Better English grammar
- bugfix: Fix wrong custom API keys being used (thanks @rakkhin)

* Fri Jun 28 2024 Fifty Dinar <srbaizoki4@tuta.io> - 137-1
- improvement: "Visual Crossing" removed from "Adaptive" setting's pool; it currently will only work with a personal API key
- bugfix: Custom API keys not being set correctly
- bugfix: Fix some API keys not being redacted with Copy Settings button

* Tue Jun 11 2024 Fifty Dinar <srbaizoki4@tuta.io> - 136-1
- feature: New "Visual Crossing" weather provider with 14-day-out forecasts
- improvement: Total Days Forecasted is now a number input box for 0 - 31 (15+ doesn't work with any default keys i.e. you have to have a paid custom key)
- improvement: Explanations for some more settings
- improvement: Better Spanish translations (thanks @federicolencina)
- improvement: Better Czech translations (thanks @lev741)
- bugfix: Fix bug where notifications spammed when a provider was rate-limiting

* Sat May 04 2024 Fifty Dinar <srbaizoki4@tuta.io> - 135-1
- feature: "Adaptive" provider which picks a random provider based on settings so one doesn't get too many requests
- feature: "Paste" settings option in Settings > About beside the "Copy" button
- improvement: Hide trailing zeroes after temperature
- improvement: Notify if a provider blocks a request because the call limit was reached
- improvement: Add locale to Copy Settings JSON
- improvement: Reload time format when Clock Format (24hr or AM/PM) is changed in GNOME Settings
- bugfix: Fix condition names not showing with OpenWeatherMap
- bugfix: Fix last day forecast of WeatherAPI.com showing all the same time
- bugfix: Fix weather provider attribution button in pop-up not updating when provider changes
- bugfix: Fix extended forecast starting on wrong day
- bugfix: Fix today's forecast starting later in the day
- bugfix: Fix crash when Nominatim fails
- bugfix: Fix forecast box being too long if forecast days option is higher than the provider gives
- bugfix: Fix geoclue failing causing errors
- bugfix: Fix sunset or sunrise in panel sometimes not showing the correct approaching one

* Wed Apr 18 2024 Fifty Dinar <srbaizoki4@tuta.io> - 134-1
- improvement: Choose between OpenWeatherMap.org or WeatherAPI.com
- bugfix: Fix location services fail sometimes crashing extension
- bugfix: Fix geolocation provider selector in preferences not working correctly
- bugfix: Checkboxes on locations in preferences finally show correctly

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
