#Connect-AzAccount
Uninstall-AzureRm
Import-Module Az.Storage

$saAvail = Get-AzStorageAccountNameAvailability -Name ajsdoiasjfoisajdoisaj | Select-Object NameAvailable

Write-Output $saAvail

if (!$saAvail) {
 Write-Output $saAvail
}