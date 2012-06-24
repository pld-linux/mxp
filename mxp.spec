Summary:	X11 Mandelbrot set generator and explorer
Summary(de):	X11 Mandelbrot-Setgenerator und Explorer
Summary(es):	Explorador y creador de conjuntos de Mandelbrot para X11
Summary(fr):	G�n�rateur et explorateur X11 d'ensembles de Mandelbrot
Summary(pl):	Generator i przegl�darka zbioru Mandelbrota
Summary(pt_BR):	Explorador e gerador de conjuntos de Mandelbrot para X11
Summary(tr):	Mandelbrot k�mesi �retici ve taray�c�
Name:		mxp
Version:	1.3
Release:	1
License:	MIT
Group:		X11/Applications/Graphics
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/math/fractals/%{name}-%{version}.tar.gz
# Source0-md5:	c53f8b91fcbb09c4ad885bb7c34d2dd0
Patch0:		%{name}-imake.patch
Patch1:		%{name}-glibc.patch
BuildRequires:	XFree86-devel
BuildRequires:	Xaw3d-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very fast Mandelbrot set generator for X Window System. It
lets you select regions to zoom in on and allows you to control other
aspects of fractal generation.

%description -l de
Dies ist ein sehr schneller Mandelbrot-Mengengenerator f�r X-Window.
Sie Zoom-Bereiche ausw�hlen und andere Parameter der Fraktalerzeugung
einstellen.

%description -l es
Este es un r�pido conjunto creador Mandelbrot para X Window. Deja que
selecciones regiones para zoom y te permite controlar otros aspectos
de generaci�n fractal.

%description -l pl
To jest bardzo szybki generator zbioru Mandelbrota pod X Window
System. Pozwala na zaznaczenie obszar�w do powi�kszenia i kontrol�
innych aspekt�w generowania fraktala.

%description -l pt_BR
Este � um r�pido conjunto gerador Mandelbrot para X Window. Ele deixa
voc� selecionar regi�es para zoom e permite voc� controlar outros
aspectos de gera��o fractal.

%description -l tr
X Window ortam�nda �al��an, g��l� bir Mandelbrot k�mesi �reticisidir.
B�y�tmek i�in b�lge se�ilebilmesine ve fraktal olu�turman�n
�zelliklerinin denetlenmesine olanak sa�lar.

%prep
%setup -q -n mxp
%patch0 -p1
%patch1 -p1

%build
xmkmf
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/mxp
