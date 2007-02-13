Summary:	X11 Mandelbrot set generator and explorer
Summary(de.UTF-8):	X11 Mandelbrot-Setgenerator und Explorer
Summary(es.UTF-8):	Explorador y creador de conjuntos de Mandelbrot para X11
Summary(fr.UTF-8):	Générateur et explorateur X11 d'ensembles de Mandelbrot
Summary(pl.UTF-8):	Generator i przeglądarka zbioru Mandelbrota
Summary(pt_BR.UTF-8):	Explorador e gerador de conjuntos de Mandelbrot para X11
Summary(tr.UTF-8):	Mandelbrot kümesi üretici ve tarayıcı
Name:		mxp
Version:	1.3
Release:	2
License:	MIT
Group:		X11/Applications/Graphics
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/math/fractals/%{name}-%{version}.tar.gz
# Source0-md5:	c53f8b91fcbb09c4ad885bb7c34d2dd0
Patch0:		%{name}-imake.patch
Patch1:		%{name}-glibc.patch
BuildRequires:	Xaw3d-devel
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very fast Mandelbrot set generator for X Window System. It
lets you select regions to zoom in on and allows you to control other
aspects of fractal generation.

%description -l de.UTF-8
Dies ist ein sehr schneller Mandelbrot-Mengengenerator für X-Window.
Sie Zoom-Bereiche auswählen und andere Parameter der Fraktalerzeugung
einstellen.

%description -l es.UTF-8
Este es un rápido conjunto creador Mandelbrot para X Window. Deja que
selecciones regiones para zoom y te permite controlar otros aspectos
de generación fractal.

%description -l pl.UTF-8
To jest bardzo szybki generator zbioru Mandelbrota pod X Window
System. Pozwala na zaznaczenie obszarów do powiększenia i kontrolę
innych aspektów generowania fraktala.

%description -l pt_BR.UTF-8
Este é um rápido conjunto gerador Mandelbrot para X Window. Ele deixa
você selecionar regiões para zoom e permite você controlar outros
aspectos de geração fractal.

%description -l tr.UTF-8
X Window ortamında çalışan, güçlü bir Mandelbrot kümesi üreticisidir.
Büyütmek için bölge seçilebilmesine ve fraktal oluşturmanın
özelliklerinin denetlenmesine olanak sağlar.

%prep
%setup -q -n mxp
%patch0 -p1
%patch1 -p1

%build
xmkmf
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	LOCAL_LDFLAGS="%{rpmldflags}"

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
