%global extension   openweatherrefined
%global uuid        openweather-extension@penguin-teal.github.io
%global gettext     gnome-shell-extension-%{extension}
%global version     131
%global commit      a83c0d427534b45ab53ca10957f645cbcf4a799d

Name:           gnome-shell-extension-%{extension}
Version:        %{version}
Release:        2%{?dist}
Summary:        Display weather information for any location on Earth in the GNOME Shell
License:        GPLv3
URL:            https://github.com/penguin-teal/gnome-openweather
Source0:        %{url}/archive/%{commit}/gnome-openweather-%{commit}.tar.gz
BuildArch:      noarch
BuildRequires:  gettext
Requires:       gnome-shell == 45

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
* Fri Mar 29 2024 Fifty Dinar <srbaizoki4@tuta.io> - 131-2
- packaging: Make sure that this version of extension doesn't install on Gnome 46/Fedora 40

* Sun Mar 10 2024 Fifty Dinar <srbaizoki4@tuta.io> - 131-1
- improvement: Notice on how to search up new locations in "Edit Location" menu
- improvement: No more space between humidity value and "%"
- bugfix: Fix extension not initializing sometimes
- bugfix: Fix migrations only happening on first extension download
