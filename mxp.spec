Summary:	X11 Mandelbrot set generator and explorer
Summary(de):	X11 Mandelbrot-Setgenerator und Explorer 
Summary(fr):	G�n�rateur et explorateur X11 d'ensembles de Mandelbrot
Summary(tr):	Mandelbrot k�mesi �retici ve taray�c�
Name:		mxp
Version:	1.0
Release:	11
Copyright:	MIT
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://sunsite.unc.edu/apps/math/fractals/%{name}-%{version}.tgz
Patch0:		mxp-imake.patch
Patch1:		mxp-glibc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is a very fast Mandelbrot set generator for X Windows. It lets
you select regions to zoom in on and allows you to control other
aspects of fractal generation.

%description -l de
Dies ist ein sehr schneller Mandelbrot-Mengengenerator f�r X-Windows.
Sie Zoom-Bereiche ausw�hlen und andere Parameter der Fraktalerzeugung
einstellen.

%description -l tr
X Windows ortam�nda �al��an, g��l� bir Mandelbrot k�mesi �reticisidir.
B�y�tmek i�in b�lge se�ilebilmesine ve fraktal olu�turman�n
�zelliklerinin denetlenmesine olanak sa�lar.

%prep
%setup -q -n mxp
%patch0 -p1
%patch1 -p1

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/mxp
