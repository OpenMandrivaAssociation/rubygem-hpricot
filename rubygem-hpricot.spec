%define oname hpricot

Summary:    A swift, liberal HTML parser with a fantastic library
Name:       rubygem-%{oname}
Version:    0.8.3
Release:    %mkrel 1
Group:      Development/Ruby
License:    MIT
URL:        http://code.whytheluckystiff.net/hpricot/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildRequires: ruby-devel
Obsoletes:  ruby-hpricot < %{version}
Provides:   rubygem(%{oname}) = %{version}

%description
Hpricot is a very flexible HTML parser, based on Tanaka Akira's
HTree and John Resig's JQuery, but with the scanner recoded in C
(using Ragel for scanning.)

%prep

%build
mkdir -p .%{ruby_gemdir}
gem install -V --local --install-dir .%{ruby_gemdir} \
               --force --rdoc %{SOURCE0}

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
cp -a .%{ruby_gemdir}/* %{buildroot}%{ruby_gemdir}
rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/

# install so files in sitearchdir
mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/*.so %{buildroot}%{ruby_sitearchdir}

for f in `find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/ -name \*.rb | sort` ; do
    sed -i -e '/^#!/d' $f
done
%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/extras/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.md
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGELOG
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/COPYING
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/*.so
