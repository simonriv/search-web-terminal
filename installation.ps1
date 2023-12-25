$installationPath = $Env:Programfiles
$currentPath = Get-Location
$verifyPath = $installationPath + "search"

If (Test-Path $verifyPath) {
  try {
    Remove-Item $verifyPath -Recurse
    Write-Host "Previous installation removed" -ForegroundColor Green
  } catch {
    Write-Host "Could not remove the previous installation" -ForegroundColor Red
    Exit 1
  }

  if (Test-Path ($currentPath + "dist\search")) {
    try {
      Copy-Item -Path ($currentPath + "dist\search") -Destination ($verifyPath) -Recurse
      Write-Host "moved program" -ForegroundColor Green
    } catch {
      Write-Host "Could not move the program" -ForegroundColor Red
      Exit 1
    }
    
    try {
      $oldpath = (Get-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH).path
      $newpath = "$oldpath;$verifyPath"
      Set-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH -Value $newpath
      Write-Host "Environment variable created" -ForegroundColor Green
    } catch {
      Host "We could not create your environment variable you will have to do it manually." -ForegroundColor Red
    }
  } else {
    Write-Host "program files do not exist" -ForegroundColor Red
    Exit 1
  }
} Else {
  if (Test-Path ($currentPath + "dist\search")) {
    try {
      Copy-Item -Path ($currentPath + "dist\search") -Destination ($verifyPath) -Recurse
      Write-Host "moved program" -ForegroundColor Green
    } catch {
      Write-Host "Could not move the program" -ForegroundColor Red
      Exit 1
    }
    
    try {
      $oldpath = (Get-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH).path
      $newpath = "$oldpath;$verifyPath"
      Set-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH -Value $newpath
      Write-Host "Environment variable created" -ForegroundColor Green
    } catch {
      Host "We could not create your environment variable you will have to do it manually." -ForegroundColor Red
    }
  } else {
    Write-Host "program files do not exist" -ForegroundColor Red
    Exit 1
  }
}

Write-Host "Installation process completed" -ForegroundColor Cyan
