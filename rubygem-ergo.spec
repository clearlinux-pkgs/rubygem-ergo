#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-ergo
Version  : 0.3.0
Release  : 5
URL      : https://rubygems.org/downloads/ergo-0.3.0.gem
Source0  : https://rubygems.org/downloads/ergo-0.3.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: rubygem-ergo-bin
BuildRequires : ruby
BuildRequires : rubygem-ae
BuildRequires : rubygem-detroit
BuildRequires : rubygem-mast
BuildRequires : rubygem-notify
BuildRequires : rubygem-qed
BuildRequires : rubygem-rdoc

%description
# Ergo ç±
[Homepage](http://rubyworks.github.com/ergo) /
[Report Issue](http://github.com/rubyworks/ergo/issues) /
[Source Code](http://github.com/rubyworks/ergo) /
[IRC Channel](http://chat.us.freenode.net/rubyworks)

%package bin
Summary: bin components for the rubygem-ergo package.
Group: Binaries

%description bin
bin components for the rubygem-ergo package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n ergo-0.3.0
gem spec %{SOURCE0} -l --ruby > rubygem-ergo.gemspec

%build
gem build rubygem-ergo.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
ergo-0.3.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/ergo-0.3.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/.index
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/HISTORY.md
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/bin/ergo
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/demo/03_runner/01_applying_rules.md
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/demo/applique/ae.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/demo/applique/ergo.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/demo/overview.md
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo.yml
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/book.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/cli.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/core_ext.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/core_ext/boolean.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/core_ext/cli.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/core_ext/true_class.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/digest.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/ignore.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/match.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/rule.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/runner.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/shellutils.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/state.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/lib/ergo/system.rb
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/man/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/man/ergo.1
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/man/ergo.1.html
/usr/lib64/ruby/gems/2.3.0/gems/ergo-0.3.0/man/ergo.1.ronn
/usr/lib64/ruby/gems/2.3.0/specifications/ergo-0.3.0.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/ergo
