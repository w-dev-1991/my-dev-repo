try{
    #Connect-AzAccount
    
    $location = "westeurope"
    $storageName = "wtstorageacc"
    $dbWorkspaceName = "wtbricks"
    $dbclusterName = "testcluster2"

    $rgName = (Get-AzResourceGroup).ResourceGroupName
        
    
    New-AzStorageAccount -ResourceGroupName $rgName -Name $storageName -Location $location -SkuName Standard_LRS
   
    
    New-AzDatabricksWorkspace `
        -Name $dbWorkspaceName `
        -ResourceGroupName $rgName `
        -Location $location `
        -Sku standard
   
   
<#    
#Generate Access Token in Databricks   
try{
    Add-DatabricksApiToken -LifetimeSeconds 72000 -Comment "Created with PowerShell"
    $accessToken = (Get-DatabricksApiToken).token_value
}
    catch{
     Write-Host "An error occurred: "
     Write-Host $_
}
#>

   #$accessToken = Read-Host -Prompt "Input Access Token to Databricks' workspace: "       
   Add-Type -AssemblyName Microsoft.VisualBasic
   $accessToken = [Microsoft.VisualBasic.Interaction]::InputBox("Enter Access Token to Databricks' workspace", "Access Token to Dabtaricks' workspace")



   $apiUrl = "https://westeurope.azuredatabricks.net"

   Set-DatabricksEnvironment -AccessToken $accessToken -ApiRootUrl $apiUrl

   #Create New Databricks Cluster
   $clusterId = Add-DatabricksCluster  `
    -NumWorkers 2 `
    -ClusterName $dbclusterName `
    -SparkVersion "7.5.x-scala2.12" `
    -AutoterminationMinutes 60 `
    -DriverNodeTypeId "Standard_F4s" `
    -NodeTypeId "Standard_F4s" `

    if ((Get-DatabricksCluster).State -eq "TERMINATED"){
        Start-DatabricksCluster -ClusterID $clusterId
    }

    $retriesCounter = 0
    Do {
    $clusterState = (Get-DatabricksCluster).State
    $retriesCounter = $retriesCounter + 1
    Start-Sleep -Seconds 6
    }
    Until ($clusterState -eq "RUNNING" -or $retriesCounter -eq 70)    

}
catch{
    Write-Host "An error occurred: "
    Write-Host $_
}

$wshell = New-Object -ComObject Wscript.Shell
$Output = $wshell.Popup("Storage Account and Databricks successfully deployed!")


#Remove Storage Account and Databricks Workspace
<#
    Remove-AzStorageAccount -ResourceGroupName $rgName -Name $storageName -Force
    Remove-AzDatabricksWorkspace -Name $dbWorkspaceName -ResourceGroupName $rgName
#>
