#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0x63D7264C05687D7E (animtim@gmail.com)
#
Name     : gcompris-qt
Version  : 3.3
Release  : 22
URL      : https://download.kde.org/stable/gcompris/qt/src/gcompris-qt-3.3.tar.xz
Source0  : https://download.kde.org/stable/gcompris/qt/src/gcompris-qt-3.3.tar.xz
Source1  : https://download.kde.org/stable/gcompris/qt/src/gcompris-qt-3.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : AGPL-3.0 Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-4.0 CC0-1.0 GFDL-1.2 GPL-2.0 GPL-3.0 LAL-1.2 LGPL-3.0 MPL-2.0 Unlicense
Requires: gcompris-qt-bin = %{version}-%{release}
Requires: gcompris-qt-data = %{version}-%{release}
Requires: gcompris-qt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : git
BuildRequires : mesa-dev
BuildRequires : openssl-dev
BuildRequires : p7zip
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Sensors)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5UiTools)
BuildRequires : pkgconfig(Qt5XmlPatterns)
BuildRequires : qml-box2d
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qttools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
GCompris / I Got IT
GCompris is a GNU package
https://gcompris.net
GCompris is a high quality educational software suite, including a large
number of activities for children aged 2 to 10. Some of the activities
are game orientated, but still educational.

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


%package license
Summary: license components for the gcompris-qt package.
Group: Default

%description license
license components for the gcompris-qt package.


