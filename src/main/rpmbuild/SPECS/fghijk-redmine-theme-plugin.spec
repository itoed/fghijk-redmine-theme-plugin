Name:           %{_name}
Version:        %{_version}
Release:        %{_release}
Summary:        FGHIJK Redmine Theme Plugin
License:        None
BuildArch:      %{_arch}
AutoReqProv:    No
Source0:        fghijk-redmine-theme-plugin

%description
The FGHIJK Redmine Theme Plugin provides stylesheets and a custom layout 
for the FGHIJK Redmine installation

%define plugindir /home/redmine/redmine/plugins

%install
rm -rf %{buildroot}
install -dm 755 %{buildroot}%{plugindir}
cp -r %{SOURCE0} %{buildroot}%{plugindir}

%files
%defattr(-,root,root,-)
%{plugindir}

%changelog
* Thu Sep 18 2014 Eduardo Ito <ed@fghijk.net> - 0.1-1
- Initial release
