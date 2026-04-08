# Applies Wonderbee Services branding + nav/footer across all HTML files.
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
if (-not (Test-Path (Join-Path $root "index.html"))) {
  $root = "c:\Users\MuhammadHassan\Desktop\Nannies and Laundary Services Website"
}

$utf8NoBom = New-Object System.Text.UTF8Encoding $false
$files = Get-ChildItem -Path $root -Recurse -Filter "*.html" -File

# --- Root-level nav: href="pages/... ---
$rootFamiliesOld = @'
                <a href="pages/our-process.html" data-nav="our-process" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Our Process</a>
                <a href="pages/our-nannies.html" data-nav="our-nannies" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Our Nannies</a>
                <a href="pages/household-managers.html" data-nav="household-managers" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Household Managers</a>
                <a href="pages/pricing.html" data-nav="pricing" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Pricing</a>
                <a href="pages/family-faq.html" data-nav="family-faq" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Family-FAQ</a>
                <a href="pages/apply-family.html" data-nav="apply-family" class="nav-apply-highlight mx-2 block px-4 py-2.5 text-sm font-medium text-nn-secondary" role="menuitem">Apply Now</a>
'@

$rootFamiliesNew = @'
                <a href="pages/our-nannies.html" data-nav="our-nannies" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Nanny Placement</a>
                <a href="pages/pricing.html" data-nav="pricing" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">On Call / Hotel</a>
                <a href="pages/household-managers.html" data-nav="household-managers" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Newborn Care Specialist NCS</a>
                <a href="pages/family-faq.html" data-nav="family-faq" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">FAQ</a>
'@

$rootNanniesOld = @'
                <a href="pages/job-openings.html" data-nav="job-openings" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Job Openings</a>
                <a href="pages/why-nannies.html" data-nav="why-nannies" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Why Work With Us?</a>
                <a href="pages/apply-nanny.html" data-nav="apply-nanny" class="nav-apply-highlight mx-2 block px-4 py-2.5 text-sm font-medium text-nn-secondary" role="menuitem">Apply Now</a>
'@

$rootNanniesNew = @'
                <a href="pages/job-openings.html" data-nav="job-openings" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Join the Team</a>
                <a href="pages/apply-family.html" data-nav="apply-family" class="nav-apply-highlight mx-2 block px-4 py-2.5 text-sm font-medium text-nn-secondary" role="menuitem">Find a Specialist</a>
'@

$rootMobileFamiliesOld = @'
              <a href="pages/our-process.html" data-nav="our-process" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Our Process</a>
              <a href="pages/our-nannies.html" data-nav="our-nannies" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Our Nannies</a>
              <a href="pages/household-managers.html" data-nav="household-managers" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Household Managers</a>
              <a href="pages/pricing.html" data-nav="pricing" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Pricing</a>
              <a href="pages/family-faq.html" data-nav="family-faq" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Family FAQ</a>
              <a href="pages/apply-family.html" data-nav="apply-family" class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Apply Now</a>
'@

$rootMobileFamiliesNew = @'
              <a href="pages/our-nannies.html" data-nav="our-nannies" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Nanny Placement</a>
              <a href="pages/pricing.html" data-nav="pricing" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">On Call / Hotel</a>
              <a href="pages/household-managers.html" data-nav="household-managers" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Newborn Care Specialist NCS</a>
              <a href="pages/family-faq.html" data-nav="family-faq" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">FAQ</a>
'@

$rootMobileNanniesOld = @'
              <a href="pages/job-openings.html" data-nav="job-openings" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Job Openings</a>
              <a href="pages/why-nannies.html" data-nav="why-nannies" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Why Work With Us</a>
              <a href="pages/apply-nanny.html" data-nav="apply-nanny" class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Apply Now</a>
'@

$rootMobileNanniesNew = @'
              <a href="pages/job-openings.html" data-nav="job-openings" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Join the Team</a>
              <a href="pages/apply-family.html" data-nav="apply-family" class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Find a Specialist</a>
'@

# --- /pages/* nav ---
$pagesFamiliesOld = @'
            <a href="our-process.html" data-nav="our-process" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Our Process</a>
            <a href="our-nannies.html" data-nav="our-nannies" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Our Nannies</a>
            <a href="household-managers.html" data-nav="household-managers" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Household Managers</a>
            <a href="pricing.html" data-nav="pricing" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Pricing</a>
            <a href="family-faq.html" data-nav="family-faq" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Family-FAQ</a>
            <a href="apply-family.html" data-nav="apply-family" class="nav-apply-highlight mx-2 block px-4 py-2.5 text-sm font-medium text-nn-secondary" role="menuitem">Apply Now</a>
