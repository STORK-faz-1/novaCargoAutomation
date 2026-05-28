# novaPurchaseAutomationV2


---

## How to Trigger Automation? (Otomasyon Nasıl Tetiklenir?)

Bu otomasyonu harici bir sistemden (CRM, ERP, Webhook vb.) tetiklemek için UiPath Orchestrator API'sini kullanarak ilgili kuyruğa (`extract-data-queue-1`) bir yeni eleman (Queue Item) eklemeniz gerekmektedir.

Aşağıdaki **cURL** komutunu kullanarak otomasyonu uzaktan tetikleyebilirsiniz:

```bash
curl -X 'POST' \
  '[https://cloud.uipath.com/may2026t/DefaultTenant/orchestrator_/odata/Queues/UiPathODataSvc.AddQueueItem](https://cloud.uipath.com/may2026t/DefaultTenant/orchestrator_/odata/Queues/UiPathODataSvc.AddQueueItem)' \
  -H 'X-UIPATH-OrganizationUnitId: 110175' \
  -H 'X-UIPATH-TenantName: DefaultTenant' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer [YOUR_BEARER_TOKEN_HERE]' \
  -d '{
  "itemData": {
    "Name": "extract-data-queue-1",
    "Priority": "Normal",
    "Reference": "Siparis_10533546279",
    "SpecificContent": {
      "SiparisNo": "10533546279",
      "AccountEmail": "example@email.com",
      "AccountPassword": "your_password_here"
    }
  }
}'
