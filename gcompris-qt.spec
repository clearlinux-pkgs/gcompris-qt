#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x63D7264C05687D7E (animtim@gmail.com)
#
Name     : gcompris-qt
Version  : 0.95
Release  : 4
URL      : https://gcompris.net/download/qt/src/gcompris-qt-0.95.tar.xz
Source0  : https://gcompris.net/download/qt/src/gcompris-qt-0.95.tar.xz
Source99 : https://gcompris.net/download/qt/src/gcompris-qt-0.95.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LAL-1.2 MPL-2.0
Requires: gcompris-qt-bin = %{version}-%{release}
Requires: gcompris-qt-data = %{version}-%{release}
Requires: gcompris-qt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : git
BuildRequires : mesa-dev
BuildRequires : p7zip
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Sensors)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5UiTools)
BuildRequires : pkgconfig(Qt5XmlPatterns)
BuildRequires : qml-box2d
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qttools-extras

%description
GCompris / I Got IT
GCompris is a GNU package
https://gcompris.net
GCompris is a high quality educational software suite, including a large
number of activities for children aged 2 to 10. Some of the activities
are game orientated, but nonetheless still educational.

%package bin
Summary: bin components for the gcompris-qt package.
Group: Binaries
Requires: gcompris-qt-data = %{version}-%{release}
Requires: gcompris-qt-license = %{version}-%{release}

%description bin
bin components for the gcompris-qt package.


%package data
Summary: data components for the gcompris-qt package.
Group: Data

%description data
data components for the gcompris-qt package.


%package doc
Summary: doc components for the gcompris-qt package.
Group: Documentation

%description doc
doc components for the gcompris-qt package.


%package license
Summary: license components for the gcompris-qt package.
Group: Default

%description license
license components for the gcompris-qt package.


