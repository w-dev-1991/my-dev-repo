$saName = 'wtsatest' #storage account's name we want to create

$rgName = (Get-AzResourceGroup).ResourceGroupName
$isSaNameAvail = (Get-AzStorageAccountNameAvailability -Name $saName).NameAvailable

if($isSaNameAvail){
    New-AzStorageAccount -ResourceGroupName $rgName -Name $saName -Location 'westeurope' -SkuName Standard_LRS
    Write "___Created new storage account: *$saName*"
}
else{
    Write-Host "___Storage Account name: *$isSaNameAvail* is not available."

    #get all storage accounts from current resource group
    $saInRg = (Get-AzStorageAccount -ResourceGroupName $rgName).StorageAccountName

    foreach ($x in $saInRg){
        if($saName -eq $x){
            Write-Host "___$saName = $x"
            Write-Host "___usuwam Storage Account: $x"
            Remove-AzStorageAccount -ResourceGroupName $rgName -Name $x -Force 
            write "___Storage Account: *$x* removed."
        }
    }
    
}

#   R all Storage Account from $rgName Resource Group
<#
foreach ($sa in (Get-AzStorageAccount -ResourceGroupName $rgName).StorageAccountName){
    Remove-AzStorageAccount -ResourceGroupName $rgName -name $sa -force 
}
#>

#   Creates several Storace Accounts
<#
$saName = 'wtsatest'
$rgName = (Get-AzResourceGroup).ResourceGroupName
foreach ($x in (1..3)){
 New-AzStorageAccount -ResourceGroupName $rgName -Name $saName$x -Location 'westeurope' -SkuName Standard_LRS -AsJob
}
#>

