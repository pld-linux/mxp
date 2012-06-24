Name: mxp
Version: 1.0
Release: 11
Copyright: MIT
Group: X11/Applications/Graphics
Summary: X11 Mandelbrot set generator and explorer
Source: ftp://sunsite.unc.edu/apps/math/fractals/mxp-1.0.tgz
Patch: mxp-1.0-imake.patch
Patch1: mxp-1.0-glibc.patch
BuildRoot: /var/tmp/mxp-root
Summary(de): X11 Mandelbrot-Setgenerator und Explorer 
Summary(fr): G�n�rateur et explorateur X11 d'ensembles de Mandelbrot
Summary(tr): Mandelbrot k�mesi �retici ve taray�c�

%description
This is a very fast Mandelbrot set generator for X Windows. It lets you
select regions to zoom in on and allows you to control other aspects
of fractal generation.

%description -l de
Dies ist ein sehr schneller Mandelbrot-Mengengenerator f�r X-Windows. Sie
Zoom-Bereiche ausw�hlen und andere Parameter der Fraktalerzeugung 
einstellen.

%description -l tr
X Windows ortam�nda �al��an, g��l� bir Mandelbrot k�mesi �reticisidir.
B�y�tmek i�in b�lge se�ilebilmesine ve fraktal olu�turman�n �zelliklerinin
denetlenmesine olanak sa�lar.

%prep
%setup -q -n mxp
%patch -p1
%patch1 -p1

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/X11R6/bin/mxp

%changelog
* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- updated the source url

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
