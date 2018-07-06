Name:             st-desktop
Version:          0.0.1
Release:          1
Summary:          Desktop file for st
License:          MIT
URL:              https://github.com/zapster/st-desktop
Source0:          st-desktop.desktop
Source1:          st.svg
BuildArch:        noarch
BuildRequires:    desktop-file-utils
BuildRequires:    ImageMagick
Requires:         st

%description
Desktop file for st

%install
for res in 16 24 32 48 256 ; do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${res}x${res}/apps
  convert %{SOURCE1} -resize ${res}x${res} \
    %{buildroot}%{_datadir}/icons/hicolor/${res}x${res}/apps/%{name}.png
done
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE0}

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*
