targetScope = 'resourceGroup'
param location string = resourceGroup().location
param environment string = 'dev'

resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: 'kv-data-ai-$environment'
  location: location
  properties: {
    sku: { family: 'A', name: 'standard' }
    tenantId: subscription().tenantId
    enableRbacAuthorization: true
  }
}
