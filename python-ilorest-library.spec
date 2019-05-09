%global sha f6dae68800d20af859ed958c322108604d6a998a

Name:           python-ilorest-library
Version:        v2.3.1.29.gf6dae68
Release:        1%{?dist}.1
Summary:        HPE RESTful API for iLO is a RESTful application programming interface for the management of iLO and iLO Chassis Manager based HPE servers.
License:        %{_platform_license} and ASL 2.0
Source0:        https://github.com/HewlettPackard/%{name}/archive/%{sha}.zip
Patch0:         0001-initial.patch
Vendor:         %{_platform_vendor} and HP

#Requires: clustermanager-python
BuildRequires: python, python-setuptools

%description
HPE RESTful API for iLO is a RESTful application programming interface for the management of iLO and iLO Chassis Manager based HPE servers.
REST (Representational State Transfer) is a web based software architectural style consisting of a set of constraints that focuses on a system's resources.
iLO REST library performs the basic HTTP operations GET, POST, PUT, PATCH and DELETE on resources using the HATEOAS (Hypermedia as the Engine of Application State) REST architecture.
The API allows the clients to manage and interact with iLO through a fixed URL and several URIs. Go to the wiki for more details.


%prep
%autosetup -n %{name}-%{sha} -p 1

#%build
#make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
#%make_install

python setup.py install --root %{buildroot} --no-compile --install-purelib %{_python_site_packages_path} --install-scripts /usr/bin

%files
%{_python_site_packages_path}/redfish
%{_python_site_packages_path}/python_ilorest_library-2.3.1-py2.7.egg-info

%pre
# Pre installation (optional)

%post

%preun
# Pre uninstall (optional)
#if [ $1 = 0 ]; then # package is being erased, not upgraded
#    /sbin/service food stop > /dev/null 2>&1
#    /sbin/chkconfig --del foo
#fi
%clean
rm -rf $RPM_BUILD_ROOT

# TIPS:
# File /usr/lib/rpm/macros contains useful variables which can be used for example to define target directory for man page.
# Running "rpm --showrc" command in RHEL host will also show available macros