'@

$pagesFamiliesNew = @'
            <a href="our-nannies.html" data-nav="our-nannies" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Nanny Placement</a>
            <a href="pricing.html" data-nav="pricing" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">On Call / Hotel</a>
            <a href="household-managers.html" data-nav="household-managers" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Newborn Care Specialist NCS</a>
            <a href="family-faq.html" data-nav="family-faq" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">FAQ</a>
'@

$pagesNanniesOld = @'
            <a href="job-openings.html" data-nav="job-openings" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Job Openings</a>
            <a href="why-nannies.html" data-nav="why-nannies" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Why Work With Us?</a>
            <a href="apply-nanny.html" data-nav="apply-nanny" class="nav-apply-highlight mx-2 block px-4 py-2.5 text-sm font-medium text-nn-secondary" role="menuitem">Apply Now</a>
'@

$pagesNanniesNew = @'
            <a href="job-openings.html" data-nav="job-openings" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Join the Team</a>
            <a href="apply-family.html" data-nav="apply-family" class="nav-apply-highlight mx-2 block px-4 py-2.5 text-sm font-medium text-nn-secondary" role="menuitem">Find a Specialist</a>
'@

$pagesMobileFamiliesOld = @'
          <a href="our-process.html" data-nav="our-process" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Our Process</a>
          <a href="our-nannies.html" data-nav="our-nannies" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Our Nannies</a>
          <a href="household-managers.html" data-nav="household-managers" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Household Managers</a>
          <a href="pricing.html" data-nav="pricing" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Pricing</a>
          <a href="family-faq.html" data-nav="family-faq" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Family FAQ</a>
          <a href="apply-family.html" data-nav="apply-family" class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Apply Now</a>
'@

$pagesMobileFamiliesNew = @'
          <a href="our-nannies.html" data-nav="our-nannies" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Nanny Placement</a>
          <a href="pricing.html" data-nav="pricing" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">On Call / Hotel</a>
          <a href="household-managers.html" data-nav="household-managers" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Newborn Care Specialist NCS</a>
          <a href="family-faq.html" data-nav="family-faq" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">FAQ</a>
'@

$pagesMobileNanniesOld = @'
          <a href="job-openings.html" data-nav="job-openings" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Job Openings</a>
          <a href="why-nannies.html" data-nav="why-nannies" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Why Work With Us</a>
          <a href="apply-nanny.html" data-nav="apply-nanny" class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Apply Now</a>
'@

$pagesMobileNanniesNew = @'
          <a href="job-openings.html" data-nav="job-openings" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Join the Team</a>
          <a href="apply-family.html" data-nav="apply-family" class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Find a Specialist</a>
'@

# --- /pages/blog/* nav ---
$blogFamiliesOld = @'
                <a href="../our-process.html" data-nav="our-process" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Our Process</a>
                <a href="../our-nannies.html" data-nav="our-nannies" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Our Nannies</a>
                <a href="../household-managers.html" data-nav="household-managers" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Household Managers</a>
                <a href="../pricing.html" data-nav="pricing" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Pricing</a>
                <a href="../family-faq.html" data-nav="family-faq" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Family-FAQ</a>
                <a href="../apply-family.html" data-nav="apply-family" class="nav-apply-highlight mx-2 block px-4 py-2.5 text-sm font-medium text-nn-secondary" role="menuitem">Apply Now</a>
'@

$blogFamiliesNew = @'
                <a href="../our-nannies.html" data-nav="our-nannies" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Nanny Placement</a>
                <a href="../pricing.html" data-nav="pricing" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">On Call / Hotel</a>
                <a href="../household-managers.html" data-nav="household-managers" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Newborn Care Specialist NCS</a>
                <a href="../family-faq.html" data-nav="family-faq" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">FAQ</a>
'@

$blogNanniesOld = @'
                <a href="../job-openings.html" data-nav="job-openings" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Job Openings</a>
                <a href="../why-nannies.html" data-nav="why-nannies" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Why Work With Us?</a>
                <a href="../apply-nanny.html" data-nav="apply-nanny" class="nav-apply-highlight mx-2 block px-4 py-2.5 text-sm font-medium text-nn-secondary" role="menuitem">Apply Now</a>
'@

$blogNanniesNew = @'
                <a href="../job-openings.html" data-nav="job-openings" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Join the Team</a>
                <a href="../apply-family.html" data-nav="apply-family" class="nav-apply-highlight mx-2 block px-4 py-2.5 text-sm font-medium text-nn-secondary" role="menuitem">Find a Specialist</a>
