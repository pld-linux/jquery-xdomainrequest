%define		plugin	xdomainrequest
Summary:	Cross-Domain AJAX for IE8
Name:		jquery-%{plugin}
Version:	1.0.1
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	http://cdnjs.cloudflare.com/ajax/libs/jquery-ajaxtransport-xdomainrequest/%{version}/jquery.xdomainrequest.min.js
# Source0-md5:	a32f9c1370fd2461ab6d0847e18a472b
URL:		https://github.com/MoonScript/jQuery-ajaxTransport-XDomainRequest
Requires:	jquery >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Implements automatic Cross Origin Resource Sharing support using the
XDomainRequest object for IE8 and IE9 when using the $.ajax function
in jQuery 1.5+.

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -qcT
cp -p %{SOURCE0} jquery.%{plugin}.min.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p jquery.%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