%prep
%setup -q -n gcompris-qt-3.3
cd %{_builddir}/gcompris-qt-3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701958242
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1701958242
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gcompris-qt
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/AGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/ab44f99cc2a8ef07a252af053e1daafc337cd2d5 || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/81bf6d7df5e1fce2d1a8b3b97bb90cc33ad11593 || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/CC-BY-SA-4.0.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/218ff5d31a950e718669755000fd08bf864a50ab || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/3cb34cfc72e87654683f2894299adf912d14b284 || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/LicenseRef-Free-Art-Licence-1.2.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/fd750610fa9e8e6e13b7305ad4afe5636f34a0ce || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/LicenseRef-Free-Art-Licence-1.2.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/fd750610fa9e8e6e13b7305ad4afe5636f34a0ce || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/MPL-2.0.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/d574726e597032f1592b3596e80feb055e2ccf93 || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/Unlicense.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/bb7181fc26314a4752223527640b17e37fa7b4c7 || :
cp %{_builddir}/gcompris-qt-%{version}/LICENSES/Unlicense.txt %{buildroot}/usr/share/package-licenses/gcompris-qt/bb7181fc26314a4752223527640b17e37fa7b4c7 || :
cp %{_builddir}/gcompris-qt-%{version}/src/core/COPYING %{buildroot}/usr/share/package-licenses/gcompris-qt/d545523e4792c3756b1e46342a2a13b5554d1594 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gcompris-qt
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
/usr/share/gcompris-qt/rcc/align4.rcc
/usr/share/gcompris-qt/rcc/align4_2players.rcc
/usr/share/gcompris-qt/rcc/alphabet-sequence.rcc
/usr/share/gcompris-qt/rcc/analog_electricity.rcc
/usr/share/gcompris-qt/rcc/baby_keyboard.rcc
/usr/share/gcompris-qt/rcc/baby_mouse.rcc
/usr/share/gcompris-qt/rcc/baby_tangram.rcc
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
/usr/share/gcompris-qt/rcc/comparator.rcc
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
/usr/share/gcompris-qt/rcc/fractions_create.rcc
/usr/share/gcompris-qt/rcc/fractions_find.rcc
/usr/share/gcompris-qt/rcc/geo-country.rcc
/usr/share/gcompris-qt/rcc/geography.rcc
/usr/share/gcompris-qt/rcc/gletters.rcc
/usr/share/gcompris-qt/rcc/gnumch-equality.rcc
/usr/share/gcompris-qt/rcc/gnumch-factors.rcc
/usr/share/gcompris-qt/rcc/gnumch-inequality.rcc
/usr/share/gcompris-qt/rcc/gnumch-multiples.rcc
/usr/share/gcompris-qt/rcc/gnumch-primes.rcc
/usr/share/gcompris-qt/rcc/graph-coloring.rcc
/usr/share/gcompris-qt/rcc/gravity.rcc
/usr/share/gcompris-qt/rcc/guesscount.rcc
/usr/share/gcompris-qt/rcc/guessnumber.rcc
/usr/share/gcompris-qt/rcc/hangman.rcc
/usr/share/gcompris-qt/rcc/hanoi.rcc
/usr/share/gcompris-qt/rcc/hanoi_real.rcc
/usr/share/gcompris-qt/rcc/hexagon.rcc
/usr/share/gcompris-qt/rcc/imagename.rcc
/usr/share/gcompris-qt/rcc/instruments.rcc
/usr/share/gcompris-qt/rcc/land_safe.rcc
/usr/share/gcompris-qt/rcc/lang.rcc
/usr/share/gcompris-qt/rcc/learn_additions.rcc
/usr/share/gcompris-qt/rcc/learn_decimals.rcc
/usr/share/gcompris-qt/rcc/learn_decimals_additions.rcc
/usr/share/gcompris-qt/rcc/learn_decimals_subtractions.rcc
/usr/share/gcompris-qt/rcc/learn_digits.rcc
/usr/share/gcompris-qt/rcc/learn_quantities.rcc
/usr/share/gcompris-qt/rcc/learn_subtractions.rcc
/usr/share/gcompris-qt/rcc/left_right_click.rcc
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
/usr/share/gcompris-qt/rcc/morse_code.rcc
/usr/share/gcompris-qt/rcc/mosaic.rcc
/usr/share/gcompris-qt/rcc/nine_men_morris.rcc
/usr/share/gcompris-qt/rcc/nine_men_morris_2players.rcc
/usr/share/gcompris-qt/rcc/note_names.rcc
/usr/share/gcompris-qt/rcc/number_sequence.rcc
/usr/share/gcompris-qt/rcc/numbers-odd-even.rcc
/usr/share/gcompris-qt/rcc/ordering_alphabets.rcc
/usr/share/gcompris-qt/rcc/ordering_chronology.rcc
/usr/share/gcompris-qt/rcc/ordering_numbers.rcc
/usr/share/gcompris-qt/rcc/ordering_sentences.rcc
/usr/share/gcompris-qt/rcc/oware.rcc
/usr/share/gcompris-qt/rcc/oware_2players.rcc
/usr/share/gcompris-qt/rcc/paintings.rcc
/usr/share/gcompris-qt/rcc/path_decoding.rcc
/usr/share/gcompris-qt/rcc/path_decoding_relative.rcc
/usr/share/gcompris-qt/rcc/path_encoding.rcc
/usr/share/gcompris-qt/rcc/path_encoding_relative.rcc
/usr/share/gcompris-qt/rcc/penalty.rcc
/usr/share/gcompris-qt/rcc/photo_hunter.rcc
/usr/share/gcompris-qt/rcc/piano_composition.rcc
/usr/share/gcompris-qt/rcc/planegame.rcc
/usr/share/gcompris-qt/rcc/play_piano.rcc
/usr/share/gcompris-qt/rcc/play_rhythm.rcc
/usr/share/gcompris-qt/rcc/positions.rcc
/usr/share/gcompris-qt/rcc/programmingMaze.rcc
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
/usr/share/gcompris-qt/rcc/tens_complement_find.rcc
/usr/share/gcompris-qt/rcc/tens_complement_swap.rcc
/usr/share/gcompris-qt/rcc/tens_complement_use.rcc
/usr/share/gcompris-qt/rcc/tic_tac_toe.rcc
/usr/share/gcompris-qt/rcc/tic_tac_toe_2players.rcc
/usr/share/gcompris-qt/rcc/traffic.rcc
/usr/share/gcompris-qt/rcc/watercycle.rcc
/usr/share/gcompris-qt/rcc/wordsgame.rcc
/usr/share/gcompris-qt/translations/gcompris_ar.qm
/usr/share/gcompris-qt/translations/gcompris_az.qm
/usr/share/gcompris-qt/translations/gcompris_be.qm
/usr/share/gcompris-qt/translations/gcompris_br.qm
/usr/share/gcompris-qt/translations/gcompris_ca.qm
/usr/share/gcompris-qt/translations/gcompris_ca@valencia.qm
/usr/share/gcompris-qt/translations/gcompris_cs.qm
/usr/share/gcompris-qt/translations/gcompris_de.qm
/usr/share/gcompris-qt/translations/gcompris_el.qm
/usr/share/gcompris-qt/translations/gcompris_en.qm
/usr/share/gcompris-qt/translations/gcompris_en_GB.qm
/usr/share/gcompris-qt/translations/gcompris_eo.qm
/usr/share/gcompris-qt/translations/gcompris_es.qm
/usr/share/gcompris-qt/translations/gcompris_et.qm
/usr/share/gcompris-qt/translations/gcompris_eu.qm
/usr/share/gcompris-qt/translations/gcompris_fi.qm
/usr/share/gcompris-qt/translations/gcompris_fr.qm
/usr/share/gcompris-qt/translations/gcompris_he.qm
/usr/share/gcompris-qt/translations/gcompris_hr.qm
/usr/share/gcompris-qt/translations/gcompris_hu.qm
/usr/share/gcompris-qt/translations/gcompris_id.qm
/usr/share/gcompris-qt/translations/gcompris_it.qm
/usr/share/gcompris-qt/translations/gcompris_lt.qm
/usr/share/gcompris-qt/translations/gcompris_mk.qm
/usr/share/gcompris-qt/translations/gcompris_ml.qm
/usr/share/gcompris-qt/translations/gcompris_nl.qm
/usr/share/gcompris-qt/translations/gcompris_nn.qm
/usr/share/gcompris-qt/translations/gcompris_pl.qm
/usr/share/gcompris-qt/translations/gcompris_pt.qm
/usr/share/gcompris-qt/translations/gcompris_pt_BR.qm
/usr/share/gcompris-qt/translations/gcompris_ro.qm
/usr/share/gcompris-qt/translations/gcompris_ru.qm
/usr/share/gcompris-qt/translations/gcompris_sk.qm
/usr/share/gcompris-qt/translations/gcompris_sl.qm
/usr/share/gcompris-qt/translations/gcompris_sq.qm
/usr/share/gcompris-qt/translations/gcompris_sv.qm
/usr/share/gcompris-qt/translations/gcompris_tr.qm
/usr/share/gcompris-qt/translations/gcompris_uk.qm
/usr/share/gcompris-qt/translations/gcompris_zh_TW.qm
/usr/share/icons/hicolor/256x256/apps/gcompris-qt.png
/usr/share/icons/hicolor/scalable/apps/gcompris-qt.svg
/usr/share/metainfo/org.kde.gcompris.appdata.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gcompris-qt/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/gcompris-qt/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/gcompris-qt/218ff5d31a950e718669755000fd08bf864a50ab
/usr/share/package-licenses/gcompris-qt/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/gcompris-qt/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee
/usr/share/package-licenses/gcompris-qt/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/gcompris-qt/81bf6d7df5e1fce2d1a8b3b97bb90cc33ad11593
/usr/share/package-licenses/gcompris-qt/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/gcompris-qt/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/gcompris-qt/ab44f99cc2a8ef07a252af053e1daafc337cd2d5
/usr/share/package-licenses/gcompris-qt/bb7181fc26314a4752223527640b17e37fa7b4c7
/usr/share/package-licenses/gcompris-qt/d545523e4792c3756b1e46342a2a13b5554d1594
/usr/share/package-licenses/gcompris-qt/d574726e597032f1592b3596e80feb055e2ccf93
/usr/share/package-licenses/gcompris-qt/e712eadfab0d2357c0f50f599ef35ee0d87534cb
/usr/share/package-licenses/gcompris-qt/fd750610fa9e8e6e13b7305ad4afe5636f34a0ce