%prep
%setup -q -n gcompris-qt-0.95

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545509066
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1545509066
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gcompris-qt
cp COPYING %{buildroot}/usr/share/package-licenses/gcompris-qt/COPYING
cp src/activities/checkers/LICENSE %{buildroot}/usr/share/package-licenses/gcompris-qt/src_activities_checkers_LICENSE
cp src/core/COPYING %{buildroot}/usr/share/package-licenses/gcompris-qt/src_core_COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gcompris-qt

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.gcompris.desktop
/usr/share/gcompris-qt/rcc/activities.rcc
/usr/share/gcompris-qt/rcc/advanced_colors.rcc
/usr/share/gcompris-qt/rcc/algebra_by.rcc
/usr/share/gcompris-qt/rcc/algebra_div.rcc
/usr/share/gcompris-qt/rcc/algebra_minus.rcc
/usr/share/gcompris-qt/rcc/algebra_plus.rcc
/usr/share/gcompris-qt/rcc/algorithm.rcc
/usr/share/gcompris-qt/rcc/align4-2players.rcc
/usr/share/gcompris-qt/rcc/align4.rcc
/usr/share/gcompris-qt/rcc/alphabet-sequence.rcc
/usr/share/gcompris-qt/rcc/baby_wordprocessor.rcc
/usr/share/gcompris-qt/rcc/babymatch.rcc
/usr/share/gcompris-qt/rcc/babyshapes.rcc
/usr/share/gcompris-qt/rcc/balancebox.rcc
/usr/share/gcompris-qt/rcc/ballcatch.rcc
/usr/share/gcompris-qt/rcc/bargame.rcc
/usr/share/gcompris-qt/rcc/bargame_2players.rcc
/usr/share/gcompris-qt/rcc/binary_bulb.rcc
/usr/share/gcompris-qt/rcc/braille_alphabets.rcc
/usr/share/gcompris-qt/rcc/braille_fun.rcc
/usr/share/gcompris-qt/rcc/calendar.rcc
/usr/share/gcompris-qt/rcc/canal_lock.rcc
/usr/share/gcompris-qt/rcc/categorization.rcc
/usr/share/gcompris-qt/rcc/checkers.rcc
/usr/share/gcompris-qt/rcc/checkers_2players.rcc
/usr/share/gcompris-qt/rcc/chess.rcc
/usr/share/gcompris-qt/rcc/chess_2players.rcc
/usr/share/gcompris-qt/rcc/chess_partyend.rcc
/usr/share/gcompris-qt/rcc/chronos.rcc
/usr/share/gcompris-qt/rcc/click_on_letter.rcc
/usr/share/gcompris-qt/rcc/click_on_letter_up.rcc
/usr/share/gcompris-qt/rcc/clickanddraw.rcc
/usr/share/gcompris-qt/rcc/clickgame.rcc
/usr/share/gcompris-qt/rcc/clockgame.rcc
/usr/share/gcompris-qt/rcc/color_mix.rcc
/usr/share/gcompris-qt/rcc/color_mix_light.rcc
/usr/share/gcompris-qt/rcc/colors.rcc
/usr/share/gcompris-qt/rcc/core.rcc
/usr/share/gcompris-qt/rcc/crane.rcc
/usr/share/gcompris-qt/rcc/details.rcc
/usr/share/gcompris-qt/rcc/digital_electricity.rcc
/usr/share/gcompris-qt/rcc/drawletters.rcc
/usr/share/gcompris-qt/rcc/drawnumbers.rcc
/usr/share/gcompris-qt/rcc/enumerate.rcc
/usr/share/gcompris-qt/rcc/erase.rcc
/usr/share/gcompris-qt/rcc/erase_2clic.rcc
/usr/share/gcompris-qt/rcc/erase_clic.rcc
/usr/share/gcompris-qt/rcc/explore_farm_animals.rcc
/usr/share/gcompris-qt/rcc/explore_monuments.rcc
/usr/share/gcompris-qt/rcc/explore_world_animals.rcc
/usr/share/gcompris-qt/rcc/explore_world_music.rcc
/usr/share/gcompris-qt/rcc/family.rcc
/usr/share/gcompris-qt/rcc/family_find_relative.rcc
/usr/share/gcompris-qt/rcc/fifteen.rcc
/usr/share/gcompris-qt/rcc/find_the_day.rcc
/usr/share/gcompris-qt/rcc/followline.rcc
/usr/share/gcompris-qt/rcc/football.rcc
/usr/share/gcompris-qt/rcc/geo-country.rcc
/usr/share/gcompris-qt/rcc/geography.rcc
/usr/share/gcompris-qt/rcc/gletters.rcc
/usr/share/gcompris-qt/rcc/gnumch-equality.rcc
/usr/share/gcompris-qt/rcc/gnumch-factors.rcc
/usr/share/gcompris-qt/rcc/gnumch-inequality.rcc
/usr/share/gcompris-qt/rcc/gnumch-multiples.rcc
/usr/share/gcompris-qt/rcc/gnumch-primes.rcc
/usr/share/gcompris-qt/rcc/graph-coloring.rcc
/usr/share/gcompris-qt/rcc/guesscount.rcc
/usr/share/gcompris-qt/rcc/guessnumber.rcc
/usr/share/gcompris-qt/rcc/hangman.rcc
/usr/share/gcompris-qt/rcc/hanoi.rcc
/usr/share/gcompris-qt/rcc/hanoi_real.rcc
/usr/share/gcompris-qt/rcc/hexagon.rcc
/usr/share/gcompris-qt/rcc/imagename.rcc
/usr/share/gcompris-qt/rcc/instruments.rcc
/usr/share/gcompris-qt/rcc/intro_gravity.rcc
/usr/share/gcompris-qt/rcc/land_safe.rcc
/usr/share/gcompris-qt/rcc/lang.rcc
/usr/share/gcompris-qt/rcc/leftright.rcc
/usr/share/gcompris-qt/rcc/letter-in-word.rcc
/usr/share/gcompris-qt/rcc/lightsoff.rcc
/usr/share/gcompris-qt/rcc/louis-braille.rcc
/usr/share/gcompris-qt/rcc/magic-hat-minus.rcc
/usr/share/gcompris-qt/rcc/magic-hat-plus.rcc
/usr/share/gcompris-qt/rcc/maze.rcc
/usr/share/gcompris-qt/rcc/mazeinvisible.rcc
/usr/share/gcompris-qt/rcc/mazerelative.rcc
/usr/share/gcompris-qt/rcc/melody.rcc
/usr/share/gcompris-qt/rcc/memory-case-association-tux.rcc
/usr/share/gcompris-qt/rcc/memory-case-association.rcc
/usr/share/gcompris-qt/rcc/memory-enumerate.rcc
/usr/share/gcompris-qt/rcc/memory-math-add-minus-mult-div-tux.rcc
/usr/share/gcompris-qt/rcc/memory-math-add-minus-mult-div.rcc
/usr/share/gcompris-qt/rcc/memory-math-add-minus-tux.rcc
/usr/share/gcompris-qt/rcc/memory-math-add-minus.rcc
/usr/share/gcompris-qt/rcc/memory-math-add-tux.rcc
/usr/share/gcompris-qt/rcc/memory-math-add.rcc
/usr/share/gcompris-qt/rcc/memory-math-div-tux.rcc
/usr/share/gcompris-qt/rcc/memory-math-div.rcc
/usr/share/gcompris-qt/rcc/memory-math-minus-tux.rcc
/usr/share/gcompris-qt/rcc/memory-math-minus.rcc
/usr/share/gcompris-qt/rcc/memory-math-mult-div-tux.rcc
/usr/share/gcompris-qt/rcc/memory-math-mult-div.rcc
/usr/share/gcompris-qt/rcc/memory-math-mult-tux.rcc
/usr/share/gcompris-qt/rcc/memory-math-mult.rcc
/usr/share/gcompris-qt/rcc/memory-sound-tux.rcc
/usr/share/gcompris-qt/rcc/memory-sound.rcc
/usr/share/gcompris-qt/rcc/memory-tux.rcc
/usr/share/gcompris-qt/rcc/memory-wordnumber.rcc
/usr/share/gcompris-qt/rcc/memory.rcc
/usr/share/gcompris-qt/rcc/menu.rcc
/usr/share/gcompris-qt/rcc/mining.rcc
/usr/share/gcompris-qt/rcc/missing-letter.rcc
/usr/share/gcompris-qt/rcc/money.rcc
/usr/share/gcompris-qt/rcc/money_back.rcc
/usr/share/gcompris-qt/rcc/money_back_cents.rcc
/usr/share/gcompris-qt/rcc/money_cents.rcc
/usr/share/gcompris-qt/rcc/mosaic.rcc
/usr/share/gcompris-qt/rcc/nine_men_morris.rcc
/usr/share/gcompris-qt/rcc/nine_men_morris_2players.rcc
/usr/share/gcompris-qt/rcc/note_names.rcc
/usr/share/gcompris-qt/rcc/number_sequence.rcc
/usr/share/gcompris-qt/rcc/numbers-odd-even.rcc
/usr/share/gcompris-qt/rcc/paintings.rcc
/usr/share/gcompris-qt/rcc/penalty.rcc
/usr/share/gcompris-qt/rcc/photo_hunter.rcc
/usr/share/gcompris-qt/rcc/piano_composition.rcc
/usr/share/gcompris-qt/rcc/planegame.rcc
/usr/share/gcompris-qt/rcc/play_piano.rcc
/usr/share/gcompris-qt/rcc/play_rhythm.rcc
/usr/share/gcompris-qt/rcc/railroad.rcc
/usr/share/gcompris-qt/rcc/readingh.rcc
/usr/share/gcompris-qt/rcc/readingv.rcc
/usr/share/gcompris-qt/rcc/redraw.rcc
/usr/share/gcompris-qt/rcc/redraw_symmetrical.rcc
/usr/share/gcompris-qt/rcc/renewable_energy.rcc
/usr/share/gcompris-qt/rcc/reversecount.rcc
/usr/share/gcompris-qt/rcc/roman_numerals.rcc
/usr/share/gcompris-qt/rcc/scalesboard.rcc
/usr/share/gcompris-qt/rcc/scalesboard_weight.rcc
/usr/share/gcompris-qt/rcc/scalesboard_weight_avoirdupois.rcc
/usr/share/gcompris-qt/rcc/share.rcc
/usr/share/gcompris-qt/rcc/simplepaint.rcc
/usr/share/gcompris-qt/rcc/smallnumbers.rcc
/usr/share/gcompris-qt/rcc/smallnumbers2.rcc
/usr/share/gcompris-qt/rcc/solar_system.rcc
/usr/share/gcompris-qt/rcc/submarine.rcc
/usr/share/gcompris-qt/rcc/sudoku.rcc
/usr/share/gcompris-qt/rcc/superbrain.rcc
/usr/share/gcompris-qt/rcc/tangram.rcc
/usr/share/gcompris-qt/rcc/target.rcc
/usr/share/gcompris-qt/rcc/tic_tac_toe.rcc
/usr/share/gcompris-qt/rcc/tic_tac_toe_2players.rcc
/usr/share/gcompris-qt/rcc/traffic.rcc
/usr/share/gcompris-qt/rcc/watercycle.rcc
/usr/share/gcompris-qt/rcc/wordsgame.rcc
/usr/share/gcompris-qt/translations/gcompris_ar.qm
/usr/share/gcompris-qt/translations/gcompris_ast.qm
/usr/share/gcompris-qt/translations/gcompris_be.qm
/usr/share/gcompris-qt/translations/gcompris_bg.qm
/usr/share/gcompris-qt/translations/gcompris_br.qm
/usr/share/gcompris-qt/translations/gcompris_bs.qm
/usr/share/gcompris-qt/translations/gcompris_ca.qm
/usr/share/gcompris-qt/translations/gcompris_ca@valencia.qm
/usr/share/gcompris-qt/translations/gcompris_cs.qm
/usr/share/gcompris-qt/translations/gcompris_da.qm
/usr/share/gcompris-qt/translations/gcompris_de.qm
/usr/share/gcompris-qt/translations/gcompris_el.qm
/usr/share/gcompris-qt/translations/gcompris_en.qm
/usr/share/gcompris-qt/translations/gcompris_en_GB.qm
/usr/share/gcompris-qt/translations/gcompris_es.qm
/usr/share/gcompris-qt/translations/gcompris_et.qm
/usr/share/gcompris-qt/translations/gcompris_eu.qm
/usr/share/gcompris-qt/translations/gcompris_fi.qm
/usr/share/gcompris-qt/translations/gcompris_fr.qm
/usr/share/gcompris-qt/translations/gcompris_ga.qm
/usr/share/gcompris-qt/translations/gcompris_gd.qm
/usr/share/gcompris-qt/translations/gcompris_gl.qm
/usr/share/gcompris-qt/translations/gcompris_hi.qm
/usr/share/gcompris-qt/translations/gcompris_hu.qm
/usr/share/gcompris-qt/translations/gcompris_id.qm
/usr/share/gcompris-qt/translations/gcompris_it.qm
/usr/share/gcompris-qt/translations/gcompris_ja.qm
/usr/share/gcompris-qt/translations/gcompris_ko.qm
/usr/share/gcompris-qt/translations/gcompris_lv.qm
/usr/share/gcompris-qt/translations/gcompris_ml.qm
/usr/share/gcompris-qt/translations/gcompris_nb.qm
/usr/share/gcompris-qt/translations/gcompris_nl.qm
/usr/share/gcompris-qt/translations/gcompris_nn.qm
/usr/share/gcompris-qt/translations/gcompris_pl.qm
/usr/share/gcompris-qt/translations/gcompris_pt.qm
/usr/share/gcompris-qt/translations/gcompris_pt_BR.qm
/usr/share/gcompris-qt/translations/gcompris_ro.qm
/usr/share/gcompris-qt/translations/gcompris_ru.qm
/usr/share/gcompris-qt/translations/gcompris_sk.qm
/usr/share/gcompris-qt/translations/gcompris_sl.qm
/usr/share/gcompris-qt/translations/gcompris_sv.qm
/usr/share/gcompris-qt/translations/gcompris_ta.qm
/usr/share/gcompris-qt/translations/gcompris_th.qm
/usr/share/gcompris-qt/translations/gcompris_tr.qm
/usr/share/gcompris-qt/translations/gcompris_uk.qm
/usr/share/gcompris-qt/translations/gcompris_zh_CN.qm
/usr/share/gcompris-qt/translations/gcompris_zh_TW.qm
/usr/share/icons/hicolor/256x256/apps/gcompris-qt.png
/usr/share/icons/hicolor/scalable/apps/gcompris-qt.svg
/usr/share/metainfo/org.kde.gcompris.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/en/gcompris-qt/gcompris-main-menu.png
/usr/share/doc/HTML/en/gcompris-qt/index.cache.bz2
/usr/share/doc/HTML/en/gcompris-qt/index.docbook
/usr/share/doc/HTML/en/gcompris-qt/traffic-select-mode.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gcompris-qt/COPYING
/usr/share/package-licenses/gcompris-qt/src_activities_checkers_LICENSE
/usr/share/package-licenses/gcompris-qt/src_core_COPYING
