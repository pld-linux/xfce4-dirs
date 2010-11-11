%define		_enable_debug_packages	0
Summary:	Xfce4 - common directories
Summary(pl.UTF-8):	Wspólne katalogi Xfce4
Name:		xfce4-dirs
Version:	4.6
Release:	2
License:	LGPL
Group:		X11/Libraries
URL:		http://www.xfce.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xfce4docdir	%{_datadir}/xfce4/doc

%description
Xfce4 common directories.

%description -l pl.UTF-8
Katalogi wspólne dla Xfce4.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT%{_sysconfdir}/xdg/xfce4 \
	$RPM_BUILD_ROOT%{_libdir}/xfce4 \
	$RPM_BUILD_ROOT%{_libdir}/xfce4/modules \
	$RPM_BUILD_ROOT%{_datadir}/xfce4 \
	$RPM_BUILD_ROOT%{_xfce4docdir}/{C,ast,ca,da,es,fr,gl,id,it,ja,pt,pt_BR,tr,zh_CN}/images \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_libdir}/xfce4
%dir %{_libdir}/xfce4/modules
%dir %{_datadir}/xfce4
%dir %{_xfce4docdir}
%dir %{_xfce4docdir}/C
%dir %{_xfce4docdir}/C/images
%lang(ast) %dir %{_xfce4docdir}/ast
%lang(ast) %dir %{_xfce4docdir}/ast/images
%lang(ca) %dir %{_xfce4docdir}/ca
%lang(ca) %dir %{_xfce4docdir}/ca/images
%lang(da) %dir %{_xfce4docdir}/da
%lang(da) %dir %{_xfce4docdir}/da/images
%lang(es) %dir %{_xfce4docdir}/es
%lang(es) %dir %{_xfce4docdir}/es/images
%lang(fr) %dir %{_xfce4docdir}/fr
%lang(fr) %dir %{_xfce4docdir}/fr/images
%lang(gl) %dir %{_xfce4docdir}/gl
%lang(gl) %dir %{_xfce4docdir}/gl/images
%lang(id) %dir %{_xfce4docdir}/id
%lang(id) %dir %{_xfce4docdir}/id/images
%lang(it) %dir %{_xfce4docdir}/it
%lang(it) %dir %{_xfce4docdir}/it/images
%lang(ja) %dir %{_xfce4docdir}/ja
%lang(ja) %dir %{_xfce4docdir}/ja/images
%lang(pt) %dir %{_xfce4docdir}/pt
%lang(pt) %dir %{_xfce4docdir}/pt/images
%lang(pt_BR) %dir %{_xfce4docdir}/pt_BR
%lang(pt_BR) %dir %{_xfce4docdir}/pt_BR/images
%lang(tr) %dir %{_xfce4docdir}/tr
%lang(tr) %dir %{_xfce4docdir}/tr/images
%lang(zh_CN) %dir %{_xfce4docdir}/zh_CN
%lang(zn_CN) %dir %{_xfce4docdir}/zh_CN/images