'@

$blogMobileFamiliesOld = @'
              <a href="../our-process.html" data-nav="our-process" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Our Process</a>
              <a href="../our-nannies.html" data-nav="our-nannies" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Our Nannies</a>
              <a href="../household-managers.html" data-nav="household-managers" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Household Managers</a>
              <a href="../pricing.html" data-nav="pricing" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Pricing</a>
              <a href="../family-faq.html" data-nav="family-faq" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Family FAQ</a>
              <a href="../apply-family.html" data-nav="apply-family" class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Apply Now</a>
'@

$blogMobileFamiliesNew = @'
              <a href="../our-nannies.html" data-nav="our-nannies" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Nanny Placement</a>
              <a href="../pricing.html" data-nav="pricing" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">On Call / Hotel</a>
              <a href="../household-managers.html" data-nav="household-managers" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Newborn Care Specialist NCS</a>
              <a href="../family-faq.html" data-nav="family-faq" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">FAQ</a>
'@

$blogMobileNanniesOld = @'
              <a href="../job-openings.html" data-nav="job-openings" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Job Openings</a>
              <a href="../why-nannies.html" data-nav="why-nannies" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Why Work With Us</a>
              <a href="../apply-nanny.html" data-nav="apply-nanny" class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Apply Now</a>
'@

$blogMobileNanniesNew = @'
              <a href="../job-openings.html" data-nav="job-openings" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Join the Team</a>
              <a href="../apply-family.html" data-nav="apply-family" class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Find a Specialist</a>
'@

foreach ($f in $files) {
  $c = [System.IO.File]::ReadAllText($f.FullName)
  $useCRLF = $c.Contains("`r`n")
  $c = $c.Replace("`r`n", "`n")

  $c = $c.Replace("Wonderbee Services LLC", "Wonderbee Services")
  $c = $c.Replace("Boutique Nanny Placement Agency", "Wonderbee Services")
  $bullet = [char]0x2022
  $c = $c.Replace("Mid-Atlantic Hub $bullet Northeast Corridor $bullet Lakeshore Metro", "Quality childcare solutions tailored to your family's needs")
  $c = $c -replace '(?s)(<p class="mx-auto mt-3 max-w-4xl text-center text-xs leading-relaxed text-nn-body sm:text-sm">\s*)Alexandria.*?</p>', ('$1Nanny Placement ' + $bullet + ' On Call / Hotel Babysitters ' + $bullet + ' Newborn Care Specialist NCS ' + $bullet + ' Personal Assistant Services</p>')
  $c = $c.Replace("For Families", "Services")
  $c = $c.Replace("For Nannies", "Careers")
  $c = $c.Replace('| Wonderbee', '| Wonderbee Services')
  # Keep Wonderbee contact channels as authored in HTML.

  $c = $c.Replace($rootFamiliesOld, $rootFamiliesNew)
  $c = $c.Replace($rootNanniesOld, $rootNanniesNew)
  $c = $c.Replace($rootMobileFamiliesOld, $rootMobileFamiliesNew)
  $c = $c.Replace($rootMobileNanniesOld, $rootMobileNanniesNew)

  $c = $c.Replace($pagesFamiliesOld, $pagesFamiliesNew)
  $c = $c.Replace($pagesNanniesOld, $pagesNanniesNew)
  $c = $c.Replace($pagesMobileFamiliesOld, $pagesMobileFamiliesNew)
  $c = $c.Replace($pagesMobileNanniesOld, $pagesMobileNanniesNew)

  $c = $c.Replace($blogFamiliesOld, $blogFamiliesNew)
  $c = $c.Replace($blogNanniesOld, $blogNanniesNew)
  $c = $c.Replace($blogMobileFamiliesOld, $blogMobileFamiliesNew)
  $c = $c.Replace($blogMobileNanniesOld, $blogMobileNanniesNew)

  $c = $c.Replace('class="nn-navlink px-3 py-2 text-nn-small">Contact Us</a>', 'class="nn-navlink px-3 py-2 text-nn-small">Contact</a>')
  $c = $c.Replace('class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Contact Us</a>', 'class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Contact</a>')

  if ($useCRLF) {
    $c = $c.Replace("`n", "`r`n")
  }
  [System.IO.File]::WriteAllText($f.FullName, $c, $utf8NoBom)
}

Write-Host "Updated $($files.Count) HTML files under $root"
