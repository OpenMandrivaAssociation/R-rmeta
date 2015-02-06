%global packname  rmeta
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.16
Release:          3
Summary:          Meta-analysis
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Source1:          NAMESPACE
BuildArch:        noarch
Requires:         R-core
Requires:         R-grid 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-grid

%description
Functions for simple fixed and random effects meta-analysis for two-sample
comparisons and cumulative meta-analyses. Draws standard summary plots,
funnel plots, and computes summaries and tests for association and

%prep
%setup -q -c -n %{packname}
cp %{SOURCE1} %{packname}/

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
