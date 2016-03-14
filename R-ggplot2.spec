#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ggplot2
Version  : 2.1.0
Release  : 20
URL      : http://cran.r-project.org/src/contrib/ggplot2_2.1.0.tar.gz
Source0  : http://cran.r-project.org/src/contrib/ggplot2_2.1.0.tar.gz
Summary  : An Implementation of the Grammar of Graphics
Group    : Development/Tools
License  : GPL-2.0
Requires: R-scales
Requires: R-digest
Requires: R-reshape2
Requires: R-gtable
BuildRequires : R-digest
BuildRequires : R-gtable
BuildRequires : R-reshape2
BuildRequires : R-scales
BuildRequires : clr-R-helpers

%description
# ggplot2
[![Build Status](https://travis-ci.org/hadley/ggplot2.png?branch=master)](https://travis-ci.org/hadley/ggplot2)
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/ggplot2)](http://cran.r-project.org/package=ggplot2)

%prep
%setup -q -c -n ggplot2

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library ggplot2
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library ggplot2 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ggplot2/CITATION
/usr/lib64/R/library/ggplot2/DESCRIPTION
/usr/lib64/R/library/ggplot2/INDEX
/usr/lib64/R/library/ggplot2/Meta/Rd.rds
/usr/lib64/R/library/ggplot2/Meta/data.rds
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
/usr/lib64/R/library/ggplot2/help/ggplot2.rdb
/usr/lib64/R/library/ggplot2/help/ggplot2.rdx
/usr/lib64/R/library/ggplot2/help/paths.rds
/usr/lib64/R/library/ggplot2/html/00Index.html
/usr/lib64/R/library/ggplot2/html/R.css
/usr/lib64/R/library/ggplot2/staticdocs/README.md
/usr/lib64/R/library/ggplot2/staticdocs/footer.html
/usr/lib64/R/library/ggplot2/staticdocs/head.html
/usr/lib64/R/library/ggplot2/staticdocs/icons.R
/usr/lib64/R/library/ggplot2/staticdocs/index.r
/usr/lib64/R/library/ggplot2/tests/testthat.R
/usr/lib64/R/library/ggplot2/tests/testthat/Rplots.pdf
/usr/lib64/R/library/ggplot2/tests/testthat/helper-plot-data.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-aes-grouping.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-aes-setting.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-aes.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-annotate.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-boxplot.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-build.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-coord-polar.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-coord-train.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-data.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-dotplot.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-empty-data.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-facet-.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-facet-labels.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-facet-layout.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-facet-locate.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-facet-strips.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-fortify.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-function-args.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-boxplot.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-freqpoly.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-ribbon.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-rule.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-text.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-tile.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-violin.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-ggsave.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-grid-utils.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-guides.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-labels.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-layer.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-munch.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-qplot.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-range.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-sanitise-dim.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-scale-discrete.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-scale-manual.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-scales-breaks-labels.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-scales.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-bin.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-bin2d.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-density.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-density2d.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-sum.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stats-function.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-stats.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-theme.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-utilities.r
