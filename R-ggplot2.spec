#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ggplot2
Version  : 3.3.4
Release  : 93
URL      : https://cran.r-project.org/src/contrib/ggplot2_3.3.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ggplot2_3.3.4.tar.gz
Summary  : Create Elegant Data Visualisations Using the Grammar of Graphics
Group    : Development/Tools
License  : MIT
Requires: R-digest
Requires: R-glue
Requires: R-gtable
Requires: R-isoband
Requires: R-rlang
Requires: R-scales
Requires: R-sp
Requires: R-tibble
Requires: R-withr
BuildRequires : R-digest
BuildRequires : R-glue
BuildRequires : R-gtable
BuildRequires : R-isoband
BuildRequires : R-rlang
BuildRequires : R-scales
BuildRequires : R-sp
BuildRequires : R-tibble
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
based on "The Grammar of Graphics". You provide the data, tell 'ggplot2'
    how to map variables to aesthetics, what graphical primitives to use,
    and it takes care of the details.

%prep
%setup -q -c -n ggplot2
cd %{_builddir}/ggplot2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623854724

%install
export SOURCE_DATE_EPOCH=1623854724
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ggplot2 || :


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
/usr/lib64/R/library/ggplot2/doc/ggplot2-in-packages.R
/usr/lib64/R/library/ggplot2/doc/ggplot2-in-packages.Rmd
/usr/lib64/R/library/ggplot2/doc/ggplot2-in-packages.html
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
/usr/lib64/R/library/ggplot2/tests/figs/annotate/line-matches-points.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-cartesian/clip-on-by-default-only-inside-visible.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-cartesian/clip-turned-off-both-inside-and-outside-visible.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-cartesian/contract-range.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-cartesian/expand-range.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-map/coord-map-switched-scale-position.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-map/usa-mercator.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-polar/racetrack-plot-closed-and-has-center-hole.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-polar/racetrack-plot-closed-and-no-center-hole.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-polar/rays-circular-arcs-and-spiral-arcs.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-polar/rose-plot-with-has-equal-spacing.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-polar/secondary-axis-ticks-and-labels.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-polar/three-concentric-circles.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-sf/limits-specified-in-long-lat.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-sf/limits-specified-in-projected-coords.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-sf/no-panel-grid.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-sf/non-sf-geoms-using-long-lat.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-sf/non-sf-geoms-using-projected-coords.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-sf/sf-polygons.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-trans/basic-coord-trans-plot.svg
/usr/lib64/R/library/ggplot2/tests/figs/coord-trans/sec-axis-with-coord-trans.svg
/usr/lib64/R/library/ggplot2/tests/figs/creating-aesthetic-mappings/alpha-set-in-alpha.svg
/usr/lib64/R/library/ggplot2/tests/figs/creating-aesthetic-mappings/alpha-set-in-colour.svg
/usr/lib64/R/library/ggplot2/tests/figs/creating-aesthetic-mappings/stat-count-width-0-5.svg
/usr/lib64/R/library/ggplot2/tests/figs/creating-aesthetic-mappings/stat-count.svg
/usr/lib64/R/library/ggplot2/tests/figs/creating-aesthetic-mappings/stat-identity-width-0-5.svg
/usr/lib64/R/library/ggplot2/tests/figs/creating-aesthetic-mappings/stat-identity.svg
/usr/lib64/R/library/ggplot2/tests/figs/deps.txt
/usr/lib64/R/library/ggplot2/tests/figs/facet-labels/parsed-facet-labels.svg
/usr/lib64/R/library/ggplot2/tests/figs/facet-strips/switched-facet-strips.svg
/usr/lib64/R/library/ggplot2/tests/figs/facetting/left-justified-facet-labels-with-margins.svg
/usr/lib64/R/library/ggplot2/tests/figs/facetting/left-justified-rotated-facet-labels-with-margins.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-boxplot/outlier-colours.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/2-na-values-bin-along-y-stack-center.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/2-na-values-dot-density-binning-binwidth-4.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/basic-dotplot-with-dot-density-binning-binwidth-4.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/bin-along-y-stack-center.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/bin-along-y-stack-centerwhole-histodot.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/bin-along-y-stack-centerwhole.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/bin-y-continous-x-axis-grouping-by-x.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/bin-y-continous-x-axis-single-x-group.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/bin-y-dodged-coord-flip.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/bin-y-dodged.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/bin-y-dodging-3-stackgroups-histodot.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/bin-y-three-x-groups-bins-aligned-across-groups.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/bin-y-three-x-groups-bins-aligned-coord-flip.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/bin-y-three-x-groups-fill-and-dodge.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/bin-y-three-x-groups-stack-centerwhole.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/dots-stacked-closer-stackratio-5-fill-white.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/facets-3-groups-histodot-stackgroups.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/histodot-binning-equal-bin-spacing.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/larger-dots-dotsize-1-5-fill-white.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/multiple-groups-bins-aligned.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/multiple-groups-bins-not-aligned.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/stack-center-with-coord-flip.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/stack-center.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/stack-centerwhole-with-coord-flip.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/stack-centerwhole.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/stack-down-with-coord-flip.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/stack-down.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/stack-up-with-coord-flip.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/stack-up.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/stackgroups-with-3-groups-bin-y-histodot.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/stackgroups-with-3-groups-dot-density-with-aligned-bins.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/stackgroups-with-3-groups-histodot.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-dotplot/variable-linetype-and-size-work-when-specified-as-aesthetics.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-hline-vline-abline/cartesian-lines-intersect-mid-bars.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-hline-vline-abline/flipped-lines-intersect-mid-bars.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-hline-vline-abline/lines-curved-in-azequalarea.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-hline-vline-abline/polar-lines-intersect-mid-bars.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-hline-vline-abline/straight-lines-in-mercator.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-path/lines-colour-with-changed-data-order-should-have-same-appearance.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-path/lines-colour.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-path/lines-with-changed-data-order-should-have-same-appearance.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-path/lines.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-path/na-linetype.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-polygon/basic-polygon-plot.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-raster/1-x-3-just-0-0.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-raster/1-x-3-set-limits.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-raster/1-x-3.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-raster/3-x-1-just-0-0.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-raster/3-x-1-set-limits.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-raster/3-x-1.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-raster/3-x-2-just-0-0.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-raster/3-x-2-set-limits.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-raster/3-x-2.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-raster/irregular-categorical.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-sf/labels-for-north-carolina.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-sf/north-carolina-county-boundaries.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-sf/spatial-points.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-sf/texts-for-north-carolina.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-smooth/ribbon-turned-off-in-geom-smooth.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-smooth/ribbon-turned-on-in-geom-smooth.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/basic.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/continuous-x-axis-multiple-groups-center-should-be-at-2-0.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/continuous-x-axis-single-group-center-should-be-at-1-0.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/coord-flip.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/coord-polar.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/dodging-and-coord-flip.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/dodging.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/grouping-on-x-and-fill-dodge-width-0-5.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/grouping-on-x-and-fill.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/narrower-width-5.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/quantiles.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/scale-area-to-sample-size-c-is-smaller.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/with-smaller-bandwidth-and-points.svg
/usr/lib64/R/library/ggplot2/tests/figs/geom-violin/with-tails-and-points.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/align-facet-labels-facets-horizontal.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/align-facet-labels-facets-vertical.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/axis-guides-basic.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/axis-guides-check-overlap.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/axis-guides-negative-rotation.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/axis-guides-positive-rotation.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/axis-guides-text-dodged-into-rows-cols.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/axis-guides-vertical-negative-rotation.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/axis-guides-vertical-rotation.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/axis-guides-zero-breaks.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/axis-guides-zero-rotation.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/facet-grid-legend-on-bottom.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/facet-grid-legend-on-left.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/facet-grid-legend-on-right.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/facet-grid-legend-on-top.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/facet-wrap-legend-on-bottom.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/facet-wrap-legend-on-left.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/facet-wrap-legend-on-right.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/facet-wrap-legend-on-top.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/guide-axis-customization.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/guide-bins-can-remove-axis.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/guide-bins-can-show-arrows.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/guide-bins-can-show-limits.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/guide-bins-can-show-ticks.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/guide-bins-looks-as-it-should.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/guide-bins-work-horizontally.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/guide-coloursteps-can-have-bins-relative-to-binsize.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/guide-coloursteps-can-show-limits.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/guide-coloursteps-looks-as-it-should.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/guide-title-and-text-positioning-and-alignment-via-themes.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/guides-specified-in-guides.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/horizontal-gap-of-1cm-between-guide-and-guide-text.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/legend-inside-plot-bottom-left-of-legend-at-center.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/legend-inside-plot-bottom-left.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/legend-inside-plot-centered.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/legend-inside-plot-top-right.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/legend-on-bottom.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/legend-on-left.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/legend-on-right.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/legend-on-top.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/multi-line-guide-title-works.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/one-combined-colorbar-for-colour-and-fill-aesthetics.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/padding-in-legend-box.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/position-guide-titles.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/rotated-guide-titles-and-labels.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/thick-axis-lines.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/vertical-gap-of-1cm-between-guide-title-and-guide.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/white-to-red-gradient-colorbar-thick-black-tick-marks-green-frame.svg
/usr/lib64/R/library/ggplot2/tests/figs/guides/white-to-red-gradient-colorbar-white-tick-marks-no-frame.svg
/usr/lib64/R/library/ggplot2/tests/figs/labels/defaults.svg
/usr/lib64/R/library/ggplot2/tests/figs/labels/manual.svg
/usr/lib64/R/library/ggplot2/tests/figs/labels/other-position.svg
/usr/lib64/R/library/ggplot2/tests/figs/legend-key-glyphs/rectangle-and-dotplot-key-glyphs.svg
/usr/lib64/R/library/ggplot2/tests/figs/legend-key-glyphs/time-series-and-polygon-key-glyphs.svg
/usr/lib64/R/library/ggplot2/tests/figs/position-stack/area-stacking.svg
/usr/lib64/R/library/ggplot2/tests/figs/scale-date/dates-along-x-default-breaks.svg
/usr/lib64/R/library/ggplot2/tests/figs/scale-date/dates-along-y-default-breaks.svg
/usr/lib64/R/library/ggplot2/tests/figs/scale-date/scale-x-date-breaks-3-weeks.svg
/usr/lib64/R/library/ggplot2/tests/figs/scale-date/scale-x-date-breaks-date-breaks-2-weeks.svg
/usr/lib64/R/library/ggplot2/tests/figs/scale-date/scale-x-date-labels-date-format-m-d.svg
/usr/lib64/R/library/ggplot2/tests/figs/scale-date/scale-x-date-labels-date-format-w-week.svg
/usr/lib64/R/library/ggplot2/tests/figs/scale-date/scale-y-date-breaks-3-weeks.svg
/usr/lib64/R/library/ggplot2/tests/figs/scale-date/scale-y-date-breaks-date-breaks-2-weeks.svg
/usr/lib64/R/library/ggplot2/tests/figs/scales-breaks-and-labels/character.svg
/usr/lib64/R/library/ggplot2/tests/figs/scales-breaks-and-labels/date.svg
/usr/lib64/R/library/ggplot2/tests/figs/scales-breaks-and-labels/functional-limits.svg
/usr/lib64/R/library/ggplot2/tests/figs/scales-breaks-and-labels/no-alpha-breaks-no-legend.svg
/usr/lib64/R/library/ggplot2/tests/figs/scales-breaks-and-labels/no-colour-breaks-no-legend.svg
/usr/lib64/R/library/ggplot2/tests/figs/scales-breaks-and-labels/no-fill-breaks-no-legend.svg
/usr/lib64/R/library/ggplot2/tests/figs/scales-breaks-and-labels/no-size-breaks-no-legend.svg
/usr/lib64/R/library/ggplot2/tests/figs/scales-breaks-and-labels/no-x-breaks.svg
/usr/lib64/R/library/ggplot2/tests/figs/scales-breaks-and-labels/no-y-breaks.svg
/usr/lib64/R/library/ggplot2/tests/figs/scales-breaks-and-labels/numeric-exp.svg
/usr/lib64/R/library/ggplot2/tests/figs/scales-breaks-and-labels/numeric-log.svg
/usr/lib64/R/library/ggplot2/tests/figs/scales-breaks-and-labels/numeric-polar.svg
/usr/lib64/R/library/ggplot2/tests/figs/scales-breaks-and-labels/numeric.svg
/usr/lib64/R/library/ggplot2/tests/figs/sec-axis/sec-axis-custom-transform.svg
/usr/lib64/R/library/ggplot2/tests/figs/sec-axis/sec-axis-datetime-scale.svg
/usr/lib64/R/library/ggplot2/tests/figs/sec-axis/sec-axis-independent-transformations.svg
/usr/lib64/R/library/ggplot2/tests/figs/sec-axis/sec-axis-monotonicity-test.svg
/usr/lib64/R/library/ggplot2/tests/figs/sec-axis/sec-axis-sec-power-transform.svg
/usr/lib64/R/library/ggplot2/tests/figs/sec-axis/sec-axis-skewed-transform.svg
/usr/lib64/R/library/ggplot2/tests/figs/sec-axis/sec-axis-with-division.svg
/usr/lib64/R/library/ggplot2/tests/figs/stat-sum/summary-with-color-and-lines.svg
/usr/lib64/R/library/ggplot2/tests/figs/stat-sum/summary-with-crossbars-manual-grouping.svg
/usr/lib64/R/library/ggplot2/tests/figs/stat-sum/summary-with-crossbars-no-grouping.svg
/usr/lib64/R/library/ggplot2/tests/figs/test-coord-flip-r/turning-off-secondary-title-with-coord-flip.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/axes-styling.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/caption-aligned-to-entire-plot.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/custom-strip-elements-can-render.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/height-is-3-times-width-2-column-facets.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/height-is-3-times-width-2-row-facets.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/height-is-3-times-width-2-wrap-facets.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/height-is-3-times-width-2x2-facets.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/height-is-3-times-width.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/rotated-x-axis-tick-labels.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/strip-styling.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-bw-large.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-bw.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-classic-large.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-classic.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-dark-large.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-dark.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-gray-large.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-gray.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-light-large.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-light.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-linedraw-large.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-linedraw.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-minimal-large.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-minimal.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-void-large.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/theme-void.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/ticks-length.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/title-aligned-to-entire-plot.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/titles-aligned-to-entire-plot.svg
/usr/lib64/R/library/ggplot2/tests/figs/themes/width-is-3-times-height.svg
/usr/lib64/R/library/ggplot2/tests/testthat.R
/usr/lib64/R/library/ggplot2/tests/testthat/Rplot001.png
/usr/lib64/R/library/ggplot2/tests/testthat/Rplots.pdf
/usr/lib64/R/library/ggplot2/tests/testthat/helper-facet.r
/usr/lib64/R/library/ggplot2/tests/testthat/helper-plot-data.r
/usr/lib64/R/library/ggplot2/tests/testthat/helper-vdiffr.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-add.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-aes-calculated.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-aes-grouping.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-aes-setting.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-aes.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-annotate.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-build.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-coord-.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-coord-cartesian.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-coord-flip.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-coord-map.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-coord-polar.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-coord-train.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-coord-transform.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-coord_sf.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-data.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-draw-key.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-empty-data.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-error.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-facet-.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-facet-labels.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-facet-layout.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-facet-map.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-facet-strips.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-fortify.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-function-args.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-bar.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-boxplot.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-col.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-dotplot.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-freqpoly.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-hex.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-hline-vline-abline.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-path.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-point.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-polygon.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-quantile.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-raster.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-ribbon.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-rug.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-rule.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-sf.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-smooth.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-text.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-tile.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-geom-violin.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-ggproto.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-ggsave.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-grid-utils.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-guides.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-labellers.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-labels.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-layer.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-munch.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-performance.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-plot-summary-api.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-position-dodge2.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-position-nudge.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-position-stack.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-position_dodge.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-prohibited-functions.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-qplot.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-range.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-rbind-dfs.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-sanitise-dim.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-scale-brewer.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-scale-colour-continuous.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-scale-date.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-scale-discrete.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-scale-expansion.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-scale-gradient.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-scale-manual.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-scale-type.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-scale_date.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-scales-breaks-labels.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-scales.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-sec-axis.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-bin.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-bin2d.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-boxplot.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-contour.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-density.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-density2d.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-ecdf.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-ellipsis.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-function.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-hex.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-sf-coordinates.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-sum.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stat-summary.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-stats.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-theme.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-utilities.r
/usr/lib64/R/library/ggplot2/tests/testthat/test-viridis.R
/usr/lib64/R/library/ggplot2/tests/testthat/test-zzz.R
