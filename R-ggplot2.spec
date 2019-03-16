#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ggplot2
Version  : 3.1.0
Release  : 64
URL      : https://cran.r-project.org/src/contrib/ggplot2_3.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ggplot2_3.1.0.tar.gz
Summary  : Create Elegant Data Visualisations Using the Grammar of Graphics
Group    : Development/Tools
License  : GPL-2.0
Requires: R-gtable
Requires: R-labeling
Requires: R-lazyeval
Requires: R-maps
Requires: R-multcomp
Requires: R-munsell
Requires: R-plyr
Requires: R-quantreg
Requires: R-reshape2
Requires: R-scales
Requires: R-sp
Requires: R-tibble
Requires: R-viridisLite
Requires: R-withr
BuildRequires : R-evaluate
BuildRequires : R-formatR
BuildRequires : R-gtable
BuildRequires : R-labeling
BuildRequires : R-lazyeval
BuildRequires : R-maps
BuildRequires : R-markdown
BuildRequires : R-multcomp
BuildRequires : R-munsell
BuildRequires : R-plyr
BuildRequires : R-quantreg
BuildRequires : R-reshape2
BuildRequires : R-scales
BuildRequires : R-sp
BuildRequires : R-tibble
BuildRequires : R-viridisLite
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
based on "The Grammar of Graphics". You provide the data, tell 'ggplot2'
    how to map variables to aesthetics, what graphical primitives to use,
    and it takes care of the details.

%prep
%setup -q -c -n ggplot2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540476337

%install
export SOURCE_DATE_EPOCH=1540476337
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggplot2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggplot2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggplot2
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library ggplot2|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ggplot2/CITATION
/usr/lib64/R/library/ggplot2/DESCRIPTION
/usr/lib64/R/library/ggplot2/INDEX
/usr/lib64/R/library/ggplot2/LICENSE
/usr/lib64/R/library/ggplot2/Meta/Rd.rds
/usr/lib64/R/library/ggplot2/Meta/data.rds
/usr/lib64/R/library/ggplot2/Meta/features.rds
/usr/lib64/R/library/ggplot2/Meta/hsearch.rds
/usr/lib64/R/library/ggplot2/Meta/links.rds
/usr/lib64/R/library/ggplot2/Meta/nsInfo.rds
/usr/lib64/R/library/ggplot2/Meta/package.rds
/usr/lib64/R/library/ggplot2/Meta/vignette.rds
/usr/lib64/R/library/ggplot2/NAMESPACE
/usr/lib64/R/library/ggplot2/NEWS.md
/usr/lib64/R/library/ggplot2/R/ggplot2
/usr/lib64/R/library/ggplot2/R/ggplot2.rdb
/usr/lib64/R/library/ggplot2/R/ggplot2.rdx
/usr/lib64/R/library/ggplot2/data/Rdata.rdb
/usr/lib64/R/library/ggplot2/data/Rdata.rds
/usr/lib64/R/library/ggplot2/data/Rdata.rdx
/usr/lib64/R/library/ggplot2/doc/extending-ggplot2.R
/usr/lib64/R/library/ggplot2/doc/extending-ggplot2.Rmd
/usr/lib64/R/library/ggplot2/doc/extending-ggplot2.html
/usr/lib64/R/library/ggplot2/doc/ggplot2-specs.R
/usr/lib64/R/library/ggplot2/doc/ggplot2-specs.Rmd
/usr/lib64/R/library/ggplot2/doc/ggplot2-specs.html
/usr/lib64/R/library/ggplot2/doc/index.html
/usr/lib64/R/library/ggplot2/help/AnIndex
/usr/lib64/R/library/ggplot2/help/aliases.rds
/usr/lib64/R/library/ggplot2/help/figures/README-example-1.png
/usr/lib64/R/library/ggplot2/help/figures/logo.png
/usr/lib64/R/library/ggplot2/help/ggplot2.rdb
/usr/lib64/R/library/ggplot2/help/ggplot2.rdx
/usr/lib64/R/library/ggplot2/help/paths.rds
/usr/lib64/R/library/ggplot2/html/00Index.html
/usr/lib64/R/library/ggplot2/html/R.css
