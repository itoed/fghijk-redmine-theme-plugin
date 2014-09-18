Name: %{_name}
Version: %{_version}
Release: %{_release}
Summary: FGHIJK Redmine Theme Plugin
License: None
BuildArch: %{_arch}
AutoReqProv: No
Source0: plugin
Source1: theme

%description
The FGHIJK Redmine Theme Plugin provides stylesheets and a custom layout
for the FGHIJK Redmine installation.

%define appdir /home/redmine/redmine
%define plugindir %{appdir}/plugins/fghijk_redmine_theme_plugin
%define themedir %{appdir}/public/themes/fghijk

%install
rm -rf %{buildroot}
install -dm 755 %{buildroot}%{appdir}/plugins
cp -r %{SOURCE0} %{buildroot}%{plugindir}
install -dm 755 %{buildroot}%{appdir}/public/themes
cp -r %{SOURCE1} %{buildroot}%{themedir}

%files
%defattr(-,redmine,redmine,-)
%{plugindir}
%{themedir}

%changelog
* Thu Sep 18 2014 Eduardo Ito <ed@fghijk.net> - 0.1-1
- Initial release
