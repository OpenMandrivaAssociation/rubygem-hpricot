Summary:	Ruby HTML parser
Name:		rubygem-hpricot
Version:	0.8.6
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://rubygems.org/gems/hpricot
Source0:	https://rubygems.org/downloads/hpricot-%{version}.gem
BuildRequires:  ruby-devel

%description
Ruby HTML parser

%prep
%autosetup -p1 -n %{gem_name}-%{version}%{?prerelease}

%build
%gem_build

%install
%gem_install

%files
%{gem_files}

# This should be autogenerated, but for some reason the
# debuginfo generator fails on the Makefiles in hpricot
%files debuginfo
%{_prefix}/lib/debug%{_libdir}/ruby/gems/*/gems/hpricot-%{version}
%{_prefix}/lib/debug/.dwz/%{name}-*
%{_prefix}/lib/debug%{_libdir}/ruby/gems/*/extensions/*/*/hpricot-%{version}
